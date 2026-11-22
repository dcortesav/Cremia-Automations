# Propuesta económica y comercial de la línea de yogur

**Presupuesto, flujo de caja, indicadores financieros, modelo de negocio y oferta para la planta La Hacienda**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Módulo 3 · Planeación y Evaluación de Proyectos

## 1. Alcance

Este documento reúne la evaluación económica y la oferta comercial de Cremia Automations para la línea de yogur de la planta La Hacienda: los supuestos de producción, precios y costos de las tres referencias; los salarios del equipo consultor y el margen de la empresa integradora; el presupuesto de inversión (CAPEX); los beneficios y costos anuales; el flujo de caja a cinco años antes y después de impuestos; los indicadores financieros; el análisis de sensibilidad y de riesgos; la financiación; el modelo de negocio y la oferta.

El análisis considera exclusivamente la línea de yogur. Todas las cifras están en pesos colombianos de 2026, sin IVA. Las tablas marcadas como generadas salen de `herramientas/modelo.py` con los supuestos de `herramientas/parametros.yaml`; el detalle completo está en `herramientas/resultados.md`.

**Versión de noviembre de 2026.** Frente a la versión de octubre de 2026, esta versión:

- reemplaza las licencias de SCADA, MES y ERP por software propio de Cremia: un SCADA en Node-RED y la plataforma Cremia MES/ERP en Huawei Cloud;
- agrega lo que necesita el segundo lote: el tanque refrigerado TK-102, el agua helada en la chaqueta para el enfriamiento nocturno y la mesa acumuladora de vasos;
- extiende el proyecto a 26 semanas por el desarrollo del software y la importación de equipos, y cobra la ingeniería para que cubra la nómina completa con el factor mínimo de 1,39;
- vende solo las unidades conformes, en la situación actual y en la propuesta;
- presenta el flujo después de impuestos, con capital de trabajo y valor residual, como indicador principal;
- costea las horas extra dominicales, la disponibilidad nocturna y el laboratorio externo.

## 2. Situación de partida

| Concepto | Situación actual (caso La Hacienda) |
| --- | --- |
| Producto | Yogur saborizado en bolsa de 200 ml |
| Lote | 550 L de leche, un lote diario |
| Producción | 3.052 bolsas llenadas por lote, de las que 2.898 son conformes (5,06 % no conforme) |
| Operarios | 4 |
| Tiempo estándar por lote | 601,3 min, más el enfriamiento natural durante la noche |
| Costo variable por bolsa llenada | 660 COP (sin leche en polvo) |
| Ventas anuales (869.400 bolsas conformes) | COP 1.043,3 millones |
| Costo variable anual (915.600 bolsas llenadas) | COP 604,3 millones |
| Margen de contribución anual | COP 439,0 millones |

El margen actual es la línea base contra la que se mide la propuesta: el flujo de caja del proyecto solo cuenta el margen adicional que genera la transformación, no el que la planta ya obtiene.

## 3. Supuestos de producción, precios y costos

### 3.1 Precios y márgenes por referencia

A partir de una investigación de mercado y de proveedores en Colombia (Darnel, Carvajal Empaques, compras de leche bajo la Resolución 017 de 2012 y preparados de fruta con trozos), se definieron los precios de venta de fábrica y los costos variables unitarios de las tres referencias:

| Concepto | YB-200 (bolsa 200 ml) | YV-150 (vaso 150 ml) | YV-300 (vaso 300 ml) |
| --- | --- | --- | --- |
| Precio de venta de fábrica (COP/und) | 1.200 | 1.500 | 2.900 |
| Costo variable por unidad llenada (COP/und) | 700 | 835 | 1.620 |
| Margen de contribución (COP/und) | 500 (41,7 %) | 665 (44,3 %) | 1.280 (44,1 %) |
| Unidades llenadas por lote (550 L de leche) | 3.079 | 4.369 | 2.260 |
| Unidades conformes por lote (1,5 % no conforme) | 3.033 | 4.303 | 2.226 |
| Margen de contribución por lote (COP) | 1.484.300 | 2.806.385 | 2.794.200 |

El margen por lote vende las unidades conformes y carga el costo de todas las llenadas. Por lote, los dos vasos dejan casi el doble de margen que la bolsa. Esa es la razón comercial para ampliar el portafolio, además de la razón técnica de aprovechar la misma base de yogur.

### 3.2 Estructura del costo variable por unidad

| Componente (COP/und) | YB-200 | YV-150 | YV-300 |
| --- | --- | --- | --- |
| Leche cruda (2.100 COP/L) | 375 | 264 | 511 |
| Leche en polvo descremada (21.600 COP/kg) | 40 | 35 | 68 |
| Azúcar (4.000 COP/kg) | 98 | 58 | 100 |
| Estabilizante, cultivo, saborizante y colorante | 52 | 39 | 74 |
| Preparado o trozos de fruta | — | 196 | 452 |
| Envase: película, o vaso con sello de aluminio | 110 | 220 | 380 |
| Energía, agua, limpieza CIP y codificado | 25 | 23 | 35 |
| **Costo variable total** | **700** | **835** | **1.620** |

Las cantidades por unidad salen de la fórmula de cada referencia (documento de recetas y lotes): 179 ml de leche por bolsa, 126 ml por vaso de 150 ml y 243 ml por vaso de 300 ml; 13,1 g de preparado de mora por vaso pequeño (unos 15.000 COP/kg) y 39,3 g de trozos de melocotón por vaso grande (unos 11.500 COP/kg). Los aditivos se reparten por lote: estabilizante a 60.000 COP/kg, un sobre de cultivo de 120.000 COP por lote, saborizante a 80.000 COP/kg y colorante a 100.000 COP/kg. El vaso de 300 ml incluye una sobretapa de domo. La energía incluye la del enfriador, que de noche enfría el lote 2, y la del tanque refrigerado TK-102. Frente a la bolsa actual (660 COP), la bolsa propuesta cuesta 40 COP más por la leche en polvo.

