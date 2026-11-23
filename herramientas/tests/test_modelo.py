"""Pruebas del modelo de la propuesta: sumas, restricciones del equipo e indicadores."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import modelo as M  # noqa: E402


@pytest.fixture(scope="module")
def p():
    return M.cargar()


@pytest.fixture(scope="module")
def r(p):
    return M.resultados(p)


def test_produccion_conformes(p):
    prod = M.produccion(p)
    act, pro = prod["actual"], prod["propuesta"]
    assert act["llenadas_dia"] == 3052
    assert act["conformes_dia"] == 2898
    assert pro["llenadas_ano"] == 1_981_320
    assert pro["conformes_ano"] == pytest.approx(1_951_600, abs=2)
    assert prod["margen_adicional"] == pytest.approx(846.9, abs=0.1)


def test_oee_actual_y_meta(p):
    o = M.oee(p)
    assert o["actual"]["oee"] == pytest.approx(0.649, abs=0.002)
    assert o["meta"]["oee"] == pytest.approx(0.816, abs=0.002)


def test_tiempo_estandar(p):
    te = M.tiempo_estandar(p)
    assert te["pasteurizacion"] == 95
    assert round(te["total"]) == 563
    env = M.tiempos_envasado(p)
    assert [round(env[k]) for k in ("YB-200", "YV-150", "YV-300")] == [124, 117, 78]


def test_horas_suman_por_cuenta_y_contrato(p):
    ing = M.ingenieria(p)
    assert ing["horas"] == 4780
    assert sum(x["horas"] for x in ing["cuentas"].values()) == ing["horas"]
    assert sum(x["horas"] for x in ing["contratos"].values()) == ing["horas"]
    assert sum(x["valor"] for x in ing["contratos"].values()) == pytest.approx(ing["valor"])
    assert ing["software_horas"] == 1830


def test_paquetes_entre_20_y_200_horas(p):
    for cod, x in M.ingenieria(p)["paquetes"].items():
        assert 20 <= x["horas"] <= 200, cod


def test_ocupacion_y_carga_semanal(p):
    ing = M.ingenieria(p)
    for k, x in ing["personas"].items():
        assert x["ocupacion"] <= 0.80, k
    cap = M.capacidad_semanal(p)
    for k, semanas in M.carga_semanal(p).items():
        for s, (h, c) in enumerate(zip(semanas, cap), start=1):
            assert h <= c + 0.05, f"{k} semana {s}: {h:.1f} h > {c:.1f} h"


def test_tarifas_cubren_nomina_con_aiu(p):
    ing = M.ingenieria(p)
    assert ing["factor_nomina"] >= p["equipo_cremia"]["factor_aiu_minimo"]
    for k, x in ing["personas"].items():
        assert x["factor"] >= p["equipo_cremia"]["factor_aiu_minimo"], k


def test_capex_suma(p):
    cap = M.capex(p)
    c = p["capex"]
    assert cap["equipos"] == pytest.approx(sum(r["valor"] for r in c["rubros"].values()))
    assert cap["total"] == pytest.approx((cap["equipos"] + cap["ingenieria"] + cap["montaje"])
                                         * (1 + c["contingencia_pct"]))
    assert cap["clase_equipos"] + cap["clase_software"] == pytest.approx(cap["total"])


def test_licencia_del_plc(p):
    c = p["capex"]
    lic = [k for k, r in c["rubros"].items() if r.get("licencia")]
    assert lic, "falta el rubro de la licencia de Studio 5000 de la planta"
    for k in lic:
        r = c["rubros"][k]
        assert r["valor"] == pytest.approx(r["valor_usd"] * p["general"]["tasa_cambio_cop_usd"] / 1e6)
        assert r.get("software"), "la licencia se deprecia a 5 años con el software"
        assert k in c["rubros_sin_mantenimiento"]
    fisicos = sum(r["valor"] for r in c["rubros"].values() if not (r.get("nube") or r.get("licencia")))
    assert M.capex(p)["montaje"] == pytest.approx(c["montaje_pct"] * fisicos)
    op = M.opex(p, M.capex(p))
    assert op["licencia"] == pytest.approx(
        p["operacion"]["licencia_studio5000_anual_usd"] * p["general"]["tasa_cambio_cop_usd"] / 1e6)


def test_cartas_de_intencion_cubren_el_equilibrio(r):
    assert r["eq_vasos"] < r["umbral_cartas"]
    assert r["vpn_umbral_cartas"] > 0


def test_indicadores_principales(r):
    b = r["base"]
    assert b["vpn"] > 0
    assert b["tir"] > r["p"]["finanzas"]["tasa_descuento"]
    assert b["rec"] < 5
    assert b["vpn_antes"] > b["vpn"]
    assert 0.85 < r["eq_vol"] < 0.95


def test_escenarios_desfavorables(r):
    assert r["sens"]["Sin valor residual"]["vpn"] < 0
    assert r["solo_bolsas"]["vpn"] < 0
    assert r["sens"]["Horas de software +30 %"]["vpn"] > 0


def test_credito_flujo_positivo(r):
    for fila in r["credito"]:
        assert fila["despues_deuda"] > 0, fila["ano"]
    assert r["credito"][-1]["saldo"] == pytest.approx(0, abs=1e-6)


def test_vpn_tir_funciones():
    flujos = [-100, 60, 60]
    assert M.vpn(flujos, 0.0) == 20
    assert M.vpn(flujos, M.tir(flujos)) == pytest.approx(0, abs=1e-6)
    assert M.recuperacion([-100, 50, 100]) == pytest.approx(1.5)


def test_formato_colombiano():
    assert M.m(1464.53) == "1.464,5"
    assert M.m(-90.2) == "−90,2"
    assert M.pct(0.198) == "19,8 %"
