# Módulo 1 · Transformación Digital Industrial

Entregables de la línea de yogur. Los documentos de este repositorio son la versión vigente (noviembre de 2026); los enlaces a Google Docs corresponden a la versión de octubre de 2026.

| Entregable | Documento |
| --- | --- |
| Estado del arte de las tres líneas y justificación de la línea de yogur | [`estado-del-arte-y-justificacion-de-eleccion.md`](../0-estado-del-arte/estado-del-arte-y-justificacion-de-eleccion.md) · [versión de octubre de 2026](https://docs.google.com/document/d/15Qr4HVqPt1KvFmihwyoIkslSdZMANpP2/edit) |
| Parámetros de proceso: temperaturas, tiempos y velocidades | [`Parametros de proceso.md`](Parametros%20de%20proceso.md) |
| Recetas y lotes según ISA-88, con el programa diario de dos lotes | [`Recetas_y_Lotes_ISA88.md`](Recetas_y_Lotes_ISA88.md) |
| Modelo físico y modelo procedimental ISA-88 | [`Modelo_ISA88_Linea_Yogur.md`](Modelo_ISA88_Linea_Yogur.md) |
| Arquitectura de automatización ISA-95 | [`2_Arquitectura_ISA95.md`](2_Arquitectura_ISA95.md) |
| Flujo de información entre OT e IT | [`1_Flujo_Informacion_OT_IT.md`](1_Flujo_Informacion_OT_IT.md) |
| Equipos, sensores, actuadores, variables, estrategia de control y comunicaciones | [`Equipos_Sensores_Actuadores_Variables_Comunicaciones.md`](Equipos_Sensores_Actuadores_Variables_Comunicaciones.md) |
| Plataforma Cremia MES/ERP en Huawei Cloud y SCADA en Node-RED: diseño, continuidad y costo | [`Plataforma_MES_ERP_y_SCADA.md`](Plataforma_MES_ERP_y_SCADA.md) |

## Decisiones de la versión de noviembre de 2026

- **Segundo lote viable.** El lote 2 se enfría de noche con agua helada en la chaqueta del tanque (TV-304) y su leche espera a 4 °C en un tanque refrigerado nuevo (TK-102). Los tiempos de pasteurización (95 min) y de envasado (124 min por lote de bolsas, con la meta de OEE) se recalcularon; el tiempo estándar por lote es de unos 563 min.
- **Software propio.** El SCADA se desarrolla en Node-RED y corre en un nodo de borde en la planta; el MES y el ERP son una sola plataforma desarrollada por Cremia, la plataforma Cremia MES/ERP, que corre en Huawei Cloud. No hay licencias de terceros para la supervisión ni para la gestión. Para el control, la inversión incluye una licencia perpetua de Studio 5000 a nombre de la planta, con la que La Hacienda abre, diagnostica y respalda el programa del PLC.
- **Inventario.** 28 equipos (9 existentes y 19 nuevos), 25 sensores, 22 actuadores, 68 señales de E/S (83 con reserva) y 20 nodos EtherNet/IP; la celda R-501 queda para una etapa posterior.

## Estrategia de control

El PLC-01 ejecuta el control secuencial por fases de ISA-88 y lazos PID con mejoras clásicas: rango dividido en la temperatura del tanque (TIC-301, que de noche usa el agua helada), prealimentación en el enfriador (TIC-302), control de relación en la fruta (FFC-403) y dosificación por peso en dos velocidades. No se usa control avanzado (MPC, difuso o adaptativo): cada lazo tiene un actuador dominante, las dinámicas son lentas y el proceso es por lotes. La justificación está en la sección 8.1 del documento de equipos.

La investigación de la línea de queso campesino está en [`0-estado-del-arte/queso`](../0-estado-del-arte/queso).