### 3.3 Precios de referencia en el mercado

| Referencia | Precio de fábrica (COP) | Precio al consumidor observado (COP) | Productos comparables |
| --- | --- | --- | --- |
| YB-200 | 1.200 | 1.800 a 2.200 en tiendas de barrio y de descuento | Yogo Yogo (Alpina), Alquería, Colanta |
| YV-150 | 1.500 | 2.400 a 2.900 | Alpina Finesse y Regeneris, San Mateo |
| YV-300 | 2.900 | 4.200 a 5.200 | Yogur griego Alpina y vasos grandes para cuchara |

El precio de fábrica deja entre 31 y 48 % de margen al canal de distribución, lo que permite que el producto llegue al consumidor en el rango de las marcas comparables.

### 3.4 Producción y ventas anuales

La planta produce de lunes a sábado, 50 semanas al año (300 días), con dos lotes por día: 12 lotes por semana y 600 al año. La mezcla sigue el ciclo de 10 lotes del documento de recetas y lotes (5 de YB-200, 3 de YV-150 y 2 de YV-300), que se repite 60 veces al año. Tabla generada:

<!-- tabla:produccion_refs -->
| Referencia | Unidades llenadas al año | Unidades conformes al año | Ventas (millones de COP) | Margen de contribución (millones de COP) |
| --- | --- | --- | --- | --- |
| YB-200 | 923.700 | 909.844 | 1.091,8 | 445,2 |
| YV-150 | 786.420 | 774.624 | 1.161,9 | 505,3 |
| YV-300 | 271.200 | 267.132 | 774,7 | 335,3 |
| **Total** | **1.981.320** | **1.951.600** | **3.028,4** | **1.285,8** |
<!-- /tabla:produccion_refs -->

| Concepto operativo | Situación actual | Propuesta (dos lotes diarios) |
| --- | --- | --- |
| Lotes por año | 300 | 600 |
| Leche procesada al año | 165.000 L | 330.000 L |
| Unidades conformes al año | 869.400 bolsas | 1.951.600 unidades |
| Ventas anuales (millones de COP) | 1.043,3 | 3.028,4 |
| Costo variable anual (millones de COP) | 604,3 | 1.742,6 |
| Margen de contribución anual (millones de COP) | 439,0 | 1.285,8 |

**Dinámica de los dos lotes diarios.** El lote 1 se carga a las 8:05, se incuba hasta las 14:35, se enfría en placas y se envasa de 15:05 a 17:10. Mientras tanto, el tanque se limpia y recibe el lote 2, cuya leche esperó a 4 °C en TK-102; el lote 2 se incuba de noche sin operario, se enfría con agua helada en la chaqueta y se envasa al día siguiente de 10:30 a 12:35. Así se duplica el volumen diario sin comprar un segundo tanque de proceso. El programa completo, verificado con `herramientas/programa.py`, está en la sección 7.4 del documento de recetas y lotes.

### 3.5 Régimen de operación, turnos y costo de la mano de obra

Hoy la planta trabaja un turno de 8 h; con la propuesta la jornada va de 7:00 a 19:00 en turnos escalonados de 7 h, que cumplen la jornada de 42 h semanales (Ley 2101 de 2021).

| Rol | Turno | Personas |
| --- | --- | --- |
| Operador de recepción y laboratorio | Lunes a sábado, 7:00–14:00 | 1 |
| Operador de preparación | Lunes a sábado, 7:00–14:00 | 1 |
| Operador de envasado | Lunes a sábado, 10:30–17:30 | 1 |
| Operador de empaque y cuarto frío | Lunes a sábado, 10:30–17:30 | 1 |
| Operador del segundo lote (nuevo) | Lunes a sábado, 12:00–19:00 | 1 |
| Envasado del lote 2 del sábado | Domingo, 7:00–10:30 | 2 por rotación |

| Concepto de mano de obra | Valor |
| --- | --- |
| Salario mensual de un operario | COP 1.842.000 |
| Costo empresa mensual, con el factor prestacional de 1,52 | COP 2.800.000 |
| Costo anual por operario | COP 33,6 millones |
| Operarios con la propuesta | 5: los 4 actuales y 1 nuevo para el segundo lote |
| Costo adicional: operario nuevo | COP 33,6 millones al año |
| Costo adicional: turno del domingo. Las 3,5 h superan las 42 h semanales, así que son horas extra dominicales: 2 operarios × 3,5 h × 50 domingos × 10.121 COP × 2,25 (hora extra del 25 % y recargo dominical del 100 % que rige desde julio de 2027, Ley 2466 de 2025) × 1,52 | COP 12,1 millones al año |
| Costo adicional: horas extra cuando la incubación se alarga hasta 300 min (unos 40 min de los operadores de envasado y empaque y 20 min del operador del segundo lote) y disponibilidad nocturna del jefe de producción para las alarmas del lote 2 | COP 5,0 millones al año |

El jefe de producción y la persona de calidad son personal que la planta ya tiene; el proyecto cambia sus herramientas, no su número.

## 4. Salarios del equipo: costo interno de Cremia (2026)

El escenario evaluado corresponde a una firma integradora conformada por seis ingenieros mecatrónicos egresados de la Universidad Nacional de Colombia, con un año de experiencia profesional en proyectos industriales.

