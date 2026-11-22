# Resultados del modelo de la propuesta

Archivo generado por `herramientas/modelo.py` a partir de `herramientas/parametros.yaml`. No se edita a mano. Millones de COP de 2026, sin IVA.

## Producción y calidad

| Concepto | Situación actual | Propuesta |
| --- | --- | --- |
| Lotes al año | 300 | 600 |
| Unidades llenadas al año | 915.600 | 1.981.320 |
| Unidades conformes al año | 869.400 | 1.951.600 |
| Unidades conformes por día | 2.898 | 6.505 |
| Unidades conformes por operario al día | 724 | 1.301 |
| Ventas | 1.043,3 | 3.028,4 |
| Costo variable | 604,3 | 1.742,6 |
| Margen de contribución | 439,0 | 1.285,8 |
| **Margen de contribución adicional** | | **846,9** |

| Referencia | Unidades llenadas al año | Unidades conformes al año | Ventas | Costo variable | Margen |
| --- | --- | --- | --- | --- | --- |
| YB-200 | 923.700 | 909.844 | 1.091,8 | 646,6 | 445,2 |
| YV-150 | 786.420 | 774.624 | 1.161,9 | 656,7 | 505,3 |
| YV-300 | 271.200 | 267.132 | 774,7 | 439,3 | 335,3 |
| **Total** | **1.981.320** | **1.951.600** | **3.028,4** | **1.742,6** | **1.285,8** |

- Productividad: de 724 a 1.301 unidades conformes por operario al día (+80 %).
- Mano de obra por unidad conforme: de 155 a 95 COP (−39 %).
- OEE de la empacadora hoy: disponibilidad 90 %, rendimiento 76 %, calidad 94,9 %: **65 %**.
- OEE meta: disponibilidad 92 %, rendimiento 90 %, calidad 98,5 %: **82 %**.
- Tiempo de envasado por lote con la meta de OEE: YB-200 124 min, YV-150 117 min, YV-300 78 min.
- Tiempo estándar por lote de YB-200: **563 min** frente a 601 min (−6 %); homogeneización y pasteurización 95 min; ocupación de T-301 419 min, 459 con el CIP.

## Ingeniería de Cremia

- Horas: **4.780**; capacidad 6.199 h; ocupación 77 %.
- Valor: **333,7**; tarifa promedio 69.815 COP/h.
- Nómina de 26 semanas: 237,1; factor facturado/nómina 1,41 (mínimo 1,39); administración, imprevistos y utilidad 96,6.
- Software propio (paquetes 1.5.3 a 1.5.5 y cuenta 1.6): 1.830 h y 123,9; costo interno ≈ 66,2.

| Integrante | Rol | Horas | Ocupación | Tarifa (COP/h) | Factor sobre su costo | Valor |
| --- | --- | --- | --- | --- | --- | --- |
| David Santiago Cortés Ávila | Gerente de proyecto | 775 | 75 % | 90.000 | 1,80 | 69,75 |
| Ana María Orozco Reyes | Líder de simulación y mejora | 810 | 78 % | 67.000 | 2,01 | 54,27 |
| Jesús Alberto Rivera Molina | Líder de arquitectura digital | 805 | 78 % | 71.000 | 2,13 | 57,16 |
| David Felipe Cárdenas Cubides | Líder de gestión de producción | 815 | 79 % | 71.000 | 2,13 | 57,87 |
| José Andrés Zapata Piñeros | Líder de procesos e instrumentación | 800 | 77 % | 67.000 | 2,01 | 53,60 |
| Cristian Stiven Hoyos Peralta | Líder financiero y comercial | 775 | 75 % | 53.000 | 1,59 | 41,08 |
| **Total** | | **4.780** | **77 %** | **69.815 en promedio** | | **333,71** |

| Cuenta | Entregable | Paquetes | Horas | Valor |
| --- | --- | --- | --- | --- |
| 1.1 | Gestión del proyecto | 4 | 310 | 22,35 |
| 1.2 | Ingeniería conceptual y básica | 5 | 260 | 18,70 |
| 1.3 | Ingeniería de detalle | 5 | 400 | 27,14 |
| 1.4 | Procura | 3 | 180 | 10,38 |
| 1.5 | Software de control y supervisión | 5 | 680 | 52,99 |
| 1.6 | Plataforma Cremia MES/ERP | 11 | 1.500 | 99,57 |
| 1.7 | Gemelo digital y puesta en marcha virtual | 3 | 340 | 25,45 |
| 1.8 | Montaje e instalación | 4 | 320 | 21,94 |
| 1.9 | Pruebas y puesta en marcha | 4 | 280 | 20,46 |
| 1.10 | Gestión del cambio, capacitación, estabilización y cierre | 4 | 510 | 34,73 |
| **Total** | | **48** | **4.780** | **333,71** |

