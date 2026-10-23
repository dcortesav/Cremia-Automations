# Estructura de desglose del trabajo (EDT) del proyecto

**Transformación Digital Industrial de la línea de yogur de La Hacienda**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Módulo 3 · Planeación y Evaluación de Proyectos

## 1. Alcance

La EDT cubre la ingeniería, el suministro, la integración, la puesta en marcha y la adopción de la solución de automatización de la línea de yogur: dosificación automática, estandarización con leche en polvo, homogeneización, control térmico, medición de pH en línea, enfriamiento en intercambiador de placas, llenadora de vasos, control de peso, codificado de lote y fecha, transporte, celda de encanastado, PLC, SCADA, MES e integración con el ERP. Incluye también la gestión del cambio de las personas que operan, mantienen y dirigen la planta.

Tiene tres niveles (proyecto, entregable y paquete de trabajo) y cumple la regla del 100 %. Las horas son del equipo de Cremia Automations; el montaje lo ejecutan contratistas bajo su supervisión. Duración del proyecto: **24 semanas** (5,5 meses), según el cronograma del proyecto.

## 2. Marco metodológico

La EDT sigue la Guía del PMBOK (7.ª edición) y el Practice Standard for Work Breakdown Structures del PMI, con cuatro reglas:

1. **Regla del 100 %.** La EDT abarca todo el trabajo del contrato y nada más. La suma de las horas de los paquetes de cada cuenta de control es igual a la de la cuenta, y la suma de las nueve cuentas es igual a la del proyecto.
2. **Descomposición por entregables.** Cada elemento es un producto verificable (planos P&ID, programa del PLC, protocolos SAT firmados), no una actividad. Las actividades están en el cronograma; los entregables son los que se aprueban y se pagan.
3. **Granularidad.** Los paquetes tienen entre 40 y 300 horas del equipo; en el cronograma se dividen en tareas semanales de 8 a 80 horas por persona.
4. **Cuentas de control y valor ganado.** Las nueve cuentas del nivel 2 integran alcance, plazo y costo, de modo que el avance se mide con la técnica de valor ganado en el paquete 1.1.2.

| Criterio | EDT del proceso productivo | EDT del proyecto (este documento) |
| --- | --- | --- |
| Qué descompone | La transformación de la leche en yogur envasado | El trabajo de ingeniería, suministro, puesta en marcha y adopción que ejecuta Cremia |
| Naturaleza | Repetitiva: ocurre cada lote durante la vida de la planta | Temporal: del 18 de enero al 2 de julio de 2027 (24 semanas) |
| Normas que la rigen | ANSI/ISA-88, Decreto 616 de 2006, Resolución 2310 de 1986, NTC 805 | Guía del PMBOK, ANSI/ISA-95, ANSI/ISA-5.1, ANSI/ISA-101, IEC 61131-3, ISO 13849-1 y RETIE |
| Entregables típicos | Leche estandarizada, mezcla pasteurizada, yogur envasado y estibas en frío | Plan del proyecto, P&ID, lista de E/S, programas del PLC, SCADA y MES, gemelo digital, protocolos FAT y SAT, personal capacitado y planos finales |
| Quién la ejecuta | Los operarios de La Hacienda | Los seis ingenieros de Cremia y sus contratistas |

## 3. Cambios frente a la primera versión

- La duración baja de 35 a 24 semanas. La ingeniería conceptual de la oferta se valida en sitio en lugar de repetirse, y los equipos de mayor tiempo de entrega se piden en la semana 4.
- La cuenta 1.9 pasa a llamarse Gestión del cambio, capacitación y cierre, con un paquete nuevo (1.9.1) para la gestión del cambio y la comunicación con el personal de la planta.
- Las horas bajan de 6.320 a 4.760 y se reparten para que nadie supere el 80 % de su capacidad; en la primera versión una persona quedaba al 101 % y otra al 20 %.

## 4. Resumen

