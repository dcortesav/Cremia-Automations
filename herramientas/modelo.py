"""Modelo de la propuesta de la línea de yogur de La Hacienda.

Calcula producción, tiempos, horas y valor de la ingeniería, inversión, costos de operación,
flujo de caja antes y después de impuestos, indicadores, sensibilidades y crédito a partir de
herramientas/parametros.yaml. Ejecutado como script, escribe herramientas/resultados.md, que es
la fuente de las cifras que citan los documentos del repositorio.

Uso:  .venv\\Scripts\\python.exe herramientas\\modelo.py
"""
from __future__ import annotations

import copy
import math
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent
PARAMETROS = RAIZ / "parametros.yaml"


def cargar(ruta: Path = PARAMETROS) -> dict:
    with open(ruta, encoding="utf-8") as f:
        p = yaml.safe_load(f)
    tasa = p["general"]["tasa_cambio_cop_usd"]
    for r in p["capex"]["rubros"].values():
        if "valor" not in r and "valor_usd" in r:
            r["valor"] = r["valor_usd"] * tasa / 1e6
    return p


# --------------------------------------------------------------------------- formato
def m(x: float, d: int = 1) -> str:
    """Formato colombiano: punto de miles y coma decimal."""
    neg = x < 0
    s = f"{abs(x):,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return ("−" if neg else "") + s


def pct(x: float, d: int = 1) -> str:
    return m(100 * x, d) + " %"


def hhmm(minutos: float) -> str:
    minutos = int(round(minutos)) % (24 * 60)
    return f"{minutos // 60}:{minutos % 60:02d}"


MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
INICIO_PROYECTO = (2027, 1, 18)  # lunes de la semana 1


def fechas_semanas(rango: str) -> tuple[str, str]:
    """'3–12' -> ('1 feb', '9 abr'): lunes de la primera semana y viernes de la última."""
    import datetime as dt
    partes = rango.replace("-", "–").split("–")
    a, b = int(partes[0]), int(partes[-1])
    base = dt.date(*INICIO_PROYECTO)
    ini = base + dt.timedelta(weeks=a - 1)
    fin = base + dt.timedelta(weeks=b - 1, days=4)
    f = lambda d: f"{d.day} {MESES[d.month - 1]}"
    return f(ini), f(fin)


# --------------------------------------------------------------------------- producción
def produccion(p: dict, mezcla: dict | None = None, factor_vol: float = 1.0,
               factor_vasos: float = 1.0) -> dict:
    ea, pr = p["estado_actual"], p["propuesta"]
    dias = p["general"]["dias_operacion"]
    actual_llenadas_dia = ea["bolsas_llenadas_lote"] * ea["lotes_dia"]
    actual_nc_dia = round(actual_llenadas_dia * ea["no_conforme"])
    actual_conformes_dia = actual_llenadas_dia - actual_nc_dia
    actual = {
        "llenadas_dia": actual_llenadas_dia,
        "no_conformes_dia": actual_nc_dia,
        "conformes_dia": actual_conformes_dia,
        "llenadas_ano": actual_llenadas_dia * dias,
        "conformes_ano": actual_conformes_dia * dias,
    }
    actual["ventas"] = actual["conformes_ano"] * ea["precio_bolsa"] / 1e6
    actual["costo_variable"] = actual["llenadas_ano"] * ea["costo_variable_bolsa"] / 1e6
    actual["margen"] = actual["ventas"] - actual["costo_variable"]

    mezcla = mezcla or pr["ciclo_lotes"]
    lotes_ano = pr["lotes_dia"] * dias
    lotes_ciclo = sum(mezcla.values())
    ciclos = lotes_ano / lotes_ciclo
    refs = {}
    for ref, datos in pr["referencias"].items():
        f = factor_vol * (factor_vasos if ref != "YB-200" else 1.0)
        lotes = mezcla.get(ref, 0) * ciclos
        llenadas = datos["unidades_lote"] * lotes * f
        conformes = round(llenadas * (1 - pr["no_conforme"]))
        refs[ref] = {
            "lotes_ano": lotes,
            "llenadas_ciclo": datos["unidades_lote"] * mezcla.get(ref, 0),
            "llenadas_ano": llenadas,
            "conformes_ano": conformes,
            "ventas": conformes * datos["precio"] / 1e6,
            "costo_variable": llenadas * datos["costo_variable"] / 1e6,
        }
        refs[ref]["margen"] = refs[ref]["ventas"] - refs[ref]["costo_variable"]
    prop = {
        "refs": refs,
        "lotes_ano": lotes_ano,
        "llenadas_ano": sum(r["llenadas_ano"] for r in refs.values()),
        "conformes_ano": sum(r["conformes_ano"] for r in refs.values()),
        "ventas": sum(r["ventas"] for r in refs.values()),
        "costo_variable": sum(r["costo_variable"] for r in refs.values()),
    }
    prop["margen"] = prop["ventas"] - prop["costo_variable"]
    prop["conformes_dia"] = prop["conformes_ano"] / dias
    return {"actual": actual, "propuesta": prop,
            "margen_adicional": prop["margen"] - actual["margen"],
            "ventas_adicionales": prop["ventas"] - actual["ventas"],
            "costo_variable_adicional": prop["costo_variable"] - actual["costo_variable"]}