- **Contexto salarial 2026.** Con un salario mínimo legal cercano a COP 1.800.000 (sin auxilio de transporte), el salario de COP 4.000.000 de los ingenieros equivale a 2,22 salarios mínimos y el de COP 6.000.000 del gerente a 3,33.
- **Sustentación.** Con un año de experiencia en automatización e integración OT/IT, un ingreso de 2,22 salarios mínimos coincide con las bandas de enganche del Observatorio Laboral para la Educación, el escalafón 1 del manual de tarifas de ACIEM y la guía salarial de Michael Page Colombia 2025-2026.

| Cargo en Cremia Automations | Cantidad | Salario mensual (COP) | Costo empresa mensual (COP) | Costo por hora (COP) |
| --- | --- | --- | --- | --- |
| Gerente de proyecto | 1 | 6.000.000 | 9.120.000 | 50.110 |
| Ingeniero de proyecto (líder de área) | 5 | 4.000.000 | 6.080.000 | 33.407 |
| Nómina mensual consolidada | 6 | 26.000.000 | 39.520.000 | — |

### 4.1 Factor prestacional

| Concepto | Porcentaje sobre el salario básico |
| --- | --- |
| Pensión a cargo del empleador | 12,0 % |
| Salud | 8,5 % |
| ARL, riesgo III (planta industrial) | 2,436 % |
| Caja de compensación | 4,0 % |
| Cesantías | 8,33 % |
| Intereses sobre cesantías | 1,0 % |
| Prima de servicios | 8,33 % |
| Vacaciones | 4,17 % |
| Dotación y seguridad y salud en el trabajo | 3,234 % |
| **Total** | **52 % (factor de 1,52)** |

Con la jornada de 42 horas semanales que rige desde el segundo semestre de 2026 (Ley 2101 de 2021), la base mensual es de 182 horas, de donde salen los costos por hora de la tabla anterior.

## 5. Servicios de ingeniería: precio por actividad

Los salarios son el costo interno de Cremia; al cliente no se le cobra nómina, sino servicios de ingeniería por actividad de la EDT. El factor de administración, imprevistos y utilidad (AIU) de 1,39 es el mínimo que debe cubrir el conjunto de la ingeniería:

| Componente de la tarifa | Porcentaje | Base de aplicación |
| --- | --- | --- |
| Administración (oficina, licencias de herramientas de ingeniería, equipos de cómputo y pólizas) | 15 % | Costo directo de personal |
| Imprevistos | 5 % | Costo directo más administración |
| Utilidad | 15 % | Costo más administración e imprevistos |
| Factor multiplicador resultante | 1,39 | Costo directo de personal |

| Cargo | Costo por hora (COP) | Tarifa mínima con el factor 1,39 (COP/h) |
| --- | --- | --- |
| Gerente de proyecto | 50.110 | 69.700 (≈ USD 17,0) |
| Líder de área | 33.407 | 46.500 (≈ USD 11,3) |

La tarifa de cada integrante parte de su costo por hora y lo multiplica por un factor que refleja el tipo de valor que aporta: 2,13 para las especialidades escasas y críticas (arquitectura OT/IT, nube y ciberseguridad; SCADA y plataforma MES/ERP), 2,01 para el núcleo técnico del proceso y de la validación, 1,80 para la dirección del proyecto, que ya parte de un costo mayor, y 1,59 para la gestión y el soporte. Tabla generada:

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

El valor de cada cuenta de la EDT sale de sus horas por la tarifa de quien la hace. Tabla generada:

<!-- tabla:cuentas_valor -->
| Cuenta de la EDT | Actividad | Horas | Millones de COP |
| --- | --- | --- | --- |
| 1.1 | Gestión del proyecto | 310 | 22,35 |
| 1.2 | Ingeniería conceptual y básica | 260 | 18,70 |
| 1.3 | Ingeniería de detalle | 400 | 27,14 |
| 1.4 | Procura | 180 | 10,38 |
| 1.5 | Software de control y supervisión | 680 | 52,99 |
| 1.6 | Plataforma Cremia MES/ERP | 1.500 | 99,57 |
| 1.7 | Gemelo digital y puesta en marcha virtual | 340 | 25,45 |
| 1.8 | Montaje e instalación | 320 | 21,94 |
| 1.9 | Pruebas y puesta en marcha | 280 | 20,46 |
| 1.10 | Gestión del cambio, capacitación, estabilización y cierre | 510 | 34,73 |
| | **Total** | **4.780** | **333,71** |
<!-- /tabla:cuentas_valor -->

La ingeniería se factura en dos contratos. Tabla generada:

<!-- tabla:contratos -->
| Contrato | Paquetes de la EDT | Semanas | Horas | Millones de COP |
| --- | --- | --- | --- | --- |
| 1. Diseño, procura y gestión de compras | 1.1.1, 1.1.3 y cuentas 1.2 a 1.4 | 1–18 | 930 | 62,1 |
| 2. Implementación, software, puesta en marcha y adopción | 1.1.2, 1.1.4 y cuentas 1.5 a 1.10 | 2–26 | 3.850 | 271,6 |
| **Total** | | **1–26** | **4.780** | **333,7** |
<!-- /tabla:contratos -->

Comprobación interna de Cremia (no es un cobro al cliente):

| Concepto | Millones de COP |
| --- | --- |
| Nómina completa del equipo durante las 26 semanas (39,52 millones al mes durante 6 meses) | 237,1 |
| Administración, imprevistos y utilidad de Cremia | 96,6 |
| **Valor de venta de los servicios de ingeniería** | **333,7** |
| Factor del valor facturado sobre la nómina | 1,41, por encima del mínimo de 1,39 |