| Código | Entregable | Paquetes | Horas |
| --- | --- | --- | --- |
| 1.1 | Gestión del proyecto | 4 | 340 |
| 1.2 | Ingeniería conceptual y básica | 5 | 380 |
| 1.3 | Ingeniería de detalle | 6 | 780 |
| 1.4 | Procura | 3 | 280 |
| 1.5 | Software de control, supervisión y gestión | 5 | 1.040 |
| 1.6 | Gemelo digital y puesta en marcha virtual | 3 | 500 |
| 1.7 | Montaje e instalación | 4 | 500 |
| 1.8 | Pruebas y puesta en marcha | 4 | 420 |
| 1.9 | Gestión del cambio, capacitación y cierre | 4 | 520 |
| **Total** | | **38** | **4.760** |

La capacidad del equipo es de 6 personas × 24 semanas × 42 h = 6.048 h. La EDT ocupa el 79 %; el resto cubre coordinación interna, reprocesos e imprevistos.

| Integrante | Rol | Horas | Ocupación |
| --- | --- | --- | --- |
| David Santiago Cortés Ávila | Gerente de proyecto | 800 | 79 % |
| Ana María Orozco Reyes | Líder de simulación y mejora | 800 | 79 % |
| Jesús Alberto Rivera Molina | Líder de arquitectura digital | 800 | 79 % |
| David Felipe Cárdenas Cubides | Líder de gestión de producción | 800 | 79 % |
| José Andrés Zapata Piñeros | Líder de procesos e instrumentación | 800 | 79 % |
| Cristian Stiven Hoyos Peralta | Líder financiero y comercial | 760 | 75 % |
| **Total** | | **4.760** | **79 %** |

Ninguna persona supera el 80 % de su capacidad (1.008 h en 24 semanas). La holgura de cerca del 21 % cubre la coordinación interna, la revisión cruzada de programas y planos, los imprevistos de procura y el soporte comercial y administrativo.

## 5. Árbol de la EDT

**1.0 Proyecto de Transformación Digital Industrial de la línea de yogur**

**1.1 Gestión del proyecto**

- 1.1.1 Plan del proyecto y línea base
- 1.1.2 Seguimiento y control de alcance, plazo y costo
- 1.1.3 Compras y contratos
- 1.1.4 Cierre administrativo

**1.2 Ingeniería conceptual y básica**

- 1.2.1 Validación en sitio de datos y parámetros
- 1.2.2 VSM y simulación del estado propuesto
- 1.2.3 Arquitectura ISA-95 y red OT/IT
- 1.2.4 Modelos ISA-88 y recetas
- 1.2.5 P&ID e índice de instrumentos

**1.3 Ingeniería de detalle**

- 1.3.1 Especificación de equipos
- 1.3.2 Lista de E/S y arquitectura de control
- 1.3.3 Diseño eléctrico y de tableros
- 1.3.4 Celda de encanastado y análisis de riesgos
- 1.3.5 Interfaz HMI
- 1.3.6 Distribución en planta

**1.4 Procura**

- 1.4.1 Cotizaciones y selección de proveedores
- 1.4.2 Órdenes de compra y seguimiento de fabricación
- 1.4.3 Pruebas FAT

**1.5 Software de control, supervisión y gestión**

- 1.5.1 PLC del proceso
- 1.5.2 PLC de envasado y transporte
- 1.5.3 SCADA e historiador
- 1.5.4 MES e integración con ERP
- 1.5.5 Recetas maestras, registro de lote y reportes

**1.6 Gemelo digital y puesta en marcha virtual**

- 1.6.1 Gemelo digital de la línea
- 1.6.2 Simulación de la celda
- 1.6.3 Puesta en marcha virtual

**1.7 Montaje e instalación**

- 1.7.1 Montaje mecánico
- 1.7.2 Instalación eléctrica y de instrumentación
- 1.7.3 Red industrial y servidores
- 1.7.4 Línea de vasos y celda de encanastado

**1.8 Pruebas y puesta en marcha**

- 1.8.1 Pruebas de lazo y de E/S
- 1.8.2 Pruebas SAT
- 1.8.3 Arranque con producto
- 1.8.4 Validación de calidad e inocuidad

**1.9 Gestión del cambio, capacitación y cierre**

- 1.9.1 Gestión del cambio y comunicación
- 1.9.2 Capacitación por rol
- 1.9.3 Procedimientos, documentación y manuales
- 1.9.4 Entrega y acompañamiento del arranque

