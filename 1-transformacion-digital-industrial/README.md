# Módulo 1 · Transformación Digital Industrial

Entregables de la línea de yogur.

| Entregable | Documento |
|---|---|
| Estado del arte de las tres líneas y justificación de la línea de yogur | [Abrir](https://docs.google.com/document/d/15Qr4HVqPt1KvFmihwyoIkslSdZMANpP2/edit) · [`3_Estado_del_Arte_y_Justificacion_Yogur.md`](../0-estado-del-arte/3_Estado_del_Arte_y_Justificacion_Yogur.md) |
| Parámetros de proceso: temperaturas, tiempos y velocidades | [Abrir](https://docs.google.com/document/d/1mB-EovLcqbgefFnWGZF3BccSLASdBvvIfBUOuBw3cVQ/edit) |
| Recetas y lotes según ISA-88 | [Abrir](https://docs.google.com/document/d/1X1U0yaOUam14wozc36GzxmGuL5SzhDa4b_BxD9mRF6A/edit) |
| Modelo físico y modelo procedimental ISA-88 | [Abrir](https://docs.google.com/document/d/1ZF-I_JR1iNFCNcEoRBKXjb61100lmu2lH0ex8rSSnnQ/edit) · [`Modelo_ISA88_Linea_Yogur.md`](Modelo_ISA88_Linea_Yogur.md) |
| Arquitectura de automatización ISA-95 | [Abrir](https://docs.google.com/document/d/1kvNnSGBzCeJxPqM4DeCohGPNIGzel8OJ/edit) · [`2_Arquitectura_ISA95.md`](2_Arquitectura_ISA95.md) |
| Flujo de información entre OT e IT | [Abrir](https://docs.google.com/document/d/1NjIe9slTbMAhIYK8SDlBFLAXtRPwuCeh/edit) · [`1_Flujo_Informacion_OT_IT.md`](1_Flujo_Informacion_OT_IT.md) |
| Equipos, sensores, actuadores, variables, estrategia de control y comunicaciones | [Abrir](https://docs.google.com/document/d/1spMO-Vy00_5qNQvk6opeh2CanFKjmcis8-Qxc25g61I/edit) |

## Estrategia de control

El PLC-01 ejecuta el control secuencial por fases de ISA-88 y lazos PID con mejoras clásicas: rango dividido en la temperatura del tanque (TIC-301), prealimentación en el enfriador (TIC-302), control de relación en la fruta (FFC-403) y dosificación por peso en dos velocidades. No se usa control avanzado (MPC, difuso o adaptativo): cada lazo tiene un actuador dominante, las dinámicas son lentas y el proceso es por lotes. La justificación está en la sección 8.1 del documento de equipos.

La investigación de la línea de queso campesino está en [`0-estado-del-arte/queso`](../0-estado-del-arte/queso).
