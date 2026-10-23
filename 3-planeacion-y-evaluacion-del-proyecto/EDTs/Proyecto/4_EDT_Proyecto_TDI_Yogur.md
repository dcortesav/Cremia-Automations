# Estructura de desglose del trabajo (EDT) del proyecto

**Transformación Digital Industrial de la línea de yogur de La Hacienda**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Módulo 3 · Planeación y Evaluación de Proyectos

## 1. Alcance

La EDT cubre la ingeniería, el suministro, la integración, la puesta en marcha y la adopción de la solución de automatización de la línea de yogur: dosificación automática, estandarización con leche en polvo, homogeneización, control térmico, medición de pH en línea, enfriamiento en intercambiador de placas, llenadora de vasos, control de peso, codificado de lote y fecha, bandas, PLC, SCADA, MES e integración con el ERP. Incluye también la gestión del cambio de las personas que operan, mantienen y dirigen la planta.

La celda robotizada de encanastado queda fuera de este proyecto: se diseña el espacio y la interfaz, y su compra se programa para una etapa posterior. Las horas son del equipo de Cremia Automations; el montaje lo ejecutan contratistas bajo su supervisión. Duración: **16 semanas**, según el cronograma del proyecto.

## 2. Marco metodológico

La EDT sigue la Guía del PMBOK (7.ª edición) y el Practice Standard for Work Breakdown Structures del PMI, con cuatro reglas:

1. **Regla del 100 %.** La EDT abarca todo el trabajo del contrato y nada más. La suma de las horas de los paquetes de cada cuenta de control es igual a la de la cuenta, y la suma de las nueve cuentas es igual a la del proyecto.
2. **Descomposición por entregables.** Cada elemento es un producto verificable (planos P&ID, programa del PLC, protocolos SAT firmados), no una actividad. Las actividades están en el cronograma; los entregables son los que se aprueban y se pagan.
3. **Granularidad.** Los paquetes tienen entre 20 y 200 horas; en el cronograma se dividen en tareas semanales por persona.
4. **Cuentas de control y valor ganado.** Las nueve cuentas del nivel 2 integran alcance, plazo y costo, de modo que el avance se mide con la técnica de valor ganado en el paquete 1.1.2.

| Criterio | EDT del proceso productivo | EDT del proyecto (este documento) |
| --- | --- | --- |
| Qué descompone | La transformación de la leche en yogur envasado | El trabajo de ingeniería, suministro, puesta en marcha y adopción que ejecuta Cremia |
| Naturaleza | Repetitiva: ocurre cada lote durante la vida de la planta | Temporal: del 18 de enero al 7 de mayo de 2027 (16 semanas) |
| Normas que la rigen | ANSI/ISA-88, Decreto 616 de 2006, Resolución 2310 de 1986, NTC 805 | Guía del PMBOK, ANSI/ISA-95, ANSI/ISA-5.1, ANSI/ISA-101, IEC 61131-3 y RETIE |
| Entregables típicos | Leche estandarizada, mezcla pasteurizada, yogur envasado y estibas en frío | Plan del proyecto, P&ID, lista de E/S, programas del PLC, SCADA y MES, gemelo digital, protocolos FAT y SAT, personal capacitado y planos finales |
| Quién la ejecuta | Los operarios de La Hacienda | Los seis ingenieros de Cremia y sus contratistas |

## 3. Cambios frente a la primera versión

- La duración baja de 35 a 16 semanas: la ingeniería conceptual de la oferta se valida en sitio, los equipos de largo plazo se piden en la semana 3 y el software se prueba en el gemelo digital durante la fabricación.
- Las horas bajan de 6.320 a 3.060 y se reparten para que nadie supere el 80 % de su capacidad; en la primera versión una persona quedaba al 101 % y otra al 20 %.
- La ingeniería se cobra por las horas de la EDT a una tarifa propia de cada integrante, según el valor que aporta, y no por meses de nómina completa; así horas, plazo y costo son coherentes.
- La cuenta 1.9 incluye la gestión del cambio (paquete 1.9.1) además de la capacitación y el cierre.
- La celda robotizada sale del alcance; el paquete 1.3.4 diseña la estación de encanastado y reserva el espacio para la celda.

## 4. Resumen

