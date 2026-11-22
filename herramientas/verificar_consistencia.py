"""Verificador de consistencia de la documentación de la línea de yogur.

1. Busca cifras y términos de versiones anteriores de la propuesta (lista PROHIBIDOS).
   Una línea queda exenta si contiene un marcador de historial (MARCADORES_HISTORIAL).
2. Comprueba que las cifras canónicas (CANONICAS) aparezcan en los documentos que deben citarlas.

Uso:  .venv\\Scripts\\python.exe -X utf8 herramientas\\verificar_consistencia.py
Sale con código 1 si encuentra inconsistencias.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

EXCLUIR = (".git", ".venv", "0-estado-del-arte/queso", "0-estado-del-arte/kumis",
           "3-planeacion-y-evaluacion-del-proyecto/actas-de-reunion", "herramientas/tests",
           "herramientas/README.md")
EXTENSIONES = (".md", ".html")

MARCADORES_HISTORIAL = ("versión de octubre de 2026", "primera versión", "descartad")

# patrón -> motivo
PROHIBIDOS = {
    r"Ignition": "SCADA y MES licenciados reemplazados por Node-RED y la plataforma Cremia MES/ERP",
    r"Sepasoft": "módulos MES licenciados reemplazados por la plataforma Cremia MES/ERP",
    r"Odoo": "ERP por suscripción reemplazado por la plataforma Cremia MES/ERP",
    r"SQL Server": "base de datos reemplazada por PostgreSQL",
    r"B2MML": "MES y ERP son una sola aplicación; no hay pasarela B2MML",
    r"Tag Historian|Alarm Notification": "módulos de Ignition",
    r"1\.325,8": "inversión de la versión de octubre",
    r"\b602\b(?!,\d)": "VPN de la versión de octubre",
    r"30,2 %": "TIR de la versión de octubre",
    r"2,7 años": "recuperación de la versión de octubre",
    r"\b493\b(?!,\d)": "tiempo por lote anterior; ahora 563 min",
    r"16 semanas": "plazo anterior; ahora 26 semanas",
    r"3\.060": "horas anteriores; ahora 4.780",
    r"190,8": "ingeniería anterior",
    r"733,4": "beneficio neto anterior",
    r"83,4 %": "equilibrio anterior",
    r"3\.215": "bolsas llenadas mal calculadas; 3.052 son las llenadas",
    r"8 semanas de acompañamiento": "ahora 6 semanas de estabilización dentro del proyecto",
    r"6\.604": "unidades por día anteriores (incluían no conformes)",
    r"1\.321": "productividad anterior",
    r"\b763\b(?!,\d)": "productividad actual anterior (incluía no conformes)",
    r"\b147 COP|\b87 COP": "costo de mano de obra anterior",
    r"18:30": "jornada anterior; ahora 7:00 a 19:00",
    r"4,6 millones": "recargo dominical anterior",
    r"1\.042,9|282,9": "división por fases anterior",
    r"960,0": "subtotal de equipos anterior",
    r"como hoy\b": "el lote 2 ya no se enfría de forma natural",
    r"7 de mayo": "fecha de entrega anterior",
    r"9,4 s": "takt anterior (contaba bolsas no conformes)",
    r"OEE[^|\n]{0,40}\b68 %|\b68 %[^|\n]{0,30}OEE|≈ 68 %": "OEE actual corregido a 65 %",
    r"23 sensores|19 actuadores|55 señales|69 señales|26 equipos": "conteos anteriores",
    r"1\.098,7|494,4|1\.332,0|3\.074,6|837,6|104,2": "cifras económicas anteriores",
    r"10:00–11:45|15:05–16:50|16:15–18:15|22:15": "programa diario anterior",
    r"3\.052 bolsas conformes": "3.052 son las bolsas llenadas; las conformes son 2.898",
    r"Pendiente de revisión": "marca de borrador",
}

# cifra canónica -> documentos que deben citarla
CANONICAS = {
    "1.464,5": ["README.md", "3-planeacion-y-evaluacion-del-proyecto/Propuesta_Economica_y_Comercial.md",
                "3-planeacion-y-evaluacion-del-proyecto/empresa/Propuesta_Empresarial.md",
                "3-planeacion-y-evaluacion-del-proyecto/EDTs/Proyecto/4_EDT_Proyecto_TDI_Yogur.md",
                "3-planeacion-y-evaluacion-del-proyecto/README.md", "docs/index.html", "docs/plan.html"],
    "231,0": ["README.md", "3-planeacion-y-evaluacion-del-proyecto/Propuesta_Economica_y_Comercial.md",
              "3-planeacion-y-evaluacion-del-proyecto/Propuesta_de_valor_y_gestion_del_cambio.md",
              "3-planeacion-y-evaluacion-del-proyecto/empresa/Propuesta_Empresarial.md",
              "3-planeacion-y-evaluacion-del-proyecto/README.md", "docs/plan.html", "docs/valor.html"],
    "19,8 %": ["README.md", "3-planeacion-y-evaluacion-del-proyecto/Propuesta_Economica_y_Comercial.md",
               "docs/plan.html", "docs/valor.html"],
    "3,8 años": ["README.md", "3-planeacion-y-evaluacion-del-proyecto/Propuesta_Economica_y_Comercial.md",
                 "docs/plan.html"],
    "89,6 %": ["3-planeacion-y-evaluacion-del-proyecto/Propuesta_Economica_y_Comercial.md",
               "3-planeacion-y-evaluacion-del-proyecto/README.md", "docs/plan.html"],
    "4.780": ["README.md", "3-planeacion-y-evaluacion-del-proyecto/Cronograma_Proyecto_TDI_Yogur.md",
              "3-planeacion-y-evaluacion-del-proyecto/EDTs/Proyecto/4_EDT_Proyecto_TDI_Yogur.md",
              "3-planeacion-y-evaluacion-del-proyecto/Propuesta_Economica_y_Comercial.md", "docs/plan.html"],
    "26 semanas": ["README.md", "3-planeacion-y-evaluacion-del-proyecto/Cronograma_Proyecto_TDI_Yogur.md",
                   "docs/plan.html"],
    "16 de julio de 2027": ["README.md", "3-planeacion-y-evaluacion-del-proyecto/Cronograma_Proyecto_TDI_Yogur.md"],
    "563 min": ["README.md", "1-transformacion-digital-industrial/Recetas_y_Lotes_ISA88.md",
                "1-transformacion-digital-industrial/Parametros de proceso.md",
                "2-gestion-y-evaluacion-de-la-produccion/Insumo - Tiempos y capacidades de la línea de yogur.md"],
    "65 %": ["2-gestion-y-evaluacion-de-la-produccion/VSM del estado actual e indicadores - Línea de yogur.md",
             "2-gestion-y-evaluacion-de-la-produccion/README.md", "docs/diagnostico.html"],
    "25 sensores": ["1-transformacion-digital-industrial/2_Arquitectura_ISA95.md", "README.md"],
    "68 señales": ["1-transformacion-digital-industrial/2_Arquitectura_ISA95.md",
                   "1-transformacion-digital-industrial/Equipos_Sensores_Actuadores_Variables_Comunicaciones.md"],
    "Node-RED": ["1-transformacion-digital-industrial/2_Arquitectura_ISA95.md",
                 "1-transformacion-digital-industrial/1_Flujo_Informacion_OT_IT.md",
                 "1-transformacion-digital-industrial/Plataforma_MES_ERP_y_SCADA.md", "docs/solucion.html"],
    "Huawei Cloud": ["1-transformacion-digital-industrial/2_Arquitectura_ISA95.md",
                     "1-transformacion-digital-industrial/Plataforma_MES_ERP_y_SCADA.md",
                     "3-planeacion-y-evaluacion-del-proyecto/Propuesta_Economica_y_Comercial.md",
                     "3-planeacion-y-evaluacion-del-proyecto/empresa/Propuesta_Empresarial.md", "docs/solucion.html"],
    "TK-102": ["1-transformacion-digital-industrial/Equipos_Sensores_Actuadores_Variables_Comunicaciones.md",
               "1-transformacion-digital-industrial/Modelo_ISA88_Linea_Yogur.md",
               "1-transformacion-digital-industrial/Recetas_y_Lotes_ISA88.md",
               "3-planeacion-y-evaluacion-del-proyecto/EDTs/Proceso/EDT_Proceso_Yogur.md"],
}


def documentos(raiz: Path = RAIZ):
    for ruta in raiz.rglob("*"):
        rel = ruta.relative_to(raiz).as_posix()
        if ruta.is_file() and ruta.suffix in EXTENSIONES and not rel.startswith(EXCLUIR):
            yield ruta, rel


def buscar_prohibidos(texto: str, rel: str) -> list[str]:
    hallazgos = []
    for n, linea in enumerate(texto.splitlines(), start=1):
        if any(mk in linea.lower() for mk in MARCADORES_HISTORIAL):
            continue
        for patron, motivo in PROHIBIDOS.items():
            if re.search(patron, linea):
                extracto = linea.strip()[:110]
                hallazgos.append(f"{rel}:{n}: «{patron}» ({motivo}) → {extracto}")
    return hallazgos


def verificar(raiz: Path = RAIZ, canonicas: dict | None = None) -> list[str]:
    errores = []
    textos = {}
    for ruta, rel in documentos(raiz):
        texto = ruta.read_text(encoding="utf-8")
        textos[rel] = texto
        errores += buscar_prohibidos(texto, rel)
    for cifra, rels in (CANONICAS if canonicas is None else canonicas).items():
        for rel in rels:
            if rel not in textos:
                errores.append(f"{rel}: no existe (debe citar «{cifra}»)")
            elif cifra not in textos[rel]:
                errores.append(f"{rel}: no cita la cifra canónica «{cifra}»")
    return errores


if __name__ == "__main__":
    errs = verificar()
    for e in errs:
        print(e)
    print(f"\n{len(errs)} inconsistencias encontradas." if errs else "Sin inconsistencias.")
    sys.exit(1 if errs else 0)
