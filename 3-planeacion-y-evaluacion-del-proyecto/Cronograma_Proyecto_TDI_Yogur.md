# Cronograma del proyecto

**Transformación Digital Industrial de la línea de yogur de La Hacienda**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Módulo 3 · Planeación y Evaluación de Proyectos

## 1. Supuestos

- El cronograma corresponde a la ejecución del proyecto en la planta del cliente y se construye a partir de la EDT del proyecto.
- Inicio: lunes 18 de enero de 2027, después de que el cliente acepta la oferta con las cartas de intención de los distribuidores para las referencias en vaso.
- Duración: **26 semanas** (unos 6 meses). Entrega: viernes 16 de julio de 2027.
- La planta sigue produciendo un lote diario durante el proyecto. La conexión de los equipos nuevos al tanque de proceso requiere una sola parada de 5 días hábiles, en la semana 19 (24 a 28 de mayo de 2027, sin festivos).
- El equipo es de seis ingenieros con jornada de 42 horas semanales (Ley 2101 de 2021). El proyecto ocupa el 77 % de su capacidad, descontados los festivos, y nadie pasa de 42 h en ninguna semana ni de las horas hábiles de las semanas con festivos; el resto del tiempo se dedica a la coordinación interna y a la gestión comercial de Cremia. El montaje lo ejecutan contratistas bajo la supervisión de Cremia.
- La ingeniería conceptual de la oferta (diagnóstico, VSM, modelos ISA-88, arquitectura ISA-95, recetas, inventario y dimensionamiento de equipos) es el punto de partida: en la ejecución se valida en sitio, no se repite.
- El alcance incluye la preparación automatizada, el enfriamiento nocturno del lote 2, el tanque refrigerado TK-102, la línea de bolsas, la línea de vasos, el SCADA en Node-RED y la plataforma Cremia MES/ERP. La celda robotizada de encanastado queda diseñada y con su espacio reservado, pero se compra en una etapa posterior.

## 2. Por qué 26 semanas

| Decisión | Efecto en el plazo | Justificación |
| --- | --- | --- |
| Validar la ingeniería conceptual de la oferta en lugar de repetirla | La ingeniería básica toma 3 semanas | El diagnóstico, el VSM, los modelos ISA-88, la arquitectura ISA-95 y el dimensionamiento de equipos ya están hechos y entregados con la oferta |
| Pedir en la semana 4 los equipos de mayor tiempo de entrega | La fabricación (10 semanas) termina en la semana 13 | Homogeneizador, intercambiador, chiller, llenadora y controladoras de peso tienen hojas de datos cerradas con el dimensionamiento de la oferta |
| Prever 4 semanas de transporte y nacionalización después de la FAT | Los equipos importados llegan en la semana 18 | Los equipos europeos viajan por vía marítima a Cartagena (unos 18 a 22 días) y se nacionalizan en 5 a 7 días hábiles. La FAT se ejecuta de forma remota: el fabricante corre los protocolos en su planta por videoconferencia y Cremia y los dos agentes de cambio los siguen y los aprueban desde Colombia, sin viajes |
| Desarrollar el software propio mientras se fabrican los equipos | El software no alarga el plazo | 2.180 h de PLC, SCADA y plataforma: la versión 1 entre las semanas 2 y 18 y la versión 2 entre las semanas 20 y 26, probadas en el gemelo digital antes de la parada |
| Preinstalar tuberías, tableros, bases y TK-102 sin detener la planta | La parada se limita a 5 días | Solo la conexión al tanque de proceso T-301 exige detener la producción |
| Estabilizar con producción dentro del proyecto | Seis semanas de acompañamiento (21 a 26; la semana 21 coincide con el arranque) | La entrega se hace con las metas de adopción medidas, no al terminar las pruebas |
| Dejar la celda robotizada para una etapa posterior | Sin instalación ni pruebas de la celda | El encajonado manual con mesa acumuladora no limita los dos lotes diarios |

