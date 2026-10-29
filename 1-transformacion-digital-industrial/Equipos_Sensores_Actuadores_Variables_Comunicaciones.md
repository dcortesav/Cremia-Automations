# Equipos, sensores, actuadores, variables y comunicaciones

**Línea de yogur: inventario del sistema actual y del sistema propuesto**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Módulo 1 · Transformación Digital Industrial

## 1. Alcance

Este documento identifica los principales equipos, sensores, actuadores, variables de proceso, lazos de control y comunicaciones de la línea de yogur. Distingue lo que la planta ya tiene de lo que la propuesta agrega, relaciona cada elemento nuevo con la oportunidad de mejora que atiende, justifica la capacidad de los equipos nuevos con cálculos de dimensionamiento y define los enclavamientos, la lista preliminar de entradas y salidas y el plan de calibración.

La situación actual se toma del estudio de la empresa La Hacienda (Grimaldo, Moreno y Salamanca, 2015): cuatro operarios, un tanque de proceso con chaqueta de vapor y agua, un tanque pulmón, una empacadora de bolsas y un cuarto frío. La dosificación, el control de temperatura, la verificación de acidez, el control de peso y el transporte son manuales. Como caso base se asume que el tanque de proceso ya cuenta con un agitador mecánico. Es una planta pequeña e industrializada, con caldera de vapor y leche recibida en cantinas, pero con bajo nivel de automatización.

La numeración de etiquetas sigue ANSI/ISA-5.1 y se organiza por áreas: 100 recepción, 200 dosificación, 300 preparación, 400 envasado, 500 producto terminado y 900 servicios. Las áreas coinciden con las unidades del modelo físico ISA-88: U1 recepción, U2 dosificación, U3 tanque de proceso, U4 enfriamiento y transferencia, U5 tanque pulmón, U6 envasado de bolsas, U7 envasado de vasos y U8 encanastado y paletizado.

## 2. Diagnóstico de la línea actual

| Etapa | Equipo actual | Operación actual | Tiempo por lote (min) | Problema |
| --- | --- | --- | --- | --- |
| Recepción | Plataforma PL-101, tanque TK-101 con filtro, bomba de leche | Descarga de 14 cantinas, análisis por cantina y transferencia por 12 m de tubería | 48,1 | Bomba subdimensionada: 28,4 min solo en la transferencia |
| Alistamiento | Gramera y recipientes | Cálculo y pesaje manual en dos cuartos; transporte de insumos | 10,2 | Error humano y sin registro de lotes de insumos |
| Preparación | Tanque de proceso T-301 de 600 L con chaqueta y agitador | Apertura manual de válvulas de vapor y agua; termómetro y acidómetro | 391,2 | Pasteurización larga (77,4 min) y enfriamiento natural durante la noche |
| Envasado | Empacadora EMP-401 y tanque pulmón T-302 | Llenado y sellado de bolsas; pesaje de una de cada cinco | 148,9 | 20,5 bolsas/min frente a 30 nominales; 5,06 % no conforme |
| Almacenamiento | Cuarto frío CF-501 | Canastas llevadas a mano | 2,9 | Sin registro de ubicación ni de temperatura |
| Servicios | Caldera CAL-901 | Vapor para la chaqueta | — | Sin control de la presión de vapor en el tanque |

La línea no tiene instrumentación conectada ni registros electrónicos: toda medición depende de un instrumento manual y de la anotación en papel. Por eso el inventario de sensores parte de cero.

## 3. Oportunidades de mejora y elementos asociados

| Oportunidad de mejora | Situación actual | Propuesta | Elementos nuevos |
| --- | --- | --- | --- |
| Transporte de la leche al tanque de proceso | La transferencia por 12 m de tubería toma 28 min por lote | Bomba sanitaria de mayor caudal y medición de la leche transferida | P-101, FT-101, WT-101 |
| Dosificación y pesaje de insumos | El operario calcula, pesa y transporta azúcar, estabilizante, colorante, saborizante y cultivo (10 min por lote) | Dosificación automática por peso desde la receta | DS-201, DS-202, P-203, P-204, WT-201, WT-202, WT-205 |
| Estandarización y homogeneización | No se ajustan los sólidos ni se homogeneiza la mezcla | Leche en polvo dosificada por peso y homogeneización a 150–200 bar antes de pasteurizar | DS-206, WT-206, H-301, PT-302, XV-302 |
| Control de la pasteurización y la incubación | Apertura manual de válvulas de vapor y de agua fría | Control automático de temperatura con registro continuo | TT-301, TIC-301, TV-301, TV-302, LT-301 |
| Verificación de acidez | Muestra y acidómetro manual | Medición de pH en línea para determinar el fin de la incubación | AT-301 |
| Enfriamiento | Agua fría en la chaqueta y enfriamiento natural durante la noche: un lote por día y alto consumo de agua | Intercambiador de placas con agua helada en circuito cerrado: enfriamiento en menos de 30 min, menor consumo de agua y segundo lote diario | E-301, P-301, CH-901, TT-302, TV-303 |
| Ruptura del coágulo y homogeneización | Agitación a baja velocidad sin control | Agitador con variador: velocidad según la fase y la referencia, simultánea con el enfriamiento | M-301 con variador, ST-301 |
| Tres referencias de producto | Solo bolsa de 200 ml | Llenadora-selladora de vasos de 150 y 300 ml y dosificación de fruta | LL-402, P-403, MX-403, XV-401, XV-402 |
| Control de peso | Una de cada cinco bolsas se pesa en gramera; el empaque con control de calidad toma 149 min por lote | Control de peso del 100 % en línea con rechazo automático | WT-401, WT-402, XY-401, XY-402 |
| Codificado de lote y fecha | Sin codificado automático | Codificador en cada máquina de envasado, con el lote y la fecha que envía el MES | CD-401, CD-402 |
| Inspección del sellado de la bolsa | El operario presiona cada bolsa y la clasifica en canastas | Se mantiene manual, por muestreo estadístico; el resultado se registra en el sistema | Estación de registro en HMI-01 |
| Paradas de la empacadora de bolsas | Paradas frecuentes por desajuste en la medida de corte de la bolsa | Registro automático de paradas y causas; rutinas de mantenimiento autónomo (TPM) | Señales de estado de EMP-401 al PLC |
| Transporte al cuarto frío | Canastas llevadas a mano | Bandas hacia el encanastado dentro del proyecto; la celda robotizada de encanastado y paletizado queda diseñada para una etapa posterior | CV-401, CV-402, CV-501; R-501 en la etapa posterior |
| Información de producción | Registros en papel | PLC, SCADA y conexión con MES y ERP | PLC-01 (CompactLogix), HMI-01 y HMI-02, SCADA (Ignition) y red industrial |