## 6. Diccionario de la EDT

| Código | Paquete de trabajo | Entregable verificable | Responsable (horas) | Horas | Depende de |
| --- | --- | --- | --- | --- | --- |
| 1.1.1 | Plan del proyecto y línea base | Plan aprobado por el cliente | David Cortés | 40 | — |
| 1.1.2 | Seguimiento y control de alcance, plazo y costo | Informes semanales de avance, plazo y costo | David Cortés (120), Cristian Hoyos (60) | 180 | 1.1.1 |
| 1.1.3 | Compras y contratos | Contratos y órdenes firmadas | Cristian Hoyos | 80 | 1.4.1 |
| 1.1.4 | Cierre administrativo | Acta de cierre y lecciones aprendidas | David Cortés | 40 | 1.9.4 |
| 1.2.1 | Validación en sitio de datos y parámetros | Datos de proceso, tiempos y parámetros validados en planta | José Andrés Zapata | 60 | 1.1.1 |
| 1.2.2 | VSM y simulación del estado propuesto | VSM futuro y simulación del estado propuesto | Ana Orozco | 100 | 1.2.1 |
| 1.2.3 | Arquitectura ISA-95 y red OT/IT | Arquitectura ISA-95 y plan de red aprobados | Jesús Rivera | 60 | 1.2.1 |
| 1.2.4 | Modelos ISA-88 y recetas | Modelos ISA-88 y recetas maestras aprobados | José Andrés Zapata | 60 | 1.2.1 |
| 1.2.5 | P&ID e índice de instrumentos | P&ID e índice de instrumentos aprobados | José Andrés Zapata (60), Jesús Rivera (40) | 100 | 1.2.1 |
| 1.3.1 | Especificación de equipos | Hojas de datos de equipos (largo plazo en la semana 3) | José Andrés Zapata | 160 | 1.2.5 |
| 1.3.2 | Lista de E/S y arquitectura de control | Lista de E/S y topología de control | Jesús Rivera | 80 | 1.2.5 |
| 1.3.3 | Diseño eléctrico y de tableros | Planos eléctricos y de tableros | Jesús Rivera (100), Cristian Hoyos (100) | 200 | 1.3.2 |
| 1.3.4 | Celda de encanastado y análisis de riesgos | Diseño de la celda y matriz de riesgos | Ana Orozco | 140 | 1.2.1 |
| 1.3.5 | Interfaz HMI | Guía de estilo ISA-101 y pantallas | David Cárdenas | 120 | 1.2.4 |
| 1.3.6 | Distribución en planta | Plano de distribución | David Cárdenas | 80 | 1.3.1 |
| 1.4.1 | Cotizaciones y selección de proveedores | Cuadro comparativo de proveedores | Cristian Hoyos | 80 | 1.2.5 |
| 1.4.2 | Órdenes de compra y seguimiento de fabricación | Órdenes emitidas y plan de entregas | Cristian Hoyos | 100 | 1.3.1, 1.4.1 |
| 1.4.3 | Pruebas FAT | Protocolos FAT firmados | José Andrés Zapata (40), Ana Orozco (60) | 100 | 1.4.2 |
| 1.5.1 | PLC del proceso | Programa de fases, lazos PID y enclavamientos probado | David Cortés (160), Jesús Rivera (140) | 300 | 1.3.2, 1.2.4 |
| 1.5.2 | PLC de envasado y transporte | Programa de envasado, peso y transporte probado | Jesús Rivera (100), Cristian Hoyos (80) | 180 | 1.3.2 |
| 1.5.3 | SCADA e historiador | Aplicación SCADA con alarmas, tendencias e historiador | David Cárdenas | 220 | 1.3.5 |
| 1.5.4 | MES e integración con ERP | Órdenes, trazabilidad e indicadores integrados con el ERP | David Cárdenas (200), Cristian Hoyos (60) | 260 | 1.2.3, 1.2.4 |
| 1.5.5 | Recetas maestras, registro de lote y reportes | Tres recetas maestras cargadas y reporte de lote | José Andrés Zapata | 80 | 1.5.4 |
| 1.6.1 | Gemelo digital de la línea | Gemelo digital con sensores y actuadores virtuales | Ana Orozco | 220 | 1.3.6 |
| 1.6.2 | Simulación de la celda | Celda simulada y programa del robot | Ana Orozco | 120 | 1.3.4 |
| 1.6.3 | Puesta en marcha virtual | Informe de validación con lotes y recetas | David Cortés | 160 | 1.5.1–1.5.3, 1.6.1 |
| 1.7.1 | Montaje mecánico | Equipos instalados | José Andrés Zapata | 160 | 1.4.3 |
| 1.7.2 | Instalación eléctrica y de instrumentación | Tableros e instrumentos conectados | Jesús Rivera | 160 | 1.3.3, 1.4.3 |
| 1.7.3 | Red industrial y servidores | Red y servidores en servicio | Jesús Rivera | 80 | 1.2.3 |
| 1.7.4 | Línea de vasos y celda de encanastado | Línea de vasos y celda instaladas con sus seguridades | Ana Orozco | 100 | 1.4.3, 1.6.2 |
| 1.8.1 | Pruebas de lazo y de E/S | Protocolos de lazo firmados | José Andrés Zapata | 80 | 1.7.2 |
| 1.8.2 | Pruebas SAT | Protocolos SAT firmados | David Cortés | 120 | 1.8.1, 1.6.3 |
| 1.8.3 | Arranque con producto | Lotes conformes de YB-200, YV-150 y YV-300 | José Andrés Zapata (100), David Cortés (40) | 140 | 1.8.2 |
| 1.8.4 | Validación de calidad e inocuidad | Registros de puntos críticos y lotes liberados | David Cárdenas | 80 | 1.8.3 |
| 1.9.1 | Gestión del cambio y comunicación | Plan de gestión del cambio, comunicaciones y medición de adopción | Cristian Hoyos (100), David Cortés (60) | 160 | 1.1.1 |
| 1.9.2 | Capacitación por rol | Personal capacitado y evaluado por rol | David Cárdenas (60), Ana Orozco (60), Cristian Hoyos (60) | 180 | 1.6.3 |
| 1.9.3 | Procedimientos, documentación y manuales | Procedimientos operativos, planos finales y manuales | Jesús Rivera (40), David Cárdenas (40), Cristian Hoyos (40) | 120 | 1.8.2 |
| 1.9.4 | Entrega y acompañamiento del arranque | Acta de entrega y plan de acompañamiento | David Cortés | 60 | 1.8.4, 1.9.2, 1.9.3 |