| Código | Entregable | Paquetes | Horas | Semanas |
| --- | --- | --- | --- | --- |
| 1.1 | Gestión del proyecto | 4 | 230 | 1–16 |
| 1.2 | Ingeniería conceptual y básica | 5 | 240 | 1–2 |
| 1.3 | Ingeniería de detalle | 6 | 480 | 1–6 |
| 1.4 | Procura | 3 | 170 | 1–13 |
| 1.5 | Software de control, supervisión y gestión | 5 | 700 | 4–12 |
| 1.6 | Gemelo digital y puesta en marcha virtual | 3 | 320 | 4–12 |
| 1.7 | Montaje e instalación | 4 | 300 | 8–14 |
| 1.8 | Pruebas y puesta en marcha | 4 | 270 | 15–16 |
| 1.9 | Gestión del cambio, capacitación y cierre | 4 | 350 | 1–16 |
| **Total** | | **38** | **3.060** | **1–16** |

La capacidad del equipo es de 6 personas × 16 semanas × 42 h = 4.032 h. La EDT ocupa el 76 %.

| Integrante | Rol | Horas | Ocupación |
| --- | --- | --- | --- |
| David Santiago Cortés Ávila | Gerente de proyecto | 530 | 79 % |
| Ana María Orozco Reyes | Líder de simulación y mejora | 470 | 70 % |
| Jesús Alberto Rivera Molina | Líder de arquitectura digital | 520 | 77 % |
| David Felipe Cárdenas Cubides | Líder de gestión de producción | 520 | 77 % |
| José Andrés Zapata Piñeros | Líder de procesos e instrumentación | 520 | 77 % |
| Cristian Stiven Hoyos Peralta | Líder financiero y comercial | 500 | 74 % |
| **Total** | | **3.060** | **76 %** |

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
- 1.3.4 Estación de encanastado y análisis de riesgos
- 1.3.5 Interfaz HMI
- 1.3.6 Distribución en planta

**1.4 Procura**

- 1.4.1 Cotizaciones y selección de proveedores
- 1.4.2 Órdenes de compra y seguimiento de fabricación
- 1.4.3 Pruebas FAT

**1.5 Software de control, supervisión y gestión**

- 1.5.1 Programa del PLC: fases del proceso
- 1.5.2 Programa del PLC: envasado y transporte
- 1.5.3 SCADA e historiador
- 1.5.4 MES e integración con ERP
- 1.5.5 Recetas maestras, registro de lote y reportes

**1.6 Gemelo digital y puesta en marcha virtual**

- 1.6.1 Gemelo digital de la línea
- 1.6.2 Simulación del envasado y el encanastado
- 1.6.3 Puesta en marcha virtual

**1.7 Montaje e instalación**