La recepción y el análisis de la leche por cantina se mantienen manuales: cada cantina debe aprobarse antes de mezclarla. La mejora en esa etapa es registrar los resultados en el sistema.

## 4. Equipos principales

### 4.1 Inventario

| Etiqueta | Equipo | Estado | Función | Capacidad de referencia | Fase |
| --- | --- | --- | --- | --- | --- |
| PL-101 | Plataforma de recepción de cantinas | Existente | Recibe la leche del proveedor | 14 cantinas de 40 L | — |
| TK-101 | Tanque de recepción con filtro | Existente | Recibe la leche aprobada | 600 L | — |
| P-101 | Bomba sanitaria de leche | Reemplazo | Envía la leche al tanque de proceso (12 m de tubería) | 3 m³/h (550 L en 11 min) | 1 |
| LAB-101 | Laboratorio de recepción | Existente | Acidez, pH, densidad y sólidos | — | — |
| DS-201 | Dosificador de azúcar: tolva y tornillo | Nuevo | Dosifica el azúcar por peso | 100 kg por lote | 1 |
| DS-202 | Microdosificador de estabilizante | Nuevo | Dosifica el estabilizante por peso | 0,5 kg por lote | 1 |
| P-203 / P-204 | Bombas dosificadoras de saborizante y colorante | Nuevo | Dosifican los aditivos líquidos | 0–2 L/min | 1 |
| BL-205 | Estación de pesaje del cultivo | Nuevo | Verifica el peso y el lote del cultivo antes de adicionarlo | 0–500 g | 1 |
| DS-206 | Dosificador de leche en polvo: tolva y tornillo | Nuevo | Dosifica la leche en polvo por peso | 20 kg por lote | 1 |
| T-301 | Tanque de proceso con chaqueta y agitador | Existente | Precalentamiento, pasteurización, incubación y saborizado | 600 L | — |
| H-301 | Homogeneizador de alta presión de dos etapas | Nuevo | Homogeneiza la mezcla en recirculación antes de pasteurizar | 1.500 L/h a 200 bar | 1 |
| E-301 | Intercambiador de calor de placas | Nuevo | Enfría el yogur de 43 °C a 15–20 °C | 1.500 L/h | 1 |
| P-301 | Bomba de lóbulos | Nuevo | Transfiere el yogur sin romper su estructura | 1.500 L/h | 1 |
| F-301 | Filtro en línea | Existente | Retiene grumos en la transferencia | — | — |
| T-302 | Tanque pulmón de envasado | Existente | Alimenta las máquinas de envasado | 650 L | — |
| EMP-401 | Empacadora de bolsas (formado, llenado y sellado) | Existente | Envasa YB-200 | 30 bolsas/min | — |
| LL-402 | Llenadora-selladora de vasos | Nuevo | Envasa YV-150 y YV-300 | 45 vasos/min | 2 |
| CD-401 / CD-402 | Codificadores de lote y fecha | Nuevo | Imprimen el lote y la fecha de vencimiento en cada unidad | 60 und/min | 1 y 2 |
| P-403 / MX-403 | Bomba dosificadora de fruta y mezclador en línea | Nuevo | Incorpora el preparado de fruta antes de la llenadora | 0–150 L/h | 2 |
| CK-401 / CK-402 | Controladoras de peso dinámicas | Nuevo | Pesan el 100 % de las unidades y rechazan las no conformes | 60 und/min | 1 y 2 |
| CV-401 / CV-402 / CV-501 | Bandas transportadoras | Nuevo | Llevan el producto a encanastado y al cuarto frío | — | 1 y 2 |
| R-501 | Celda robotizada de encanastado y paletizado (robot ABB) | Nuevo | Arma canastas, cajas y estibas | 10 ciclos/min | Etapa posterior |
| CF-501 | Cuarto frío | Existente | Almacena el producto terminado a 4 °C | — | — |
| CAL-901 | Caldera de vapor | Existente | Suministra vapor a la chaqueta del tanque | — | — |
| CH-901 | Enfriador de agua (chiller) y banco de agua helada | Nuevo | Suministra agua helada al intercambiador de placas | Agua a 2 °C | 1 |
| CIP-901 | Estación de limpieza CIP de dos tanques | Nuevo | Limpia tanques y tuberías entre lotes | — | 1 |

