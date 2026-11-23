# Cremia Automations

Proyecto Integrador de Automatización de Procesos de Manufactura (APM) 2026-2S, Universidad Nacional de Colombia.

**Cremia Automations** es la empresa integradora del equipo. El proyecto es la Transformación Digital Industrial de la **línea de yogur** de la planta La Hacienda Productos Alimenticios.

Página web: https://dcortesav.github.io/Cremia-Automations/

Versión vigente: noviembre de 2026.

## El proyecto en cifras

| | Situación actual | Propuesta |
|---|---|---|
| Lotes por día (550 L de leche) | 1 | 2 |
| Operación | Un turno de 8 h, lunes a sábado | Lunes a sábado de 7:00 a 19:00 en turnos de 7 h; turno corto el domingo para envasar el lote del sábado |
| Referencias | Bolsa de 200 ml | Bolsa de 200 ml y vasos de 150 y 300 ml |
| Unidades por lote | 3.052 bolsas llenadas, 2.898 conformes | 3.079 bolsas, 4.369 vasos de 150 ml o 2.260 vasos de 300 ml, con 1,5 % no conforme |
| Unidades conformes por día | 2.898 | 6.505 en promedio |
| Tiempo estándar por lote | 601 min | ≈ 563 min; el tanque queda libre a las 15:05 para el segundo lote |
| Enfriamiento | Natural, toda la noche | Lote 1 en intercambiador de placas; lote 2 con agua helada en la chaqueta, de noche y sin operario |
| Producto no conforme | 5,06 % | 1,5 % o menos |
| Instrumentación conectada | Ninguna | 25 sensores, 22 actuadores, 68 señales de E/S y 20 nodos EtherNet/IP (diseño completo) |
| Robots | Ninguno | Uno de paletizado (R-501), diseñado y comprado en una etapa posterior |
| Control | Válvulas manuales, termómetro y acidómetro | Control secuencial ISA-88 y lazos PID en el PLC, sin control avanzado |
| Gestión de la información | Registros en papel | PLC CompactLogix 5380, SCADA desarrollado en Node-RED en la planta y plataforma Cremia MES/ERP en Huawei Cloud, sin licencias de terceros en el runtime (supervisión y gestión) |

El estado actual se toma del estudio de tiempos de la planta (Grimaldo, Moreno y Salamanca, 2015).

## Propuesta de valor para los dueños

| Dimensión | Resultado esperado |
|---|---|
| Productividad | De 724 a 1.301 unidades conformes por operario al día (+80 %) |
| Costos | Mano de obra de 155 a 95 COP por unidad conforme (−39 %) y costo real por lote |
| Calidad | Producto no conforme de 5,06 % a 1,5 % o menos, con peso del 100 % |
| Trazabilidad | Registro electrónico de cada lote, desde la cantina hasta la estiba |
| Información y decisiones | Tablero diario con OEE, rendimiento, consumos y paradas, en la nube, disponible aunque falle la planta |
| Eficiencia de la empacadora | OEE estimado de 65 % hoy; meta de 82 % |
| Resultado financiero | Inversión de COP 1.464,5 millones; VPN al 15 % después de impuestos de COP 231,0 millones, TIR de 19,8 % y recuperación en 3,8 años |

La transformación incluye a las personas: no hay despidos, el segundo lote crea un puesto, la capacitación es por rol en el gemelo digital, la gestión del cambio sigue el modelo ADKAR y el proyecto incluye seis semanas de estabilización con producción.

## Plan del proyecto

26 semanas, del 18 de enero al 16 de julio de 2027, con una sola parada de planta de 5 días. La ingeniería conceptual de la oferta se valida en sitio, los equipos de largo plazo se piden en la semana 4 y llegan, ya nacionalizados, en la semana 18; mientras tanto, Cremia desarrolla el software y lo prueba en el gemelo digital. La ingeniería se cobra por horas reales (4.780 h, COP 333,7 millones) en dos contratos, a una tarifa que refleja el valor que aporta cada integrante y que cubre la nómina completa del proyecto. La celda robotizada de encanastado queda diseñada para una etapa posterior. La oferta se firma con cartas de intención de los distribuidores por al menos el 85 % del volumen de vasos, porque la viabilidad depende de esas referencias.

## Estructura del repositorio

| Carpeta | Contenido |
|---|---|
| [`0-estado-del-arte`](0-estado-del-arte) | Estado del arte de las tres líneas y justificación de la línea de yogur (versión inicial); investigación de las líneas de queso campesino y kumis |
| [`1-transformacion-digital-industrial`](1-transformacion-digital-industrial) | Parámetros de proceso, recetas y lotes, modelos ISA-88, arquitectura ISA-95, flujo de información OT/IT, equipos e instrumentación, y la plataforma Cremia MES/ERP con el SCADA en Node-RED |
| [`2-gestion-y-evaluacion-de-la-produccion`](2-gestion-y-evaluacion-de-la-produccion) | Tiempos y capacidades, VSM del estado actual y del propuesto, e indicadores; necesidades de información del MES y del ERP |
| [`3-planeacion-y-evaluacion-del-proyecto`](3-planeacion-y-evaluacion-del-proyecto) | Empresa, EDT del proyecto, [EDT del proceso productivo](3-planeacion-y-evaluacion-del-proyecto/EDTs/Proceso/EDT_Proceso_Yogur.md), cronograma, presupuesto, análisis económico, propuesta de valor y gestión del cambio |
| [`herramientas`](herramientas) | Fuente única de cifras (`parametros.yaml`), modelo de producción, programa diario y finanzas, generador de tablas y verificador de consistencia |
| [`docs`](docs) | Página web del proyecto |

Cada carpeta de módulo tiene un `README.md` con el índice de sus entregables.

## Cómo se mantienen consistentes las cifras

Todas las cifras de la propuesta salen de [`herramientas/parametros.yaml`](herramientas/parametros.yaml). Después de cambiar un supuesto:

```powershell
.venv\Scripts\python.exe -X utf8 herramientas\modelo.py               # recalcula y escribe herramientas\resultados.md
.venv\Scripts\python.exe -X utf8 herramientas\generar_tablas.py        # actualiza las tablas generadas de los documentos
.venv\Scripts\python.exe -X utf8 herramientas\verificar_consistencia.py  # busca cifras desactualizadas
.venv\Scripts\python.exe -m pytest herramientas\tests -q              # pruebas del modelo, del programa y del verificador
```

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
