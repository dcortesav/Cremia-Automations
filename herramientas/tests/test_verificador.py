"""Pruebas del verificador de consistencia y del generador de tablas."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import generar_tablas as G  # noqa: E402
import verificar_consistencia as V  # noqa: E402


def test_detecta_cifras_y_terminos_viejos():
    texto = "El SCADA en Ignition cuesta 1.325,8 millones y dura 16 semanas.\nTodo bien aquí."
    hallazgos = V.buscar_prohibidos(texto, "doc.md")
    assert len(hallazgos) == 3
    assert all(h.startswith("doc.md:1:") for h in hallazgos)


def test_marcador_de_historial_exime_la_linea():
    texto = "En la versión de octubre de 2026 el plazo era de 16 semanas."
    assert V.buscar_prohibidos(texto, "doc.md") == []


def test_no_confunde_cifras_parecidas():
    assert V.buscar_prohibidos("El valor residual es 763,9 millones.", "doc.md") == []


def test_cifras_canonicas(tmp_path):
    (tmp_path / "a.md").write_text("VPN de 231,0 millones", encoding="utf-8")
    (tmp_path / "b.md").write_text("Sin la cifra", encoding="utf-8")
    errores = V.verificar(tmp_path, {"231,0": ["a.md", "b.md", "c.md"]})
    assert any("b.md" in e for e in errores)
    assert any("c.md: no existe" in e for e in errores)
    assert not any(e.startswith("a.md") for e in errores)


def test_repositorio_sin_inconsistencias():
    assert V.verificar() == []


def test_bloques_generados_al_dia():
    assert G.main(verificar=True) == 0


def test_aplicar_reemplaza_solo_el_bloque():
    texto = "antes\n<!-- tabla:pagos -->\nviejo\n<!-- /tabla:pagos -->\ndespués"
    nuevo = G.aplicar(texto, {"pagos": "nuevo"})
    assert nuevo == "antes\n<!-- tabla:pagos -->\nnuevo\n<!-- /tabla:pagos -->\ndespués"