El valor facturado cubre la nómina completa de las 26 semanas, aunque el proyecto ocupe el 77 % de la capacidad del equipo; el resto del tiempo se dedica a la coordinación interna y a la gestión comercial de Cremia. De las 4.780 h, 1.830 son de desarrollo de software (SCADA y plataforma), con un costo interno de unos COP 66,2 millones y un valor de venta de COP 123,9 millones.

## 6. Presupuesto de inversión (CAPEX)

### 6.1 Rubros

La celda robotizada de encanastado y paletizado (robot ABB, unos COP 180 millones) queda diseñada, con su espacio y su interfaz reservados, pero se compra en una etapa posterior, cuando el volumen de producción la justifique; mientras tanto, el encajonado es manual con una mesa acumuladora. Tabla generada:

<!-- tabla:capex -->
| N.º | Rubro tecnológico o maquinaria cotizada | Valor estimado (millones de COP) |
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
| | **Subtotal de equipos y software** | **947,0** |
| | Servicios de ingeniería de Cremia Automations (4.780 h en dos contratos, con tarifa por integrante) | 333,7 |
| | Montaje mecánico y eléctrico por contratistas certificados (8 % de los equipos físicos) | 75,3 |
| | **Subtotal** | **1.356,0** |
| | Contingencia del proyecto (8 %) | 108,5 |
| | **Inversión total** | **1.464,5** |
| | Margen no percibido por 5 días de parada de planta durante el montaje | 7,3 |
| | **Desembolso total del año 0** | **1.471,8** |
<!-- /tabla:capex -->

### 6.2 Composición de la inversión

Tabla generada:

<!-- tabla:capex_grupos -->
| Grupo | Rubros | Millones de COP | Participación |
| --- | --- | --- | --- |
| Equipos de proceso | 1, 3, 4, 5, 7, 13, 14, 15, 17 y 18 | 460,0 | 31,4 % |
| Envasado, inspección y transporte | 6, 8, 9, 16 y 19 | 311,0 | 21,2 % |
| Instrumentación, control, nodo de borde y nube | 2, 10, 11 y 12 | 176,0 | 12,0 % |
| Ingeniería de Cremia (incluye 1.830 h de software) | — | 333,7 | 22,8 % |
| Montaje y contingencia | — | 183,8 | 12,5 % |
| **Total** | | **1.464,5** | **100 %** |
<!-- /tabla:capex_grupos -->

Los valores de equipos son estimaciones de orden de magnitud a partir de catálogos y cotizaciones de referencia de proveedores del sector lácteo; la cotización formal de cada rubro es parte del paquete de procura de la EDT (1.4.1). La contingencia del 8 % cubre la incertidumbre de esas estimaciones, la variación de la tasa de cambio en los equipos importados y los cambios menores que puedan surgir por pedir los equipos de largo plazo en la semana 4.

### 6.3 Desembolsos del cliente por hitos

Tabla generada:

<!-- tabla:pagos -->
| Hito | Semana | Porcentaje | Millones de COP |
| --- | --- | --- | --- |
| Firma del contrato (anticipo) | 1 | 30 % | 439,3 |
| Pruebas FAT aprobadas | 14 | 30 % | 439,3 |
| Pruebas SAT y puesta en marcha | 21 | 30 % | 439,3 |
| Cierre y entrega | 26 | 10 % | 146,4 |
| **Total** | | **100 %** | **1.464,5** |
<!-- /tabla:pagos -->

### 6.4 Costo completo del software de supervisión y gestión

El SCADA y la plataforma MES/ERP no tienen licencias de terceros, pero sí costo de desarrollo, de hardware y de nube. El detalle está en el documento de la plataforma Cremia MES/ERP y el SCADA en Node-RED (módulo 1).

| Componente | Qué incluye | Horas | Millones de COP |
| --- | --- | --- | --- |
| SCADA en Node-RED (paquetes 1.5.3 a 1.5.5) | Guía de estilo ISA-101 y pantallas, alarmas ISA-18.2, historiador local y nodo de borde con operación sin conexión | 330 | Dentro de la ingeniería |
| Plataforma Cremia MES/ERP (cuenta 1.6) | Infraestructura en Huawei Cloud, núcleo, recetas, registro de lote, calidad, integración borde–nube, ERP ligero, OEE, tablero y pruebas, en dos versiones | 1.500 | Dentro de la ingeniería |
| **Desarrollo de software (valor de venta)** | | **1.830** | **123,9** |
| Hardware de borde (rubro 11) | PC industrial principal y de repuesto, dos paneles táctiles IP65, UPS, router con 4G y equipo de salto | — | 30,0 |
| Nube durante el proyecto (rubro 12) | Entornos de desarrollo, pruebas y producción en Huawei Cloud | — | 6,0 |
| **Inversión inicial en supervisión y gestión de la producción** | | | **159,9** |

Desde el año 1, el software cuesta COP 40,0 millones al año (sección 7.2).

## 7. Beneficios y costos anuales de la propuesta

Tabla generada:

