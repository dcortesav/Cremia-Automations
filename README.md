# Cremia Automations

Proyecto Integrador de Automatización de Procesos de Manufactura (APM) 2026-2S, Universidad Nacional de Colombia.

**Cremia Automations** es la empresa integradora del equipo. El proyecto es la Transformación Digital Industrial de la **línea de yogur** de la planta La Hacienda Productos Alimenticios.

Página web: https://dcortesav.github.io/Cremia-Automations/

## El proyecto en cifras

| | Situación actual | Propuesta |
|---|---|---|
| Lotes por día (550 L de leche) | 1 | 2 |
| Referencias | Bolsa de 200 ml | Bolsa de 200 ml y vasos de 150 y 300 ml |
| Unidades por lote | 3.052 bolsas | 3.079 bolsas, 4.369 vasos de 150 ml o 2.260 vasos de 300 ml |
| Tiempo estándar por lote | 601 min | ≈ 493 min |
| Producto no conforme | 5,06 % | 1,5 % o menos |
| Instrumentación conectada | Ninguna | 23 sensores, 19 actuadores, 55 señales de E/S y 20 nodos EtherNet/IP |
| Robots | Ninguno | Uno de paletizado (R-501), diseñado y comprado en una etapa posterior |
| Control | Válvulas manuales, termómetro y acidómetro | Control secuencial ISA-88 y lazos PID en el PLC, sin control avanzado |
| Gestión de la información | Registros en papel | PLC CompactLogix 5380, SCADA en Ignition, MES con módulos Sepasoft y ERP Odoo en la nube |

El estado actual se toma del estudio de tiempos de la planta (Grimaldo, Moreno y Salamanca, 2015).

## Propuesta de valor para los dueños

| Dimensión | Resultado esperado |
|---|---|
| Productividad | De 763 a 1.321 unidades por operario al día (+73 %) |
| Costos | Mano de obra de 147 a 85 COP por unidad (−42 %) y costo real por lote |
| Calidad | Producto no conforme de 5,06 % a 1,5 % o menos, con peso del 100 % |
| Trazabilidad | Registro electrónico de cada lote, desde la cantina hasta la estiba |
| Información y decisiones | Tablero diario con OEE, rendimiento, consumos y paradas |
| Eficiencia de la empacadora | OEE estimado de 68 % hoy; meta de 82 % |
| Resultado financiero | Inversión de COP 1.325,8 millones; VPN al 15 % de COP 617 millones, TIR de 30,6 % y recuperación en 2,7 años |

La transformación incluye a las personas: no hay despidos, el segundo lote crea un puesto, la capacitación es por rol en el gemelo digital y la gestión del cambio sigue el modelo ADKAR, con 8 semanas de acompañamiento después de la entrega.

## Plan del proyecto

16 semanas, del 18 de enero al 7 de mayo de 2027, con una sola parada de planta de 5 días. La ingeniería conceptual de la oferta se valida en sitio, los equipos de largo plazo se piden en la semana 3 y el software se prueba en el gemelo digital mientras se fabrican los equipos. La ingeniería se cobra por horas reales (3.060 h, COP 190,8 millones) en dos contratos, diseño y procura e implementación, a una tarifa que refleja el valor que aporta cada integrante y no solo su salario. La celda robotizada de encanastado queda diseñada para una etapa posterior.

## Estructura del repositorio

| Carpeta | Contenido |
|---|---|
| [`0-estado-del-arte`](0-estado-del-arte) | Estado del arte de las tres líneas y justificación de la línea de yogur; investigación de la línea de queso campesino y versión inicial del proyecto con tres líneas |
| [`1-transformacion-digital-industrial`](1-transformacion-digital-industrial) | Parámetros de proceso, recetas y lotes, modelos ISA-88, arquitectura ISA-95, flujo de información OT/IT, equipos e instrumentación |
| [`2-gestion-y-evaluacion-de-la-produccion`](2-gestion-y-evaluacion-de-la-produccion) | Tiempos y capacidades, VSM e indicadores, necesidades de información con MES y ERP |
| [`3-planeacion-y-evaluacion-del-proyecto`](3-planeacion-y-evaluacion-del-proyecto) | Empresa, EDT del proyecto, [EDT del proceso productivo](3-planeacion-y-evaluacion-del-proyecto/EDTs/Proceso/EDT_Proceso_Yogur.md), cronograma, presupuesto, análisis económico, propuesta de valor y gestión del cambio |
| [`docs`](docs) | Página web del proyecto |

Cada carpeta de módulo tiene un `README.md` con el índice de sus entregables.

## Equipo

| Integrante | Rol | Líder técnico de |
|---|---|---|
| David Santiago Cortés Ávila | Gerente de proyecto | Integración de los módulos |
| Ana María Orozco Reyes | Líder de simulación y mejora | — (apoya el módulo 2: VSM y simulación) |
| Jesús Alberto Rivera Molina | Líder de arquitectura digital | Módulo 0 · Estado del arte |
| David Felipe Cárdenas Cubides | Líder de gestión de producción | Módulo 2 · Gestión y evaluación de la producción |
| Cristian Stiven Hoyos Peralta | Líder financiero y comercial | Módulo 3 · Planeación y evaluación del proyecto |
| José Andrés Zapata Piñeros | Líder de procesos e instrumentación | Módulo 1 · Transformación Digital Industrial |

## Fechas

| Hito | Fecha |
|---|---|
| Entrega intermedia | 12 de octubre de 2026 |
| Sustentaciones | 14 y 16 de octubre de 2026 |
| Visita a Alpina (Sopó) | 27 y 28 de octubre de 2026 |
| Entrega final | 7 de diciembre de 2026 |