El riesgo de pedir equipos antes de cerrar todo el detalle se controla con tres medidas: las hojas de datos de largo plazo se aprueban con el cliente en la semana 3, la contingencia del 8 %, que queda del lado de Cremia porque el valor de la oferta es un precio fijo, cubre cambios menores, y los contratos de compra fijan las interfaces (conexiones sanitarias, señales y protocolo) desde el pedido.

| Indicador | Versión de octubre de 2026 | Versión vigente |
| --- | --- | --- |
| Duración | 16 semanas (versión de octubre de 2026) | 26 semanas |
| Fecha de entrega | 7 de mayo de 2027 (versión de octubre de 2026) | 16 de julio de 2027 |
| Semana del pedido de equipos | 3 | 4 |
| Transporte y nacionalización | No previstos | 4 semanas |
| Software de supervisión y gestión | Licenciado | Desarrollado por Cremia (2.180 h con el PLC) |
| Horas de ingeniería | 3.060 h (versión de octubre de 2026) | 4.780 h |
| Ocupación del equipo | 76 %, sin control semanal (versión de octubre de 2026) | 77 %, con un máximo de 42 h en cualquier semana |
| Parada de planta | 5 días | 5 días |
| Estabilización con producción | Fuera del proyecto | Semanas 21 a 26 |

## 3. Cronograma por paquete de trabajo

