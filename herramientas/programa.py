"""Programa diario de los dos lotes y verificación de recursos y turnos.

Genera el programa de un día típico (lote 1, lote 2 y el envasado del lote 2 del día anterior)
a partir de los tiempos de herramientas/parametros.yaml y verifica que:
  - ningún recurso (T-301, T-302, CIP-901, E-301) tenga dos usos a la vez;
  - cada tarea atendida por un rol caiga dentro de su turno y no se cruce con otra del mismo rol;
  - con la incubación máxima (300 min) las horas extra sean acotadas.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from modelo import cargar, hhmm, tiempos_envasado

TURNOS = {  # rol: (inicio, fin) en minutos desde las 0:00, lunes a sábado
    "R": (7 * 60, 14 * 60),             # recepción y laboratorio
    "P": (7 * 60, 14 * 60),             # preparación
    "E": (10 * 60 + 30, 17 * 60 + 30),  # envasado
    "K": (10 * 60 + 30, 17 * 60 + 30),  # empaque y cuarto frío
    "S": (12 * 60, 19 * 60),            # segundo lote
}
NOMBRES_ROL = {"R": "Operador de recepción y laboratorio", "P": "Operador de preparación",
               "E": "Operador de envasado", "K": "Operador de empaque y cuarto frío",
               "S": "Operador del segundo lote", "A": "Automático (PLC), sin operario"}
INICIO_ENVASADO_LOTE2 = 10 * 60 + 30


@dataclass
class Tarea:
    nombre: str
    lote: str
    inicio: float
    duracion: float
    recursos: list[str] = field(default_factory=list)
    rol: str = "A"
    atendida: bool = False

    @property
    def fin(self) -> float:
        return self.inicio + self.duracion


def r5(x: float) -> str:
    """Hora redondeada a 5 minutos para los documentos."""
    return hhmm(5 * round(x / 5))


def programa(p: dict | None = None, incubacion: float | None = None,
             ref_l1: str = "YB-200", ref_l2: str = "YB-200", ref_l2_prev: str = "YB-200") -> list[Tarea]:
    p = p or cargar()
    t = p["tiempos_min"]
    env = tiempos_envasado(p)
    inc = incubacion or t["incubar"]
    past = t["calentar_a_62"] + t["homogeneizar"] + t["calentar_a_87"] + t["sostener"]
    T = []
    add = lambda *a, **k: T.append(Tarea(*a, **k)) or T[-1]
    t0 = 7 * 60

    # Mañana: lote 2 del día anterior
    add("Muestra del lote 2 anterior y confirmación de acidez", "L2 anterior", t0, t["muestra_acidez"], ["LAB-101"], "R", True)
    tr = add("Transferencia del lote 2 anterior por E-301 a T-302", "L2 anterior", t0, t["transferencia"],
             ["T-301", "T-302", "E-301"], "P", True)
    add("Espera del lote 2 anterior en T-302 a 12–15 °C", "L2 anterior", tr.fin, INICIO_ENVASADO_LOTE2 - tr.fin, ["T-302"])
    e2 = add(f"Envasado del lote 2 anterior ({ref_l2_prev})", "L2 anterior", INICIO_ENVASADO_LOTE2, env[ref_l2_prev],
             ["T-302", "MAQ-" + ref_l2_prev], "E", True)
    add("Encanastado o encajonado del lote 2 anterior", "L2 anterior", e2.inicio, e2.duracion, [], "K", True)
    add("CIP de T-302 y de la línea de envasado", "L2 anterior", e2.fin, t["cip_completo"], ["T-302", "CIP-901"], "E")

    # Recepción de la leche de los dos lotes
    rec = add("Recepción y análisis de 14 cantinas del lote 1 (a TK-101)", "L1", t0 + t["muestra_acidez"],
              t["recepcion_14_cantinas"], ["LAB-101", "TK-101"], "R", True)
    add("Recepción y análisis de 14 cantinas del lote 2 (a TK-102, a 4 °C)", "L2", rec.fin, t["recepcion_14_cantinas"],
        ["LAB-101", "TK-102"], "R", True)

    # Lote 1
    c1 = add("CIP de T-301", "L1", tr.fin, t["cip_completo"], ["T-301", "CIP-901"], "P")
    x = add("Carga de 550 L desde TK-101", "L1", c1.fin, t["carga"], ["T-301", "TK-101"], "R", True)
    x = add("Precalentamiento a 25 °C y dosificación en paralelo", "L1", x.fin, t["precalentamiento_lote1"], ["T-301"], "P")
    x = add("Homogeneización y pasteurización", "L1", x.fin, past, ["T-301", "CAL-901"], "P")
    x = add("Enfriamiento a 43 °C con agua de red en la chaqueta", "L1", x.fin, t["enfriar_a_inoculacion"], ["T-301"], "P")
    x = add("Inoculación", "L1", x.fin, t["inocular"], ["T-301"], "P", True)
    x = add("Incubación hasta pH 4,5", "L1", x.fin, inc, ["T-301"], "A")
    x = add("Ruptura del coágulo y saborizado", "L1", x.fin, t["ruptura_saborizado"], ["T-301"], "S")
    add("Confirmación de acidez del lote 1", "L1", x.inicio, t["muestra_acidez"], ["LAB-101"], "S", True)
    x = add("Enfriamiento en placas y transferencia a T-302", "L1", x.fin, t["transferencia"], ["T-301", "T-302", "E-301"], "S", True)
    libre = x.fin
    e1 = add(f"Envasado del lote 1 ({ref_l1})", "L1", libre, env[ref_l1], ["T-302", "MAQ-" + ref_l1], "E", True)
    add("Encanastado o encajonado del lote 1", "L1", e1.inicio, e1.duracion, [], "K", True)
    add("CIP de fin de día de T-302 y de la línea de envasado", "L1", e1.fin, t["cip_completo"], ["T-302", "CIP-901"], "S")

    # Lote 2
    c2 = add("CIP de T-301", "L2", libre, t["cip_completo"], ["T-301", "CIP-901"], "S")
    x = add("Carga de 550 L desde TK-102", "L2", c2.fin, t["carga"], ["T-301", "TK-102"], "S", True)
    x = add("Precalentamiento desde 4 °C a 25 °C y dosificación", "L2", x.fin, t["precalentamiento_lote2"], ["T-301"], "S")
    x = add("Homogeneización y pasteurización", "L2", x.fin, past, ["T-301", "CAL-901"], "S")
    x = add("Enfriamiento a 43 °C con agua de red en la chaqueta", "L2", x.fin, t["enfriar_a_inoculacion"], ["T-301"], "S")
    x = add("Inoculación", "L2", x.fin, t["inocular"], ["T-301"], "S", True)
    x = add("Incubación sin operario hasta pH 4,6, con alarmas remotas", "L2", x.fin, inc, ["T-301"], "A")
    x = add("Ruptura del coágulo y saborizado automáticos", "L2", x.fin, t["ruptura_saborizado"], ["T-301"], "A")
    add("Enfriamiento con agua helada en la chaqueta y mantenimiento a 12–15 °C", "L2", x.fin,
        24 * 60 + t0 - x.fin, ["T-301", "CH-901"], "A")
    return T


def conflictos_recursos(T: list[Tarea], compartidos=("LAB-101", "CAL-901", "TK-101", "TK-102", "CH-901")) -> list[str]:
    errores = []
    por_rec: dict[str, list[Tarea]] = {}
    for x in T:
        for r in x.recursos:
            if r not in compartidos:
                por_rec.setdefault(r, []).append(x)
    for r, ts in por_rec.items():
        ts = sorted(ts, key=lambda z: z.inicio)
        for a, b in zip(ts, ts[1:]):
            if b.inicio < a.fin - 1e-6:
                errores.append(f"{r}: '{a.nombre}' ({hhmm(a.inicio)}–{hhmm(a.fin)}) se cruza con '{b.nombre}' ({hhmm(b.inicio)})")
    return errores


def fuera_de_turno(T: list[Tarea]) -> dict[str, float]:
    """Minutos de cada rol por fuera de su turno (horas extra)."""
    extra = {}
    for x in T:
        if x.rol in TURNOS:
            ini, fin = TURNOS[x.rol]
            fuera = max(0.0, ini - x.inicio) + max(0.0, x.fin - fin)
            extra[x.rol] = max(extra.get(x.rol, 0.0), fuera)
    return extra


def cruces_de_rol(T: list[Tarea]) -> list[str]:
    errores = []
    for rol in TURNOS:
        ts = sorted([x for x in T if x.rol == rol and x.atendida], key=lambda z: z.inicio)
        for a, b in zip(ts, ts[1:]):
            if b.inicio < a.fin - 1e-6:
                errores.append(f"{rol}: '{a.nombre}' se cruza con '{b.nombre}'")
    return errores


def tabla(T: list[Tarea]) -> str:
    filas = ["| Hora exacta | Lote | Actividad | Responsable |", "| --- | --- | --- | --- |"]
    for x in sorted(T, key=lambda z: (z.inicio, z.lote)):
        filas.append(f"| {hhmm(x.inicio)}–{hhmm(x.fin)} | {x.lote} | {x.nombre} | {NOMBRES_ROL[x.rol]} |")
    return "\n".join(filas)


def resumen(p: dict | None = None) -> str:
    p = p or cargar()
    T = programa(p)
    T300 = programa(p, incubacion=p["tiempos_min"]["incubar_maximo"])
    libre = next(x for x in T if x.lote == "L1" and x.nombre.startswith("Enfriamiento en placas")).fin
    inoc2 = next(x for x in T if x.lote == "L2" and x.nombre == "Inoculación").fin
    lineas = ["## Programa diario (lote 1 y lote 2 de YB-200)", "",
              "Horas exactas del modelo. Los documentos las redondean a 5 min.", "", tabla(T), "",
              f"- T-301 queda libre a las {r5(libre)}; el lote 2 termina la inoculación a las {r5(inoc2)}.",
              f"- Conflictos de recursos: {len(conflictos_recursos(T))}; cruces de tareas atendidas por un mismo rol: {len(cruces_de_rol(T))}.",
              "- Minutos fuera de turno con la incubación de 240 min: "
              + ", ".join(f"{k} {v:.0f}" for k, v in fuera_de_turno(T).items()) + ".",
              "- Minutos fuera de turno con la incubación máxima de 300 min: "
              + ", ".join(f"{k} {v:.0f}" for k, v in fuera_de_turno(T300).items()) + ".", ""]
    return "\n".join(lineas)


if __name__ == "__main__":
    print(resumen())
