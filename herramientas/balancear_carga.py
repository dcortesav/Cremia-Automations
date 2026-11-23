"""Reparte las horas de cada paquete de la EDT entre los integrantes que pueden hacerlo.
La penalidad castiga con fuerza que alguien pase de su capacidad semanal (42 h menos los
festivos) y, con menos peso, que pase de 36 h por semana (proporcional a los días hábiles) o de
860 h en el proyecto. El límite del 80 % de ocupación lo comprueba tests/test_modelo.py.

Búsqueda local: mueve bloques de 5 h entre integrantes elegibles mientras baje la penalidad.
Uso: .venv\\Scripts\\python.exe -X utf8 herramientas\\balancear_carga.py  (imprime la asignación)
"""
from __future__ import annotations

import itertools

from modelo import cargar, capacidad_semanal, paquetes

ELEGIBLES = {
    "1.1.2": "DC CH", "1.2.4": "DC JZ", "1.2.5": "JZ JR", "1.3.3": "JR JZ", "1.3.4": "AO JZ",
    "1.3.5": "AO DF JZ", "1.4.3": "JZ AO", "1.5.1": "DC JR", "1.5.2": "JR JZ DC", "1.5.3": "DF AO DC",
    "1.5.4": "DF JR", "1.5.5": "JR DF", "1.6.2": "DF JR", "1.3.1": "JZ AO", "1.6.1": "JR DF", "1.8.3": "JR DF", "1.8.1": "JZ AO", "1.6.3": "DC JZ DF", "1.6.4": "DF DC",
    "1.6.5": "JZ AO DF", "1.6.6": "AO JR DF", "1.6.7": "JR CH DF", "1.6.8": "CH DF", "1.6.10": "CH AO JR",
    "1.6.11": "AO DF CH JR", "1.7.3": "DC DF AO", "1.8.2": "JR JZ", "1.8.4": "AO JZ", "1.9.1": "JZ AO JR",
    "1.9.2": "DC JR DF JZ", "1.9.3": "JZ DC AO JR", "1.9.4": "JZ DF", "1.10.1": "CH DC", "1.10.2": "DF AO CH JZ",
    "1.10.3": "DF CH JR", "1.10.4": "DC JZ DF AO",
}
TOPE_SEMANA = 36.0
TOPE_TOTAL = 860.0
# ventanas en las que puede moverse cada paquete (semana mínima de inicio, semana máxima de fin)
VENTANAS = {
    "1.3.3": (3, 10), "1.3.4": (3, 9), "1.3.5": (3, 8), "1.5.1": (5, 13), "1.5.2": (6, 14), "1.5.3": (3, 9),
    "1.5.4": (8, 17), "1.5.5": (12, 18), "1.6.1": (4, 12), "1.6.2": (2, 9), "1.6.3": (5, 13), "1.6.4": (7, 17),
    "1.6.5": (10, 17), "1.6.6": (20, 25), "1.6.7": (9, 17), "1.6.8": (6, 17), "1.6.9": (20, 25),
    "1.6.10": (20, 26), "1.6.11": (10, 25), "1.7.1": (3, 13), "1.7.2": (9, 16), "1.10.3": (16, 25),
    "1.10.4": (21, 26),
}


def semanas(rango: str) -> range:
    partes = str(rango).replace("-", "–").split("–")
    return range(int(partes[0]), int(partes[-1]) + 1)


def penalidad(asig, pqs, personas, n, cap=None):
    cap = cap or [42.0] * n
    carga = {k: [0.0] * n for k in personas}
    for cod, h in asig.items():
        sem = semanas(pqs[cod]["semanas"])
        peso = sum(cap[s - 1] for s in sem)
        for k, x in h.items():
            for s in sem:
                carga[k][s - 1] += x * cap[s - 1] / peso
    pen = 0.0
    for k, v in carga.items():
        pen += sum(10 * max(0.0, x - TOPE_SEMANA * c / 42) ** 2 + 1000 * max(0.0, x - c) ** 2
                   for x, c in zip(v, cap))
        pen += 5 * max(0.0, sum(v) - TOPE_TOTAL) ** 2
    totales = [sum(v) for v in carga.values()]
    media = sum(totales) / len(totales)
    pen += 0.001 * sum((t - media) ** 2 for t in totales)
    return pen, carga


def balancear(p):
    pqs = {c: dict(x) for c, x in paquetes(p).items()}
    personas = list(p["equipo_cremia"]["integrantes"])
    n = p["equipo_cremia"]["semanas_proyecto"]
    asig = {cod: dict(pq["h"]) for cod, pq in pqs.items()}
    cap = capacidad_semanal(p)
    mejor, _ = penalidad(asig, pqs, personas, n, cap)
    mejoro = True
    while mejoro:
        mejoro = False
        for cod, eleg in ELEGIBLES.items():
            for a, b in itertools.permutations(eleg.split(), 2):
                if asig[cod].get(a, 0) < 5:
                    continue
                prueba = {c: dict(h) for c, h in asig.items()}
                prueba[cod][a] -= 5
                prueba[cod][b] = prueba[cod].get(b, 0) + 5
                if prueba[cod][a] == 0:
                    del prueba[cod][a]
                pen, _ = penalidad(prueba, pqs, personas, n, cap)
                if pen < mejor - 1e-9:
                    asig, mejor, mejoro = prueba, pen, True
        for cod, (lo, hi) in VENTANAS.items():
            sem = semanas(pqs[cod]["semanas"])
            a, b = sem.start, sem.stop - 1
            for na, nb in ((a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1), (a - 1, b - 1), (a + 1, b + 1)):
                if na < lo or nb > hi or nb < na:
                    continue
                viejo = pqs[cod]["semanas"]
                pqs[cod]["semanas"] = f"{na}–{nb}" if na != nb else f"{na}"
                pen, _ = penalidad(asig, pqs, personas, n, cap)
                if pen < mejor - 1e-9:
                    mejor, mejoro = pen, True
                    break
                pqs[cod]["semanas"] = viejo
    return asig, pqs, penalidad(asig, pqs, personas, n, cap)


def escribir(asig, pqs, ruta="parametros.yaml"):
    import re
    from pathlib import Path
    r = Path(__file__).resolve().parent / ruta
    t = r.read_text(encoding="utf-8")
    for cod, h in asig.items():
        hs = "{" + ", ".join(f"{k}: {int(v)}" for k, v in h.items()) + "}"
        patron = re.compile(r'(  "' + re.escape(cod) + r'": \{nombre: "[^"]+", semanas: ")[^"]+(", h: )\{[^}]*\}\}')
        t, k = patron.subn(lambda mo: mo.group(1) + str(pqs[cod]["semanas"]) + mo.group(2) + hs + "}", t)
        assert k == 1, cod
    r.write_text(t, encoding="utf-8")


if __name__ == "__main__":
    import sys
    p = cargar()
    asig, pqs, (pen, carga) = balancear(p)
    for cod, h in asig.items():
        print(cod, pqs[cod]["semanas"], "{" + ", ".join(f"{k}: {int(v)}" for k, v in h.items()) + "}")
    for k, v in carga.items():
        print(k, " ".join(f"{x:3.0f}" for x in v), "max", round(max(v)), "tot", round(sum(v)))
    print("penalidad", round(pen, 2))
    if "--escribir" in sys.argv:
        escribir(asig, pqs)
        print("parametros.yaml actualizado")