La fase indica la etapa de inversión: en la fase 1 se automatiza la preparación y la línea de bolsas; en la fase 2 se agrega la línea de vasos. Las dos fases caben en el proyecto de 16 semanas. La celda robotizada R-501 queda diseñada, con su espacio, su interfaz con el PLC y sus seguridades definidas, pero se compra en una etapa posterior, cuando el volumen la justifique; mientras tanto el encanastado es manual.

### 4.2 Criterios de diseño sanitario

- Superficies en contacto con el producto en acero inoxidable AISI 316L, con rugosidad Ra ≤ 0,8 µm, uniones soldadas continuas y sin tramos muertos, como pide la Resolución 2674 de 2013.
- Equipos con diseño higiénico según 3-A o EHEDG, drenables y limpiables por CIP sin desarmar.
- Conexiones sanitarias tipo clamp en instrumentos y válvulas; electrodos y sensores con montaje a ras.
- Motores, sensores y tableros en zona húmeda con protección IP66 o superior; equipos sometidos a lavado a presión con IP69K.
- Tuberías de producto con pendiente mínima de 1 % hacia los puntos de drenaje y velocidad de limpieza mayor de 1,5 m/s durante el CIP.

### 4.3 Dimensionamiento de los equipos nuevos

| Equipo | Criterio | Cálculo | Resultado |
| --- | --- | --- | --- |
| P-101 bomba de leche | Cargar 550 L en 11 a 12 min | 0,55 m³ ÷ 0,19 h | 3 m³/h |
| P-101 a 2.600 msnm | Evitar cavitación con presión atmosférica de unos 74 kPa | NPSH disponible ≈ (74 − 2,3) kPa ÷ (1.030 kg/m³ × 9,81 m/s²) ≈ 7,1 m, menos pérdidas de succión | Margen amplio frente a los 2–3 m que exige una centrífuga sanitaria de este tamaño |
| H-301 homogeneizador | Dos pasos de unos 600 L de mezcla dentro del calentamiento | 1.200 L ÷ 1.500 L/h | 48 min |
| H-301 potencia | Caudal por presión dividido por la eficiencia | 0,000417 m³/s × 200 bar ÷ 0,85 | ≈ 9,8 kW; motor de 11 kW |
| Calentamiento de T-301 | 600 kg de 20 a 85 °C en unos 45 min | 600 kg × 3,93 kJ/kg·K × 65 K ÷ 2.700 s | ≈ 57 kW, cerca de 100 kg/h de vapor saturado |
| E-301 intercambiador | 1.500 L/h de yogur de 43 a 18 °C | 0,44 kg/s × 3,8 kJ/kg·K × 25 K | ≈ 42 kW |
| Agua helada de E-301 | Entrada a 2 °C y salida a 8 °C | 42 kW ÷ (4,18 kJ/kg·K × 6 K) | ≈ 6 m³/h |
| CH-901 enfriador | Energía de enfriamiento por lote | 42 kW × 25 min | ≈ 17 kWh por lote; enfriador de unos 15 kW con banco de agua helada que acumula la carga entre lotes |
| P-301 bomba de lóbulos | Transferir el lote más grande en menos de 30 min | 679 L ÷ 1.500 L/h | 27 min |
| T-302 tanque pulmón | Recibir el yogur base de un lote antes de la fruta | YB-200: 616 L; YV-300: 601 L de base (la fruta se agrega en línea) | 650 L es suficiente |
| LL-402 llenadora | Envasar un lote de vasos dentro de un turno | 4.369 vasos ÷ 45 vasos/min; 2.260 ÷ 35 | 97 y 65 min |
| R-501 celda robotizada | Cadencia frente al flujo de unidades | 45 vasos/min ÷ 24 por caja ≈ 1,9 cajas/min; 30 bolsas/min ÷ 120 ≈ 0,25 canastas/min | 10 ciclos/min dan margen para agrupar y paletizar |

La caldera CAL-901 se conserva. Su capacidad nominal no aparece en el caso de estudio, de modo que la ingeniería de detalle verifica que entregue al menos 100 kg/h de vapor en la pasteurización.

### 4.4 Especificación de los equipos nuevos principales

| Equipo | Especificación |
| --- | --- |
| H-301 homogeneizador | Dos etapas, 1.500 L/h, presión de trabajo de 150–200 bar, motor de 11 kW con variador, válvula de alivio y manómetro sanitario; ejecución 316L |
| E-301 intercambiador de placas | Una sección yogur–agua helada, placas de 316L con juntas de EPDM grado alimentario, diseño para producto viscoso (canales anchos), 1.500 L/h |
| P-301 bomba de lóbulos | Desplazamiento positivo, 1.500 L/h, rotores que no cizallan el gel, variador de velocidad |
| LL-402 llenadora-selladora | Lineal de dos carriles, vasos de 150 y 300 ml con el mismo diámetro de boca, dosificador volumétrico de pistón, termosellado de tapa de aluminio, 45 vasos/min |
| CK-401 / CK-402 controladoras de peso | Celda de carga dinámica, resolución de 0,1 g, expulsor neumático, comunicación EtherNet/IP |
| CD-401 / CD-402 codificadores | Transferencia térmica sobre la película de la bolsa (CD-401) e inyección de tinta continua sobre la tapa del vaso (CD-402); imprimen lote y vencimiento y reciben el código del MES |
| R-501 celda robotizada (etapa posterior) | Un robot de paletizado de cuatro ejes (ABB IRB 460) con herramienta de vacío que encanasta bolsas, encajona vasos y arma la estiba; vallado perimetral, cortinas de luz y zona de estiba |
| CIP-901 estación de limpieza | Dos tanques (soda y ácido) con calentamiento, bomba de impulsión, retorno con CT-901 y válvulas de ruta XV-901 |
| CH-901 enfriador | Unidad compacta de unos 15 kW con banco de agua helada a 2 °C y bomba de circulación |