## 7. Fichas por cuenta de control

| Cuenta | Horas | Objetivo | Desafío principal | Mitigación |
| --- | --- | --- | --- | --- |
| 1.1 Gestión del proyecto | 340 | Dirigir el proyecto, controlar cambios y medir el avance con valor ganado | Solicitudes de cambio de alcance durante la ejecución | Procedimiento formal de solicitudes de cambio con evaluación de costo y plazo |
| 1.2 Ingeniería conceptual y básica | 380 | Validar en planta la ingeniería de la oferta: datos de proceso, VSM, ISA-88, ISA-95 y P&ID | Diferencias entre los datos del caso de estudio y la planta real | Levantamiento en sitio en las semanas 1 y 2 y simulación del estado propuesto en Tecnomatix |
| 1.3 Ingeniería de detalle | 780 | Especificar equipos, lista de E/S, planos eléctricos según RETIE, celda robotizada, HMI y distribución | Espacio limitado en la sala de derivados lácteos | Distribución en planta con zonas húmeda y seca separadas y pasillos de 800 mm o más |
| 1.4 Procura | 280 | Cotizar, comprar, seguir la fabricación y probar los equipos en fábrica | Fabricación de 10 semanas de los equipos de largo plazo | Pedido en la semana 4 con hojas de datos aprobadas en la semana 3, seguimiento semanal y FAT antes del despacho |
| 1.5 Software | 1.040 | Programar el PLC según IEC 61131-3 e ISA-88, el SCADA según ISA-101 e ISA-18.2, el MES y la integración con el ERP | Integrar PLC, OPC UA, SQL y B2MML sin pérdida de datos de lote | Fases ISA-88 desacopladas de la interfaz y base de datos única del MES |
| 1.6 Gemelo digital | 500 | Construir el gemelo de la línea, simular la celda y hacer la puesta en marcha virtual | Diferencias entre el modelo y el comportamiento real | Gemelo en Tecnomatix Plant Simulation y RobotStudio conectado al PLC emulado (Studio 5000 Logix Emulate) por OPC UA |
| 1.7 Montaje e instalación | 500 | Supervisar el montaje mecánico, eléctrico, de red y de la celda | Parada de solo 5 días para conectar el tanque T-301 | Preinstalación de tuberías y canalizaciones en las semanas 15 a 17 sin detener la planta |
| 1.8 Pruebas y puesta en marcha | 420 | Probar lazos y E/S, hacer las SAT y arrancar las tres referencias | Yogur viscoso en el intercambiador y fruta en trozos | Pruebas con agua y con producto, y arranque escalonado por referencia |
| 1.9 Gestión del cambio, capacitación y cierre | 520 | Preparar a las personas, escribir los procedimientos, entregar la documentación y acompañar el arranque | Resistencia al cambio y poca experiencia con sistemas digitales | Plan ADKAR desde la semana 1, agentes de cambio, capacitación en el gemelo digital y 8 semanas de acompañamiento |