| Contrato | Semanas | Horas | Valor |
| --- | --- | --- | --- |
| 1. Diseño, procura y gestión de compras | 1–18 | 930 | 62,1 |
| 2. Implementación, software, puesta en marcha y adopción | 2–26 | 3.850 | 271,6 |

| Paquete | Nombre | Semanas | Horas | Responsables |
| --- | --- | --- | --- | --- |
| 1.1.1 | Plan del proyecto y línea base | 1 | 30 | DC (30) |
| 1.1.2 | Seguimiento y control de alcance, plazo y costo | 2–25 | 200 | DC (110), CH (90) |
| 1.1.3 | Compras, contratos e importación | 1–18 | 60 | CH (60) |
| 1.1.4 | Cierre administrativo | 26 | 20 | DC (20) |
| 1.2.1 | Validación en sitio de datos, parámetros y capacidad del cuarto frío | 1 | 40 | JZ (40) |
| 1.2.2 | VSM y simulación del estado propuesto | 1–3 | 60 | AO (60) |
| 1.2.3 | Arquitectura ISA-95, red OT/IT y nube | 1–3 | 60 | JR (60) |
| 1.2.4 | Modelos ISA-88 y recetas | 2–3 | 40 | DC (40) |
| 1.2.5 | P&ID e índice de instrumentos | 2–3 | 60 | JZ (30), JR (30) |
| 1.3.1 | Especificación de equipos | 2–6 | 100 | JZ (100) |
| 1.3.2 | Lista de E/S y arquitectura de control | 4–5 | 60 | JR (60) |
| 1.3.3 | Diseño eléctrico y de tableros | 4–10 | 130 | JR (20), JZ (110) |
| 1.3.4 | Estación de encanastado y análisis de riesgos | 3–9 | 60 | AO (60) |
| 1.3.5 | Distribución en planta | 3–8 | 50 | AO (45), DF (5) |
| 1.4.1 | Cotizaciones y selección de proveedores | 1–3 | 50 | CH (50) |
| 1.4.2 | Órdenes de compra, seguimiento de fabricación e importación | 4–18 | 70 | CH (70) |
| 1.4.3 | Pruebas FAT | 13–14 | 60 | JZ (15), AO (45) |
| 1.5.1 | Programa del PLC: fases del proceso y lote nocturno | 5–13 | 200 | DC (140), JR (60) |
| 1.5.2 | Programa del PLC: envasado y transporte | 6–14 | 150 | JR (90), DC (60) |
| 1.5.3 | SCADA Node-RED: guía de estilo ISA-101 y pantallas | 3–6 | 90 | DF (30), AO (10), DC (50) |
| 1.5.4 | SCADA Node-RED: alarmas ISA-18.2 e historiador | 8–15 | 140 | DF (140) |
| 1.5.5 | Nodo de borde: usuarios, recetas locales y operación sin conexión | 13–18 | 100 | JR (75), DF (25) |
| 1.6.1 | Infraestructura en Huawei Cloud, seguridad, respaldos y despliegue | 6–12 | 120 | JR (100), DF (20) |
| 1.6.2 | Núcleo: datos maestros, usuarios y roles, auditoría y API | 2–7 | 180 | DF (175), JR (5) |
| 1.6.3 | Recetas ISA-88 y órdenes de producción | 7–13 | 200 | DC (35), JZ (145), DF (20) |
| 1.6.4 | Registro electrónico de lote y genealogía | 8–16 | 140 | DF (95), DC (45) |
| 1.6.5 | Calidad y liberación de lotes | 11–17 | 100 | JZ (75), AO (20), DF (5) |
| 1.6.6 | OEE, paradas y horas de equipo | 21–25 | 120 | AO (60), JR (60) |
| 1.6.7 | Integración borde–nube: MQTT, almacenamiento y reenvío | 9–17 | 100 | JR (30), CH (50), DF (20) |
| 1.6.8 | ERP ligero I: inventario por lote y vencimiento, pedidos y despacho | 6–17 | 160 | CH (160) |
| 1.6.9 | ERP ligero II: compras, requerimiento de materiales, costo por lote y exportación al facturador | 20–25 | 140 | CH (140) |
| 1.6.10 | Tablero gerencial y reportes | 23–26 | 80 | AO (50), JR (30) |
| 1.6.11 | Pruebas y documentación del software | 10–25 | 160 | AO (120), JR (25), CH (15) |
| 1.7.1 | Gemelo digital de la línea | 4–12 | 160 | AO (160) |
| 1.7.2 | Simulación del envasado y el encanastado | 9–16 | 60 | AO (60) |
| 1.7.3 | Puesta en marcha virtual: PLC, SCADA y MES/ERP | 16–19 | 120 | DC (115), DF (5) |
| 1.8.1 | Montaje mecánico | 14–19 | 110 | JZ (110) |
| 1.8.2 | Instalación eléctrica y de instrumentación | 14–19 | 100 | JR (75), JZ (25) |
| 1.8.3 | Red industrial, nodo de borde y nube de producción | 16–18 | 50 | JR (20), DF (30) |
| 1.8.4 | Línea de vasos | 18–19 | 60 | AO (40), JZ (20) |
| 1.9.1 | Pruebas de lazo y de E/S | 19–20 | 50 | JR (40), AO (5), JZ (5) |
| 1.9.2 | Pruebas SAT | 20–21 | 80 | DC (55), JR (20), DF (5) |
| 1.9.3 | Arranque con producto | 20–22 | 100 | JZ (65), AO (35) |
| 1.9.4 | Validación de calidad e inocuidad | 21–23 | 50 | JZ (5), DF (45) |
| 1.10.1 | Gestión del cambio y comunicación | 1–26 | 130 | CH (130) |
| 1.10.2 | Capacitación por rol | 17–20 | 130 | DF (75), AO (35), JZ (10), CH (10) |
| 1.10.3 | Procedimientos, documentación y manuales | 19–25 | 100 | DF (95), JR (5) |
| 1.10.4 | Estabilización y entrega | 22–26 | 150 | DC (75), JZ (45), DF (25), AO (5) |

