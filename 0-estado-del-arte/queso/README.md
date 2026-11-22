# Línea 2 – Queso Campesino

Documentación de ingeniería de la línea 2 (queso campesino): queso fresco no madurado, prensado y salado. Reúne el P&ID, el proceso y sus parámetros, el análisis del cuello de botella, el modelo ISA-88, el VSM con indicadores, la información para MES y ERP, y la planeación (EDT, presupuesto y análisis económico).

**Proyecto Integrador APM 2026-2S** · Automatización de Procesos de Manufactura – UNAL
**Responsables línea 2:** Cristian S. Hoyos P. · José Andrés Zapata P.
**Referencias de producto:** QC-250 (cuña de 250 g), QC-1K (bloque de 1 kg) y QC-3K (bloque de 3 kg).
**Lote base:** 5.000 L de leche por tina → 666,7 kg de queso campesino.

## Contenido

| Carpeta | Documento | Contenido |
|---|---|---|
| [`diagramas-de-instrumentacion/`](diagramas-de-instrumentacion) | [`PID_Queso.md`](diagramas-de-instrumentacion/PID_Queso.md) | P&ID (ANSI/ISA-5.1): equipos, índice de 34 instrumentos y lazos de control; plano vectorial `PID_Queso.svg` |
| [`diagramas-de-proceso/`](diagramas-de-proceso) | [`Proceso_Queso_Campesino.md`](diagramas-de-proceso/Proceso_Queso_Campesino.md) | Proceso: materia prima, maquinaria, secuencia, DOP, cursograma, EDT de producción, PCC y recursos compartidos |
| | [`Receta_y_Parametros_Queso.md`](diagramas-de-proceso/Receta_y_Parametros_Queso.md) | Receta, dosificación y parámetros de proceso por referencia |
| | [`Cuello_de_Botella_Queso.md`](diagramas-de-proceso/Cuello_de_Botella_Queso.md) | Análisis de capacidad y propuesta de mejora (antes/después) |
| [`gestion-de-la-informacion/`](gestion-de-la-informacion) | [`Informacion_MES_ERP_Queso.md`](gestion-de-la-informacion/Informacion_MES_ERP_Queso.md) | Necesidades de información de la línea y su relación con MES y ERP según ISA-95 |
| [`modelos-ISA/`](modelos-ISA) | [`Modelo_ISA88_Queso.md`](modelos-ISA/Modelo_ISA88_Queso.md) | Modelo físico, modelo procedimental y recetas según ANSI/ISA-88 |
| [`planeacion/`](planeacion) | [`EDT_Proceso_Queso.md`](planeacion/EDT_Proceso_Queso.md) | EDT/WBS de proyecto (PMBOK): entregables, paquetes de trabajo y horas |
| | [`Presupuesto_Linea_Queso.md`](planeacion/Presupuesto_Linea_Queso.md) | Inversión estimada (equipos, software, montaje) |
| | [`Analisis_Economico_Linea_Queso.md`](planeacion/Analisis_Economico_Linea_Queso.md) | Flujo de caja e indicadores (VPN, TIR, recuperación, B/C) |
| [`vsm-e-indicadores/`](vsm-e-indicadores) | [`VSM_e_Indicadores_Queso.md`](vsm-e-indicadores/VSM_e_Indicadores_Queso.md) | VSM actual y propuesto e indicadores (takt, MLT, OEE, WIP); mapas `VSM_Queso_Actual.svg` y `VSM_Queso_Propuesto.svg` |

## Planos y mapas (regeneración)

El plano P&ID se regenera ejecutando `node generar_pid.js` desde `diagramas-de-instrumentacion/`; los mapas de flujo de valor, con `node generar_vsm.js` desde `vsm-e-indicadores/` (requieren Node.js).

> **Nota sobre los dos "EDT":** `Proceso_Queso_Campesino.md` §8 es el *EDT de producción* (desglose del proceso por etapas); `planeacion/EDT_Proceso_Queso.md` es la *EDT/WBS del proyecto* (entregables y horas, PMBOK). Son documentos distintos y complementarios.

> **Nota:** los parámetros de proceso provienen de la búsqueda y el análisis del sector lácteo. Constituyen la propuesta inicial de ingeniería y se contrastarán con la visita técnica a Alpina Sopó (27 y 28 de octubre de 2026).