<!-- tabla:beneficio -->
| Concepto operativo anual | Millones de COP por año |
| --- | --- |
| Margen de contribución anual con la propuesta (600 lotes, unidades conformes) | 1.285,8 |
| Margen de contribución actual de la planta (300 lotes, unidades conformes) | −439,0 |
| **Margen de contribución adicional** | **846,9** |
| Mantenimiento preventivo de equipos de proceso y envasado | −24,8 |
| Plan de servicio Cremia: nube Huawei | −15,0 |
| Plan de servicio Cremia: soporte y evolución del software y del control | −21,0 |
| Conectividad doble (fibra y 4G) | −4,0 |
| Operario adicional para el segundo lote | −33,6 |
| Turno del domingo (horas extra dominicales) | −12,1 |
| Horas extra por incubaciones largas y disponibilidad nocturna | −5,0 |
| Laboratorio externo: microbiología por muestreo | −12,0 |
| **Beneficio operativo anual a plena producción, antes de impuestos** | **719,3** |
<!-- /tabla:beneficio -->

El mantenimiento preventivo es el 3 % anual de los equipos de proceso y envasado (COP 828,0 millones), con repuestos y electrodos de pH. El laboratorio externo hace unos 120 análisis microbiológicos al año, uno de cada cinco lotes, a unos COP 100.000 cada uno.

### 7.1 Beneficios que no entran en el flujo de caja

- **Trazabilidad por lote.** Un retiro de producto se limita a los lotes afectados, en lugar de toda la producción de varios días.
- **Menor consumo de agua de red.** Los dos lotes se enfrían con agua helada en circuito cerrado (el lote 1 en placas y el lote 2 en la chaqueta), en lugar de dejar correr agua de red toda la noche.
- **Información para decidir.** La plataforma entrega rendimiento, OEE y costos reales por lote, que hoy no existen.
- **Continuidad de la gestión.** La plataforma en la nube sigue disponible para ventas, inventario y despacho aunque falle la planta.
- **Descuento tributario por inversión en ciencia, tecnología e innovación.** Si el proyecto obtiene la calificación correspondiente, el artículo 256 del Estatuto Tributario permite descontar del impuesto de renta una parte de la inversión. No se incluye en el caso base.

La reducción del producto no conforme ya está en el flujo: la situación actual y la propuesta venden solo las unidades conformes.

### 7.2 Costo del ciclo de vida del software y sostenibilidad

| Costo anual del software | Millones de COP por año |
| --- | --- |
| Plan de servicio Cremia: nube Huawei (servidor virtual, base de datos principal y en espera, respaldos, IP y avisos; unos USD 300 al mes) | 15,0 |
| Plan de servicio Cremia: soporte de segundo nivel del PLC, el SCADA y la plataforma, actualizaciones de seguridad, ajustes de recetas y reportes, copias de respaldo y revisión trimestral de indicadores (unas 0,2 personas de tiempo completo) | 21,0 |
| Conectividad doble de la planta: fibra y respaldo 4G | 4,0 |
| **Total anual** | **40,0** |

En cinco años, el software cuesta COP 359,9 millones: 159,9 de inversión inicial (desarrollo, hardware de borde y nube del proyecto) y 200,0 de costos recurrentes. Solo los tres módulos MES licenciados de la versión de octubre de 2026 cuestan unos COP 223 millones en la lista de precios del fabricante, sin el SCADA, el ERP ni su soporte anual.

**Por qué software propio.** Para una planta de una línea, las plataformas licenciadas traen más funciones y más costo de los que necesita. Cremia desarrolla un software de complejidad media, a la escala de la planta, con tecnologías abiertas (Python, Django, PostgreSQL, MQTT, OPC UA y Node-RED), y lo reutiliza en otras plantas del segmento.

**Cómo se evita la dependencia de un solo proveedor.**
- La Hacienda recibe una licencia de uso perpetua de la plataforma para su sitio; el código fuente se deposita con un tercero y se entrega al cliente si Cremia deja de prestar el servicio.
- La planta es dueña de sus datos, que puede exportar completos en cualquier momento, y del programa del PLC, de los flujos de Node-RED y de las recetas, que se entregan con su documentación (paquete 1.10.3 de la EDT).
- Soporte en tres niveles: el técnico de primer nivel de la planta, Cremia en el segundo y los fabricantes de los equipos en el tercero.
- Una actualización trimestral de seguridad de la plataforma y una anual del nodo de borde, probadas antes en el entorno de pruebas y aplicadas en una ventana sin producción.
- Copias de respaldo diarias cifradas en la nube, con una prueba de restauración cada semestre.
- Repuestos críticos en la planta: un módulo de E/S, una fuente, un variador, electrodos de pH y el PC de repuesto del nodo de borde.
- Renovación del hardware de borde hacia el año 6, fuera del horizonte de evaluación; el PLC y la red tienen una vida útil de más de diez años.

## 8. Flujo de caja proyectado a cinco años

El horizonte es de cinco años desde la entrega. Se modela una rampa de adopción comercial conservadora: 50 % del margen adicional el primer año, 75 % el segundo y 100 % desde el tercero, porque las referencias en vaso necesitan tiempo para entrar al canal y el personal necesita tiempo para dominar la nueva operación. La producción de las semanas de estabilización no se cuenta.

Supuestos del flujo:

- **Impuesto de renta** del 35 % sobre el resultado operativo menos la depreciación.
- **Depreciación** en línea recta: 10 años para los equipos, el montaje y la ingeniería de la línea (COP 1.291,8 millones) y 5 años para el software y el hardware de borde (COP 172,7 millones), en ambos casos con su parte de la contingencia. La depreciación anual es de COP 163,7 millones.
- **Capital de trabajo:** 30 días de cartera sobre las ventas adicionales y 15 días de inventario menos 30 días de proveedores sobre el costo variable adicional; COP 118,0 millones a plena producción, que se recuperan en el año 5.
- **Valor residual** en el año 5: el valor en libros de los equipos, COP 645,9 millones. El software y el hardware de borde llegan al año 5 sin valor en libros.
- **Tasa de descuento** del 15 %, la tasa de oportunidad del cliente.

