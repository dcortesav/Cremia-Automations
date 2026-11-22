"""Pruebas del programa diario de dos lotes."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import modelo as M  # noqa: E402
import programa as P  # noqa: E402


@pytest.fixture(scope="module")
def p():
    return M.cargar()


@pytest.mark.parametrize("refs", [
    ("YB-200", "YB-200", "YB-200"),
    ("YV-150", "YB-200", "YV-150"),
    ("YB-200", "YV-300", "YV-150"),
])
def test_sin_conflictos_ni_cruces(p, refs):
    T = P.programa(p, ref_l1=refs[0], ref_l2=refs[1], ref_l2_prev=refs[2])
    assert P.conflictos_recursos(T) == []
    assert P.cruces_de_rol(T) == []
    assert all(v == 0 for v in P.fuera_de_turno(T).values())


def test_tanque_libre_y_lote_2(p):
    T = P.programa(p)
    libre = next(x for x in T if x.lote == "L1" and x.nombre.startswith("Enfriamiento en placas")).fin
    inoc2 = next(x for x in T if x.lote == "L2" and x.nombre == "Inoculación").fin
    assert P.r5(libre) == "15:05"
    assert P.r5(inoc2) == "18:20"
    assert inoc2 <= P.TURNOS["S"][1]


def test_incubacion_maxima_horas_extra_acotadas(p):
    T = P.programa(p, incubacion=p["tiempos_min"]["incubar_maximo"])
    assert P.conflictos_recursos(T) == []
    assert max(P.fuera_de_turno(T).values()) <= 60


def test_turnos_de_siete_horas():
    for ini, fin in P.TURNOS.values():
        assert fin - ini == 7 * 60