def oee(p: dict) -> dict:
    ea, pr = p["estado_actual"], p["propuesta"]
    t, par, v = ea["tiempo_envasado_min"], ea["paradas_envasado_min"], ea["velocidad_nominal_empacadora"]
    llenadas = ea["bolsas_llenadas_lote"]
    conformes = llenadas - round(llenadas * ea["no_conforme"])
    disp = (t - par) / t
    rend = llenadas / (v * (t - par))
    cal = 1 - ea["no_conforme"]  # 94,9 %: 100 % − 5,06 % del caso (2.898 de 3.052 bolsas)
    meta = pr["oee_meta"]
    return {"actual": {"disponibilidad": disp, "rendimiento": rend, "calidad": cal,
                       "oee": disp * rend * cal},
            "meta": {**meta, "oee": meta["disponibilidad"] * meta["rendimiento"] * meta["calidad"]}}


def tiempos_envasado(p: dict) -> dict:
    meta = p["propuesta"]["oee_meta"]
    ap = meta["disponibilidad"] * meta["rendimiento"]
    return {ref: d["unidades_lote"] / (d["velocidad"] * ap)
            for ref, d in p["propuesta"]["referencias"].items()}


def tiempo_estandar(p: dict, ref: str = "YB-200") -> dict:
    t = p["tiempos_min"]
    env = tiempos_envasado(p)[ref]
    past = t["calentar_a_62"] + t["homogeneizar"] + t["calentar_a_87"] + t["sostener"]
    fases = {
        "Recibir y analizar la leche": t["recepcion_14_cantinas"],
        "Cargar el tanque de proceso": t["carga"],
        "Precalentar y dosificar (en paralelo)": t["precalentamiento_lote1"],
        "Homogeneizar y pasteurizar": past,
        "Enfriar a inoculación": t["enfriar_a_inoculacion"],
        "Inocular": t["inocular"],
        "Incubar": t["incubar"],
        "Romper el coágulo y saborizar": t["ruptura_saborizado"],
        "Enfriar en placas y transferir": t["transferencia"],
        "Envasar": env,
    }
    total = sum(fases.values())
    ocupacion = (t["carga"] + t["precalentamiento_lote1"] + past + t["enfriar_a_inoculacion"]
                 + t["inocular"] + t["incubar"] + t["ruptura_saborizado"] + t["transferencia"])
    return {"fases": fases, "total": total, "pasteurizacion": past,
            "ocupacion_t301": ocupacion, "ocupacion_con_cip": ocupacion + t["cip_completo"]}


# --------------------------------------------------------------------------- ingeniería
def paquetes(p: dict) -> dict:
    return {k: v for k, v in p["edt"].items() if "h" in v}


def cuenta_de(codigo: str) -> str:
    partes = codigo.split(".")
    return ".".join(partes[:2])


def capacidad_semanal(p: dict) -> list[float]:
    """Horas disponibles por persona en cada semana, descontando los festivos (8,4 h por día)."""
    eq = p["equipo_cremia"]
    fest = eq.get("festivos_por_semana", {}) or {}
    return [eq["horas_semana"] * (5 - fest.get(s, 0)) / 5 for s in range(1, eq["semanas_proyecto"] + 1)]


def carga_semanal(p: dict) -> dict[str, list[float]]:
    """Horas por integrante y semana. Cada paquete reparte sus horas entre sus semanas en
    proporción a los días hábiles de cada semana (las semanas con festivos reciben menos)."""
    n = p["equipo_cremia"]["semanas_proyecto"]
    cap = capacidad_semanal(p)
    carga = {k: [0.0] * n for k in p["equipo_cremia"]["integrantes"]}
    for pq in paquetes(p).values():
        partes = str(pq["semanas"]).replace("-", "–").split("–")
        a, b = int(partes[0]), int(partes[-1])
        peso = sum(cap[s - 1] for s in range(a, b + 1))
        for k, h in pq["h"].items():
            for s in range(a, b + 1):
                carga[k][s - 1] += h * cap[s - 1] / peso
    return carga


