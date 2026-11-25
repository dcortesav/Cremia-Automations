# Estructura de desglose del trabajo (EDT) del proyecto

**Transformación Digital Industrial de la línea de yogur de La Hacienda**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Módulo 3 · Planeación y Evaluación de Proyectos

## 1. Alcance

La EDT cubre la ingeniería, el suministro, la integración, el desarrollo del software, la puesta en marcha y la adopción de la solución de automatización de la línea de yogur: dosificación automática, estandarización con leche en polvo, homogeneización, control térmico, medición de pH en línea, enfriamiento en intercambiador de placas y, de noche, con agua helada en la chaqueta, tanque refrigerado de leche para el segundo lote, llenadora de vasos, control de peso, codificado de lote y fecha, bandas, PLC, SCADA en Node-RED y la plataforma Cremia MES/ERP en Huawei Cloud. Incluye también la gestión del cambio de las personas que operan, mantienen y dirigen la planta, y seis semanas de estabilización con producción.

La celda robotizada de encanastado queda fuera de este proyecto: se diseña el espacio y la interfaz, y su compra se programa para una etapa posterior. Las horas son del equipo de Cremia Automations; el montaje lo ejecutan contratistas bajo su supervisión. Duración: **26 semanas**, del 18 de enero al 16 de julio de 2027, según el cronograma del proyecto. Las cifras de horas, tarifas y valores salen de `herramientas/parametros.yaml` y `herramientas/resultados.md`.

## 2. Marco metodológico

La EDT sigue la Guía del PMBOK (7.ª edición) y el Practice Standard for Work Breakdown Structures del PMI, con cuatro reglas:

1. **Regla del 100 %.** La EDT abarca todo el trabajo del contrato y nada más. La suma de las horas de los paquetes de cada cuenta de control es igual a la de la cuenta, y la suma de las diez cuentas es igual a la del proyecto.
2. **Descomposición por entregables.** Cada elemento es un producto verificable (planos P&ID, programa del PLC, protocolos SAT firmados), no una actividad. Las actividades están en el cronograma; los entregables son los que se aprueban y se pagan.
3. **Granularidad.** Los paquetes tienen entre 20 y 200 horas; en el cronograma se dividen en tareas semanales por persona.
4. **Cuentas de control y valor ganado.** Las diez cuentas del nivel 2 integran alcance, plazo y costo, de modo que el avance se mide con la técnica de valor ganado en el paquete 1.1.2.

| Criterio | EDT del proceso productivo | EDT del proyecto (este documento) |
| --- | --- | --- |
| Qué descompone | La transformación de la leche en yogur envasado | El trabajo de ingeniería, suministro, software, puesta en marcha y adopción que ejecuta Cremia |
| Naturaleza | Repetitiva: ocurre cada lote durante la vida de la planta | Temporal: del 18 de enero al 16 de julio de 2027 (26 semanas) |
| Normas que la rigen | ANSI/ISA-88, Decreto 616 de 2006, Resolución 2310 de 1986, NTC 805 | Guía del PMBOK, ANSI/ISA-95, ANSI/ISA-5.1, ANSI/ISA-101, ANSI/ISA-18.2, IEC 61131-3, IEC 62443 y RETIE |
| Entregables típicos | Leche estandarizada, mezcla pasteurizada, yogur envasado y estibas en frío | Plan del proyecto, P&ID, lista de E/S, programas del PLC, SCADA y plataforma MES/ERP, gemelo digital, protocolos FAT y SAT, personal capacitado y planos finales |
| Quién la ejecuta | Los operarios de La Hacienda | Los seis ingenieros de Cremia y sus contratistas |

## 3. Cambios frente a la versión de octubre de 2026