| Paquete | Semanas | Inicio | Fin |
| --- | --- | --- | --- |
| 1.1.1 | 1 | 18 ene | 22 ene |
| 1.1.2 | 2–25 | 25 ene | 9 jul |
| 1.1.3 | 1–18 | 18 ene | 21 may |
| 1.1.4 | 26 | 12 jul | 16 jul |
| 1.2.1 | 1 | 18 ene | 22 ene |
| 1.2.2 | 1–3 | 18 ene | 5 feb |
| 1.2.3 | 1–3 | 18 ene | 5 feb |
| 1.2.4 | 2–3 | 25 ene | 5 feb |
| 1.2.5 | 2–3 | 25 ene | 5 feb |
| 1.3.1 | 2–6 | 25 ene | 26 feb |
| 1.3.2 | 4–5 | 8 feb | 19 feb |
| 1.3.3 | 4–10 | 8 feb | 26 mar |
| 1.3.4 | 3–9 | 1 feb | 19 mar |
| 1.3.5 | 3–8 | 1 feb | 12 mar |
| 1.4.1 | 1–3 | 18 ene | 5 feb |
| 1.4.2 | 4–18 | 8 feb | 21 may |
| 1.4.3 | 13–14 | 12 abr | 23 abr |
| 1.5.1 | 5–13 | 15 feb | 16 abr |
| 1.5.2 | 6–14 | 22 feb | 23 abr |
| 1.5.3 | 3–6 | 1 feb | 26 feb |
| 1.5.4 | 8–15 | 8 mar | 30 abr |
| 1.5.5 | 13–18 | 12 abr | 21 may |
| 1.6.1 | 6–12 | 22 feb | 9 abr |
| 1.6.2 | 2–7 | 25 ene | 5 mar |
| 1.6.3 | 7–13 | 1 mar | 16 abr |
| 1.6.4 | 8–16 | 8 mar | 7 may |
| 1.6.5 | 11–17 | 29 mar | 14 may |
| 1.6.6 | 21–25 | 7 jun | 9 jul |
| 1.6.7 | 9–17 | 15 mar | 14 may |
| 1.6.8 | 6–17 | 22 feb | 14 may |
| 1.6.9 | 20–25 | 31 may | 9 jul |
| 1.6.10 | 23–26 | 21 jun | 16 jul |
| 1.6.11 | 10–25 | 22 mar | 9 jul |
| 1.7.1 | 4–12 | 8 feb | 9 abr |
| 1.7.2 | 9–16 | 15 mar | 7 may |
| 1.7.3 | 16–19 | 3 may | 28 may |
| 1.8.1 | 14–19 | 19 abr | 28 may |
| 1.8.2 | 14–19 | 19 abr | 28 may |
| 1.8.3 | 16–18 | 3 may | 21 may |
| 1.8.4 | 18–19 | 17 may | 28 may |
| 1.9.1 | 19–20 | 24 may | 4 jun |
| 1.9.2 | 20–21 | 31 may | 11 jun |
| 1.9.3 | 20–22 | 31 may | 18 jun |
| 1.9.4 | 21–23 | 7 jun | 25 jun |
| 1.10.1 | 1–26 | 18 ene | 16 jul |
| 1.10.2 | 17–20 | 10 may | 4 jun |
| 1.10.3 | 19–25 | 24 may | 9 jul |
| 1.10.4 | 22–26 | 14 jun | 16 jul |