Valores en millones de COP. Tabla generada:

<!-- tabla:flujo -->
| Concepto financiero | Año 0 | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Inversión y parada por montaje | −1.471,8 | — | — | — | — | — |
| Margen adicional (rampa de ventas) | — | 423,4 | 635,1 | 846,9 | 846,9 | 846,9 |
| Costos de operación | — | −127,6 | −127,6 | −127,6 | −127,6 | −127,6 |
| Resultado operativo (EBITDA) | — | 295,9 | 507,6 | 719,3 | 719,3 | 719,3 |
| Depreciación (no es salida de caja) | — | 163,7 | 163,7 | 163,7 | 163,7 | 163,7 |
| Impuesto de renta (35 %) | — | −46,3 | −120,4 | −194,5 | −194,5 | −194,5 |
| Variación del capital de trabajo | — | −59,0 | −29,5 | −29,5 | 0,0 | 0,0 |
| Recuperación del capital de trabajo y valor residual en libros | — | 0,0 | 0,0 | 0,0 | 0,0 | 763,9 |
| **Flujo neto antes de impuestos** | −1.471,8 | 236,9 | 478,1 | 689,8 | 719,3 | 1.483,2 |
| **Flujo neto después de impuestos** | −1.471,8 | 190,6 | 357,7 | 495,3 | 524,8 | 1.288,7 |
| Flujo acumulado después de impuestos | −1.471,8 | −1.281,2 | −923,4 | −428,1 | 96,7 | 1.385,5 |
<!-- /tabla:flujo -->

## 9. Indicadores financieros

Tabla generada:

<!-- tabla:indicadores -->
| Indicador | Después de impuestos (principal) | Antes de impuestos |
| --- | --- | --- |
| VPN al 15 % | COP 231,0 millones | COP 697,9 millones |
| TIR | 19,8 % | 28,9 % |
| Periodo de recuperación | 3,8 años | 3,1 años |
| Relación beneficio-costo (valor presente de los flujos ÷ desembolso) | 1,16 | — |
| Volumen de equilibrio (VPN = 0) | 89,6 % del plan | — |
| Vasos de equilibrio, con las bolsas al 100 % | 84,1 % del plan | — |
<!-- /tabla:indicadores -->

El indicador principal es el VPN después de impuestos: COP 231,0 millones, con una TIR de 19,8 % y recuperación en 3,8 años. El proyecto crea valor para el cliente, pero con menos holgura que la versión de octubre de 2026 (VPN de 602 millones antes de impuestos y sin valor residual), por tres razones: el flujo ahora paga impuestos, la propuesta incluye lo que necesita el segundo lote (TK-102, agua helada en la chaqueta, horas extra y laboratorio) y la ingeniería cubre la nómina completa de un proyecto de 26 semanas. La propuesta es más cara que en octubre, pero ahora sus cifras son completas.

## 10. Sensibilidad, alcance y financiación

### 10.1 Sensibilidad

El volumen se expresa como porcentaje de la producción de la propuesta que efectivamente se vende; la situación actual se mantiene como base. Tabla generada (después de impuestos):

<!-- tabla:sensibilidad -->
| Escenario | VPN al 15 % (millones de COP) | TIR | Recuperación |
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
| Solo preparación y bolsas: 600 lotes de YB-200 sin línea de vasos (inversión de 1.174,6) | −264,0 | 7,7 % | 4,5 años |
<!-- /tabla:sensibilidad -->

**Lectura.**
- **El volumen es la variable más sensible.** Por debajo del 89,6 % del plan, el VPN es negativo. Si las bolsas se venden completas, el equilibrio de los vasos está en el 84,1 % de lo planeado.
- **El valor residual pesa.** Sin él, el VPN es negativo. Es razonable incluirlo porque los equipos de proceso tienen más de 10 años de vida útil y se valoran en libros, no a precio de mercado, pero el cliente debe saber que buena parte del valor llega al final del horizonte.
- **El software propio aguanta un sobrecosto.** Con 30 % más de horas de software, el VPN sigue en COP 200,2 millones.
- **Solo bolsas no es viable.** Duplicar las bolsas sin la línea de vasos da un VPN de −264,0 millones: el negocio de la propuesta depende de los vasos.

### 10.2 Alcance y condición para firmar

Como el proyecto solo es viable con las referencias en vaso, la oferta exige, antes de firmar, cartas de intención de los distribuidores por al menos el 85 % del volumen de vasos del plan. Así, el cliente no se compromete con el anticipo sin haber validado la demanda que sostiene el VPN. La celda robotizada de encanastado y paletizado (unos COP 180 millones en equipos) queda para una etapa posterior, cuando el volumen la justifique.

### 10.3 Estructura de financiación

Si el cliente financia el 70 % de la inversión (COP 1.025,1 millones) con un crédito de modernización industrial a cinco años, al 18 % efectivo anual, el crédito necesita un año de gracia con pago de intereses: sin él, la cuota de los años 1 a 5 superaría el flujo del año 1. Tabla generada (millones de COP):

<!-- tabla:credito -->
| Año | Intereses | Abono a capital | Cuota | Saldo al final del año | Flujo del proyecto después de impuestos | Ahorro tributario de los intereses | Flujo después de la deuda |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 184,5 | 0,0 | 184,5 | 1.025,1 | 190,6 | 64,6 | 70,7 |
| 2 | 184,5 | 196,6 | 381,1 | 828,6 | 357,7 | 64,6 | 41,2 |
| 3 | 149,1 | 231,9 | 381,1 | 596,6 | 495,3 | 52,2 | 166,5 |
| 4 | 107,4 | 273,7 | 381,1 | 323,0 | 524,8 | 37,6 | 181,4 |
| 5 | 58,1 | 323,0 | 381,1 | 0,0 | 524,8 | 20,3 | 164,1 |
<!-- /tabla:credito -->