- La versión de octubre de 2026 duraba 16 semanas y licenciaba el SCADA, el MES y el ERP; esta versión dura 26 semanas porque Cremia desarrolla su propio software y porque la importación de equipos necesita 4 semanas de transporte y nacionalización después de la FAT.
- Se agrega la cuenta 1.6, Plataforma Cremia MES/ERP (1.500 h), y el SCADA en Node-RED pasa a la cuenta 1.5 (paquetes 1.5.3 a 1.5.5, 330 h). Las cuentas siguientes se renumeran: el gemelo digital pasa a 1.7, el montaje a 1.8, las pruebas a 1.9 y la gestión del cambio a 1.10.
- Las horas suben a 4.780 y se reparten para que nadie supere el 80 % de su capacidad en el proyecto ni 42 h en ninguna semana, descontando los festivos (la Semana Santa deja la semana 10 con dos días hábiles).
- Las tarifas suben para que el valor facturado cubra la nómina completa de las 26 semanas con el factor mínimo de 1,39.
- La estabilización con producción (semanas 21 a 26; la semana 21 solapa con el arranque y la validación) queda dentro del proyecto y con horas asignadas.
- La celda robotizada sigue fuera del alcance; el paquete 1.3.4 diseña la estación de encanastado y reserva el espacio para la celda.

## 4. Resumen

<!-- tabla:edt_resumen -->
| Código | Entregable | Paquetes | Horas | Semanas | Millones de COP |
| --- | --- | --- | --- | --- | --- |
| 1.1 | Gestión del proyecto | 4 | 310 | 1–26 | 22,35 |
| 1.2 | Ingeniería conceptual y básica | 5 | 260 | 1–3 | 18,70 |
| 1.3 | Ingeniería de detalle | 5 | 400 | 2–10 | 27,14 |
| 1.4 | Procura | 3 | 180 | 1–18 | 10,38 |
| 1.5 | Software de control y supervisión | 5 | 680 | 3–18 | 52,99 |
| 1.6 | Plataforma Cremia MES/ERP | 11 | 1.500 | 2–26 | 99,57 |
| 1.7 | Gemelo digital y puesta en marcha virtual | 3 | 340 | 4–19 | 25,45 |
| 1.8 | Montaje e instalación | 4 | 320 | 14–19 | 21,94 |
| 1.9 | Pruebas y puesta en marcha | 4 | 280 | 19–23 | 20,46 |
| 1.10 | Gestión del cambio, capacitación, estabilización y cierre | 4 | 510 | 1–26 | 34,73 |
| **Total** | | **48** | **4.780** | **1–26** | **333,71** |
<!-- /tabla:edt_resumen -->

La capacidad del equipo es de 6 personas × 26 semanas × 42 h, menos los 7 días festivos de 2027 que caen en el proyecto: 6.199 h. La EDT ocupa el 77 %; el resto se dedica a la coordinación interna y a la gestión comercial de Cremia.

<!-- tabla:edt_personas -->
| Integrante | Rol | Horas | Ocupación | Semana más cargada |
| --- | --- | --- | --- | --- |
| David Santiago Cortés Ávila | Gerente de proyecto | 775 | 75 % | 41 h |
| Ana María Orozco Reyes | Líder de simulación y mejora | 810 | 78 % | 42 h |
| Jesús Alberto Rivera Molina | Líder de arquitectura digital | 805 | 78 % | 42 h |
| David Felipe Cárdenas Cubides | Líder de gestión de producción | 815 | 79 % | 41 h |
| José Andrés Zapata Piñeros | Líder de procesos e instrumentación | 800 | 77 % | 42 h |
| Cristian Stiven Hoyos Peralta | Líder financiero y comercial | 775 | 75 % | 39 h |
| **Total** | | **4.780** | **77 %** | |
<!-- /tabla:edt_personas -->

La carga semanal se calcula repartiendo las horas de cada paquete entre sus semanas en proporción a sus días hábiles (`herramientas/modelo.py`, función `carga_semanal`) y se equilibra con `herramientas/balancear_carga.py`.

## 5. Árbol de la EDT

**1.0 Proyecto de Transformación Digital Industrial de la línea de yogur**

**1.1 Gestión del proyecto**

- 1.1.1 Plan del proyecto y línea base
- 1.1.2 Seguimiento y control de alcance, plazo y costo
- 1.1.3 Compras, contratos e importación
- 1.1.4 Cierre administrativo

**1.2 Ingeniería conceptual y básica**

- 1.2.1 Validación en sitio de datos, parámetros y capacidad del cuarto frío
- 1.2.2 VSM y simulación del estado propuesto
- 1.2.3 Arquitectura ISA-95, red OT/IT y nube
- 1.2.4 Modelos ISA-88 y recetas
- 1.2.5 P&ID e índice de instrumentos

**1.3 Ingeniería de detalle**