## Inversión

| N.º | Rubro | Valor |
| --- | --- | --- |
| 1 | Dosificación automática de azúcar, estabilizante, colorante y saborizante; pesaje de cultivo | 70,0 |
| 2 | Instrumentación sanitaria: temperatura PT100, nivel, pH en línea, caudal, peso y presión | 57,0 |
| 3 | Válvulas de control proporcional, válvulas sanitarias de desvío y neumática | 35,0 |
| 4 | Intercambiador de placas sanitario, bomba de lóbulos P-301 y bomba de recepción P-101 | 60,0 |
| 5 | Enfriador industrial (chiller) y banco de agua helada | 60,0 |
| 6 | Llenadora-selladora automática de vasos de 150 y 300 ml (mismo diámetro de boca) | 160,0 |
| 7 | Dosificación de fruta en trozos y mezclador estático en línea | 30,0 |
| 8 | Dos controladoras de peso dinámicas con rechazo automático | 80,0 |
| 9 | Bandas transportadoras modulares sanitarias | 40,0 |
| 10 | PLC CompactLogix 5380 Allen-Bradley, dos estaciones de E/S remotas, tableros IP66, variadores PowerFlex, conmutador Stratix 5700 y cortafuegos de la zona desmilitarizada | 83,0 |
| 11 | Nodo de borde y supervisión: PC industrial principal y de repuesto con Node-RED, dos paneles táctiles de 15" IP65 (HMI-01 y HMI-02), UPS, router industrial con 4G y equipo de salto | 30,0 |
| 12 | Entornos de la plataforma Cremia MES/ERP en Huawei Cloud durante el proyecto (desarrollo, pruebas y producción) | 6,0 |
| 13 | Estación de limpieza CIP automatizada de dos tanques | 50,0 |
| 14 | Homogeneizador de alta presión de dos etapas (1.500 L/h, 200 bar) | 95,0 |
| 15 | Dosificador de leche en polvo por peso | 20,0 |
| 16 | Dos codificadores de lote y fecha de vencimiento | 25,0 |
| 17 | Circuito de agua helada a la chaqueta de T-301: TV-304, XV-904 y tubería aislada | 10,0 |
| 18 | Tanque refrigerado de leche TK-102 de 1.000 L con válvulas de selección XV-101 y XV-102 | 30,0 |
| 19 | Mesa acumuladora para el encajonado de vasos | 6,0 |
| | Subtotal de equipos y software | 947,0 |
| | Ingeniería de Cremia | 333,7 |
| | Montaje (8 % de equipos físicos) | 75,3 |
| | Subtotal | 1.356,0 |
| | Contingencia (8 %) | 108,5 |
| | **Inversión total** | **1.464,5** |
| | Margen no percibido por 5 días de parada | 7,3 |
| | **Desembolso del año 0** | **1.471,8** |

- Línea de vasos: 289,9; preparación y bolsas: 1.174,6.
- Clase de depreciación de equipos (10 años): 1.291,8; software y hardware de borde (5 años): 172,7.
- Grupos: proceso 460,0; instrumentacion 57,0; envasado 311,0; control 119,0.
- Base de mantenimiento: 828,0.

## Costos anuales de operación

| Partida | Millones de COP por año |
| --- | --- |
| Mantenimiento preventivo de equipos de proceso y envasado | 24,8 |
| Plan de servicio Cremia: nube Huawei | 15,0 |
| Plan de servicio Cremia: soporte y evolución del software y del control | 21,0 |
| Conectividad doble (fibra y 4G) | 4,0 |
| Operario adicional para el segundo lote | 33,6 |
| Turno del domingo (horas extra dominicales) | 12,1 |
| Horas extra por incubaciones largas y disponibilidad nocturna | 5,0 |
| Laboratorio externo: microbiología por muestreo | 12,0 |
| **Total** | **127,6** |