El flujo después de la deuda es positivo todos los años, aunque el año 2 es estrecho (COP 41,2 millones). El 30 % restante (COP 439,3 millones) lo aporta el cliente con recursos propios y coincide con el anticipo a la firma del contrato.

## 11. Riesgos y mitigación

| Riesgo | Efecto | Probabilidad | Mitigación |
| --- | --- | --- | --- |
| Las referencias en vaso se venden menos de lo previsto | VPN negativo por debajo del 84,1 % de los vasos del plan | Media | Cartas de intención por el 85 % del volumen de vasos antes de firmar; plan de lanzamiento con los distribuidores |
| Baja del precio de venta en el canal | Una baja del 5 % reduce el VPN a 58,2 millones | Media | Contratos de suministro con precio indexado; mezcla con más vasos |
| Sobrecosto de equipos importados por tasa de cambio | Un 10 % más de inversión reduce el VPN a 135,8 millones | Media | Contingencia del 8 %; cotizaciones con validez de 90 días |
| Retraso en la fabricación, el transporte o la nacionalización | La entrega se corre más allá de la semana 26 | Media | Pedido en la semana 4 con hojas de datos aprobadas, seguimiento semanal, FAT antes del despacho y agente de aduanas desde la orden de compra |
| El desarrollo del software toma más horas | Un 30 % más de horas reduce el VPN a 200,2 millones | Media | Dos versiones: si el desarrollo se atrasa, se corren funciones a la versión 2 y no el arranque; pruebas en el gemelo digital |
| Falla de la nube o de internet | Pérdida temporal de la gestión de la producción | Baja | El PLC y el nodo de borde producen sin internet durante 72 h; base de datos con réplica en espera; conectividad doble |
| Incidente de ciberseguridad | Parada de producción o pérdida de datos | Baja | Zonas según IEC 62443, solo conexiones salientes, certificados por dispositivo, doble factor y respaldos cifrados |
| El lote 2 nocturno sale fuera de especificación | Lote no conforme o retenido | Media | pH de corte de 4,6, enfriamiento con agua helada, respaldo con agua de red, alarmas por SMS y acidez de confirmación a las 7:00; validación en el arranque con un lote nocturno de cada referencia |
| Dependencia del software de Cremia | La planta no puede mantener la plataforma si Cremia desaparece | Baja | Licencia perpetua, depósito del código fuente y exportación completa de datos |
| Resistencia del personal al cambio | Rendimiento menor al esperado en el primer año | Media | Plan de gestión del cambio (EDT 1.10.1), capacitación por rol (1.10.2), seis semanas de estabilización y rampa de adopción del 50 % y 75 % |

## 12. Modelo de negocio

| Criterio de decisión | A. Llave en mano clásico | B. Arrendamiento de equipos | C. Llave en mano con plan de servicio (recomendado) |
| --- | --- | --- | --- |
| Qué paga el cliente | La inversión, por hitos | Una cuota mensual | La inversión por hitos y un plan de servicio anual |
| Propiedad de los equipos | Cliente | Cremia | Cliente |
| Software de gestión | Licencias de terceros | Incluido en la cuota | Plataforma Cremia MES/ERP con licencia perpetua para el sitio |
| Capital que necesita Cremia | Bajo | Muy alto | Bajo |
| Riesgo para Cremia | Bajo | Alto: cartera y obsolescencia | Bajo |
| Relación a largo plazo | Termina con el proyecto | Continua | Continua y colaborativa |

**Modelo recomendado: C.** Cremia es una firma de seis ingenieros sin capital para financiar maquinaria de proceso, lo que descarta el arrendamiento. El cliente queda como dueño de los equipos y recibe una licencia perpetua de la plataforma para su sitio, con el código en depósito. Cremia conserva la propiedad intelectual de la plataforma, la reutiliza en otras plantas lácteas y mantiene un ingreso recurrente con el plan de servicio de COP 36,0 millones al año: la nube Huawei (15,0) y el soporte y la evolución del software y del control (21,0), con una revisión trimestral de indicadores con la gerencia de la planta. El plan ya está en los costos de operación del flujo de caja.

## 13. Propuesta de valor y oferta comercial

### 13.1 Beneficios para los dueños de la planta

| Dimensión | Hoy | Con la propuesta | Cambio |
| --- | --- | --- | --- |
| Productividad | 2.898 bolsas conformes por día; 724 por operario | 6.505 unidades conformes por día en promedio; 1.301 por operario | +124 % de producción conforme y +80 % por operario |
| Ingresos y margen | Ventas de COP 1.043,3 millones y margen de 439,0 millones al año | Ventas de COP 3.028,4 millones y margen de 1.285,8 millones al año | +846,9 millones de margen y +719,3 millones de beneficio operativo al año |
| Costo de mano de obra por unidad conforme | 155 COP | 95 COP | −39 % |
| Calidad | 5,06 % de producto no conforme; peso de una de cada cinco bolsas | 1,5 % o menos; peso del 100 % y puntos críticos con registro continuo | Menos producto perdido, ya incluido en el flujo |
| Eficiencia de la empacadora (OEE) | ≈ 65 % | 82 % | Menos paradas y peso en línea |
| Trazabilidad | Registros en papel; un retiro afecta varios días de producción | Registro electrónico por lote, desde la cantina hasta la estiba | El retiro se limita a los lotes afectados |
| Información | No existe: la programación es verbal | Tablero diario con OEE, rendimiento, no conformes, consumos y costo real por lote, disponible desde la nube | Datos del mismo día, no del mes siguiente |
| Tiempo y flexibilidad | 601 min por lote, una referencia, un lote al día | 563 min por lote, tres referencias, dos lotes al día; cambio de referencia en 5 a 40 min | El tanque queda libre a las 15:05 |

