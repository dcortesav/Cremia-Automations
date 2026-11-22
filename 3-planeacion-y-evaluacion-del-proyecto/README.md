# Módulo 3 · Planeación y Evaluación de Proyectos

Entregables del proyecto para la línea de yogur. Los documentos de este repositorio son la versión vigente (noviembre de 2026); los enlaces a Google Docs corresponden a la versión de octubre de 2026.

| Entregable | Documento |
| --- | --- |
| Propuesta empresarial: roles, contribuciones, salarios, margen y modelo de negocio | [`empresa/Propuesta_Empresarial.md`](empresa/Propuesta_Empresarial.md) |
| Propuesta económica y comercial: presupuesto, flujo de caja, indicadores y oferta | [`Propuesta_Economica_y_Comercial.md`](Propuesta_Economica_y_Comercial.md) |
| Propuesta de valor y gestión del cambio | [`Propuesta_de_valor_y_gestion_del_cambio.md`](Propuesta_de_valor_y_gestion_del_cambio.md) |
| EDT del proyecto | [`EDTs/Proyecto/4_EDT_Proyecto_TDI_Yogur.md`](EDTs/Proyecto/4_EDT_Proyecto_TDI_Yogur.md) |
| Cronograma del proyecto (26 semanas) | [`Cronograma_Proyecto_TDI_Yogur.md`](Cronograma_Proyecto_TDI_Yogur.md) |
| EDT del proceso de yogur | [`EDTs/Proceso/EDT_Proceso_Yogur.md`](EDTs/Proceso/EDT_Proceso_Yogur.md) |
| Acta del 26 de septiembre de 2026 | [`actas-de-reunion/2026-09-26.md`](actas-de-reunion/2026-09-26.md) |
| Acta del 10 de octubre de 2026 | [`actas-de-reunion/2026-10-10.md`](actas-de-reunion/2026-10-10.md) |
| Acta del 11 de octubre de 2026 | [`actas-de-reunion/2026-10-11.md`](actas-de-reunion/2026-10-11.md) |

## Resumen del plan y de la evaluación

| Concepto | Valor |
| --- | --- |
| Duración | 26 semanas (18 de enero a 16 de julio de 2027), una parada de planta de 5 días en la semana 19 |
| Horas de ingeniería | 4.780 h, 77 % de la capacidad del equipo descontados los festivos; nadie pasa de 42 h en ninguna semana |
| Servicios de ingeniería | COP 333,7 millones, 1,41 veces la nómina de las 26 semanas, en dos contratos: diseño, procura y gestión de compras (62,1) e implementación, software, puesta en marcha y adopción (271,6) |
| Software propio | SCADA en Node-RED y plataforma Cremia MES/ERP en Huawei Cloud: 1.830 h de desarrollo (COP 123,9 millones), sin licencias de terceros |
| Inversión total | COP 1.464,5 millones; celda robotizada en una etapa posterior |
| Indicadores para el cliente (después de impuestos) | VPN al 15 % de COP 231,0 millones, TIR de 19,8 %, recuperación en 3,8 años |
| Indicadores antes de impuestos | VPN al 15 % de COP 697,9 millones, TIR de 28,9 %, recuperación en 3,1 años |
| Volumen de equilibrio | 89,6 % del plan; los vasos, con las bolsas al 100 %, en el 84,1 % |
| Condición para firmar | Cartas de intención de los distribuidores por al menos el 85 % del volumen de vasos |

## Decisiones de la versión de noviembre de 2026

Las actas registran las decisiones hasta el 11 de octubre de 2026. Después de la sustentación, el equipo tomó estas decisiones, que esta versión aplica en todos los documentos:

| N.º | Decisión |
| --- | --- |
| D7 | Cremia desarrolla su propio software de gestión: la plataforma Cremia MES/ERP, de complejidad media, a la escala de una pyme, en lugar de licenciar un MES y un ERP. |
| D8 | La plataforma se despliega en Huawei Cloud, para que la gestión siga disponible aunque falle la planta. |
| D9 | El SCADA se desarrolla en Node-RED, sin licencias de terceros. |
| D10 | Se mantienen los dos lotes diarios; el lote 2 se enfría de noche con agua helada en la chaqueta y su leche espera en un tanque refrigerado nuevo (TK-102). |
| D11 | El proyecto se extiende a 26 semanas; la ingeniería cubre la nómina completa con el factor mínimo de 1,39. |
| D12 | El indicador financiero principal es el VPN después de impuestos, con capital de trabajo y valor residual. |
| D13 | Cremia conserva la propiedad de la plataforma; La Hacienda recibe una licencia perpetua para su sitio, con el código fuente en depósito. |

## Carpetas

- `EDTs`: estructuras de desglose del trabajo.
- `empresa/logo`: logo de Cremia Automations.
- `actas-de-reunion`: actas de reunión.

Las cifras de este módulo salen de [`herramientas/parametros.yaml`](../herramientas/parametros.yaml) y [`herramientas/resultados.md`](../herramientas/resultados.md).
