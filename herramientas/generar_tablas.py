"""Genera las tablas de los documentos a partir del modelo y las escribe en bloques marcados.

En un documento, un bloque generado se marca así:
    <!-- tabla:nombre -->
    ...contenido generado...
    <!-- /tabla:nombre -->
El contenido entre las marcas se reemplaza cada vez que se ejecuta este script.

Uso:  .venv\\Scripts\\python.exe -X utf8 herramientas\\generar_tablas.py
      .venv\\Scripts\\python.exe -X utf8 herramientas\\generar_tablas.py --verificar   (no escribe; falla si algo cambiaría)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import modelo as M

RAIZ = Path(__file__).resolve().parent.parent
CORTOS = {"DC": "David Cortés", "AO": "Ana Orozco", "JR": "Jesús Rivera", "DF": "David Cárdenas",
          "JZ": "José Andrés Zapata", "CH": "Cristian Hoyos"}

# entregable verificable y dependencias de cada paquete de la EDT
ENTREGABLES = {
    "1.1.1": ("Plan aprobado por el cliente", "—"),
    "1.1.2": ("Informes semanales de avance, plazo, costo y valor ganado", "1.1.1"),
    "1.1.3": ("Contratos, órdenes firmadas y trámites de importación", "1.4.1"),
    "1.1.4": ("Acta de cierre y lecciones aprendidas", "1.10.4"),
    "1.2.1": ("Datos de proceso, tiempos y capacidad de la caldera y del cuarto frío validados en planta", "1.1.1"),
    "1.2.2": ("Simulación en Tecnomatix del programa de dos lotes", "1.2.1"),
    "1.2.3": ("Arquitectura, plan de red, zonas IEC 62443 y región de Huawei Cloud aprobados", "1.2.1"),
    "1.2.4": ("Modelos ISA-88 y recetas maestras aprobados", "1.2.1"),
    "1.2.5": ("P&ID, índice de instrumentos y hojas de datos de largo plazo aprobados", "1.2.1"),
    "1.3.1": ("Hojas de datos de equipos, incluidos TK-102 y el circuito de agua helada a la chaqueta", "1.2.5"),
    "1.3.2": ("Lista de E/S y topología de control", "1.2.5"),
    "1.3.3": ("Planos eléctricos y de tableros según RETIE", "1.3.2"),
    "1.3.4": ("Diseño de la estación de encanastado con la mesa acumuladora, espacio para la celda y matriz de riesgos", "1.2.2"),
    "1.3.5": ("Plano de distribución con TK-102", "1.3.1"),
    "1.4.1": ("Cuadro comparativo de proveedores", "Ingeniería conceptual de la oferta"),
    "1.4.2": ("Órdenes emitidas en la semana 4, plan de entregas y nacionalización", "1.3.1, 1.4.1"),
    "1.4.3": ("Protocolos FAT ejecutados por el fabricante y aprobados de forma remota, por videoconferencia", "1.4.2"),
    "1.5.1": ("Programa de fases, lazos PID, enfriamiento nocturno y enclavamientos probado en el emulador", "1.3.2, 1.2.4"),
    "1.5.2": ("Programa de envasado, peso y transporte probado", "1.3.2"),
    "1.5.3": ("Guía de estilo y pantallas de HMI-01 y HMI-02", "1.2.4"),
    "1.5.4": ("Alarmas con prioridades y registro, historiador local y tendencias", "1.5.3"),
    "1.5.5": ("Nodo de borde que opera 72 h sin internet, con imagen en el PC de repuesto", "1.5.4, 1.6.7"),
    "1.6.1": ("Entornos de desarrollo, pruebas y producción con respaldos probados", "1.2.3"),
    "1.6.2": ("Núcleo de la plataforma con pruebas automáticas", "1.2.3"),
    "1.6.3": ("Tres recetas maestras cargadas, órdenes y receta de control escalada", "1.6.2, 1.2.4"),
    "1.6.4": ("Expediente de lote y genealogía probados con lotes simulados", "1.6.3"),
    "1.6.5": ("Flujo de liberación y retención con firma electrónica", "1.6.4"),
    "1.6.6": ("OEE por turno con los datos del arranque (versión 2)", "1.6.4, 1.9.3"),
    "1.6.7": ("Mensajería probada con cortes de internet simulados", "1.6.1, 1.6.2"),
    "1.6.8": ("Inventario, pedidos y despacho en producción", "1.6.2"),
    "1.6.9": ("Compras, requerimiento de materiales, costo por lote y exportación al facturador (versión 2)", "1.6.8"),
    "1.6.10": ("Tablero diario y reportes aprobados por la gerencia (versión 2)", "1.6.6, 1.6.9"),
    "1.6.11": ("Informes de pruebas unitarias, de integración, de carga y de seguridad; manuales", "1.6.2"),
    "1.7.1": ("Gemelo digital en Siemens NX Mechatronics Concept Designer y Tecnomatix con sensores y actuadores virtuales", "1.2.2"),
    "1.7.2": ("Simulación de las líneas de bolsas y vasos y del encajonado manual", "1.3.4"),
    "1.7.3": ("Informe de validación con lotes, recetas y cortes de internet simulados", "1.5.1–1.5.5, 1.6.3–1.6.5, 1.6.7, 1.7.1"),
    "1.8.1": ("Equipos, TK-102, tuberías y soportes instalados", "1.3.5; 1.4.3 para los equipos importados"),
    "1.8.2": ("Tableros e instrumentos conectados", "1.3.3; 1.4.3"),
    "1.8.3": ("Red, nodo de borde, conectividad doble y entorno de producción en servicio", "1.6.1, 1.5.5"),
    "1.8.4": ("Llenadora, dosificación de fruta, controladora, codificador y mesa acumuladora instalados", "1.4.3"),
    "1.9.1": ("Protocolos de lazo firmados", "1.8.2"),
    "1.9.2": ("Protocolos SAT firmados, incluido un corte de internet en planta", "1.9.1, 1.7.3"),
    "1.9.3": ("Lotes conformes de YB-200, YV-150 y YV-300, incluido un lote 2 nocturno de cada referencia", "1.9.2"),
    "1.9.4": ("Registros de puntos críticos, curvas de enfriamiento nocturno y primeros lotes liberados por registro de proceso", "1.9.3"),
    "1.10.1": ("Plan de gestión del cambio, comunicaciones y medición de adopción", "1.1.1"),
    "1.10.2": ("Personal capacitado y evaluado por rol, en el gemelo digital y en la plataforma", "1.7.3"),
    "1.10.3": ("Procedimientos operativos, planos finales, manuales, depósito del código fuente y programa del PLC entregado con la licencia de Studio 5000 de la planta activada", "1.9.2"),
    "1.10.4": ("Acompañamiento con producción en las semanas 22–26, dentro de la estabilización de seis semanas (21–26; el paquete cubre 22–26 y la semana 21 es de arranque/validación), acta de entrega y metas de adopción medidas", "1.9.4, 1.10.2, 1.10.3"),
}


def _resp(h: dict) -> str:
    if len(h) == 1:
        return CORTOS[next(iter(h))]
    return ", ".join(f"{CORTOS[k]} ({M.m(v, 0)})" for k, v in h.items())


def _rango(cods: list[str], pqs: dict) -> str:
    ini, fin = 99, 0
    for c in cods:
        partes = str(pqs[c]["semanas"]).replace("-", "–").split("–")
        ini, fin = min(ini, int(partes[0])), max(fin, int(partes[-1]))
    return f"{ini}–{fin}" if ini != fin else str(ini)


def tablas(r: dict) -> dict[str, str]:
    p, b = r["p"], r["base"]
    cap, op, prod = b["cap"], b["op"], b["prod"]
    ing = cap["ing"]
    pqs = ing["paquetes"]
    carga = M.carga_semanal(p)
    T = {}

    # --- EDT
    filas = ["| Código | Entregable | Paquetes | Horas | Semanas | Millones de COP |", "| --- | --- | --- | --- | --- | --- |"]
    for c, x in ing["cuentas"].items():
        cods = [k for k in pqs if M.cuenta_de(k) == c]
        filas.append(f"| {c} | {x['nombre']} | {x['paquetes']} | {M.m(x['horas'], 0)} | {_rango(cods, pqs)} | {M.m(x['valor'], 2)} |")
    filas.append(f"| **Total** | | **{sum(x['paquetes'] for x in ing['cuentas'].values())}** | **{M.m(ing['horas'], 0)}** | **1–{p['equipo_cremia']['semanas_proyecto']}** | **{M.m(ing['valor'], 2)}** |")
    T["edt_resumen"] = "\n".join(filas)

    filas = ["| Integrante | Rol | Horas | Ocupación | Semana más cargada |", "| --- | --- | --- | --- | --- |"]
    for k, x in ing["personas"].items():
        filas.append(f"| {x['nombre']} | {x['rol']} | {M.m(x['horas'], 0)} | {M.pct(x['ocupacion'], 0)} | {M.m(max(carga[k]), 0)} h |")
    filas.append(f"| **Total** | | **{M.m(ing['horas'], 0)}** | **{M.pct(ing['ocupacion'], 0)}** | |")
    T["edt_personas"] = "\n".join(filas)

    filas = ["| Código | Paquete de trabajo | Entregable verificable | Responsable (horas) | Horas | Semanas | Depende de |",
             "| --- | --- | --- | --- | --- | --- | --- |"]
    for c, x in pqs.items():
        ent, dep = ENTREGABLES[c]
        filas.append(f"| {c} | {x['nombre']} | {ent} | {_resp(x['h'])} | {M.m(x['horas'], 0)} | {x['semanas']} | {dep} |")
    T["edt_diccionario"] = "\n".join(filas)

    filas = ["| Integrante | Tipo de valor | Horas | Tarifa (COP/h) | Factor sobre su costo | Millones de COP |", "| --- | --- | --- | --- | --- | --- |"]
    for k, x in ing["personas"].items():
        filas.append(f"| {x['nombre']} | {x['tipo']} | {M.m(x['horas'], 0)} | {M.m(x['tarifa'], 0)} | {M.m(x['factor'], 2)} | {M.m(x['valor'], 2)} |")
    filas.append(f"| **Total** | | **{M.m(ing['horas'], 0)}** | **{M.m(ing['tarifa_promedio'], 0)} en promedio** | | **{M.m(ing['valor'], 2)}** |")
    T["tarifas"] = "\n".join(filas)

    filas = ["| Cuenta de la EDT | Actividad | Horas | Millones de COP |", "| --- | --- | --- | --- |"]
    for c, x in ing["cuentas"].items():
        filas.append(f"| {c} | {x['nombre']} | {M.m(x['horas'], 0)} | {M.m(x['valor'], 2)} |")
    filas.append(f"| | **Total** | **{M.m(ing['horas'], 0)}** | **{M.m(ing['valor'], 2)}** |")
    T["cuentas_valor"] = "\n".join(filas)

    alcance = {"1. Diseño, procura y gestión de compras": "1.1.1, 1.1.3 y cuentas 1.2 a 1.4",
               "2. Implementación, software, puesta en marcha y adopción": "1.1.2, 1.1.4 y cuentas 1.5 a 1.10"}
    filas = ["| Contrato | Paquetes de la EDT | Semanas | Horas | Millones de COP |", "| --- | --- | --- | --- | --- |"]
    for n, x in ing["contratos"].items():
        filas.append(f"| {n} | {alcance[n]} | {x['semanas']} | {M.m(x['horas'], 0)} | {M.m(x['valor'])} |")
    filas.append(f"| **Total** | | **1–{p['equipo_cremia']['semanas_proyecto']}** | **{M.m(ing['horas'], 0)}** | **{M.m(ing['valor'])}** |")
    T["contratos"] = "\n".join(filas)

    filas = ["| Hito | Semana | Porcentaje | Millones de COP |", "| --- | --- | --- | --- |"]
    for nombre, sem, pc in p["finanzas"]["pagos_hitos"]:
        filas.append(f"| {nombre} | {sem} | {M.pct(pc, 0)} | {M.m(pc * cap['total'])} |")
    filas.append(f"| **Total** | | **100 %** | **{M.m(cap['total'])}** |")
    T["pagos"] = "\n".join(filas)

    filas = ["| Código | Actividad | Semanas | Inicio | Fin |", "| --- | --- | --- | --- | --- |"]
    for c, x in ing["cuentas"].items():
        cods = [k for k in pqs if M.cuenta_de(k) == c]
        rg = _rango(cods, pqs)
        ini, fin = M.fechas_semanas(rg)
        filas.append(f"| {c} | **{x['nombre']}** | {rg} | {ini} | {fin} |")
        for k in cods:
            i2, f2 = M.fechas_semanas(pqs[k]["semanas"])
            filas.append(f"| {k} | {pqs[k]['nombre']} | {pqs[k]['semanas']} | {i2} | {f2} |")
    for nombre, rg in (("Fabricación de los equipos de largo plazo", "4–13"),
                       ("Transporte y nacionalización de los equipos importados", "15–18"),
                       ("Parada de planta para la conexión al tanque de proceso", "19")):
        ini, fin = M.fechas_semanas(rg)
        filas.append(f"| — | {nombre} | {rg} | {ini} | {fin} |")
    T["cronograma"] = "\n".join(filas)

    # --- economía
    filas = ["| N.º | Rubro tecnológico o maquinaria cotizada | Valor estimado (millones de COP) |", "| --- | --- | --- |"]
    for k, x in p["capex"]["rubros"].items():
        filas.append(f"| {k} | {x['nombre']} | {M.m(x['valor'])} |")
    filas += [f"| | **Subtotal de equipos y software** | **{M.m(cap['equipos'])}** |",
              f"| | Servicios de ingeniería de Cremia Automations ({M.m(ing['horas'], 0)} h en dos contratos, con tarifa por integrante) | {M.m(cap['ingenieria'])} |",
              f"| | Montaje mecánico y eléctrico por contratistas certificados ({M.pct(p['capex']['montaje_pct'], 0)} de los equipos físicos, sin la nube ni la licencia) | {M.m(cap['montaje'])} |",
              f"| | **Subtotal** | **{M.m(cap['subtotal'])}** |",
              f"| | Contingencia del proyecto ({M.pct(p['capex']['contingencia_pct'], 0)}) | {M.m(cap['contingencia'])} |",
              f"| | **Inversión total** | **{M.m(cap['total'])}** |",
              f"| | Margen no percibido por {p['capex']['dias_parada']} días de parada de planta durante el montaje | {M.m(b['parada'])} |",
              f"| | **Desembolso total del año 0** | **{M.m(cap['total'] + b['parada'])}** |"]
    T["capex"] = "\n".join(filas)

    g = cap["grupos"]
    filas = ["| Grupo | Rubros | Millones de COP | Participación |", "| --- | --- | --- | --- |"]
    def _lista(grupos_rub):
        ks = [str(k) for k, x in p["capex"]["rubros"].items() if x["grupo"] in grupos_rub]
        return ", ".join(ks[:-1]) + " y " + ks[-1] if len(ks) > 1 else ks[0]
    grupos = [("Equipos de proceso", "proceso", _lista({"proceso"})),
              ("Envasado, inspección y transporte", "envasado", _lista({"envasado"})),
              ("Instrumentación, control, nodo de borde, nube y licencia del PLC", None,
               _lista({"instrumentacion", "control"}))]
    for nombre, clave, rub in grupos:
        v = g[clave] if clave else g["instrumentacion"] + g["control"]
        filas.append(f"| {nombre} | {rub} | {M.m(v)} | {M.pct(v / cap['total'])} |")
    filas.append(f"| Ingeniería de Cremia (incluye {M.m(ing['software_horas'], 0)} h de software) | — | {M.m(cap['ingenieria'])} | {M.pct(cap['ingenieria'] / cap['total'])} |")
    mc = cap["montaje"] + cap["contingencia"]
    filas.append(f"| Montaje y contingencia | — | {M.m(mc)} | {M.pct(mc / cap['total'])} |")
    filas.append(f"| **Total** | | **{M.m(cap['total'])}** | **100 %** |")
    T["capex_grupos"] = "\n".join(filas)

    filas = ["| Concepto operativo anual | Millones de COP por año |", "| --- | --- |",
             f"| Margen de contribución anual con la propuesta (600 lotes, unidades conformes) | {M.m(prod['propuesta']['margen'])} |",
             f"| Margen de contribución actual de la planta (300 lotes, unidades conformes) | {M.m(-prod['actual']['margen'])} |",
             f"| **Margen de contribución adicional** | **{M.m(prod['margen_adicional'])}** |"]
    for n, v in op["partidas"].items():
        filas.append(f"| {n} | {M.m(-v)} |")
    filas.append(f"| **Beneficio operativo anual a plena producción, antes de impuestos** | **{M.m(prod['margen_adicional'] - op['total'])}** |")
    T["beneficio"] = "\n".join(filas)

    F = b["filas"]
    fila = lambda nombre, clave, signo=1: "| " + nombre + " | — | " + " | ".join(M.m(signo * x[clave]) for x in F) + " |"
    filas = ["| Concepto financiero | Año 0 | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 |", "| --- | --- | --- | --- | --- | --- | --- |",
             f"| Inversión y parada por montaje | {M.m(b['despues'][0])} | — | — | — | — | — |",
             fila("Margen adicional (rampa de ventas)", "margen"),
             fila("Costos de operación", "opex", -1),
             fila("Resultado operativo (EBITDA)", "ebitda"),
             fila("Depreciación (no es salida de caja)", "dep"),
             fila("Impuesto de renta (35 %)", "impuesto", -1),
             fila("Variación del capital de trabajo", "dct", -1),
             fila("Recuperación del capital de trabajo y valor residual en libros", "final"),
             "| **Flujo neto antes de impuestos** | " + " | ".join(M.m(x) for x in b["antes"]) + " |",
             "| **Flujo neto después de impuestos** | " + " | ".join(M.m(x) for x in b["despues"]) + " |"]
    acum, s = [], 0.0
    for x in b["despues"]:
        s += x
        acum.append(s)
    filas.append("| Flujo acumulado después de impuestos | " + " | ".join(M.m(x) for x in acum) + " |")
    T["flujo"] = "\n".join(filas)

    filas = ["| Indicador | Después de impuestos (principal) | Antes de impuestos |", "| --- | --- | --- |",
             f"| VPN al 15 % | COP {M.m(b['vpn'])} millones | COP {M.m(b['vpn_antes'])} millones |",
             f"| TIR | {M._fmt_tir(b['tir'])} | {M._fmt_tir(b['tir_antes'])} |",
             f"| Periodo de recuperación | {M._fmt_rec(b['rec'])} | {M._fmt_rec(b['rec_antes'])} |",
             f"| Relación beneficio-costo (valor presente de los flujos ÷ desembolso) | {M.m(b['bc'], 2)} | — |",
             f"| Volumen de equilibrio (VPN = 0) | {M.pct(r['eq_vol'])} del plan | — |",
             f"| Vasos de equilibrio, con las bolsas al 100 % | {M.pct(r['eq_vasos'])} del plan | — |"]
    T["indicadores"] = "\n".join(filas)

    filas = ["| Escenario | VPN al 15 % (millones de COP) | TIR | Recuperación |", "| --- | --- | --- | --- |"]
    for n, s2 in r["sens"].items():
        filas.append(f"| {n} | {M.m(s2['vpn'])} | {M._fmt_tir(s2['tir'])} | {M._fmt_rec(s2['rec'])} |")
    sb = r["solo_bolsas"]
    filas.append(f"| Solo preparación y bolsas: 600 lotes de YB-200 sin línea de vasos (inversión de {M.m(sb['cap']['total'])}) | {M.m(sb['vpn'])} | {M._fmt_tir(sb['tir'])} | {M._fmt_rec(sb['rec'])} |")
    T["sensibilidad"] = "\n".join(filas)

    filas = ["| Año | Intereses | Abono a capital | Cuota | Saldo al final del año | Flujo del proyecto después de impuestos | Ahorro tributario de los intereses | Flujo después de la deuda |",
             "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for c in r["credito"]:
        filas.append(f"| {c['ano']} | {M.m(c['interes'])} | {M.m(c['abono'])} | {M.m(c['cuota'])} | {M.m(c['saldo'])} | {M.m(c['flujo_proyecto'])} | {M.m(c['escudo'])} | {M.m(c['despues_deuda'])} |")
    T["credito"] = "\n".join(filas)

    filas = ["| Referencia | Unidades llenadas al año | Unidades conformes al año | Ventas (millones de COP) | Margen de contribución (millones de COP) |",
             "| --- | --- | --- | --- | --- |"]
    for ref, x in prod["propuesta"]["refs"].items():
        filas.append(f"| {ref} | {M.m(x['llenadas_ano'], 0)} | {M.m(x['conformes_ano'], 0)} | {M.m(x['ventas'])} | {M.m(x['margen'])} |")
    pr = prod["propuesta"]
    filas.append(f"| **Total** | **{M.m(pr['llenadas_ano'], 0)}** | **{M.m(pr['conformes_ano'], 0)}** | **{M.m(pr['ventas'])}** | **{M.m(pr['margen'])}** |")
    T["produccion_refs"] = "\n".join(filas)
    return T


PATRON = re.compile(r"(<!-- tabla:(?P<n>[a-z_]+) -->\n)(.*?)(\n<!-- /tabla:(?P=n) -->)", re.S)


def aplicar(texto: str, T: dict) -> str:
    def rep(mo):
        n = mo.group("n")
        if n not in T:
            raise KeyError(f"tabla desconocida: {n}")
        return mo.group(1) + T[n] + mo.group(4)
    return PATRON.sub(rep, texto)


def documentos():
    for ruta in RAIZ.rglob("*.md"):
        if ".venv" in ruta.parts or ".git" in ruta.parts:
            continue
        yield ruta


def main(verificar: bool = False) -> int:
    T = tablas(M.resultados())
    cambios = []
    for ruta in documentos():
        texto = ruta.read_text(encoding="utf-8")
        if "<!-- tabla:" not in texto:
            continue
        nuevo = aplicar(texto, T)
        if nuevo != texto:
            cambios.append(ruta.relative_to(RAIZ).as_posix())
            if not verificar:
                ruta.write_text(nuevo, encoding="utf-8")
    for c in cambios:
        print(("desactualizado: " if verificar else "actualizado: ") + c)
    return 1 if (verificar and cambios) else 0


if __name__ == "__main__":
    sys.exit(main("--verificar" in sys.argv))
