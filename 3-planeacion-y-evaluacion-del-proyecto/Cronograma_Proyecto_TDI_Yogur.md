# Cronograma del proyecto

**Transformación Digital Industrial de la línea de yogur de La Hacienda**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Módulo 3 · Planeación y Evaluación de Proyectos

## 1. Supuestos

- El cronograma corresponde a la ejecución del proyecto en la planta del cliente y se construye a partir de la EDT del proyecto.
- Inicio: lunes 18 de enero de 2027, después de la aceptación de la oferta.
- Duración: **24 semanas** (5,5 meses). Entrega: viernes 2 de julio de 2027.
- La planta sigue produciendo durante el proyecto. La conexión de los equipos nuevos al tanque de proceso requiere una sola parada de 5 días hábiles, en la semana 18.
- El equipo es de seis ingenieros con jornada de 42 horas semanales (Ley 2101 de 2021). El montaje lo ejecutan contratistas bajo la supervisión de Cremia.
- La ingeniería conceptual de la oferta (diagnóstico, VSM, modelos ISA-88, arquitectura ISA-95, recetas, inventario y dimensionamiento de equipos) es el punto de partida: en la ejecución se valida en sitio, no se repite.
- La inversión va en dos fases. La fase 1 automatiza la preparación y la línea de bolsas; la fase 2 agrega la línea de vasos y la celda de encanastado. La compra de la fase 2 se decide en la semana 6 con los pedidos o cartas de intención de los distribuidores.

## 2. Por qué 24 semanas y no 35

La primera versión del cronograma tenía 35 semanas y pedía los equipos en la semana 12, después de terminar toda la ingeniería de detalle. Esa secuencia era segura, pero dejaba once semanas de ingeniería antes de la fabricación, que es la actividad más larga del proyecto (10 semanas). La versión revisada reorganiza el trabajo con cinco decisiones:

| Decisión | Efecto en el plazo | Justificación técnica |
| --- | --- | --- |
| Validar la ingeniería conceptual de la oferta en lugar de repetirla | La ingeniería básica pasa de 7 a 3 semanas | El diagnóstico, el VSM, los modelos ISA-88, la arquitectura ISA-95 y el dimensionamiento de equipos ya están hechos y entregados con la oferta |
| Pedir en la semana 4 los equipos de mayor tiempo de entrega | La fabricación empieza 8 semanas antes | Homogeneizador, intercambiador, chiller, llenadora y robot tienen hojas de datos cerradas con el dimensionamiento de la oferta; la ingeniería de detalle sigue en paralelo sin afectar su compra |
| Programar el PLC, el SCADA y el MES mientras se fabrican los equipos | El software no alarga el plazo | La puesta en marcha virtual en el gemelo digital prueba el programa antes de que lleguen los equipos |
| Preinstalar tuberías, tableros y bases sin detener la planta | La parada se limita a 5 días | Solo la conexión al tanque de proceso T-301 exige detener la producción |
| Ejecutar la fase 2 en paralelo con la fase 1 | La línea de vasos no se suma al final | La línea de vasos (U7) y la celda (U8) están aguas abajo del tanque pulmón y se instalan sin parar la preparación |

El riesgo de pedir equipos antes de cerrar todo el detalle se controla con tres medidas: las hojas de datos de largo plazo se aprueban con el cliente en la semana 3, la contingencia del 8 % cubre cambios menores y los contratos de compra fijan las interfaces (conexiones sanitarias, señales y protocolo) desde el pedido.

| Indicador | Versión anterior | Versión revisada |
| --- | --- | --- |
| Duración | 35 semanas | 24 semanas |
| Fecha de entrega | 17 de septiembre de 2027 | 2 de julio de 2027 |
| Semana del pedido de equipos | 12 | 4 |
| Ingeniería conceptual y básica | 7 semanas | 3 semanas |
| Horas de ingeniería | 6.320 h | 4.760 h |
| Ocupación del equipo | 72 %, con una persona al 101 % | 79 %, nadie por encima del 80 % |
| Parada de planta | 5 días | 5 días |
| Valor de los servicios de ingeniería | COP 439,0 millones | COP 301,8 millones |

## 3. Cronograma por paquete de trabajo