## 5. Sensores

### 5.1 Inventario

| Etiqueta | Variable | Tipo de sensor | Rango | Ubicación | Señal |
| --- | --- | --- | --- | --- | --- |
| WT-101 | Peso de leche recibida | Celdas de carga | 0–700 kg | Tanque de recepción TK-101 | 4–20 mA |
| FT-101 | Caudal de leche | Caudalímetro electromagnético sanitario | 0–5 m³/h | Tubería hacia T-301 | 4–20 mA y pulsos |
| WT-201 | Peso de azúcar | Celdas de carga | 0–150 kg | Tolva DS-201 | 4–20 mA |
| WT-202 | Peso de estabilizante | Celda de carga de precisión | 0–2 kg | Microdosificador DS-202 | 4–20 mA |
| FQ-203 / FQ-204 | Volumen de saborizante y colorante | Conteo de pulsos de la bomba | 0–2 L | Bombas P-203 y P-204 | Pulsos |
| WT-205 | Peso de cultivo | Balanza de precisión | 0–500 g | Estación BL-205 | Ethernet |
| WT-206 | Peso de leche en polvo | Celdas de carga | 0–30 kg | Tolva DS-206 | 4–20 mA |
| TT-301 | Temperatura del producto | PT100 sanitaria doble | 0–100 °C | Tanque de proceso T-301 | 4–20 mA |
| LT-301 | Nivel del tanque de proceso | Transmisor de presión hidrostática | 0–600 L | Tanque de proceso T-301 | IO-Link |
| AT-301 | pH del producto | Electrodo de pH higiénico | pH 3–8 | Tanque de proceso T-301 | 4–20 mA |
| ST-301 | Velocidad del agitador | Realimentación del variador | 0–60 rpm | Agitador M-301 | EtherNet/IP |
| PT-302 | Presión de homogeneización | Transmisor de presión sanitario | 0–250 bar | Salida de H-301 | 4–20 mA |
| TT-302 | Temperatura de salida del enfriador | PT100 sanitaria | 0–60 °C | Salida de E-301 | 4–20 mA |
| PT-301 | Presión de la línea de transferencia | Transmisor de presión sanitario | 0–6 bar | Descarga de P-301 | IO-Link |
| LT-302 | Nivel del tanque pulmón | Transmisor de presión hidrostática | 0–650 L | Tanque pulmón T-302 | IO-Link |
| TT-303 | Temperatura del tanque pulmón | PT100 sanitaria | 0–50 °C | Tanque pulmón T-302 | 4–20 mA |
| WT-401 / WT-402 | Peso de cada unidad | Celda de carga dinámica | 0–500 g | Controladoras CK-401 y CK-402 | EtherNet/IP |
| ZS-401 / ZS-402 | Presencia de producto | Sensor fotoeléctrico | Discreto | Bandas CV-401 y CV-402 | 24 V DC |
| ZS-403 | Presencia de la tapa sellada | Sensor inductivo para tapa de aluminio | Discreto | Salida de LL-402 | 24 V DC |
| ZS-501 | Canasta o caja en posición | Sensor inductivo y fotoeléctrico | Discreto | Celda R-501 | 24 V DC |
| TT-501 | Temperatura del cuarto frío | PT100 | −5 a 20 °C | Cuarto frío CF-501 | 4–20 mA |
| TT-901 | Temperatura del agua helada | PT100 | 0–20 °C | Banco de agua helada | 4–20 mA |
| CT-901 | Conductividad del retorno de CIP | Sensor de conductividad | 0–200 mS/cm | Retorno de CIP-901 | 4–20 mA |

### 5.2 Criterios de selección

| Tipo de sensor | Criterio | Exactitud de referencia |
| --- | --- | --- |
| Temperatura (PT100) | Clase A, vaina sanitaria, elemento doble en TT-301 para comparar las dos lecturas en el punto crítico de la pasteurización | ± 0,3 °C a 85 °C |
| pH (AT-301) | Electrodo de vidrio higiénico, resistente a 90 °C y al CIP, con compensación de temperatura | ± 0,05 pH |
| Celdas de carga | Acero inoxidable, IP68, módulos de montaje que absorben la dilatación del tanque | 0,1 % de la escala |
| Caudal (FT-101) | Electromagnético, sin partes móviles ni obstrucciones; la leche es conductiva | 0,5 % de la lectura |
| Presión | Membrana sanitaria a ras, sin cavidades | 0,25 % de la escala |
| Nivel | Presión hidrostática con compensación de densidad desde la receta | 0,5 % de la escala |
| Discretos | Fotoeléctricos e inductivos IP69K para zonas de lavado | — |

## 6. Actuadores

### 6.1 Inventario

