# Cronograma del proyecto

**Transformación Digital Industrial de la línea de yogur de La Hacienda**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Módulo 3 · Planeación y Evaluación de Proyectos

## 1. Supuestos

- El cronograma corresponde a la ejecución del proyecto en la planta del cliente y se construye a partir de la EDT del proyecto.
- Inicio: lunes 18 de enero de 2027, después de la aceptación de la oferta.
- Duración: **16 semanas** (unos 3,7 meses). Entrega: viernes 7 de mayo de 2027.
- La planta sigue produciendo durante el proyecto. La conexión de los equipos nuevos al tanque de proceso requiere una sola parada de 5 días hábiles, en la semana 14.
- El equipo es de seis ingenieros con jornada de 42 horas semanales (Ley 2101 de 2021). El proyecto ocupa el 76 % de su capacidad; el resto se dedica a la coordinación interna y a la gestión comercial de Cremia. El montaje lo ejecutan contratistas bajo la supervisión de Cremia.
- La ingeniería conceptual de la oferta (diagnóstico, VSM, modelos ISA-88, arquitectura ISA-95, recetas, inventario y dimensionamiento de equipos) es el punto de partida: en la ejecución se valida en sitio, no se repite.
- El alcance incluye la preparación automatizada, la línea de bolsas y la línea de vasos. La compra de la línea de vasos se confirma en la semana 2 con cartas de intención de los distribuidores. La celda robotizada de encanastado queda diseñada y con su espacio reservado, pero se compra en una etapa posterior, cuando el volumen la justifique.

## 2. Por qué 16 semanas

La primera versión del cronograma tenía 35 semanas: pedía los equipos en la semana 12 y facturaba ocho meses de nómina completa aunque la EDT solo ocupaba el 72 % del equipo. La versión de 16 semanas corrige las dos cosas:

| Decisión | Efecto en el plazo | Justificación técnica |
| --- | --- | --- |
| Validar la ingeniería conceptual de la oferta en lugar de repetirla | La ingeniería básica pasa de 7 a 2 semanas | El diagnóstico, el VSM, los modelos ISA-88, la arquitectura ISA-95 y el dimensionamiento de equipos ya están hechos y entregados con la oferta |
| Pedir en la semana 3 los equipos de mayor tiempo de entrega | La fabricación (10 semanas) empieza 9 semanas antes | Homogeneizador, intercambiador, chiller y llenadora tienen hojas de datos cerradas con el dimensionamiento de la oferta; la ingeniería de detalle sigue en paralelo |
| Programar el PLC, el SCADA y el MES mientras se fabrican los equipos | El software no alarga el plazo | La puesta en marcha virtual en el gemelo digital prueba el programa antes de que lleguen los equipos |
| Preinstalar tuberías, tableros y bases sin detener la planta | La parada se limita a 5 días | Solo la conexión al tanque de proceso T-301 exige detener la producción |
| Dejar la celda robotizada para una etapa posterior | Sin instalación ni pruebas de la celda dentro del proyecto | El encanastado manual no limita los dos lotes diarios; la celda se justifica cuando crezca el volumen |
| Cobrar la ingeniería por horas de la EDT | Las horas, el plazo y el costo cuadran | 3.060 horas a la tarifa de cada integrante según el valor que aporta, en dos contratos: diseño e implementación |

El riesgo de pedir equipos antes de cerrar todo el detalle se controla con tres medidas: las hojas de datos de largo plazo se aprueban con el cliente en la semana 2, la contingencia del 8 % cubre cambios menores y los contratos de compra fijan las interfaces (conexiones sanitarias, señales y protocolo) desde el pedido.

| Indicador | Primera versión | Versión revisada |
| --- | --- | --- |
| Duración | 35 semanas | 16 semanas |
| Fecha de entrega | 17 de septiembre de 2027 | 7 de mayo de 2027 |
| Semana del pedido de equipos | 12 | 3 |
| Ingeniería conceptual y básica | 7 semanas | 2 semanas |
| Horas de ingeniería | 6.320 h | 3.060 h |
| Ocupación del equipo | 72 %, con una persona al 101 % | 76 %, nadie por encima del 80 % |
| Parada de planta | 5 días | 5 días |
| Servicios de ingeniería | COP 439,0 millones (8 meses de nómina) | COP 190,8 millones (horas × tarifa de cada integrante) |
| Inversión total | COP 1.803,8 millones | COP 1.325,8 millones |