<!-- tabla:cronograma -->
| Código | Actividad | Semanas | Inicio | Fin |
| --- | --- | --- | --- | --- |
| 1.1 | **Gestión del proyecto** | 1–26 | 18 ene | 16 jul |
| 1.1.1 | Plan del proyecto y línea base | 1 | 18 ene | 22 ene |
| 1.1.2 | Seguimiento y control de alcance, plazo y costo | 2–25 | 25 ene | 9 jul |
| 1.1.3 | Compras, contratos e importación | 1–18 | 18 ene | 21 may |
| 1.1.4 | Cierre administrativo | 26 | 12 jul | 16 jul |
| 1.2 | **Ingeniería conceptual y básica** | 1–3 | 18 ene | 5 feb |
| 1.2.1 | Validación en sitio de datos, parámetros y capacidad del cuarto frío | 1 | 18 ene | 22 ene |
| 1.2.2 | VSM y simulación del estado propuesto | 1–3 | 18 ene | 5 feb |
| 1.2.3 | Arquitectura ISA-95, red OT/IT y nube | 1–3 | 18 ene | 5 feb |
| 1.2.4 | Modelos ISA-88 y recetas | 2–3 | 25 ene | 5 feb |
| 1.2.5 | P&ID e índice de instrumentos | 2–3 | 25 ene | 5 feb |
| 1.3 | **Ingeniería de detalle** | 2–10 | 25 ene | 26 mar |
| 1.3.1 | Especificación de equipos | 2–6 | 25 ene | 26 feb |
| 1.3.2 | Lista de E/S y arquitectura de control | 4–5 | 8 feb | 19 feb |
| 1.3.3 | Diseño eléctrico y de tableros | 4–10 | 8 feb | 26 mar |
| 1.3.4 | Estación de encanastado y análisis de riesgos | 3–9 | 1 feb | 19 mar |
| 1.3.5 | Distribución en planta | 3–8 | 1 feb | 12 mar |
| 1.4 | **Procura** | 1–18 | 18 ene | 21 may |
| 1.4.1 | Cotizaciones y selección de proveedores | 1–3 | 18 ene | 5 feb |
| 1.4.2 | Órdenes de compra, seguimiento de fabricación e importación | 4–18 | 8 feb | 21 may |
| 1.4.3 | Pruebas FAT | 13–14 | 12 abr | 23 abr |
| 1.5 | **Software de control y supervisión** | 3–18 | 1 feb | 21 may |
| 1.5.1 | Programa del PLC: fases del proceso y lote nocturno | 5–13 | 15 feb | 16 abr |
| 1.5.2 | Programa del PLC: envasado y transporte | 6–14 | 22 feb | 23 abr |
| 1.5.3 | SCADA Node-RED: guía de estilo ISA-101 y pantallas | 3–6 | 1 feb | 26 feb |
| 1.5.4 | SCADA Node-RED: alarmas ISA-18.2 e historiador | 8–15 | 8 mar | 30 abr |
| 1.5.5 | Nodo de borde: usuarios, recetas locales y operación sin conexión | 13–18 | 12 abr | 21 may |
| 1.6 | **Plataforma Cremia MES/ERP** | 2–26 | 25 ene | 16 jul |
| 1.6.1 | Infraestructura en Huawei Cloud, seguridad, respaldos y despliegue | 6–12 | 22 feb | 9 abr |
| 1.6.2 | Núcleo: datos maestros, usuarios y roles, auditoría y API | 2–7 | 25 ene | 5 mar |
| 1.6.3 | Recetas ISA-88 y órdenes de producción | 7–13 | 1 mar | 16 abr |
| 1.6.4 | Registro electrónico de lote y genealogía | 8–16 | 8 mar | 7 may |
| 1.6.5 | Calidad y liberación de lotes | 11–17 | 29 mar | 14 may |
| 1.6.6 | OEE, paradas y horas de equipo | 21–25 | 7 jun | 9 jul |
| 1.6.7 | Integración borde–nube: MQTT, almacenamiento y reenvío | 9–17 | 15 mar | 14 may |
| 1.6.8 | ERP ligero I: inventario por lote y vencimiento, pedidos y despacho | 6–17 | 22 feb | 14 may |
| 1.6.9 | ERP ligero II: compras, requerimiento de materiales, costo por lote y exportación al facturador | 20–25 | 31 may | 9 jul |
| 1.6.10 | Tablero gerencial y reportes | 23–26 | 21 jun | 16 jul |
| 1.6.11 | Pruebas y documentación del software | 10–25 | 22 mar | 9 jul |
| 1.7 | **Gemelo digital y puesta en marcha virtual** | 4–19 | 8 feb | 28 may |
| 1.7.1 | Gemelo digital de la línea | 4–12 | 8 feb | 9 abr |
| 1.7.2 | Simulación del envasado y el encanastado | 9–16 | 15 mar | 7 may |
| 1.7.3 | Puesta en marcha virtual: PLC, SCADA y MES/ERP | 16–19 | 3 may | 28 may |
| 1.8 | **Montaje e instalación** | 14–19 | 19 abr | 28 may |
| 1.8.1 | Montaje mecánico | 14–19 | 19 abr | 28 may |
| 1.8.2 | Instalación eléctrica y de instrumentación | 14–19 | 19 abr | 28 may |
| 1.8.3 | Red industrial, nodo de borde y nube de producción | 16–18 | 3 may | 21 may |
| 1.8.4 | Línea de vasos | 18–19 | 17 may | 28 may |
| 1.9 | **Pruebas y puesta en marcha** | 19–23 | 24 may | 25 jun |
| 1.9.1 | Pruebas de lazo y de E/S | 19–20 | 24 may | 4 jun |
| 1.9.2 | Pruebas SAT | 20–21 | 31 may | 11 jun |
| 1.9.3 | Arranque con producto | 21–22 | 7 jun | 18 jun |
| 1.9.4 | Validación de calidad e inocuidad | 21–23 | 7 jun | 25 jun |
| 1.10 | **Gestión del cambio, capacitación, estabilización y cierre** | 1–26 | 18 ene | 16 jul |
| 1.10.1 | Gestión del cambio y comunicación | 1–26 | 18 ene | 16 jul |
| 1.10.2 | Capacitación por rol | 17–20 | 10 may | 4 jun |
| 1.10.3 | Procedimientos, documentación y manuales | 19–25 | 24 may | 9 jul |
| 1.10.4 | Estabilización y entrega | 22–26 | 14 jun | 16 jul |
| — | Fabricación de los equipos de largo plazo | 4–13 | 8 feb | 16 abr |
| — | Transporte y nacionalización de los equipos importados | 15–18 | 26 abr | 21 may |
| — | Parada de planta para la conexión al tanque de proceso | 19 | 24 may | 28 may |
<!-- /tabla:cronograma -->