| Código | Actividad | Semanas | Inicio | Fin |
| --- | --- | --- | --- | --- |
| 1.1 | Gestión del proyecto | 1–24 | 18 ene | 2 jul |
| 1.1.1 | Plan del proyecto y línea base | 1 | 18 ene | 22 ene |
| 1.1.2 | Seguimiento y control de alcance, plazo y costo | 2–23 | 25 ene | 25 jun |
| 1.1.3 | Compras y contratos | 2–7 | 25 ene | 5 mar |
| 1.1.4 | Cierre administrativo | 24 | 28 jun | 2 jul |
| 1.2 | Ingeniería conceptual y básica | 1–3 | 18 ene | 5 feb |
| 1.2.1 | Validación en sitio de datos y parámetros | 1–2 | 18 ene | 29 ene |
| 1.2.2 | VSM y simulación del estado propuesto | 2–3 | 25 ene | 5 feb |
| 1.2.3 | Arquitectura ISA-95 y red OT/IT | 2–3 | 25 ene | 5 feb |
| 1.2.4 | Modelos ISA-88 y recetas | 2–3 | 25 ene | 5 feb |
| 1.2.5 | P&ID e índice de instrumentos | 1–3 | 18 ene | 5 feb |
| 1.3 | Ingeniería de detalle | 2–8 | 25 ene | 12 mar |
| 1.3.1 | Especificación de equipos (largo plazo hasta la semana 3) | 2–6 | 25 ene | 26 feb |
| 1.3.2 | Lista de E/S y arquitectura de control | 4–5 | 8 feb | 19 feb |
| 1.3.3 | Diseño eléctrico y de tableros | 5–8 | 15 feb | 12 mar |
| 1.3.4 | Celda de encanastado y análisis de riesgos | 4–7 | 8 feb | 5 mar |
| 1.3.5 | Interfaz HMI | 5–8 | 15 feb | 12 mar |
| 1.3.6 | Distribución en planta | 4–6 | 8 feb | 26 feb |
| 1.4 | Procura | 2–17 | 25 ene | 14 may |
| 1.4.1 | Cotizaciones y selección de proveedores | 2–3 | 25 ene | 5 feb |
| 1.4.2 | Órdenes de compra y seguimiento de fabricación | 4–16 | 8 feb | 7 may |
| — | Fabricación de equipos de la fase 1 | 4–13 | 8 feb | 16 abr |
| — | Fabricación de equipos de la fase 2 | 7–16 | 1 mar | 7 may |
| 1.4.3 | Pruebas FAT (fase 1 en la semana 14, fase 2 en la 17) | 14–17 | 19 abr | 14 may |
| 1.5 | Software de control, supervisión y gestión | 6–16 | 22 feb | 7 may |
| 1.5.1 | PLC del proceso | 6–11 | 22 feb | 2 abr |
| 1.5.2 | PLC de envasado y transporte | 8–13 | 8 mar | 16 abr |
| 1.5.3 | SCADA e historiador | 7–13 | 1 mar | 16 abr |
| 1.5.4 | MES e integración con ERP | 8–15 | 8 mar | 30 abr |
| 1.5.5 | Recetas maestras, registro de lote y reportes | 13–16 | 12 abr | 7 may |
| 1.6 | Gemelo digital y puesta en marcha virtual | 6–16 | 22 feb | 7 may |
| 1.6.1 | Gemelo digital de la línea | 6–11 | 22 feb | 2 abr |
| 1.6.2 | Simulación de la celda | 8–12 | 8 mar | 9 abr |
| 1.6.3 | Puesta en marcha virtual | 13–16 | 12 abr | 7 may |
| 1.7 | Montaje e instalación | 12–20 | 5 abr | 4 jun |
| 1.7.3 | Red industrial y servidores | 12–14 | 5 abr | 23 abr |
| 1.7.1 | Montaje mecánico (preinstalación en las semanas 15 a 17) | 15–18 | 26 abr | 21 may |
| 1.7.2 | Instalación eléctrica y de instrumentación | 15–18 | 26 abr | 21 may |
| — | Parada de planta para la conexión al tanque de proceso | 18 | 17 may | 21 may |
| 1.7.4 | Línea de vasos y celda de encanastado | 18–20 | 17 may | 4 jun |
| 1.8 | Pruebas y puesta en marcha | 19–23 | 24 may | 25 jun |
| 1.8.1 | Pruebas de lazo y de E/S | 19 | 24 may | 28 may |
| 1.8.2 | Pruebas SAT (fase 1 en la semana 20, fase 2 en la 21) | 20–21 | 31 may | 11 jun |
| 1.8.3 | Arranque con producto (bolsas desde la semana 20, vasos desde la 21) | 20–22 | 31 may | 18 jun |
| 1.8.4 | Validación de calidad e inocuidad | 21–23 | 7 jun | 25 jun |
| 1.9 | Gestión del cambio, capacitación y cierre | 1–24 | 18 ene | 2 jul |
| 1.9.1 | Gestión del cambio y comunicación | 1–24 | 18 ene | 2 jul |
| 1.9.2 | Capacitación por rol | 15–22 | 26 abr | 18 jun |
| 1.9.3 | Procedimientos, documentación y manuales | 18–23 | 17 may | 25 jun |
| 1.9.4 | Entrega y acompañamiento del arranque | 23–24 | 21 jun | 2 jul |