## 8. Articulación con el cronograma y el presupuesto

**Ruta crítica.** Validación de la ingeniería básica (semanas 1 a 3) → pedido de equipos de largo plazo (semana 4) → fabricación de la fase 1 (semanas 4 a 13) → FAT (semana 14) → montaje con parada en la semana 18 → pruebas de lazo (19) → SAT (20) → arranque y validación (20 a 23) → entrega (24). El detalle está en el cronograma del proyecto.

| Hito de pago | Semana | Porcentaje | Millones de COP |
| --- | --- | --- | --- |
| Firma del contrato | 1 | 30 % | 496,7 |
| Pruebas FAT de la fase 1 aprobadas | 14 | 30 % | 496,7 |
| Pruebas SAT y puesta en marcha | 21 | 30 % | 496,7 |
| Entrega y documentación | 24 | 10 % | 165,5 |
| **Total** | | **100 %** | **1.655,6** |

Los servicios de ingeniería de la EDT valen COP 301,8 millones: 5,5 meses de nómina (COP 217,4 millones) con el factor de administración, imprevistos y utilidad de 1,39. Con los equipos (1.140,0), el montaje (91,2) y la contingencia (122,6), la inversión total es de COP 1.655,6 millones. Para el cliente, el VPN al 15 % es de COP 318 millones, la TIR de 21,8 % y la recuperación de 3,1 años, según la propuesta económica.

## 9. Criterios de la descomposición

- Cada paquete tiene un entregable verificable y un responsable, y ninguno pasa de 300 horas, de modo que se puede seguir semana a semana.
- Las cuentas 1.2 a 1.8 siguen el ciclo de vida de un proyecto de automatización: ingeniería, compra, programación, prueba virtual, montaje y prueba en sitio.
- La cuenta 1.9 trata a las personas como parte del alcance: la gestión del cambio empieza en la semana 1, la capacitación usa el gemelo digital antes del arranque y el acompañamiento sigue después de la entrega.
- La programación del PLC sigue el modelo procedimental ISA-88 y la estrategia de control definida en el documento de equipos: control regulatorio PID con rango dividido, prealimentación y control de relación, sin control avanzado.

## Referencias

- ANSI/ISA-88.00.01-2010 y ANSI/ISA-95.00.01-2010.
- IEC 61131-3. Programmable controllers, Part 3: Programming languages.
- ISO 13849-1:2015 e ISO 10218-2:2011.
- Reglamento Técnico de Instalaciones Eléctricas (RETIE), Ministerio de Minas y Energía.
- Project Management Institute. Guía de los fundamentos para la dirección de proyectos (Guía del PMBOK), 7.ª ed.
- Project Management Institute. Practice Standard for Work Breakdown Structures, 3.ª ed.