- 1.3.1 Especificación de equipos
- 1.3.2 Lista de E/S y arquitectura de control
- 1.3.3 Diseño eléctrico y de tableros
- 1.3.4 Estación de encanastado y análisis de riesgos
- 1.3.5 Distribución en planta

**1.4 Procura**

- 1.4.1 Cotizaciones y selección de proveedores
- 1.4.2 Órdenes de compra, seguimiento de fabricación e importación
- 1.4.3 Pruebas FAT

**1.5 Software de control y supervisión**

- 1.5.1 Programa del PLC: fases del proceso y lote nocturno
- 1.5.2 Programa del PLC: envasado y transporte
- 1.5.3 SCADA Node-RED: guía de estilo ISA-101 y pantallas
- 1.5.4 SCADA Node-RED: alarmas ISA-18.2 e historiador
- 1.5.5 Nodo de borde: usuarios, recetas locales y operación sin conexión

**1.6 Plataforma Cremia MES/ERP**

- 1.6.1 Infraestructura en Huawei Cloud, seguridad, respaldos y despliegue
- 1.6.2 Núcleo: datos maestros, usuarios y roles, auditoría y API
- 1.6.3 Recetas ISA-88 y órdenes de producción
- 1.6.4 Registro electrónico de lote y genealogía
- 1.6.5 Calidad y liberación de lotes
- 1.6.6 OEE, paradas y horas de equipo
- 1.6.7 Integración borde–nube: MQTT, almacenamiento y reenvío
- 1.6.8 ERP ligero I: inventario por lote y vencimiento, pedidos y despacho
- 1.6.9 ERP ligero II: compras, requerimiento de materiales, costo por lote y exportación al facturador
- 1.6.10 Tablero gerencial y reportes
- 1.6.11 Pruebas y documentación del software

**1.7 Gemelo digital y puesta en marcha virtual**

- 1.7.1 Gemelo digital de la línea
- 1.7.2 Simulación del envasado y el encanastado
- 1.7.3 Puesta en marcha virtual: PLC, SCADA y MES/ERP

**1.8 Montaje e instalación**

- 1.8.1 Montaje mecánico
- 1.8.2 Instalación eléctrica y de instrumentación
- 1.8.3 Red industrial, nodo de borde y nube de producción
- 1.8.4 Línea de vasos

**1.9 Pruebas y puesta en marcha**

- 1.9.1 Pruebas de lazo y de E/S
- 1.9.2 Pruebas SAT
- 1.9.3 Arranque con producto
- 1.9.4 Validación de calidad e inocuidad

**1.10 Gestión del cambio, capacitación, estabilización y cierre**

- 1.10.1 Gestión del cambio y comunicación
- 1.10.2 Capacitación por rol
- 1.10.3 Procedimientos, documentación y manuales
- 1.10.4 Estabilización y entrega

## 6. Diccionario de la EDT

La columna «Depende de» indica de qué paquete toma insumos cada uno. El plan usa ejecución rápida: salvo que se diga otra cosa, la dependencia es de comienzo a comienzo, con un desfase, y no exige que el predecesor termine. Así, la puesta en marcha virtual integra los paquetes de software a medida que terminan (semanas 16 a 18); la capacitación empieza con versiones preliminares de los procedimientos, que se cierran después de la SAT; y los procedimientos se escriben desde la semana 19 y se ajustan con los resultados de la SAT y del arranque. Las dependencias de fin a comienzo, que sí exigen que el predecesor termine, son el pedido de equipos (después de aprobar las hojas de datos en la semana 3), la FAT (después de la fabricación), la instalación de los equipos importados (después de su llegada en la semana 18) y el arranque con producto, que empieza en la semana 21 a medida que concluyen las pruebas SAT de los equipos de preparación y envasado; el acta de aprobación de la SAT y de la puesta en marcha (11 de junio, hito del pago) se firma con los primeros lotes del arranque.