- Hora ordinaria del operario: 10.121 COP.
- Beneficio operativo anual a plena producción (antes de impuestos): 719,3.
- Capital de trabajo a plena producción: 118,0.

## Flujo de caja

| Concepto | Año 0 | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Inversión y parada | −1.471,8 | — | — | — | — | — |
| Margen adicional (rampa) | — | 423,4 | 635,1 | 846,9 | 846,9 | 846,9 |
| Costos de operación | — | −127,6 | −127,6 | −127,6 | −127,6 | −127,6 |
| Resultado operativo (EBITDA) | — | 295,9 | 507,6 | 719,3 | 719,3 | 719,3 |
| Depreciación (no es salida de caja) | — | 163,7 | 163,7 | 163,7 | 163,7 | 163,7 |
| Impuesto de renta (35 %) | — | −46,3 | −120,4 | −194,5 | −194,5 | −194,5 |
| Variación del capital de trabajo | — | −59,0 | −29,5 | −29,5 | 0,0 | 0,0 |
| Recuperación del capital de trabajo y valor residual | — | 0,0 | 0,0 | 0,0 | 0,0 | 763,9 |
| **Flujo antes de impuestos** | −1.471,8 | 236,9 | 478,1 | 689,8 | 719,3 | 1.483,2 |
| **Flujo después de impuestos** | −1.471,8 | 190,6 | 357,7 | 495,3 | 524,8 | 1.288,7 |

- Valor residual en libros en el año 5: 645,9.

## Indicadores

| Indicador | Después de impuestos (principal) | Antes de impuestos |
| --- | --- | --- |
| VPN al 15 % | 231,0 | 697,9 |
| TIR | 19,8 % | 28,9 % |
| Recuperación | 3,8 años | 3,1 años |
| Relación beneficio-costo | 1,16 | — |
| Volumen de equilibrio | 89,6 % del plan | — |
| Vasos de equilibrio (bolsas al 100 %) | 84,1 % del plan | — |

## Sensibilidad (después de impuestos)

| Escenario | VPN al 15 % | TIR | Recuperación |
| --- | --- | --- | --- |
| Base | 231,0 | 19,8 % | 3,8 años |
| Volumen vendido al 90 % | 8,2 | 15,2 % | 4,1 años |
| Volumen vendido al 80 % | −214,6 | 10,3 % | 4,4 años |
| Vasos vendidos al 80 % (bolsas al 100 %) | −60,4 | 13,7 % | 4,2 años |
| Precio de venta −5 % | 58,2 | 16,2 % | 4,1 años |
| Precio de venta +5 % | 403,7 | 23,3 % | 3,5 años |
| Leche cruda +10 % | 170,0 | 18,6 % | 4,0 años |
| Leche cruda −10 % | 291,9 | 21,1 % | 3,7 años |
| Inversión +10 % | 135,8 | 17,6 % | 4,0 años |
| Inversión −10 % | 326,1 | 22,5 % | 3,6 años |
| Horas de software +30 % | 200,2 | 19,1 % | 3,9 años |
| Sin valor residual | −90,2 | 12,8 % | 3,8 años |
| Solo preparación y bolsas (600 lotes de YB-200, sin línea de vasos) | −264,0 | 7,7 % | 4,5 años |

- Inversión del escenario solo bolsas: 1.174,6; margen adicional 451,5.

## Crédito

70 % de la inversión (1.025,1) a 18 % efectivo anual, 5 años, 1 año de gracia con pago de intereses.

| Año | Intereses | Abono a capital | Cuota | Saldo | Flujo del proyecto después de impuestos | Ahorro tributario de intereses | Flujo después de la deuda |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 184,5 | 0,0 | 184,5 | 1.025,1 | 190,6 | 64,6 | 70,7 |
| 2 | 184,5 | 196,6 | 381,1 | 828,6 | 357,7 | 64,6 | 41,2 |
| 3 | 149,1 | 231,9 | 381,1 | 596,6 | 495,3 | 52,2 | 166,5 |
| 4 | 107,4 | 273,7 | 381,1 | 323,0 | 524,8 | 37,6 | 181,4 |
| 5 | 58,1 | 323,0 | 381,1 | 0,0 | 524,8 | 20,3 | 164,1 |

## Pagos por hitos