| Etiqueta | Actuador | Ubicación | Función | Mando |
| --- | --- | --- | --- | --- |
| P-101 | Motor de bomba centrífuga con variador | Recepción | Transfiere la leche a T-301 | EtherNet/IP |
| M-201 | Motor del tornillo dosificador con variador | DS-201 | Dosifica azúcar: grueso y afine | EtherNet/IP |
| M-202 | Motor del microdosificador | DS-202 | Dosifica estabilizante | EtherNet/IP |
| P-203 / P-204 | Bombas peristálticas | Dosificación | Dosifican saborizante y colorante | Pulsos, 24 V DC |
| M-206 | Motor del tornillo dosificador | DS-206 | Dosifica la leche en polvo | EtherNet/IP |
| TV-301 | Válvula de control de vapor | Chaqueta de T-301 | Calienta en precalentamiento y pasteurización | 4–20 mA |
| TV-302 | Válvula de control de agua fría | Chaqueta de T-301 | Enfría hasta la temperatura de inoculación | 4–20 mA |
| M-301 | Motor del agitador con variador | T-301 | Mezcla, mantiene homogénea la temperatura y rompe el coágulo | EtherNet/IP |
| XV-301 | Válvula de fondo de asiento sanitario | T-301 | Descarga el tanque de proceso | Neumático, 24 V DC |
| M-302 | Motor del homogeneizador con variador | H-301 | Impulsa la mezcla a alta presión | EtherNet/IP |
| XV-302 | Válvula de tres vías sanitaria | Descarga de T-301 | Dirige la mezcla al homogeneizador o a la transferencia | Neumático, 24 V DC |
| P-301 | Bomba de lóbulos con variador | Transferencia | Lleva el yogur al enfriador y al tanque pulmón | EtherNet/IP |
| TV-303 | Válvula de control de agua helada | E-301 | Regula la temperatura de salida del yogur | 4–20 mA |
| XV-401 / XV-402 | Válvulas de derivación sanitarias | Salida de T-302 | Dirigen el producto a la empacadora de bolsas o a la llenadora de vasos | Neumático, 24 V DC |
| P-403 | Bomba dosificadora de fruta | Antes de LL-402 | Incorpora la fruta en proporción al caudal de yogur | EtherNet/IP |
| XY-401 / XY-402 | Expulsores neumáticos | CK-401 y CK-402 | Retiran las unidades fuera de peso | 24 V DC |
| M-401 / M-402 / M-501 | Motores de bandas con variador | CV-401, CV-402 y CV-501 | Transportan el producto | EtherNet/IP |
| R-501 | Robot industrial con herramienta de vacío | Celda de paletizado | Encanasta, encajona y paletiza | EtherNet/IP |
| XV-901… | Válvulas de ruta de CIP | CIP-901 | Configuran los circuitos de limpieza | Neumático, 24 V DC |

### 6.2 Criterios de selección

- Válvulas de control TV-301, TV-302 y TV-303 de globo con posicionador electroneumático; TV-301 cierra al perder el aire o la señal, para que una falla nunca deje vapor entrando a la chaqueta.
- Válvulas de producto de asiento sanitario con cabezal de control y finales de carrera, para confirmar al PLC la posición real antes de mover producto.
- La separación entre la ruta de producto y la de CIP se hace con válvulas de doble asiento, de modo que el detergente no pueda llegar al producto.
- Variadores de frecuencia en todos los motores que cambian de velocidad con la fase o la receta: bombas, agitador, homogeneizador, dosificadores y bandas.

## 7. Variables de proceso

| Variable | Consigna o límite | Medición | Acción de control | Importancia |
| --- | --- | --- | --- | --- |
| Calidad de la leche cruda | Acidez, pH, densidad y sólidos en especificación | Laboratorio, por cantina | Aceptar o rechazar la cantina | Inocuidad y aptitud para fermentar |
| Cantidad de leche del lote | 480–550 L | WT-101 y FT-101 | Escala la fórmula de la receta | Base de la dosificación |
| Cantidad de cada insumo | Fórmula de la receta, ± 1 % | WT-201, WT-202, FQ-203, FQ-204, WT-205, WT-206 | Dosificación automática con corte por peso | Uniformidad entre lotes |
| Presión de homogeneización | 150–200 bar a 60–65 °C | PT-302 y TT-301 | Consigna del variador de M-302; alarma por baja presión | Estabilidad y textura del producto |
| Temperatura de precalentamiento | 25 °C | TT-301 | TIC-301 sobre TV-301 | Disolución del azúcar |
| Temperatura y tiempo de pasteurización | 85–90 °C durante 5 a 10 min | TT-301, con registro | TIC-301 sobre TV-301; temporizador de sostenimiento | Punto crítico de control |
| Temperatura de inoculación | 42–45 °C | TT-301 | TIC-301 sobre TV-302 | Viabilidad del cultivo |
| Temperatura de incubación | 41–45 °C (consigna de 43 °C) | TT-301 | TIC-301 sobre TV-301 y TV-302 | Velocidad de fermentación |
| pH al final de la incubación | pH 4,4–4,6 (acidez de 80–90 °Th) | AT-301 | Termina la fase de incubación e inicia el enfriamiento | Calidad del producto |
| Temperatura de salida del enfriador | 15–20 °C | TT-302 | TIC-302 sobre TV-303 | Detiene la fermentación |
| Velocidad de agitación | Según la fase y la referencia | ST-301 | Consigna del variador de M-301 | Textura del producto |
| Nivel del tanque pulmón | Mínimo y máximo | LT-302 | Permite o detiene el envasado y la transferencia | Continuidad del envasado |
| Proporción de fruta | 8 % o 12 % | Velocidad de LL-402 y caudal de P-403 | Control de relación | Cumplimiento de la receta |
| Peso de la unidad | 195–205, 146–154 o 293–307 ml | WT-401 y WT-402 | Rechazo automático; ajuste de la dosis | Requisito de calidad y de ley |
| Temperatura del cuarto frío | 4 °C | TT-501 | Alarma por desviación | Cadena de frío |