<!-- tabla:edt_diccionario -->
| Código | Paquete de trabajo | Entregable verificable | Responsable (horas) | Horas | Semanas | Depende de |
| --- | --- | --- | --- | --- | --- | --- |
| 1.1.1 | Plan del proyecto y línea base | Plan aprobado por el cliente | David Cortés | 30 | 1 | — |
| 1.1.2 | Seguimiento y control de alcance, plazo y costo | Informes semanales de avance, plazo, costo y valor ganado | David Cortés (110), Cristian Hoyos (90) | 200 | 2–25 | 1.1.1 |
| 1.1.3 | Compras, contratos e importación | Contratos, órdenes firmadas y trámites de importación | Cristian Hoyos | 60 | 1–18 | 1.4.1 |
| 1.1.4 | Cierre administrativo | Acta de cierre y lecciones aprendidas | David Cortés | 20 | 26 | 1.10.4 |
| 1.2.1 | Validación en sitio de datos, parámetros y capacidad del cuarto frío | Datos de proceso, tiempos y capacidad de la caldera y del cuarto frío validados en planta | José Andrés Zapata | 40 | 1 | 1.1.1 |
| 1.2.2 | VSM y simulación del estado propuesto | Simulación en Tecnomatix del programa de dos lotes | Ana Orozco | 60 | 1–3 | 1.2.1 |
| 1.2.3 | Arquitectura ISA-95, red OT/IT y nube | Arquitectura, plan de red, zonas IEC 62443 y región de Huawei Cloud aprobados | Jesús Rivera | 60 | 1–3 | 1.2.1 |
| 1.2.4 | Modelos ISA-88 y recetas | Modelos ISA-88 y recetas maestras aprobados | David Cortés | 40 | 2–3 | 1.2.1 |
| 1.2.5 | P&ID e índice de instrumentos | P&ID, índice de instrumentos y hojas de datos de largo plazo aprobados | José Andrés Zapata (30), Jesús Rivera (30) | 60 | 2–3 | 1.2.1 |
| 1.3.1 | Especificación de equipos | Hojas de datos de equipos, incluidos TK-102 y el circuito de agua helada a la chaqueta | José Andrés Zapata | 100 | 2–6 | 1.2.5 |
| 1.3.2 | Lista de E/S y arquitectura de control | Lista de E/S y topología de control | Jesús Rivera | 60 | 4–5 | 1.2.5 |
| 1.3.3 | Diseño eléctrico y de tableros | Planos eléctricos y de tableros según RETIE | Jesús Rivera (20), José Andrés Zapata (110) | 130 | 4–10 | 1.3.2 |
| 1.3.4 | Estación de encanastado y análisis de riesgos | Diseño de la estación de encanastado con la mesa acumuladora, espacio para la celda y matriz de riesgos | Ana Orozco | 60 | 3–9 | 1.2.2 |
| 1.3.5 | Distribución en planta | Plano de distribución con TK-102 | Ana Orozco (45), David Cárdenas (5) | 50 | 3–8 | 1.3.1 |
| 1.4.1 | Cotizaciones y selección de proveedores | Cuadro comparativo de proveedores | Cristian Hoyos | 50 | 1–3 | Ingeniería conceptual de la oferta |
| 1.4.2 | Órdenes de compra, seguimiento de fabricación e importación | Órdenes emitidas en la semana 4, plan de entregas y nacionalización | Cristian Hoyos | 70 | 4–18 | 1.3.1, 1.4.1 |
| 1.4.3 | Pruebas FAT | Protocolos FAT ejecutados por el fabricante y aprobados de forma remota, por videoconferencia | José Andrés Zapata (15), Ana Orozco (45) | 60 | 13–14 | 1.4.2 |
| 1.5.1 | Programa del PLC: fases del proceso y lote nocturno | Programa de fases, lazos PID, enfriamiento nocturno y enclavamientos probado en el emulador | David Cortés (140), Jesús Rivera (60) | 200 | 5–13 | 1.3.2, 1.2.4 |
| 1.5.2 | Programa del PLC: envasado y transporte | Programa de envasado, peso y transporte probado | Jesús Rivera (90), David Cortés (60) | 150 | 6–14 | 1.3.2 |
| 1.5.3 | SCADA Node-RED: guía de estilo ISA-101 y pantallas | Guía de estilo y pantallas de HMI-01 y HMI-02 | David Cárdenas (30), Ana Orozco (10), David Cortés (50) | 90 | 3–6 | 1.2.4 |
| 1.5.4 | SCADA Node-RED: alarmas ISA-18.2 e historiador | Alarmas con prioridades y registro, historiador local y tendencias | David Cárdenas | 140 | 8–15 | 1.5.3 |
| 1.5.5 | Nodo de borde: usuarios, recetas locales y operación sin conexión | Nodo de borde que opera 72 h sin internet, con imagen en el PC de repuesto | Jesús Rivera (75), David Cárdenas (25) | 100 | 13–18 | 1.5.4, 1.6.7 |
| 1.6.1 | Infraestructura en Huawei Cloud, seguridad, respaldos y despliegue | Entornos de desarrollo, pruebas y producción con respaldos probados | Jesús Rivera (100), David Cárdenas (20) | 120 | 6–12 | 1.2.3 |
| 1.6.2 | Núcleo: datos maestros, usuarios y roles, auditoría y API | Núcleo de la plataforma con pruebas automáticas | David Cárdenas (175), Jesús Rivera (5) | 180 | 2–7 | 1.2.3 |
| 1.6.3 | Recetas ISA-88 y órdenes de producción | Tres recetas maestras cargadas, órdenes y receta de control escalada | David Cortés (35), José Andrés Zapata (145), David Cárdenas (20) | 200 | 7–13 | 1.6.2, 1.2.4 |
| 1.6.4 | Registro electrónico de lote y genealogía | Expediente de lote y genealogía probados con lotes simulados | David Cárdenas (95), David Cortés (45) | 140 | 8–16 | 1.6.3 |
| 1.6.5 | Calidad y liberación de lotes | Flujo de liberación y retención con firma electrónica | José Andrés Zapata (75), Ana Orozco (20), David Cárdenas (5) | 100 | 11–17 | 1.6.4 |
| 1.6.6 | OEE, paradas y horas de equipo | OEE por turno con los datos del arranque (versión 2) | Ana Orozco (60), Jesús Rivera (60) | 120 | 21–25 | 1.6.4, 1.9.3 |
| 1.6.7 | Integración borde–nube: MQTT, almacenamiento y reenvío | Mensajería probada con cortes de internet simulados | Jesús Rivera (30), Cristian Hoyos (50), David Cárdenas (20) | 100 | 9–17 | 1.6.1, 1.6.2 |
| 1.6.8 | ERP ligero I: inventario por lote y vencimiento, pedidos y despacho | Inventario, pedidos y despacho en producción | Cristian Hoyos | 160 | 6–17 | 1.6.2 |
| 1.6.9 | ERP ligero II: compras, requerimiento de materiales, costo por lote y exportación al facturador | Compras, requerimiento de materiales, costo por lote y exportación al facturador (versión 2) | Cristian Hoyos | 140 | 20–25 | 1.6.8 |
| 1.6.10 | Tablero gerencial y reportes | Tablero diario y reportes aprobados por la gerencia (versión 2) | Ana Orozco (50), Jesús Rivera (30) | 80 | 23–26 | 1.6.6, 1.6.9 |
| 1.6.11 | Pruebas y documentación del software | Informes de pruebas unitarias, de integración, de carga y de seguridad; manuales | Ana Orozco (120), Jesús Rivera (25), Cristian Hoyos (15) | 160 | 10–25 | 1.6.2 |
| 1.7.1 | Gemelo digital de la línea | Gemelo digital en Siemens NX Mechatronics Concept Designer y Tecnomatix con sensores y actuadores virtuales | Ana Orozco | 160 | 4–12 | 1.2.2 |
| 1.7.2 | Simulación del envasado y el encanastado | Simulación de las líneas de bolsas y vasos y del encajonado manual | Ana Orozco | 60 | 9–16 | 1.3.4 |
| 1.7.3 | Puesta en marcha virtual: PLC, SCADA y MES/ERP | Informe de validación con lotes, recetas y cortes de internet simulados | David Cortés (115), David Cárdenas (5) | 120 | 16–19 | 1.5.1–1.5.5, 1.6.3–1.6.5, 1.6.7, 1.7.1 |
| 1.8.1 | Montaje mecánico | Equipos, TK-102, tuberías y soportes instalados | José Andrés Zapata | 110 | 14–19 | 1.3.5; 1.4.3 para los equipos importados |
| 1.8.2 | Instalación eléctrica y de instrumentación | Tableros e instrumentos conectados | Jesús Rivera (75), José Andrés Zapata (25) | 100 | 14–19 | 1.3.3; 1.4.3 |
| 1.8.3 | Red industrial, nodo de borde y nube de producción | Red, nodo de borde, conectividad doble y entorno de producción en servicio | Jesús Rivera (20), David Cárdenas (30) | 50 | 16–18 | 1.6.1, 1.5.5 |
| 1.8.4 | Línea de vasos | Llenadora, dosificación de fruta, controladora, codificador y mesa acumuladora instalados | Ana Orozco (40), José Andrés Zapata (20) | 60 | 18–19 | 1.4.3 |
| 1.9.1 | Pruebas de lazo y de E/S | Protocolos de lazo firmados | Jesús Rivera (40), Ana Orozco (5), José Andrés Zapata (5) | 50 | 19–20 | 1.8.2 |
| 1.9.2 | Pruebas SAT | Protocolos SAT firmados, incluido un corte de internet en planta | David Cortés (55), Jesús Rivera (10), José Andrés Zapata (10), David Cárdenas (5) | 80 | 20–21 | 1.9.1, 1.7.3 |
| 1.9.3 | Arranque con producto | Lotes conformes de YB-200, YV-150 y YV-300, incluido un lote 2 nocturno de cada referencia | José Andrés Zapata (55), Ana Orozco (35), Jesús Rivera (10) | 100 | 21–22 | 1.9.2 |
| 1.9.4 | Validación de calidad e inocuidad | Registros de puntos críticos, curvas de enfriamiento nocturno y primeros lotes liberados por registro de proceso | José Andrés Zapata (5), David Cárdenas (45) | 50 | 21–23 | 1.9.3 |
| 1.10.1 | Gestión del cambio y comunicación | Plan de gestión del cambio, comunicaciones y medición de adopción | Cristian Hoyos | 130 | 1–26 | 1.1.1 |
| 1.10.2 | Capacitación por rol | Personal capacitado y evaluado por rol, en el gemelo digital y en la plataforma | David Cárdenas (75), Ana Orozco (35), José Andrés Zapata (10), Cristian Hoyos (10) | 130 | 17–20 | 1.7.3 |
| 1.10.3 | Procedimientos, documentación y manuales | Procedimientos operativos, planos finales, manuales, depósito del código fuente y programa del PLC entregado con la licencia de Studio 5000 de la planta activada | David Cárdenas (95), Jesús Rivera (5) | 100 | 19–25 | 1.7.3, 1.9.2 |
| 1.10.4 | Estabilización y entrega | Acompañamiento con producción en las semanas 22–26, dentro de la estabilización de seis semanas (21–26; el paquete cubre 22–26 y la semana 21 es de arranque/validación), acta de entrega y metas de adopción medidas | David Cortés (75), José Andrés Zapata (45), David Cárdenas (25), Ana Orozco (5) | 150 | 22–26 | 1.9.4, 1.10.2, 1.10.3 |
<!-- /tabla:edt_diccionario -->