Después de la entrega, Cremia acompaña la operación durante 8 semanas dentro de la garantía (sección 6).

## 4. Hitos

| Hito | Semana | Fecha | Pago asociado |
| --- | --- | --- | --- |
| Firma del contrato e inicio | 1 | 18 de enero de 2027 | 30 % |
| Ingeniería básica y hojas de datos de largo plazo aprobadas | 3 | 5 de febrero de 2027 | — |
| Pedido de los equipos de la fase 1 | 4 | 8 de febrero de 2027 | — |
| Decisión de compra de la fase 2 | 6 | 26 de febrero de 2027 | — |
| Ingeniería de detalle aprobada | 8 | 12 de marzo de 2027 | — |
| Pruebas FAT de la fase 1 aprobadas | 14 | 23 de abril de 2027 | 30 % |
| Puesta en marcha virtual aprobada | 16 | 7 de mayo de 2027 | — |
| Parada de planta | 18 | 17 a 21 de mayo de 2027 | — |
| Pruebas SAT y puesta en marcha aprobadas | 21 | 11 de junio de 2027 | 30 % |
| Lotes conformes de las tres referencias y validación de calidad | 23 | 25 de junio de 2027 | — |
| Entrega del proyecto | 24 | 2 de julio de 2027 | 10 % |

## 5. Ruta crítica

Validación de la ingeniería básica (semanas 1 a 3) → pedido de equipos de largo plazo (semana 4) → fabricación de la fase 1 (semanas 4 a 13) → FAT (semana 14) → preinstalación y montaje (semanas 15 a 18, con la parada en la 18) → pruebas de lazo (semana 19) → SAT (semana 20) → arranque y validación (semanas 20 a 23) → entrega (semana 24).

El plazo lo sigue fijando la fabricación de los equipos (10 semanas), pero ahora empieza en la semana 4. La rama de la fase 2 (decisión en la semana 6, fabricación de la 7 a la 16, FAT en la 17, instalación de la 18 a la 20 y SAT en la 21) tiene una semana de holgura frente a la entrega. El software, el gemelo digital y la capacitación avanzan en paralelo y no están en la ruta crítica.

## 6. Carga de trabajo

| Fase | Semanas | Horas |
| --- | --- | --- |
| 1.1 Gestión del proyecto | 1–24 | 340 |
| 1.2 Ingeniería conceptual y básica | 1–3 | 380 |
| 1.3 Ingeniería de detalle | 2–8 | 780 |
| 1.4 Procura | 2–17 | 280 |
| 1.5 Software de control, supervisión y gestión | 6–16 | 1.040 |
| 1.6 Gemelo digital y puesta en marcha virtual | 6–16 | 500 |
| 1.7 Montaje e instalación | 12–20 | 500 |
| 1.8 Pruebas y puesta en marcha | 19–23 | 420 |
| 1.9 Gestión del cambio, capacitación y cierre | 1–24 | 520 |
| **Total** | **24** | **4.760** |
| Integrante | Horas | Ocupación |
| David Santiago Cortés Ávila | 800 | 79 % |
| Ana María Orozco Reyes | 800 | 79 % |
| Jesús Alberto Rivera Molina | 800 | 79 % |
| David Felipe Cárdenas Cubides | 800 | 79 % |
| José Andrés Zapata Piñeros | 800 | 79 % |
| Cristian Stiven Hoyos Peralta | 760 | 75 % |
| **Total** | **4.760** | **79 %** |

La capacidad es de 6 personas × 24 semanas × 42 h = 6.048 h. Con el 79 % de ocupación queda cerca de un 21 % para coordinación interna, reprocesos e imprevistos, y ninguna persona pasa del 80 %. Después de la entrega, el acompañamiento de 8 semanas lo cubre el contrato de garantía y soporte.

## Referencias

- Project Management Institute (2021). Guía de los fundamentos para la dirección de proyectos (Guía del PMBOK), 7.ª ed.
- Congreso de la República de Colombia (2021). Ley 2101 de 2021, reducción de la jornada laboral.