## 8. Estrategia de control, lazos, enclavamientos y seguridad

### 8.1 Estrategia de control

La línea se controla con dos capas, ambas en el PLC-01:

- **Control secuencial por fases (ISA-88).** Ejecuta el procedimiento de la receta: abre y cierra rutas, arranca y detiene equipos, cambia consignas por fase y verifica las condiciones de fin. No es un lazo de control, sino una máquina de estados por fase (en espera, en ejecución, en pausa, completa y abortada).
- **Control regulatorio con PID.** Mantiene cada variable continua en su consigna. Todos los lazos son PID o PI, algunos con mejoras clásicas: rango dividido, prealimentación, control de relación y dosificación en dos velocidades.

La propuesta no usa control avanzado. En control de procesos, control avanzado (APC) es el que usa un modelo matemático del proceso para predecir su comportamiento y optimizar varias variables a la vez con restricciones, como el control predictivo por modelo (MPC); también se incluyen el control difuso y el control adaptativo. Las mejoras clásicas sobre el PID (rango dividido, prealimentación, relación y cascada) a veces se llaman control regulatorio avanzado, pero siguen siendo PID y son las que usa esta línea.

| Criterio | Control regulatorio PID (el que se usa) | Control avanzado tipo MPC (no se usa) |
| --- | --- | --- |
| Cómo decide | Corrige el error entre la medición y la consigna de una variable | Predice con un modelo varias variables y optimiza sus acciones con restricciones |
| Qué necesita | Un instrumento, un actuador y una sintonía | Un modelo identificado del proceso, software especializado y personal que lo mantenga |
| Dónde conviene | Variables con un actuador dominante y poca interacción entre lazos | Procesos continuos con muchas variables acopladas, tiempos muertos largos o restricciones económicas |
| Quién lo mantiene en La Hacienda | El técnico de primer nivel, con soporte de Cremia | Solo un especialista |

El PID es suficiente en esta línea por cuatro razones:

1. **Pocas variables acopladas.** Cada lazo tiene una variable controlada y un actuador dominante: la temperatura del tanque con la chaqueta, la salida del intercambiador con el agua helada, la fruta con su bomba. No hay interacción fuerte que obligue a un controlador multivariable.
2. **Dinámicas lentas y conocidas.** El calentamiento de 600 kg en la chaqueta tiene constantes de tiempo de minutos y la incubación dura horas; un PID bien sintonizado mantiene la pasteurización entre 85 y 90 °C y la inoculación entre 42 y 45 °C.
3. **El proceso es por lotes.** El desempeño depende sobre todo de la secuencia correcta de fases y de los enclavamientos, no de optimizar en continuo.
4. **Costo y mantenimiento.** Un MPC exige identificar el modelo, licenciar el software y tener personal especializado, un costo que no se justifica en una planta de cinco operarios y que el personal de la planta no podría mantener.

Un control avanzado solo se justificaría si la línea cambiara a pasteurización continua en intercambiador (HTST) con varias temperaturas acopladas, o si se quisiera optimizar en conjunto el consumo de la caldera y del enfriador. Queda como posible mejora de la etapa de análisis de la hoja de ruta, no dentro del alcance.

| Lazo | Proceso | Estrategia | Por qué esa estrategia |
| --- | --- | --- | --- |
| TIC-301 | Precalentamiento, homogeneización, pasteurización, enfriamiento a inoculación e incubación en T-301 | PID con rango dividido sobre vapor (TV-301) y agua fría (TV-302) | Un solo controlador mueve dos actuadores opuestos sin que se abran al tiempo |
| TIC-302 | Salida del intercambiador E-301 | PID con prealimentación del caudal de P-301 | El caudal es la perturbación principal y se mide antes de que cambie la temperatura |
| FFC-403 | Dosificación de fruta | Control de relación sobre la velocidad de la llenadora | La fruta debe seguir al yogur en proporción fija (8 % o 12 %) |
| PIC-302 | Presión del homogeneizador | PI sobre el variador de M-302 | Una sola variable con respuesta rápida |
| WIC-201/202/206 | Dosificación de azúcar, estabilizante y leche en polvo | Dos velocidades con corte anticipado | El material en vuelo se compensa sin modelo dinámico |
| LIC-302 | Nivel del tanque pulmón | Control por bandas | Basta con mantener el nivel entre un mínimo y un máximo |
| SIC-301 | Velocidad del agitador | Consigna de velocidad del variador | La receta define la velocidad de cada fase |

### 8.2 Lazos de control