## 7. Contratos y valor de la ingeniería

La ingeniería se factura en dos contratos, con las horas de la EDT a una tarifa propia de cada integrante. La tarifa parte del costo por hora de cada uno y lo multiplica por un factor según el tipo de valor que aporta: 2,13 para las especialidades escasas y críticas (arquitectura OT/IT, nube y ciberseguridad; SCADA y plataforma MES/ERP), 2,01 para el núcleo técnico del proceso y de la validación, 1,80 para la dirección del proyecto, que ya parte de un costo mayor, y 1,59 para la gestión y el soporte. En conjunto, el valor facturado es 1,41 veces la nómina completa de las 26 semanas, por encima del mínimo de 1,39.

<!-- tabla:tarifas -->
| Integrante | Tipo de valor | Horas | Tarifa (COP/h) | Factor sobre su costo | Millones de COP |
| --- | --- | --- | --- | --- | --- |
| David Santiago Cortés Ávila | Dirección y control | 775 | 90.000 | 1,80 | 69,75 |
| Ana María Orozco Reyes | Núcleo técnico de validación | 810 | 67.000 | 2,01 | 54,27 |
| Jesús Alberto Rivera Molina | Especialidad escasa y crítica | 805 | 71.000 | 2,13 | 57,16 |
| David Felipe Cárdenas Cubides | Especialidad escasa y crítica | 815 | 71.000 | 2,13 | 57,87 |
| José Andrés Zapata Piñeros | Núcleo técnico del proceso | 800 | 67.000 | 2,01 | 53,60 |
| Cristian Stiven Hoyos Peralta | Gestión y soporte | 775 | 53.000 | 1,59 | 41,08 |
| **Total** | | **4.780** | **69.815 en promedio** | | **333,71** |
<!-- /tabla:tarifas -->