## 3. Cronograma por paquete de trabajo

| Código | Actividad | Semanas | Inicio | Fin |
| --- | --- | --- | --- | --- |
| 1.1 | Gestión del proyecto | 1–16 | 18 ene | 7 may |
| 1.1.1 | Plan del proyecto y línea base | 1 | 18 ene | 22 ene |
| 1.1.2 | Seguimiento y control de alcance, plazo y costo | 2–15 | 25 ene | 30 abr |
| 1.1.3 | Compras y contratos | 2–5 | 25 ene | 19 feb |
| 1.1.4 | Cierre administrativo | 16 | 3 may | 7 may |
| 1.2 | Ingeniería conceptual y básica | 1–2 | 18 ene | 29 ene |
| 1.2.1 | Validación en sitio de datos y parámetros | 1 | 18 ene | 22 ene |
| 1.2.2 | VSM y simulación del estado propuesto | 1–2 | 18 ene | 29 ene |
| 1.2.3 | Arquitectura ISA-95 y red OT/IT | 1–2 | 18 ene | 29 ene |
| 1.2.4 | Modelos ISA-88 y recetas | 1–2 | 18 ene | 29 ene |
| 1.2.5 | P&ID e índice de instrumentos | 1–2 | 18 ene | 29 ene |
| 1.3 | Ingeniería de detalle | 1–6 | 18 ene | 26 feb |
| 1.3.1 | Especificación de equipos | 1–4 | 18 ene | 12 feb |
| 1.3.2 | Lista de E/S y arquitectura de control | 3–4 | 1 feb | 12 feb |
| 1.3.3 | Diseño eléctrico y de tableros | 3–6 | 1 feb | 26 feb |
| 1.3.4 | Estación de encanastado y análisis de riesgos | 3–5 | 1 feb | 19 feb |
| 1.3.5 | Interfaz HMI | 3–6 | 1 feb | 26 feb |
| 1.3.6 | Distribución en planta | 3–4 | 1 feb | 12 feb |
| 1.4 | Procura | 1–13 | 18 ene | 16 abr |
| 1.4.1 | Cotizaciones y selección de proveedores | 1–2 | 18 ene | 29 ene |
| 1.4.2 | Órdenes de compra y seguimiento de fabricación | 3–12 | 1 feb | 9 abr |
| 1.4.3 | Pruebas FAT | 13 | 12 abr | 16 abr |
| 1.5 | Software de control, supervisión y gestión | 4–12 | 8 feb | 9 abr |
| 1.5.1 | Programa del PLC: fases del proceso | 4–9 | 8 feb | 19 mar |
| 1.5.2 | Programa del PLC: envasado y transporte | 5–10 | 15 feb | 26 mar |
| 1.5.3 | SCADA e historiador | 5–10 | 15 feb | 26 mar |
| 1.5.4 | MES e integración con ERP | 5–11 | 15 feb | 2 abr |
| 1.5.5 | Recetas maestras, registro de lote y reportes | 10–12 | 22 mar | 9 abr |
| 1.6 | Gemelo digital y puesta en marcha virtual | 4–12 | 8 feb | 9 abr |
| 1.6.1 | Gemelo digital de la línea | 4–9 | 8 feb | 19 mar |
| 1.6.2 | Simulación del envasado y el encanastado | 6–9 | 22 feb | 19 mar |
| 1.6.3 | Puesta en marcha virtual | 10–12 | 22 mar | 9 abr |
| 1.7 | Montaje e instalación | 8–14 | 8 mar | 23 abr |
| 1.7.1 | Montaje mecánico | 10–14 | 22 mar | 23 abr |
| 1.7.2 | Instalación eléctrica y de instrumentación | 10–14 | 22 mar | 23 abr |
| 1.7.3 | Red industrial y servidores | 8–9 | 8 mar | 19 mar |
| 1.7.4 | Línea de vasos | 13–14 | 12 abr | 23 abr |
| 1.8 | Pruebas y puesta en marcha | 15–16 | 26 abr | 7 may |
| 1.8.1 | Pruebas de lazo y de E/S | 15 | 26 abr | 30 abr |
| 1.8.2 | Pruebas SAT | 15 | 26 abr | 30 abr |
| 1.8.3 | Arranque con producto | 15–16 | 26 abr | 7 may |
| 1.8.4 | Validación de calidad e inocuidad | 16 | 3 may | 7 may |
| 1.9 | Gestión del cambio, capacitación y cierre | 1–16 | 18 ene | 7 may |
| 1.9.1 | Gestión del cambio y comunicación | 1–16 | 18 ene | 7 may |
| 1.9.2 | Capacitación por rol | 11–16 | 29 mar | 7 may |
| 1.9.3 | Procedimientos, documentación y manuales | 12–16 | 5 abr | 7 may |
| 1.9.4 | Entrega y acompañamiento del arranque | 16 | 3 may | 7 may |
| — | Fabricación de equipos de preparación, bolsas y vasos | 3–12 | 1 feb | 9 abr |
| — | Parada de planta para la conexión al tanque de proceso | 14 | 19 abr | 23 abr |