def ingenieria(p: dict, factor_horas_software: float = 1.0) -> dict:
    eq = p["equipo_cremia"]
    tarifas = {k: v["tarifa"] for k, v in eq["integrantes"].items()}
    sw = p["paquetes_software"]
    por_paquete, por_persona, por_cuenta = {}, {k: 0.0 for k in tarifas}, {}
    for cod, pq in paquetes(p).items():
        es_sw = any(cod == s or cod.startswith(s + ".") for s in sw)
        f = factor_horas_software if es_sw else 1.0
        horas = {k: h * f for k, h in pq["h"].items()}
        valor = sum(h * tarifas[k] for k, h in horas.items()) / 1e6
        por_paquete[cod] = {"nombre": pq["nombre"], "semanas": pq["semanas"], "horas": sum(horas.values()),
                            "valor": valor, "h": horas, "software": es_sw}
        for k, h in horas.items():
            por_persona[k] += h
        c = cuenta_de(cod)
        acc = por_cuenta.setdefault(c, {"nombre": p["edt"][c]["nombre"], "horas": 0.0, "valor": 0.0, "paquetes": 0,
                                        "_cop": 0.0})
        acc["horas"] += sum(horas.values())
        # se acumula en pesos y se divide al final, para que el redondeo no dependa del orden de la suma
        acc["_cop"] += sum(h * tarifas[k] for k, h in horas.items())
        acc["valor"] = acc["_cop"] / 1e6
        acc["paquetes"] += 1
    capacidad = sum(capacidad_semanal(p))
    total_h = sum(por_persona.values())
    total_v = sum(x["valor"] for x in por_paquete.values())
    nomina = eq["nomina_mensual"] * eq["semanas_proyecto"] / 52 * 12
    personas = {k: {**eq["integrantes"][k], "horas": h, "valor": h * tarifas[k] / 1e6,
                    "ocupacion": h / capacidad,
                    "factor": tarifas[k] / eq["integrantes"][k]["costo_hora"]}
                for k, h in por_persona.items()}
    contratos = {}
    for nombre, c in p["contratos"].items():
        sel = [x for cod, x in por_paquete.items()
               if any(cod == s or cod.startswith(s + ".") for s in c["paquetes"])]
        contratos[nombre] = {"semanas": c["semanas"], "horas": sum(x["horas"] for x in sel),
                             "valor": sum(x["valor"] for x in sel)}
    software_h = sum(x["horas"] for x in por_paquete.values() if x["software"])
    software_v = sum(x["valor"] for x in por_paquete.values() if x["software"])
    return {"paquetes": por_paquete, "personas": personas, "cuentas": por_cuenta,
            "contratos": contratos, "horas": total_h, "valor": total_v,
            "capacidad_persona": capacidad, "capacidad_total": capacidad * len(personas),
            "ocupacion": total_h / (capacidad * len(personas)), "nomina": nomina,
            "factor_nomina": total_v / nomina, "tarifa_promedio": total_v * 1e6 / total_h,
            "software_horas": software_h, "software_valor": software_v}


# --------------------------------------------------------------------------- inversión
def capex(p: dict, factor_capex: float = 1.0, factor_horas_software: float = 1.0,
          incluir_vasos: bool = True) -> dict:
    c = p["capex"]
    rub = c["rubros"]
    peso = {k: (1 - r.get("vasos", 0.0)) if not incluir_vasos else 1.0 for k, r in rub.items()}
    equipos = sum(r["valor"] * peso[k] for k, r in rub.items())
    sin_montaje = sum(r["valor"] * peso[k] for k, r in rub.items() if r.get("nube") or r.get("licencia"))
    ing = ingenieria(p, factor_horas_software)
    ingenieria_v = ing["valor"]
    montaje = c["montaje_pct"] * (equipos - sin_montaje)
    subtotal = equipos + ingenieria_v + montaje
    contingencia = c["contingencia_pct"] * subtotal
    total = (subtotal + contingencia) * factor_capex
    vasos = sum(r["valor"] * r.get("vasos", 0.0) for r in rub.values()) \
        * (1 + c["montaje_pct"]) * (1 + c["contingencia_pct"])
    sw_base = sum(r["valor"] * peso[k] for k, r in rub.items() if r.get("software")) + ing["software_valor"]
    clase_sw = sw_base * (1 + c["contingencia_pct"]) * factor_capex
    clase_eq = total - clase_sw
    grupos = {}
    for k, r in rub.items():
        grupos.setdefault(r["grupo"], 0.0)
        grupos[r["grupo"]] += r["valor"] * peso[k]
    mant_base = sum(r["valor"] * peso[k] for k, r in rub.items() if k not in c["rubros_sin_mantenimiento"])
    return {"equipos": equipos, "ingenieria": ingenieria_v, "montaje": montaje, "subtotal": subtotal,
            "contingencia": contingencia, "total": total, "vasos": vasos, "fase1": total - vasos,
            "clase_software": clase_sw, "clase_equipos": clase_eq, "grupos": grupos,
            "base_mantenimiento": mant_base, "ing": ing}