- 1.7.1 Montaje mecánico
- 1.7.2 Instalación eléctrica y de instrumentación
- 1.7.3 Red industrial y servidores
- 1.7.4 Línea de vasos

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
| 1.1.1 | Plan del proyecto y línea base | Plan aprobado por el cliente | David Cortés | 30 | — |
| 1.1.2 | Seguimiento y control de alcance, plazo y costo | Informes semanales de avance, plazo y costo | David Cortés (90), Cristian Hoyos (40) | 130 | 1.1.1 |
| 1.1.3 | Compras y contratos | Contratos y órdenes firmadas | Cristian Hoyos | 50 | 1.4.1 |
| 1.1.4 | Cierre administrativo | Acta de cierre y lecciones aprendidas | David Cortés | 20 | 1.9.4 |
| 1.2.1 | Validación en sitio de datos y parámetros | Datos de proceso, tiempos y parámetros validados en planta | José Andrés Zapata | 40 | 1.1.1 |
| 1.2.2 | VSM y simulación del estado propuesto | VSM futuro y simulación del estado propuesto | Ana Orozco | 60 | 1.2.1 |
| 1.2.3 | Arquitectura ISA-95 y red OT/IT | Arquitectura ISA-95 y plan de red aprobados | Jesús Rivera | 40 | 1.2.1 |
| 1.2.4 | Modelos ISA-88 y recetas | Modelos ISA-88 y recetas maestras aprobados | José Andrés Zapata | 40 | 1.2.1 |
| 1.2.5 | P&ID e índice de instrumentos | P&ID e índice de instrumentos aprobados | José Andrés Zapata (40), Jesús Rivera (20) | 60 | 1.2.1 |
| 1.3.1 | Especificación de equipos | Hojas de datos de equipos (largo plazo en la semana 2) | José Andrés Zapata | 90 | 1.2.5 |
| 1.3.2 | Lista de E/S y arquitectura de control | Lista de E/S y topología de control | Jesús Rivera | 60 | 1.2.5 |
| 1.3.3 | Diseño eléctrico y de tableros | Planos eléctricos y de tableros | Jesús Rivera (70), Cristian Hoyos (60) | 130 | 1.3.2 |
| 1.3.4 | Estación de encanastado y análisis de riesgos | Diseño de la estación de encanastado, espacio reservado para la celda y matriz de riesgos | Ana Orozco | 60 | 1.2.1 |
| 1.3.5 | Interfaz HMI | Guía de estilo ISA-101 y pantallas | David Cárdenas | 90 | 1.2.4 |
| 1.3.6 | Distribución en planta | Plano de distribución | David Cárdenas | 50 | 1.3.1 |
| 1.4.1 | Cotizaciones y selección de proveedores | Cuadro comparativo de proveedores | Cristian Hoyos | 50 | 1.2.5 |
| 1.4.2 | Órdenes de compra y seguimiento de fabricación | Órdenes emitidas y plan de entregas | Cristian Hoyos | 60 | 1.3.1, 1.4.1 |
| 1.4.3 | Pruebas FAT | Protocolos FAT firmados | José Andrés Zapata (30), Ana Orozco (30) | 60 | 1.4.2 |
| 1.5.1 | Programa del PLC: fases del proceso | Programa de fases, lazos PID y enclavamientos probado | David Cortés (110), Jesús Rivera (90) | 200 | 1.3.2, 1.2.4 |
| 1.5.2 | Programa del PLC: envasado y transporte | Programa de envasado, peso y transporte probado | Jesús Rivera (70), Cristian Hoyos (60) | 130 | 1.3.2 |
| 1.5.3 | SCADA e historiador | Aplicación SCADA con alarmas, tendencias e historiador | David Cárdenas | 140 | 1.3.5 |
| 1.5.4 | MES e integración con ERP | Órdenes, trazabilidad e indicadores integrados con el ERP | David Cárdenas (130), Cristian Hoyos (40) | 170 | 1.2.3, 1.2.4 |
| 1.5.5 | Recetas maestras, registro de lote y reportes | Tres recetas maestras cargadas y reporte de lote | José Andrés Zapata | 60 | 1.5.4 |
| 1.6.1 | Gemelo digital de la línea | Gemelo digital con sensores y actuadores virtuales | Ana Orozco | 160 | 1.3.6 |
| 1.6.2 | Simulación del envasado y el encanastado | Simulación de las líneas de bolsas y vasos y del encanastado | Ana Orozco | 60 | 1.3.4 |
| 1.6.3 | Puesta en marcha virtual | Informe de validación con lotes y recetas | David Cortés | 100 | 1.5.1–1.5.3, 1.6.1 |
| 1.7.1 | Montaje mecánico | Equipos instalados | José Andrés Zapata | 100 | 1.4.3 |
| 1.7.2 | Instalación eléctrica y de instrumentación | Tableros e instrumentos conectados | Jesús Rivera | 100 | 1.3.3, 1.4.3 |
| 1.7.3 | Red industrial y servidores | Red y servidores en servicio | Jesús Rivera | 40 | 1.2.3 |
| 1.7.4 | Línea de vasos | Llenadora, dosificación de fruta, controladora y codificador de vasos instalados | Ana Orozco | 60 | 1.4.3 |
| 1.8.1 | Pruebas de lazo y de E/S | Protocolos de lazo firmados | José Andrés Zapata | 50 | 1.7.2 |
| 1.8.2 | Pruebas SAT | Protocolos SAT firmados | David Cortés | 70 | 1.8.1, 1.6.3 |
| 1.8.3 | Arranque con producto | Lotes conformes de YB-200, YV-150 y YV-300 | José Andrés Zapata (70), David Cortés (30) | 100 | 1.8.2 |
| 1.8.4 | Validación de calidad e inocuidad | Registros de puntos críticos y lotes liberados | David Cárdenas | 50 | 1.8.3 |
| 1.9.1 | Gestión del cambio y comunicación | Plan de gestión del cambio, comunicaciones y medición de adopción | Cristian Hoyos (70), David Cortés (40) | 110 | 1.1.1 |
| 1.9.2 | Capacitación por rol | Personal capacitado y evaluado por rol | David Cárdenas (40), Ana Orozco (40), Cristian Hoyos (40) | 120 | 1.6.3 |
| 1.9.3 | Procedimientos, documentación y manuales | Procedimientos operativos, planos finales y manuales | Jesús Rivera (30), David Cárdenas (20), Cristian Hoyos (30) | 80 | 1.8.2 |
| 1.9.4 | Entrega y acompañamiento del arranque | Acta de entrega y plan de acompañamiento | David Cortés | 40 | 1.8.4, 1.9.2, 1.9.3 |