| Lazo | Variable medida | Elemento final | Estrategia | Observación |
| --- | --- | --- | --- | --- |
| TIC-301 | TT-301 | TV-301 (vapor) y TV-302 (agua fría) | PID con rango dividido: de 0 a 50 % de salida abre el agua y de 50 a 100 % el vapor, con zona muerta en el centro | La consigna cambia por fase: 25, 62, 87 y 43 °C |
| TIC-302 | TT-302 | TV-303 (agua helada) | PID con prealimentación del caudal de P-301 | Mantiene 15–20 °C aunque cambie el caudal |
| PIC-302 | PT-302 | Variador de M-302 | PI sobre la velocidad del homogeneizador | Limita la rampa de arranque para proteger la bomba |
| FFC-403 | Velocidad de LL-402 (vasos/min × dosis) | Variador de P-403 | Control de relación: caudal de fruta = 8 % o 12 % del caudal de yogur que entra a la llenadora | Relación tomada de la receta de control |
| LIC-302 | LT-302 | Variador de P-301 | Control de nivel por bandas: transfiere hasta el nivel alto y habilita el envasado sobre el nivel mínimo | Evita que la llenadora trabaje en vacío |
| WIC-201/202/206 | WT-201, WT-202 y WT-206 | Variadores de M-201, M-202 y M-206 | Dosificación en dos velocidades (grueso y afine) con corte anticipado por la caída del material en vuelo | Precisión de ± 1 % de la fórmula |
| SIC-301 | ST-301 | Variador de M-301 | Consigna de velocidad por fase y por referencia | Detenido durante la incubación |

### 8.3 Enclavamientos

| Enclavamiento | Condición | Acción |
| --- | --- | --- |
| Pasteurización incompleta | TT-301 por debajo de 85 °C durante el sostenimiento | Reinicia el temporizador; bloquea el paso a enfriamiento |
| Inoculación caliente | TT-301 mayor de 46 °C | No permite adicionar el cultivo |
| Fermentación sin terminar | pH mayor de 4,6 | No permite iniciar la ruptura del coágulo ni la transferencia |
| Rutas incompatibles | XV-401 y XV-402 abiertas a la vez, o ruta de CIP abierta con producto en la línea | Cierra las válvulas de producto y detiene P-301 |
| Tanque vacío | LT-301 en nivel bajo | Detiene P-301 y el agitador M-301 |
| Tanque pulmón lleno | LT-302 en nivel alto | Detiene P-301 |
| Sobrepresión del homogeneizador | PT-302 mayor de 220 bar | Detiene M-302; la válvula de alivio protege el equipo |
| Agua helada caliente | TT-901 mayor de 5 °C | No permite iniciar la transferencia por E-301 |
| Celda robotizada abierta | Puerta del vallado abierta o cortina de luz interrumpida | Parada segura del robot R-501 |
| Paro de emergencia | Cualquier pulsador de emergencia | Detiene motores y cierra vapor; el lote queda en pausa |

### 8.4 Seguridad de personas y máquinas

- La celda R-501 cumple ISO 10218 para robots industriales: vallado perimetral, puertas con interruptor de seguridad, cortinas de luz en la entrada y salida de estibas, y funciones de seguridad con nivel de desempeño PL d según ISO 13849.
- Las líneas de vapor tienen aislamiento térmico, válvula de seguridad y trampa de vapor; el mando de TV-301 se bloquea mientras la tapa del tanque está abierta.
- El homogeneizador trabaja a 200 bar: tiene válvula de alivio, guardas sobre las partes móviles y bloqueo de arranque sin flujo de entrada.
- El CIP maneja soda y ácido calientes: la estación tiene bandeja de contención, ducha de emergencia y enclavamiento que impide abrir tapas de tanques durante el lavado.

## 9. Comunicaciones

### 9.1 Arquitectura por niveles

| Nivel (ISA-95) | Elementos | Medio y protocolo | Información que circula |
| --- | --- | --- | --- |
| 0: proceso | Equipos de las unidades U1 a U8 | — | — |
| 1: instrumentación y accionamientos | Transmisores, válvulas de control, sensores discretos, E/S remotas y variadores | 4–20 mA, IO-Link y señales de 24 V DC hacia las E/S remotas; EtherNet/IP hacia el PLC | Mediciones, estados y mandos |
| 2: control | PLC-01 (CompactLogix 5380) y las máquinas con controlador propio: controladoras de peso, codificadores, llenadora y empacadora; el robot se suma en la etapa posterior | EtherNet/IP en anillo DLR, que se recupera en menos de 3 ms si se corta un cable | Consignas, estados de equipo, conteos, pesos y alarmas |
| 2: supervisión | SCADA en Ignition (Perspective y Tag Historian), HMI-01 en preparación y HMI-02 en envasado | OPC UA cifrado entre el PLC y el SCADA | Variables de proceso, alarmas, tendencias, receta activa y estado del lote |
| 3: gestión de operaciones | MES con módulos Sepasoft sobre el mismo servidor Ignition | Etiquetas del SCADA dentro del mismo servidor; base de datos Microsoft SQL Server | Órdenes de producción, recetas de control, registro de lote, paradas e indicadores |
| 4: gestión empresarial | ERP Odoo en la nube | Mensajes B2MML de ISA-95 traducidos a la API de Odoo en la pasarela de la zona desmilitarizada | Plan de producción, inventarios, consumos y producción terminada |

ISA-95 ubica el control automático en el nivel 2, junto con la supervisión; el modelo Purdue lo llama control básico y lo dibuja en el nivel 1. Este documento y el de arquitectura siguen la definición de ISA-95: el PLC está en el nivel 2 y el nivel 1 corresponde a la medición y la actuación sobre el proceso. La red de planta se separa de la red administrativa con una zona desmilitarizada entre dos cortafuegos. El detalle de la arquitectura y del flujo de información entre OT e IT está en el documento de arquitectura ISA-95.