| Hito | Semana | Porcentaje | Valor |
| --- | --- | --- | --- |
| Firma del contrato (anticipo) | 1 | 30 % | 439,3 |
| Pruebas FAT aprobadas | 14 | 30 % | 439,3 |
| Pruebas SAT y puesta en marcha | 21 | 30 % | 439,3 |
| Cierre y entrega | 26 | 10 % | 146,4 |

## Programa diario (lote 1 y lote 2 de YB-200)

Horas exactas del modelo. Los documentos las redondean a 5 min.

| Hora exacta | Lote | Actividad | Responsable |
| --- | --- | --- | --- |
| 7:00–7:05 | L2 anterior | Muestra del lote 2 anterior y confirmación de acidez | Operador de recepción y laboratorio |
| 7:00–7:25 | L2 anterior | Transferencia del lote 2 anterior por E-301 a T-302 | Operador de preparación |
| 7:05–7:25 | L1 | Recepción y análisis de 14 cantinas del lote 1 (a TK-101) | Operador de recepción y laboratorio |
| 7:25–7:44 | L2 | Recepción y análisis de 14 cantinas del lote 2 (a TK-102, a 4 °C) | Operador de recepción y laboratorio |
| 7:25–8:05 | L1 | CIP de T-301 | Operador de preparación |
| 7:25–10:30 | L2 anterior | Espera del lote 2 anterior en T-302 a 12–15 °C | Automático (PLC), sin operario |
| 8:05–8:17 | L1 | Carga de 550 L desde TK-101 | Operador de recepción y laboratorio |
| 8:17–8:29 | L1 | Precalentamiento a 25 °C y dosificación en paralelo | Operador de preparación |
| 8:29–10:04 | L1 | Homogeneización y pasteurización | Operador de preparación |
| 10:04–10:29 | L1 | Enfriamiento a 43 °C con agua de red en la chaqueta | Operador de preparación |
| 10:29–10:34 | L1 | Inoculación | Operador de preparación |
| 10:30–12:34 | L2 anterior | Envasado del lote 2 anterior (YB-200) | Operador de envasado |
| 10:30–12:34 | L2 anterior | Encanastado o encajonado del lote 2 anterior | Operador de empaque y cuarto frío |
| 10:34–14:34 | L1 | Incubación hasta pH 4,4–4,5 | Automático (PLC), sin operario |
| 12:34–13:14 | L2 anterior | CIP de T-302 y de la línea de envasado | Operador de envasado |
| 14:34–14:39 | L1 | Ruptura del coágulo y saborizado | Operador del segundo lote |
| 14:34–14:39 | L1 | Confirmación de acidez del lote 1 | Operador del segundo lote |
| 14:39–15:04 | L1 | Enfriamiento en placas y transferencia a T-302 | Operador del segundo lote |
| 15:04–17:08 | L1 | Envasado del lote 1 (YB-200) | Operador de envasado |
| 15:04–17:08 | L1 | Encanastado o encajonado del lote 1 | Operador de empaque y cuarto frío |
| 15:04–15:44 | L2 | CIP de T-301 | Operador del segundo lote |
| 15:44–15:56 | L2 | Carga de 550 L desde TK-102 | Operador del segundo lote |
| 15:56–16:14 | L2 | Precalentamiento desde 4 °C a 25 °C y dosificación | Operador del segundo lote |
| 16:14–17:49 | L2 | Homogeneización y pasteurización | Operador del segundo lote |
| 17:08–17:48 | L1 | CIP de fin de día de T-302 y de la línea de envasado | Operador del segundo lote |
| 17:49–18:14 | L2 | Enfriamiento a 43 °C con agua de red en la chaqueta | Operador del segundo lote |
| 18:14–18:19 | L2 | Inoculación | Operador del segundo lote |
| 18:19–22:19 | L2 | Incubación sin operario hasta pH 4,6, con alarmas remotas | Automático (PLC), sin operario |
| 22:19–22:24 | L2 | Ruptura del coágulo y saborizado automáticos | Automático (PLC), sin operario |
| 22:24–7:00 | L2 | Enfriamiento con agua helada en la chaqueta y mantenimiento a 12–15 °C | Automático (PLC), sin operario |

- T-301 queda libre a las 15:05; el lote 2 termina la inoculación a las 18:20.
- Conflictos de recursos: 0; cruces de tareas atendidas por un mismo rol: 0.
- Minutos fuera de turno con la incubación de 240 min: R 0, P 0, E 0, K 0, S 0.
- Minutos fuera de turno con la incubación máxima de 300 min: R 0, P 0, E 38, K 38, S 19.