def opex(p: dict, cap: dict) -> dict:
    o, per = p["operacion"], p["personal"]
    hora = per["salario_operario"] / per["horas_mes"]
    d = per["domingo"]
    domingo = (d["operarios"] * d["horas"] * p["general"]["domingos"] * hora
               * d["factor_hora_extra_dominical"] * per["factor_prestacional"]) / 1e6
    lab = o["laboratorio_externo"]["analisis"] * o["laboratorio_externo"]["costo_cop"] / 1e6
    licencia = o["licencia_studio5000_anual_usd"] * p["general"]["tasa_cambio_cop_usd"] / 1e6
    partidas = {
        "Mantenimiento preventivo de equipos de proceso, instrumentación y envasado": o["mantenimiento_pct"] * cap["base_mantenimiento"],
        "Plan de servicio Cremia: nube Huawei": o["plan_servicio_cremia"]["nube_huawei"],
        "Plan de servicio Cremia: soporte y evolución del software y del control": o["plan_servicio_cremia"]["soporte_y_evolucion"],
        "Mantenimiento anual de la licencia de Studio 5000 de la planta": licencia,
        "Conectividad doble (fibra y 4G)": o["conectividad"],
        "Operario adicional para el segundo lote": per["operario_anual"],
        "Turno del domingo (horas extra dominicales)": domingo,
        "Horas extra por incubaciones largas y disponibilidad nocturna": per["horas_extra_y_disponibilidad"],
        "Laboratorio externo: microbiología por muestreo": lab,
    }
    return {"partidas": partidas, "total": sum(partidas.values()), "hora_ordinaria": hora,
            "domingo": domingo, "licencia": licencia}


# --------------------------------------------------------------------------- flujo de caja
def vpn(flujos: list[float], tasa: float) -> float:
    return sum(f / (1 + tasa) ** t for t, f in enumerate(flujos))