### 9.2 Lista de entradas y salidas de la ingeniería básica

| Tipo de señal | Cantidad | Elementos |
| --- | --- | --- |
| Entradas analógicas de 4–20 mA | 14 | WT-101, FT-101, WT-201, WT-202, WT-206, TT-301 (dos elementos), AT-301, PT-302, TT-302, TT-303, TT-501, TT-901 y CT-901 |
| Salidas analógicas de 4–20 mA | 3 | TV-301, TV-302 y TV-303 |
| Entradas de pulsos rápidos | 3 | FT-101, FQ-203 y FQ-204 |
| Puertos IO-Link | 3 | LT-301, PT-301 y LT-302 |
| Entradas digitales | 16 | ZS-401, ZS-402, ZS-403 y ZS-501 (4); dos finales de carrera por válvula en XV-301, XV-302, XV-401 y XV-402 (8); puerta de la celda (1); paros de emergencia en preparación, envasado y celda (3) |
| Salidas digitales | 16 | XV-301, XV-302, XV-401, XV-402, XY-401, XY-402, P-203, P-204 y válvulas de ruta de CIP |
| Nodos EtherNet/IP | 20 | 11 variadores, CK-401, CK-402, CD-401, CD-402, LL-402, EMP-401, R-501, BL-205 y CIP-901 |
| **Total** | **55 señales cableadas o IO-Link y 20 nodos de red** | 69 señales con la reserva del 20 % redondeada por tipo |

Se deja una reserva del 20 % en cada tipo de señal para ampliaciones. Con estas cantidades un CompactLogix 5380 con dos estaciones de E/S remotas (preparación y envasado) cubre la línea. La red de control es un anillo DLR de EtherNet/IP con un conmutador administrable de celda (Stratix 5700), de modo que el corte de un cable no detiene el proceso; desde ese conmutador la red de supervisión es en estrella. Un ControlLogix solo se justificaría si el cliente exigiera redundancia de controlador.

## 10. Calibración y mantenimiento de la instrumentación

| Instrumento | Frecuencia de verificación | Método |
| --- | --- | --- |
| TT-301 (punto crítico) | Mensual, y comparación continua de sus dos elementos | Termómetro patrón a 85 °C |
| AT-301 | Diaria antes del primer lote; calibración semanal | Soluciones tampón de pH 4 y pH 7 |
| Celdas de carga de dosificación | Mensual | Pesas patrón |
| Controladoras de peso CK-401 y CK-402 | Al arranque de cada turno | Unidades patrón dentro y fuera de tolerancia |
| FT-101 | Semestral | Comparación con el peso de WT-101 |
| Transmisores de presión y nivel | Semestral | Patrón de presión |
| CT-901 | Mensual | Solución de conductividad conocida |
| Juntas de E-301 y sellos de bombas | Según horas de trabajo del fabricante | Inspección y cambio programado |

Las verificaciones quedan registradas en el MES, y el lote no se libera si un instrumento de punto crítico tiene la calibración vencida.

## 11. Resumen

| Concepto | Existente | Nuevo | Total |
| --- | --- | --- | --- |
| Equipos principales | 9 | 17 | 26 |
| Sensores | 0 | 23 | 23 |
| Actuadores | 1 | 18 | 19 |

La línea actual no tiene instrumentación conectada: las mediciones se hacen con instrumentos manuales (termómetro, acidómetro y gramera). El único actuador que se conserva es el agitador del tanque de proceso; la bomba de leche se reemplaza por una de mayor caudal. En la columna de nuevos se cuentan los reemplazos. Las cifras corresponden al diseño completo: el proyecto de 16 semanas compra 25 de los 26 equipos, porque la celda R-501, con su sensor ZS-501 y su robot, queda para una etapa posterior; la lista de E/S ya reserva sus señales. Los equipos e instrumentos que se instalan en pares iguales, uno por máquina de envasado o por bomba de aditivo (por ejemplo, WT-401 y WT-402), se cuentan como una sola entrada del inventario.

## Referencias

- ANSI/ISA-5.1-2009. Instrumentation Symbols and Identification. International Society of Automation.
- ANSI/ISA-18.2-2016. Management of Alarm Systems for the Process Industries. International Society of Automation.
- ANSI/ISA-88.00.01-2010. Batch Control Part 1: Models and Terminology. International Society of Automation.
- ANSI/ISA-95.00.01. Enterprise-Control System Integration. International Society of Automation.
- Grimaldo, G., Moreno, D. y Salamanca, M. (2015). Medición del trabajo de una línea de producción de yogurt – Empresa La Hacienda. Revista I3+, 2(2), 62–81.
- ISO 10218-2:2011. Robots and robotic devices — Safety requirements for industrial robots — Part 2: Robot systems and integration.
- ISO 13849-1:2015. Safety of machinery — Safety-related parts of control systems.
- Resolución 2674 de 2013. Requisitos sanitarios para fabricar, procesar, envasar y comercializar alimentos. Ministerio de Salud y Protección Social.
- Tecnilac Willgo. Soluciones y equipos para la fabricación de yogurt.
- Tetra Pak (2015). Dairy Processing Handbook, capítulo 11: Fermented milk products.