Después de la entrega, Cremia acompaña la operación durante 8 semanas dentro de la garantía.

## 4. Hitos

| Hito | Semana | Fecha | Pago asociado |
| --- | --- | --- | --- |
| Firma del contrato e inicio | 1 | 18 de enero de 2027 | 30 % |
| Ingeniería básica y hojas de datos de largo plazo aprobadas; confirmación de la línea de vasos | 2 | 29 de enero de 2027 | — |
| Pedido de los equipos | 3 | 1 de febrero de 2027 | — |
| Ingeniería de detalle aprobada | 6 | 26 de febrero de 2027 | — |
| Puesta en marcha virtual aprobada | 12 | 9 de abril de 2027 | — |
| Pruebas FAT aprobadas | 13 | 16 de abril de 2027 | 30 % |
| Parada de planta | 14 | 19 a 23 de abril de 2027 | — |
| Pruebas SAT y puesta en marcha aprobadas | 15 | 30 de abril de 2027 | 30 % |
| Lotes conformes de las tres referencias y entrega del proyecto | 16 | 7 de mayo de 2027 | 10 % |

## 5. Ruta crítica

Validación de la ingeniería básica (semanas 1 y 2) → pedido de equipos de largo plazo (semana 3) → fabricación (semanas 3 a 12) → FAT (semana 13) → montaje con preinstalación desde la semana 10 y parada en la semana 14 → pruebas de lazo y SAT (semana 15) → arranque y validación (semanas 15 y 16) → entrega (semana 16).

El plazo lo fija la fabricación de los equipos (10 semanas), que empieza en la semana 3. El software, el gemelo digital y la capacitación avanzan en paralelo y no están en la ruta crítica. La liberación microbiológica de los primeros lotes se completa durante el acompañamiento posterior a la entrega.

## 6. Carga de trabajo

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
| Integrante | Rol | Horas | Ocupación |
| David Santiago Cortés Ávila | Gerente de proyecto | 530 | 79 % |
| Ana María Orozco Reyes | Líder de simulación y mejora | 470 | 70 % |
| Jesús Alberto Rivera Molina | Líder de arquitectura digital | 520 | 77 % |
| David Felipe Cárdenas Cubides | Líder de gestión de producción | 520 | 77 % |
| José Andrés Zapata Piñeros | Líder de procesos e instrumentación | 520 | 77 % |
| Cristian Stiven Hoyos Peralta | Líder financiero y comercial | 500 | 74 % |
| **Total** | | **3.060** | **76 %** |

La capacidad es de 6 personas × 16 semanas × 42 h = 4.032 h. Las 3.060 horas de la EDT son las que se facturan al cliente y ninguna persona pasa del 80 % de su capacidad.

## Referencias

- Project Management Institute (2021). Guía de los fundamentos para la dirección de proyectos (Guía del PMBOK), 7.ª ed.
- Congreso de la República de Colombia (2021). Ley 2101 de 2021, reducción de la jornada laboral.