Los festivos de 2027 que caen en el proyecto reducen las horas hábiles de cinco semanas: la semana 10 tiene solo dos días hábiles por San José (22 de marzo) y la Semana Santa (25 y 26 de marzo); las semanas 17, 20, 21 y 25 pierden un día por la Ascensión (10 de mayo), el Corpus Christi (31 de mayo), el Sagrado Corazón (7 de junio) y San Pedro y San Pablo (5 de julio). La carga de cada integrante respeta esas horas. Por el festivo del 31 de mayo, las pruebas SAT usan también la semana 21. El arranque con producto empieza en la semana 21 a medida que concluyen las pruebas SAT de los equipos de preparación y envasado, y termina en la 22; el acta de la SAT y de la puesta en marcha (11 de junio) se firma con los primeros lotes del arranque.

## 4. Hitos

| Hito | Semana | Fecha | Pago asociado |
| --- | --- | --- | --- |
| Firma del contrato e inicio, con las cartas de intención de los distribuidores | 1 | 18 de enero de 2027 | 30 % |
| Ingeniería básica y hojas de datos de largo plazo aprobadas | 3 | 5 de febrero de 2027 | — |
| Pedido de los equipos de largo plazo | 4 | 8 de febrero de 2027 | — |
| Ingeniería de detalle aprobada | 10 | 24 de marzo de 2027, último día hábil de la semana | — |
| Pruebas FAT aprobadas | 14 | 23 de abril de 2027 | 30 % |
| Puesta en marcha virtual aprobada | 19 | 28 de mayo de 2027 | — |
| Parada de planta | 19 | 24 a 28 de mayo de 2027 | — |
| Pruebas SAT y puesta en marcha aprobadas | 21 | 11 de junio de 2027 | 30 % |
| Lotes conformes de las tres referencias, incluido un lote 2 nocturno de cada una | 22 | 18 de junio de 2027 | — |
| Versión 2 de la plataforma, metas de adopción medidas y entrega del proyecto | 26 | 16 de julio de 2027 | 10 % |

## 5. Ruta crítica

Validación de la ingeniería básica (semanas 1 a 3) → pedido de equipos de largo plazo (semana 4) → fabricación (semanas 4 a 13) → FAT (semanas 13 y 14) → transporte y nacionalización (semanas 15 a 18) → montaje con preinstalación desde la semana 14 y parada en la semana 19 → pruebas de lazo y SAT (semanas 19 a 21) → arranque y validación (semanas 21 a 23) → estabilización (semanas 21 a 26) → entrega (semana 26).

Una segunda cadena llega también a la semana 26 sin holgura: arranque con producto (semanas 21 y 22) → OEE, paradas y horas de equipo con los datos del arranque (semanas 21 a 25) → tablero gerencial y reportes (semanas 23 a 26). Es la versión 2 de la plataforma, de la que depende el pago del 10 % de la entrega, así que se sigue con la misma prioridad que la ruta de los equipos.

El plazo lo fijan la fabricación y la importación de los equipos (15 semanas desde el pedido: 10 de fabricación, 1 de FAT y 4 de transporte y nacionalización). La versión 1 del software tiene una holgura de una semana frente a las pruebas de lazo (semana 20): sus paquetes terminan entre las semanas 16 y 18 y se integran a medida que llegan a la puesta en marcha virtual de las semanas 16 a 19. Si la versión 1 se atrasa, se pasan a la versión 2 funciones que no se necesitan para producir; como la versión 2 no tiene holgura, ese traslado se compensa con horas del equipo en las semanas 23 a 26 y no con un plazo mayor. La verificación microbiológica de los primeros lotes, por muestreo en un laboratorio externo, se completa durante la estabilización.

## 6. Carga de trabajo

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

La capacidad es de 6 personas × 26 semanas × 42 h, menos los 7 días festivos: 6.199 h. Las 4.780 horas de la EDT son las que se facturan al cliente. La carga semanal de cada integrante se calcula con `herramientas/modelo.py` y se equilibra con `herramientas/balancear_carga.py`.

## Referencias

- Project Management Institute (2021). Guía de los fundamentos para la dirección de proyectos (Guía del PMBOK), 7.ª ed.
- Congreso de la República de Colombia (2021). Ley 2101 de 2021, reducción de la jornada laboral.
- Ley 51 de 1983, sobre el traslado de días festivos al lunes.