## 7. Contratos y valor de la ingeniería

La ingeniería se factura en dos contratos, con las horas de la EDT a una tarifa propia de cada integrante. La tarifa parte del costo por hora de cada uno y lo multiplica por un factor según el tipo de valor que aporta: 1,9 para las especialidades escasas y críticas (arquitectura OT/IT y ciberseguridad; SCADA, MES y ERP), 1,8 para el núcleo técnico del proceso y de la validación, 1,6 para la dirección del proyecto y 1,4 para la gestión y el soporte.

| Integrante | Tipo de valor | Horas | Tarifa (COP/h) | Millones de COP |
| --- | --- | --- | --- | --- |
| David Santiago Cortés Ávila | Dirección y control | 530 | 80.000 | 42,40 |
| Jesús Alberto Rivera Molina | Especialidad escasa y crítica | 520 | 63.000 | 32,76 |
| David Felipe Cárdenas Cubides | Especialidad escasa y crítica | 520 | 63.000 | 32,76 |
| José Andrés Zapata Piñeros | Núcleo técnico del proceso | 520 | 60.000 | 31,20 |
| Ana María Orozco Reyes | Núcleo técnico de validación | 470 | 60.000 | 28,20 |
| Cristian Stiven Hoyos Peralta | Gestión y soporte | 500 | 47.000 | 23,50 |
| **Total** | | **3.060** | **62.400 en promedio** | **190,82** |
| Contrato | Cuentas de la EDT | Semanas | Horas | Millones de COP |
| 1. Diseño y procura | 1.1 a 1.4 | 1–13 | 1.120 | 67,6 |
| 2. Implementación, puesta en marcha y adopción | 1.5 a 1.9 | 4–16 | 1.940 | 123,2 |
| **Total** | | **1–16** | **3.060** | **190,8** |

## 8. Articulación con el cronograma y el presupuesto

**Ruta crítica.** Validación de la ingeniería básica (semanas 1 y 2) → pedido de equipos de largo plazo (semana 3) → fabricación (semanas 3 a 12) → FAT (semana 13) → montaje con parada en la semana 14 → pruebas de lazo y SAT (semana 15) → arranque y validación (semanas 15 y 16) → entrega (semana 16).

| Hito de pago | Semana | Porcentaje | Millones de COP |
| --- | --- | --- | --- |
| Firma del contrato | 1 | 30 % | 397,7 |
| Pruebas FAT aprobadas | 13 | 30 % | 397,7 |
| Pruebas SAT y puesta en marcha | 15 | 30 % | 397,7 |
| Entrega y documentación | 16 | 10 % | 132,7 |
| **Total** | | **100 %** | **1.325,8** |

Con los equipos (960,0), la ingeniería (190,8), el montaje (76,8) y la contingencia (98,2), la inversión total es de COP 1.325,8 millones. Para el cliente, el VPN al 15 % es de COP 617 millones, la TIR de 30,6 % y la recuperación de 2,7 años, según la propuesta económica.

## 9. Criterios de la descomposición

- Cada paquete tiene un entregable verificable y un responsable, de modo que se puede seguir semana a semana.
- Las cuentas 1.2 a 1.8 siguen el ciclo de vida de un proyecto de automatización: ingeniería, compra, programación, prueba virtual, montaje y prueba en sitio.
- La cuenta 1.9 trata a las personas como parte del alcance: la gestión del cambio empieza en la semana 1, la capacitación usa el gemelo digital antes del arranque y el acompañamiento sigue después de la entrega.
- La programación del PLC sigue el modelo procedimental ISA-88 y la estrategia de control definida en el documento de equipos: control regulatorio PID con rango dividido, prealimentación y control de relación, sin control avanzado.

## Referencias

- Project Management Institute. Guía de los fundamentos para la dirección de proyectos (Guía del PMBOK), 7.ª ed.
- Project Management Institute. Practice Standard for Work Breakdown Structures, 3.ª ed.
- IEC 61131-3. Programmable controllers, Part 3: Programming languages.