La propuesta de valor y el plan de gestión del cambio se desarrollan en el documento Propuesta de valor y gestión del cambio.

### 13.2 Propuesta de valor

1. **Más producción con la misma planta:** de uno a dos lotes diarios (1.100 L de leche por día), sin ampliar el tanque de proceso, gracias al enfriamiento rápido en placas y al enfriamiento nocturno con agua helada.
2. **Portafolio ampliado de mayor margen:** de una a tres referencias, con vasos de 150 y 300 ml con fruta que dejan hasta 1.280 COP de margen por unidad.
3. **Calidad uniforme y menos desperdicio:** dosificación por celdas de carga, control automático de temperatura y pH, y control de peso del 100 % en línea. Meta de producto no conforme: 1,5 % o menos, frente al 5,06 % actual.
4. **Trazabilidad integral ISA-88 e ISA-95:** registro electrónico por lote desde la cantina de leche cruda hasta el despacho, sin papel.
5. **Software a la escala de la planta, sin licencias de terceros:** SCADA en Node-RED y plataforma Cremia MES/ERP en Huawei Cloud, que sigue disponible aunque falle la planta y avisa si se pierde la señal del lote nocturno.
6. **Menor riesgo de puesta en marcha:** el programa del PLC, el SCADA y la plataforma se validan en un gemelo digital antes del montaje físico.
7. **Personas preparadas para operar la nueva línea:** gestión del cambio desde la semana 1, capacitación por rol en el gemelo digital, procedimientos actualizados y seis semanas de estabilización con producción.

### 13.3 Oferta comercial

| Elemento contractual | Condición ofertada |
| --- | --- |
| Alcance del suministro | Ingeniería, suministro de equipos, montaje, programación del PLC, SCADA en Node-RED, plataforma Cremia MES/ERP en Huawei Cloud, pruebas FAT y SAT, puesta en marcha, gestión del cambio, capacitación y estabilización |
| Valor total de la oferta | COP 1.464,5 millones, sin IVA |
| Servicios de ingeniería | COP 333,7 millones en dos contratos: diseño, procura y gestión de compras (62,1) e implementación, software, puesta en marcha y adopción (271,6), con tarifa según el valor que aporta cada integrante |
| Condición para firmar | Cartas de intención de los distribuidores por al menos el 85 % del volumen de vasos del plan |
| Plazo de ejecución | 26 semanas, del 18 de enero al 16 de julio de 2027 |
| Forma de pago por hitos | 30 % de anticipo a la firma, 30 % contra pruebas FAT (semana 14), 30 % con la puesta en marcha y las pruebas SAT (semana 21) y 10 % al cierre (semana 26) |
| Software | Licencia perpetua de la plataforma Cremia MES/ERP para el sitio, código fuente en depósito con un tercero y exportación completa de datos |
| Garantía y servicio | 12 meses de garantía integral sobre la integración, seis semanas de estabilización dentro del proyecto y plan de servicio anual de COP 36,0 millones (nube y soporte), incluido en los costos de operación |
| Etapa posterior opcional | Celda robotizada de encanastado y paletizado, con espacio e interfaz ya diseñados |

## 14. Referencias

1. Asociación Colombiana de Ingenieros (ACIEM). (2024). Manual de referencia de tarifas para la contratación de servicios profesionales de ingeniería en Colombia. Bogotá: ACIEM.
2. Congreso de la República de Colombia. (2021). Ley 2101 de 2021, por medio de la cual se reduce la jornada laboral semanal de manera gradual. Diario Oficial.
3. Congreso de la República de Colombia. (2025). Ley 2466 de 2025, reforma laboral (recargo dominical y festivo).
4. Estatuto Tributario, artículos 137 (depreciación), 240 (tarifa del impuesto de renta) y 256 (descuento por inversiones en ciencia, tecnología e innovación).
5. Grimaldo, G., Moreno, D. y Salamanca, M. (2015). Medición del trabajo de una línea de producción de yogurt – Empresa La Hacienda. Revista I3+, 2(2), 62–81.
6. Michael Page Colombia. (2025). Estudio de remuneración Colombia: sector ingeniería y manufactura. Bogotá: PageGroup.
7. Ministerio de Agricultura y Desarrollo Rural. (2012). Resolución 017 de 2012, por la cual se establece el sistema de pago de la leche cruda al proveedor. Bogotá: MADR.
8. Ministerio de la Protección Social. (2006). Decreto 616 de 2006, reglamento técnico sobre los requisitos que debe cumplir la leche para el consumo humano.
9. Oficina Internacional del Trabajo (OIT). (2005). Introducción al estudio del trabajo (4.ª ed. revisada). México: Limusa.
10. Project Management Institute. (2021). Guía de los fundamentos para la dirección de proyectos (Guía del PMBOK), 7.ª ed. Newtown Square, PA: PMI.
11. Sapag Chain, N., Sapag Chain, R. y Sapag, J. M. (2014). Preparación y evaluación de proyectos (6.ª ed.). México: McGraw-Hill.
12. Sepasoft. Lista de precios de los módulos MES (alternativa descartada), consultada en noviembre de 2026: https://www.sepasoft.com/pricing/
