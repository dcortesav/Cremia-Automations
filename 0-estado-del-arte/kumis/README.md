# Línea 3 – Kumis

Documentación de ingeniería de la línea 3 (kumis), leche fermentada mesófila. Reúne el P&ID, el proceso y sus parámetros, el análisis del cuello de botella y los requerimientos de información para MES y ERP.

**Proyecto Integrador APM 2026-2S** · Automatización de Procesos de Manufactura – UNAL
**Responsables línea 3:** Jesús A. Rivera M. · David F. Cárdenas C.
**Referencias de producto:** KU-200 (vaso de 200 g), KU-1L (botella PEAD de 1 L) y KU-NAT (bolsa de 1 kg, natural sin azúcar).

## Contenido

| Carpeta | Documento | Contenido |
|---|---|---|
| [`diagramas-de-instrumentacion/`](diagramas-de-instrumentacion) | [`PID_Kumis.md`](diagramas-de-instrumentacion/PID_Kumis.md) | P&ID (ANSI/ISA-5.1) en dos hojas: equipos, índice de instrumentos, lazos de control y notas de diseño |
| [`diagramas-de-proceso/`](diagramas-de-proceso) | [`Proceso_Kumis.md`](diagramas-de-proceso/Proceso_Kumis.md) | Proceso de producción: materia prima, maquinaria, secuencia, DOP, cursograma, EDT, puntos de control y recursos compartidos |
| | [`Receta_y_Parametros_Kumis.md`](diagramas-de-proceso/Receta_y_Parametros_Kumis.md) | Receta, dosificación y parámetros de proceso por referencia |
| | [`Cuello_de_Botella_Kumis.md`](diagramas-de-proceso/Cuello_de_Botella_Kumis.md) | Análisis de capacidad y propuesta de mejora de la línea |
| [`gestion-de-la-informacion/`](gestion-de-la-informacion) | [`Informacion_MES_ERP_Kumis.md`](gestion-de-la-informacion/Informacion_MES_ERP_Kumis.md) | Necesidades de información de la línea y su relación con MES y ERP según ISA-95 |

## Planos P&ID

Los planos vectoriales están en `diagramas-de-instrumentacion/imagenes/` (hoja 1 y hoja 2); su código fuente en Python está en `diagramas-de-instrumentacion/scripts/` y los planos se regeneran ejecutando `python generar_pid.py` desde esa carpeta `scripts/` (requiere `matplotlib`). Los detalles están en el [README de diagramas de instrumentación](diagramas-de-instrumentacion/README.md).

> **Nota:** los parámetros de proceso provienen de la búsqueda y el análisis del sector lácteo. Constituyen la propuesta inicial de ingeniería y se contrastarán con la visita técnica a Alpina Sopó (27 y 28 de octubre de 2026).