<!-- tabla:contratos -->
| Contrato | Paquetes de la EDT | Semanas | Horas | Millones de COP |
| --- | --- | --- | --- | --- |
| 1. Diseño, procura y gestión de compras | 1.1.1, 1.1.3 y cuentas 1.2 a 1.4 | 1–18 | 930 | 62,1 |
| 2. Implementación, software, puesta en marcha y adopción | 1.1.2, 1.1.4 y cuentas 1.5 a 1.10 | 2–26 | 3.850 | 271,6 |
| **Total** | | **1–26** | **4.780** | **333,7** |
<!-- /tabla:contratos -->

## 8. Articulación con el cronograma y el presupuesto

**Ruta crítica.** Validación de la ingeniería básica (semanas 1 a 3) → pedido de los equipos de largo plazo (semana 4) → fabricación (semanas 4 a 13) → FAT (semanas 13 y 14) → transporte y nacionalización (semanas 15 a 18) → montaje con preinstalación desde la semana 14 y parada en la semana 19 → pruebas de lazo y SAT (semanas 19 a 21) → arranque y validación (semanas 21 a 23) → estabilización (semanas 21 a 26) → entrega (semana 26).

El software tiene su propia cadena: núcleo de la plataforma (semanas 2 a 7) → recetas, registro de lote, calidad e integración (semanas 7 a 17) → puesta en marcha virtual (semanas 16 a 19) → SAT (semanas 20 y 21). Tiene una holgura de una semana frente a las pruebas de lazo; si se consume, se pasan a la versión 2 funciones que no se necesitan para producir, no el arranque.