def tir(flujos: list[float]) -> float | None:
    lo, hi = -0.99, 5.0
    if vpn(flujos, lo) * vpn(flujos, hi) > 0:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2
        if vpn(flujos, lo) * vpn(flujos, mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def recuperacion(flujos: list[float]) -> float | None:
    acum = flujos[0]
    for t in range(1, len(flujos)):
        if acum + flujos[t] >= 0:
            return t - 1 + (-acum) / flujos[t]
        acum += flujos[t]
    return None


def flujo(p: dict, factor_vol=1.0, factor_vasos=1.0, factor_precio=1.0, factor_leche=1.0,
          factor_capex=1.0, factor_horas_software=1.0, valor_residual=True, mezcla=None,
          incluir_vasos=True) -> dict:
    p = copy.deepcopy(p)
    if factor_precio != 1.0:
        p["estado_actual"]["precio_bolsa"] *= factor_precio
        for r in p["propuesta"]["referencias"].values():
            r["precio"] *= factor_precio
    if factor_leche != 1.0:
        p["estado_actual"]["costo_variable_bolsa"] += p["propuesta"]["leche_cop_bolsa_actual"] * (factor_leche - 1)
        for r in p["propuesta"]["referencias"].values():
            r["costo_variable"] += r["leche_cop"] * (factor_leche - 1)
    prod = produccion(p, mezcla=mezcla, factor_vol=factor_vol, factor_vasos=factor_vasos)
    cap = capex(p, factor_capex, factor_horas_software, incluir_vasos)
    op = opex(p, cap)
    fin = p["finanzas"]
    ct = fin["capital_trabajo"]
    base = ct["base_dias"]
    ct_pleno = (prod["ventas_adicionales"] * ct["cartera_dias"] / base
                + prod["costo_variable_adicional"] * (ct["inventario_dias"] - ct["proveedores_dias"]) / base)
    parada = prod["actual"]["margen"] / p["general"]["dias_operacion"] * p["capex"]["dias_parada"]
    dep = cap["clase_equipos"] / fin["vida_equipos"] + cap["clase_software"] / fin["vida_software"]
    residual = cap["clase_equipos"] * (1 - fin["horizonte"] / fin["vida_equipos"]) if valor_residual else 0.0
    filas, antes, despues = [], [-(cap["total"] + parada)], [-(cap["total"] + parada)]
    ct_prev = 0.0
    for t, r in enumerate(fin["rampa"], start=1):
        margen = r * prod["margen_adicional"]
        ebitda = margen - op["total"]
        imp = max(0.0, fin["impuesto_renta"] * (ebitda - dep))
        ct_t = r * ct_pleno
        dct = ct_t - ct_prev
        ct_prev = ct_t
        final = (ct_t + residual) if t == fin["horizonte"] else 0.0
        filas.append({"ano": t, "margen": margen, "opex": op["total"], "ebitda": ebitda, "dep": dep,
                      "impuesto": imp, "dct": dct, "final": final,
                      "antes": ebitda - dct + final, "despues": ebitda - imp - dct + final})
        antes.append(ebitda - dct + final)
        despues.append(ebitda - imp - dct + final)
    tasa = fin["tasa_descuento"]
    return {"prod": prod, "cap": cap, "op": op, "parada": parada, "dep": dep, "residual": residual,
            "ct_pleno": ct_pleno, "filas": filas, "antes": antes, "despues": despues,
            "vpn_antes": vpn(antes, tasa), "vpn": vpn(despues, tasa),
            "tir_antes": tir(antes), "tir": tir(despues),
            "rec_antes": recuperacion(antes), "rec": recuperacion(despues),
            "bc": (vpn(despues, tasa) + cap["total"] + parada) / (cap["total"] + parada)}


def equilibrio(p: dict, campo: str) -> float:
    lo, hi = 0.0, 1.5
    for _ in range(100):
        mid = (lo + hi) / 2
        if flujo(p, **{campo: mid})["vpn"] < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def credito(p: dict, f: dict) -> list[dict]:
    c, fin = p["finanzas"]["credito"], p["finanzas"]
    principal = c["porcentaje"] * f["cap"]["total"]
    r, n, g = c["tasa"], c["anos"], c["gracia_anos"]
    cuota_amort = principal * r / (1 - (1 + r) ** -(n - g))
    saldo, filas = principal, []
    for t in range(1, n + 1):
        interes = saldo * r
        if t <= g:
            abono, cuota = 0.0, interes
        else:
            cuota = cuota_amort
            abono = cuota - interes
        saldo -= abono
        fila = f["filas"][t - 1]
        operativo = fila["despues"] - (fila["final"] if t == n else 0.0)
        escudo = fin["impuesto_renta"] * interes
        filas.append({"ano": t, "interes": interes, "abono": abono, "cuota": cuota, "saldo": max(saldo, 0.0),
                      "flujo_proyecto": operativo, "escudo": escudo,
                      "despues_deuda": operativo + escudo - cuota})
    return filas


# --------------------------------------------------------------------------- resultados
def resultados(p: dict | None = None) -> dict:
    p = p or cargar()
    base = flujo(p)
    umbral = p["finanzas"]["cartas_intencion_vasos"]
    sens = {
        "Base": base,
        "Volumen vendido al 90 %": flujo(p, factor_vol=0.9),
        "Volumen vendido al 80 %": flujo(p, factor_vol=0.8),
        f"Vasos vendidos al {pct(umbral, 0)}, umbral de las cartas de intención (bolsas al 100 %)": flujo(p, factor_vasos=umbral),
        "Vasos vendidos al 80 % (bolsas al 100 %)": flujo(p, factor_vasos=0.8),
        "Precio de venta −5 %": flujo(p, factor_precio=0.95),
        "Precio de venta +5 %": flujo(p, factor_precio=1.05),
        "Leche cruda +10 %": flujo(p, factor_leche=1.10),
        "Leche cruda −10 %": flujo(p, factor_leche=0.90),
        "Inversión +10 %": flujo(p, factor_capex=1.10),
        "Inversión −10 %": flujo(p, factor_capex=0.90),
        "Horas de software +30 %": flujo(p, factor_horas_software=1.30),
        "Sin valor residual": flujo(p, valor_residual=False),
    }
    solo_bolsas = flujo(p, mezcla={"YB-200": 10}, incluir_vasos=False)
    return {"p": p, "base": base, "sens": sens, "solo_bolsas": solo_bolsas,
            "umbral_cartas": umbral, "vpn_umbral_cartas": sens[next(k for k in sens if "umbral" in k)]["vpn"],
            "eq_vol": equilibrio(p, "factor_vol"), "eq_vasos": equilibrio(p, "factor_vasos"),
            "credito": credito(p, base), "oee": oee(p), "envasado": tiempos_envasado(p),
            "te": tiempo_estandar(p)}


def _fmt_rec(x):
    return "más de 5 años" if x is None else m(x) + " años"


def _fmt_tir(x):
    return "negativa" if x is None else pct(x)


def reporte(r: dict) -> str:
    p, b = r["p"], r["base"]
    prod, cap, op, ing = b["prod"], b["cap"], b["op"], b["cap"]["ing"]
    act, pro = prod["actual"], prod["propuesta"]
    L = ["# Resultados del modelo de la propuesta", "",
         "Archivo generado por `herramientas/modelo.py` a partir de `herramientas/parametros.yaml`. "
         "No se edita a mano. Millones de COP de 2026, sin IVA.", ""]
    o = r["oee"]
    L += ["## Producción y calidad", "",
          "| Concepto | Situación actual | Propuesta |", "| --- | --- | --- |",
          f"| Lotes al año | {m(p['general']['dias_operacion'],0)} | {m(pro['lotes_ano'],0)} |",
          f"| Unidades llenadas al año | {m(act['llenadas_ano'],0)} | {m(pro['llenadas_ano'],0)} |",
          f"| Unidades conformes al año | {m(act['conformes_ano'],0)} | {m(pro['conformes_ano'],0)} |",
          f"| Unidades conformes por día | {m(act['conformes_dia'],0)} | {m(pro['conformes_dia'],0)} |",
          f"| Unidades conformes por operario al día | {m(act['conformes_dia']/p['estado_actual']['operarios'],0)} | {m(pro['conformes_dia']/p['propuesta']['operarios'],0)} |",
          f"| Ventas | {m(act['ventas'])} | {m(pro['ventas'])} |",
          f"| Costo variable | {m(act['costo_variable'])} | {m(pro['costo_variable'])} |",
          f"| Margen de contribución | {m(act['margen'])} | {m(pro['margen'])} |",
          f"| **Margen de contribución adicional** | | **{m(prod['margen_adicional'])}** |", "",
          "| Referencia | Unidades llenadas al año | Unidades conformes al año | Ventas | Costo variable | Margen |",
          "| --- | --- | --- | --- | --- | --- |"]
    for ref, x in pro["refs"].items():
        L.append(f"| {ref} | {m(x['llenadas_ano'],0)} | {m(x['conformes_ano'],0)} | {m(x['ventas'])} | {m(x['costo_variable'])} | {m(x['margen'])} |")
    L += [f"| **Total** | **{m(pro['llenadas_ano'],0)}** | **{m(pro['conformes_ano'],0)}** | **{m(pro['ventas'])}** | **{m(pro['costo_variable'])}** | **{m(pro['margen'])}** |", ""]
    mo_act = p["estado_actual"]["operarios"] * p["personal"]["operario_anual"] * 1e6 / act["conformes_ano"]
    mo_pro = (p["propuesta"]["operarios"] * p["personal"]["operario_anual"] + op["domingo"]
              + p["personal"]["horas_extra_y_disponibilidad"]) * 1e6 / pro["conformes_ano"]
    prod_act = act["conformes_dia"] / p["estado_actual"]["operarios"]
    prod_pro = pro["conformes_dia"] / p["propuesta"]["operarios"]
    L += [f"- Productividad: de {m(prod_act,0)} a {m(prod_pro,0)} unidades conformes por operario al día ({'+' + pct(prod_pro/prod_act-1,0)}).",
          f"- Mano de obra por unidad conforme: de {m(mo_act,0)} a {m(mo_pro,0)} COP ({pct(mo_pro/mo_act-1,0)}).",
          f"- OEE de la empacadora hoy: disponibilidad {pct(o['actual']['disponibilidad'],0)}, rendimiento {pct(o['actual']['rendimiento'],0)}, calidad {pct(o['actual']['calidad'],1)}: **{pct(o['actual']['oee'],0)}**.",
          f"- OEE meta: disponibilidad {pct(o['meta']['disponibilidad'],0)}, rendimiento {pct(o['meta']['rendimiento'],0)}, calidad {pct(o['meta']['calidad'],1)}: **{pct(o['meta']['oee'],0)}**.",
          "- Tiempo de envasado por lote con la meta de OEE: " + ", ".join(f"{k} {m(v,0)} min" for k, v in r["envasado"].items()) + ".",
          f"- Tiempo estándar por lote de YB-200: **{m(r['te']['total'],0)} min** frente a {m(p['estado_actual']['tiempo_estandar_min'],0)} min ({pct(r['te']['total']/p['estado_actual']['tiempo_estandar_min']-1,0)}); "
          f"homogeneización y pasteurización {m(r['te']['pasteurizacion'],0)} min; ocupación de T-301 {m(r['te']['ocupacion_t301'],0)} min, {m(r['te']['ocupacion_con_cip'],0)} con el CIP.", ""]
    L += ["## Ingeniería de Cremia", "",
          f"- Horas: **{m(ing['horas'],0)}**; capacidad {m(ing['capacidad_total'],0)} h; ocupación {pct(ing['ocupacion'],0)}.",
          f"- Valor: **{m(ing['valor'])}**; tarifa promedio {m(ing['tarifa_promedio'],0)} COP/h.",
          f"- Nómina de {p['equipo_cremia']['semanas_proyecto']} semanas: {m(ing['nomina'])}; factor facturado/nómina {m(ing['factor_nomina'],2)} (mínimo {m(p['equipo_cremia']['factor_aiu_minimo'],2)}); administración, imprevistos y utilidad {m(ing['valor']-ing['nomina'])}.",
          f"- Software propio (paquetes 1.5.3 a 1.5.5 y cuenta 1.6): {m(ing['software_horas'],0)} h y {m(ing['software_valor'])}; costo interno ≈ {m(ing['software_horas']*p['software']['costo_hora_promedio_interno']/1e6)}.", "",
          "| Integrante | Rol | Horas | Ocupación | Tarifa (COP/h) | Factor sobre su costo | Valor |",
          "| --- | --- | --- | --- | --- | --- | --- |"]
    for k, x in ing["personas"].items():
        L.append(f"| {x['nombre']} | {x['rol']} | {m(x['horas'],0)} | {pct(x['ocupacion'],0)} | {m(x['tarifa'],0)} | {m(x['factor'],2)} | {m(x['valor'],2)} |")
    L += [f"| **Total** | | **{m(ing['horas'],0)}** | **{pct(ing['ocupacion'],0)}** | **{m(ing['tarifa_promedio'],0)} en promedio** | | **{m(ing['valor'],2)}** |", "",
          "| Cuenta | Entregable | Paquetes | Horas | Valor |", "| --- | --- | --- | --- | --- |"]
    for c, x in ing["cuentas"].items():
        L.append(f"| {c} | {x['nombre']} | {x['paquetes']} | {m(x['horas'],0)} | {m(x['valor'],2)} |")
    L += [f"| **Total** | | **{sum(x['paquetes'] for x in ing['cuentas'].values())}** | **{m(ing['horas'],0)}** | **{m(ing['valor'],2)}** |", "",
          "| Contrato | Semanas | Horas | Valor |", "| --- | --- | --- | --- |"]
    for n, x in ing["contratos"].items():
        L.append(f"| {n} | {x['semanas']} | {m(x['horas'],0)} | {m(x['valor'])} |")
    L += ["", "| Paquete | Nombre | Semanas | Horas | Responsables |", "| --- | --- | --- | --- | --- |"]
    for cod, x in ing["paquetes"].items():
        resp = ", ".join(f"{k} ({m(h,0)})" for k, h in x["h"].items())
        L.append(f"| {cod} | {x['nombre']} | {x['semanas']} | {m(x['horas'],0)} | {resp} |")
    L += ["", "| Paquete | Semanas | Inicio | Fin |", "| --- | --- | --- | --- |"]
    for cod, x in ing["paquetes"].items():
        ini, fin = fechas_semanas(x["semanas"])
        L.append(f"| {cod} | {x['semanas']} | {ini} | {fin} |")
    L += ["", "## Inversión", "", "| N.º | Rubro | Valor |", "| --- | --- | --- |"]
    for k, x in p["capex"]["rubros"].items():
        L.append(f"| {k} | {x['nombre']} | {m(x['valor'])} |")
    L += [f"| | Subtotal de equipos y software | {m(cap['equipos'])} |",
          f"| | Ingeniería de Cremia | {m(cap['ingenieria'])} |",
          f"| | Montaje ({pct(p['capex']['montaje_pct'],0)} de equipos físicos, sin la nube ni la licencia) | {m(cap['montaje'])} |",
          f"| | Subtotal | {m(cap['subtotal'])} |",
          f"| | Contingencia ({pct(p['capex']['contingencia_pct'],0)}) | {m(cap['contingencia'])} |",
          f"| | **Inversión total** | **{m(cap['total'])}** |",
          f"| | Margen no percibido por {p['capex']['dias_parada']} días de parada | {m(b['parada'])} |",
          f"| | **Desembolso del año 0** | **{m(cap['total']+b['parada'])}** |", "",
          f"- Línea de vasos: {m(cap['vasos'])}; preparación y bolsas: {m(cap['fase1'])}.",
          f"- Clase de depreciación de equipos (10 años): {m(cap['clase_equipos'])}; software, hardware de borde y licencia del PLC (5 años): {m(cap['clase_software'])}.",
          "- Grupos: " + "; ".join(f"{g} {m(v)}" for g, v in cap["grupos"].items()) + ".",
          f"- Base de mantenimiento: {m(cap['base_mantenimiento'])}.", "",
          "## Costos anuales de operación", "", "| Partida | Millones de COP por año |", "| --- | --- |"]
    for n, v in op["partidas"].items():
        L.append(f"| {n} | {m(v)} |")
    L += [f"| **Total** | **{m(op['total'])}** |", "",
          f"- Hora ordinaria del operario: {m(op['hora_ordinaria'],0)} COP.",
          f"- Beneficio operativo anual a plena producción (antes de impuestos): {m(prod['margen_adicional']-op['total'])}.",
          f"- Capital de trabajo a plena producción: {m(b['ct_pleno'])}.", "",
          "## Flujo de caja", "",
          "| Concepto | Año 0 | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 |", "| --- | --- | --- | --- | --- | --- | --- |"]
    F = b["filas"]
    fila = lambda nombre, clave, signo=1, a0="—": "| " + nombre + " | " + a0 + " | " + " | ".join(m(signo * x[clave]) for x in F) + " |"
    L += [f"| Inversión y parada | {m(b['despues'][0])} | — | — | — | — | — |",
          fila("Margen adicional (rampa)", "margen"),
          fila("Costos de operación", "opex", -1),
          fila("Resultado operativo (EBITDA)", "ebitda"),
          fila("Depreciación (no es salida de caja)", "dep"),
          fila("Impuesto de renta (35 %)", "impuesto", -1),
          fila("Variación del capital de trabajo", "dct", -1),
          fila("Recuperación del capital de trabajo y valor residual", "final"),
          "| **Flujo antes de impuestos** | " + " | ".join(m(x) for x in b["antes"]) + " |",
          "| **Flujo después de impuestos** | " + " | ".join(m(x) for x in b["despues"]) + " |", "",
          f"- Valor residual en libros en el año 5: {m(b['residual'])}.", "",
          "## Indicadores", "", "| Indicador | Después de impuestos (principal) | Antes de impuestos |", "| --- | --- | --- |",
          f"| VPN al 15 % | {m(b['vpn'])} | {m(b['vpn_antes'])} |",
          f"| TIR | {_fmt_tir(b['tir'])} | {_fmt_tir(b['tir_antes'])} |",
          f"| Recuperación | {_fmt_rec(b['rec'])} | {_fmt_rec(b['rec_antes'])} |",
          f"| Relación beneficio-costo | {m(b['bc'],2)} | — |",
          f"| Volumen de equilibrio | {pct(r['eq_vol'])} del plan | — |",
          f"| Vasos de equilibrio (bolsas al 100 %) | {pct(r['eq_vasos'])} del plan | — |", "",
          "## Sensibilidad (después de impuestos)", "", "| Escenario | VPN al 15 % | TIR | Recuperación |", "| --- | --- | --- | --- |"]
    for n, s in r["sens"].items():
        L.append(f"| {n} | {m(s['vpn'])} | {_fmt_tir(s['tir'])} | {_fmt_rec(s['rec'])} |")
    sb = r["solo_bolsas"]
    L += [f"| Solo preparación y bolsas (600 lotes de YB-200, sin línea de vasos) | {m(sb['vpn'])} | {_fmt_tir(sb['tir'])} | {_fmt_rec(sb['rec'])} |",
          f"", f"- Inversión del escenario solo bolsas: {m(sb['cap']['total'])}; margen adicional {m(sb['prod']['margen_adicional'])}.", "",
          "## Crédito", "",
          f"{pct(p['finanzas']['credito']['porcentaje'],0)} de la inversión ({m(p['finanzas']['credito']['porcentaje']*cap['total'])}) a {pct(p['finanzas']['credito']['tasa'],0)} efectivo anual, {p['finanzas']['credito']['anos']} años, {p['finanzas']['credito']['gracia_anos']} año de gracia con pago de intereses.", "",
          "| Año | Intereses | Abono a capital | Cuota | Saldo | Flujo del proyecto después de impuestos | Ahorro tributario de intereses | Flujo después de la deuda |",
          "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for c in r["credito"]:
        L.append(f"| {c['ano']} | {m(c['interes'])} | {m(c['abono'])} | {m(c['cuota'])} | {m(c['saldo'])} | {m(c['flujo_proyecto'])} | {m(c['escudo'])} | {m(c['despues_deuda'])} |")
    L += ["", "## Pagos por hitos", "", "| Hito | Semana | Porcentaje | Valor |", "| --- | --- | --- | --- |"]
    for nombre, sem, pc in p["finanzas"]["pagos_hitos"]:
        L.append(f"| {nombre} | {sem} | {pct(pc,0)} | {m(pc*cap['total'])} |")
    L.append("")
    return "\n".join(L)


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(RAIZ))
    from programa import resumen as resumen_programa

    res = resultados()
    salida = RAIZ / "resultados.md"
    salida.write_text(reporte(res) + "\n" + resumen_programa(res["p"]), encoding="utf-8")
    b = res["base"]
    print(f"Inversión {m(b['cap']['total'])} | VPN {m(b['vpn'])} | TIR {_fmt_tir(b['tir'])} | "
          f"recuperación {_fmt_rec(b['rec'])} | VPN antes de impuestos {m(b['vpn_antes'])}")
    print(f"Escrito {salida}")