La versión 2 forma una segunda cadena sin holgura que también termina en la semana 26: arranque con producto (semanas 21 y 22) → OEE, paradas y horas de equipo (semanas 21 a 25) → tablero gerencial y reportes (semanas 23 a 26). El pago del 10 % de la entrega depende de ella, así que un traslado de funciones desde la versión 1 se compensa con horas del equipo en las semanas 23 a 26, no con plazo.

<!-- tabla:pagos -->
| Hito | Semana | Porcentaje | Millones de COP |
| --- | --- | --- | --- |
| Firma del contrato (anticipo) | 1 | 30 % | 448,6 |
| Pruebas FAT aprobadas | 14 | 30 % | 448,6 |
| Pruebas SAT y puesta en marcha | 21 | 30 % | 448,6 |
| Cierre y entrega | 26 | 10 % | 149,5 |
| **Total** | | **100 %** | **1.495,5** |
<!-- /tabla:pagos -->

Con los equipos y el software (975,7, incluida la licencia de Studio 5000 de la planta), la ingeniería (333,7), el montaje (75,3) y la contingencia (110,8), la inversión total es de COP 1.495,5 millones. Para el cliente, el VPN al 15 % después de impuestos es de COP 189,4 millones, la TIR de 18,9 % y la recuperación de 3,9 años, según la propuesta económica.

## 9. Criterios de la descomposición

- Cada paquete tiene un entregable verificable y un responsable, de modo que se puede seguir semana a semana.
- Las cuentas 1.2 a 1.9 siguen el ciclo de vida de un proyecto de automatización: ingeniería, compra, programación, prueba virtual, montaje y prueba en sitio.
- La cuenta 1.6 separa el software de gestión en paquetes de menos de 200 h y en dos versiones, para que un retraso del desarrollo no mueva el arranque.
- La cuenta 1.10 trata a las personas como parte del alcance: la gestión del cambio empieza en la semana 1, la capacitación usa el gemelo digital antes del arranque y la estabilización con producción tiene horas asignadas.
- La programación del PLC sigue el modelo procedimental ISA-88 y la estrategia de control definida en el documento de equipos: control regulatorio PID con rango dividido, prealimentación y control de relación, sin control avanzado.

## Referencias

- Project Management Institute. Guía de los fundamentos para la dirección de proyectos (Guía del PMBOK), 7.ª ed.
- Project Management Institute. Practice Standard for Work Breakdown Structures, 3.ª ed.
- IEC 61131-3. Programmable controllers, Part 3: Programming languages.
