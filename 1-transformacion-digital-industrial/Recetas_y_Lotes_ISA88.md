# Recetas y lotes de la línea de yogur

**Estructura de recetas, fórmulas, parámetros y lotes de producción según ISA-88**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Módulo 1 · Transformación Digital Industrial

## 1. Alcance

Este documento estructura las recetas y los lotes de la línea de yogur de la planta del cliente según ANSI/ISA-88. Define las tres referencias de producto, su especificación, la fórmula y el balance de materia de cada una, los parámetros de procedimiento que se mantienen y los que cambian con la propuesta, la estructura de recetas general, de sitio, maestra y de control, y la forma de identificar, programar, controlar, liberar y registrar cada lote.

La base es el estudio de tiempos de la empresa La Hacienda Productos Alimenticios (Grimaldo, Moreno y Salamanca, 2015): una línea que procesa un lote diario de 550 L de leche y produce 3.052 bolsas de yogur de 200 ml con cuatro operarios, en 601,3 min de proceso y un enfriamiento natural durante la noche. Sobre esa base se incorporan las decisiones de diseño de la propuesta: estandarización de sólidos con leche en polvo, homogeneización, control automático de temperatura y pH, una segunda presentación en vaso con fruta, codificado de lote y fecha, y un segundo lote diario.

Las etiquetas de equipos e instrumentos son las del documento de equipos, sensores, actuadores, variables y comunicaciones. Las unidades (U1 a U8) y los procedimientos de unidad (PU1 a PU6) son los del modelo físico y procedimental ISA-88 de la línea.

## 2. Marco de referencia

### 2.1 ANSI/ISA-88 y la gestión de recetas

La norma ANSI/ISA-88 separa tres cosas que en la planta actual están mezcladas en la experiencia del operario: el equipo (modelo físico), la secuencia de pasos (modelo procedimental) y los datos que hacen distinto a cada producto (la receta). Esta separación permite fabricar varias referencias con los mismos equipos y el mismo programa de control, cambiando solo la receta.

| Concepto ISA-88 | Definición | Aplicación en la línea de yogur |
| --- | --- | --- |
| Receta general | Define el producto sin referirse a equipos ni a un sitio | Yogur batido con 1 % de leche en polvo y 12 % de azúcar, fermentado a 43 °C (41–45 °C) hasta pH 4,4–4,6 |
| Receta de sitio | Adapta la receta general a las materias primas, la normativa y el idioma del sitio | Leche de cantinas de la zona de Guasca, insumos homologados y requisitos del INVIMA |
| Receta maestra | Receta de sitio ligada a los equipos de una célula de proceso; es la plantilla de los lotes | RM-YB-200, RM-YV-150 y RM-YV-300, ligadas a T-301, H-301, E-301 y a la ruta U6 o U7 |
| Receta de control | Copia de la receta maestra para un lote concreto, con su tamaño real y sus equipos asignados | YV150-20270510-2: 520 L de leche, fórmula escalada, LL-402 asignada |
| Fórmula | Lista de entradas, parámetros de proceso y salidas esperadas | Insumos por lote, consignas de fase y unidades esperadas |
| Requisitos de equipo | Clases o unidades que puede usar la receta | Tanque de proceso con chaqueta, homogeneizador y máquina de la presentación |
| Procedimiento | Secuencia de procedimientos de unidad, operaciones y fases | PU1 a PU6 del modelo procedimental |

La parte 2 de la norma (ANSI/ISA-88.00.02) define las estructuras de datos para guardar recetas y registros de lote; el MES de la propuesta usa esas estructuras para que las recetas se puedan versionar, aprobar e intercambiar con el ERP sin reescribir el programa del PLC.

### 2.2 Requisitos sanitarios y de identidad del producto

| Norma | Exigencia que afecta la receta o el lote | Cómo se atiende |
| --- | --- | --- |
| Decreto 616 de 2006 | Requisitos de la leche cruda para consumo humano: temperatura, densidad, acidez, grasa, sólidos, prueba de alcohol y ausencia de antibióticos | Análisis por cantina en LAB-101 y registro en HMI-01 antes de aceptar la leche |
| Resolución 2310 de 1986 | Define el yogur como leche higienizada fermentada por Streptococcus thermophilus y Lactobacillus delbrueckii subsp. bulgaricus, con o sin fruta, edulcorantes y estabilizantes autorizados | Cultivo termófilo DVS en las tres referencias; aditivos declarados en la fórmula |
| NTC 805 | Requisitos fisicoquímicos de las leches fermentadas: grasa, proteína láctea, sólidos no grasos, acidez y recuento de bacterias lácticas | Especificación de la sección 3.2 y verificación por lote |
| Resolución 2674 de 2013 | Buenas prácticas de manufactura: diseño sanitario, limpieza, control de procesos y registros | Equipos en acero inoxidable AISI 316L, CIP con registro y registro electrónico de lote |
| Resolución 1407 de 2022 | Criterios microbiológicos de los alimentos, con planes de muestreo por clases | Plan de muestreo de la sección 8.3 para liberar el lote |
| Resolución 5109 de 2005 | Rotulado: número de lote y fecha de vencimiento legibles en cada envase | Codificadores CD-401 y CD-402 con los datos que envía el MES |
| Resolución 810 de 2021 y Resolución 2492 de 2022 | Etiquetado nutricional y sellos frontales de advertencia | Las tres referencias llevan sello de exceso en azúcares por el azúcar añadido; la fórmula y el rótulo se revisan juntos en cada cambio de versión |

## 3. Referencias de producto

### 3.1 Fichas de producto

La línea produce tres referencias. Comparten la base de yogur y los equipos de preparación (U1 a U5), y se diferencian en formulación, presentación, equipo de envasado, velocidad, inspección y empaque secundario.

| Atributo | YB-200 | YV-150 | YV-300 |
| --- | --- | --- | --- |
| Producto | Yogur saborizado bebible | Yogur con fruta | Yogur con trozos de fruta |
| Sabor | Fresa | Mora | Melocotón |
| Presentación | Bolsa de 200 ml | Vaso de 150 ml | Vaso de 300 ml |
| Estado | Producto actual de la planta | Nueva referencia | Nueva referencia |
| Equipo de envasado | Empacadora de bolsas EMP-401 (existente) | Llenadora-selladora de vasos LL-402 (nueva) | Llenadora-selladora de vasos LL-402 (nueva) |
| Fruta | No | Preparado de mora, 8 % | Trozos de melocotón, 12 % |
| Empaque secundario | Canasta de 120 bolsas | Caja de 24 vasos | Caja de 20 vasos |
| Inspección | Peso del 100 % en línea y hermeticidad del sellado por muestreo | Peso del 100 % en línea y verificación de tapa | Peso del 100 % en línea y verificación de tapa |
| Unidades por lote de 550 L | 3.079 bolsas | 4.369 vasos | 2.260 vasos |
| Vida útil asignada | 21 días a 4 °C | 21 días a 4 °C | 21 días a 4 °C |
| Receta maestra | RM-YB-200 | RM-YV-150 | RM-YV-300 |

Los dos vasos tienen el mismo diámetro de boca y cambian en altura, de modo que una sola llenadora-selladora atiende ambas referencias con un cambio de dosis y de altura. La vida útil se asigna en 21 días para la liberación inicial y puede extenderse hasta 28 días a 4 °C con estudios de estabilidad, que es el rango de referencia para yogur batido refrigerado.

### 3.2 Especificación fisicoquímica

| Parámetro | YB-200 | YV-150 | YV-300 | Verificación |
| --- | --- | --- | --- | --- |
| Grasa láctea | 2,9–3,1 % | 2,7–2,9 % | 2,6–2,8 % | Laboratorio, una muestra por lote |
| Proteína láctea | ≥ 2,9 % | ≥ 2,8 % | ≥ 2,7 % | Laboratorio, una muestra por lote |
| Sólidos lácteos no grasos sobre la fracción láctea | ≥ 9,2 % | ≥ 9,4 % | ≥ 9,4 % | Cálculo de la fórmula y análisis de la mezcla |
| Azúcar añadido sobre el producto | 11,7 % | 9,1 % | 7,9 % | Dosificación registrada por WT-201 |
| pH al final de la incubación | 4,4–4,6 | 4,4–4,6 | 4,4–4,6 | AT-301, en línea |
| Acidez titulable | 80–90 °Th | 80–90 °Th | 80–90 °Th | Laboratorio, confirmación por lote |
| Temperatura de envasado | 15–20 °C | 15–20 °C | 15–20 °C | TT-302 y TT-303 |
| Contenido por unidad | 195–205 ml | 146–154 ml | 293–307 ml | WT-401 o WT-402, el 100 % |
| Temperatura de almacenamiento | 2–6 °C | 2–6 °C | 2–6 °C | TT-501 |

Todos los valores de proteína quedan por encima del mínimo de 2,6 % de la NTC 805 para leches fermentadas, y los de grasa corresponden a un yogur entero. Las referencias en vaso tienen menos grasa y proteína por dilución con la fruta, no por cambio de la base.

### 3.3 Supuestos de composición

La composición de la tabla anterior es un cálculo a partir de la fórmula, con estos supuestos: leche cruda con 3,4 % de grasa, 3,1 % de proteína y 8,5 % de sólidos no grasos; leche en polvo descremada con 35 % de proteína y 96 % de sólidos; preparado de fruta con cerca de 35 % de sólidos. Con esos valores los sólidos totales del producto quedan entre 22,6 y 22,9 % en las tres referencias, lo que da una textura de yogur batido. Los valores se confirman con los análisis de la leche que recibe la planta durante la puesta en marcha.

## 4. Fórmula por lote

### 4.1 Fórmula de las tres referencias

Tamaño de lote nominal: 550 L de leche cruda (566,5 kg con densidad de 1,030), que es la capacidad útil de la línea. La fórmula de YB-200 parte de la que usa hoy la planta, que produce 3.052 bolsas por lote, y agrega leche en polvo. Las de YV-150 y YV-300 reducen el azúcar de la base, porque el preparado de fruta ya aporta azúcar, y duplican el estabilizante para lograr la textura firme de un yogur en vaso.

| Insumo | YB-200 | YV-150 | YV-300 |
| --- | --- | --- | --- |
| Leche cruda | 550 L (566,5 kg) | 550 L (566,5 kg) | 550 L (566,5 kg) |
| Azúcar | 75,7 kg (12 %) | 63,1 kg (10 %) | 56,7 kg (9 %) |
| Estabilizante | 0,206 kg | 0,412 kg | 0,412 kg |
| Leche en polvo descremada | 5,7 kg (1 %) | 7,1 kg (1,25 %) | 7,1 kg (1,25 %) |
| Cultivo láctico | 7 g | 7 g | 7 g |
| Saborizante | 0,206 kg (fresa) | 0,206 kg (mora) | 0,206 kg (melocotón) |
| Colorante | 0,110 kg | 0,090 kg | 0,060 kg |
| Preparado de fruta | — | 57,2 kg (8 % del producto) | 88,8 kg (12 % del producto) |
| Yogur obtenido | 615,9 L | ≈ 656 L | ≈ 679 L |
| Unidades por lote | 3.079 bolsas | ≈ 4.369 vasos | ≈ 2.260 vasos |
| Empaque secundario | 26 canastas | 183 cajas | 113 cajas |
| Material de envase | Rollo de película para 3.079 bolsas | 4.369 vasos y tapas | 2.260 vasos y tapas |

El porcentaje de azúcar se expresa sobre la masa de yogur base. El de fruta, sobre el producto final. La leche en polvo se expresa sobre la leche cruda; su aporte al volumen, cercano al 1 %, ya está incluido en las unidades por lote. Las cantidades de YV-150 y YV-300 son estimadas y se ajustan con pruebas de formulación.

### 4.2 Balance de materia

El balance compara la masa de insumos con la masa envasada, calculada con las unidades por lote y una densidad de 1,05 kg/L para el yogur batido.

| Concepto | YB-200 | YV-150 | YV-300 |
| --- | --- | --- | --- |
| Leche cruda | 566,50 kg | 566,50 kg | 566,50 kg |
| Azúcar | 75,70 kg | 63,10 kg | 56,70 kg |
| Leche en polvo | 5,70 kg | 7,10 kg | 7,10 kg |
| Estabilizante, cultivo, saborizante y colorante | 0,53 kg | 0,72 kg | 0,69 kg |
| Preparado de fruta | — | 57,20 kg | 88,80 kg |
| **Total de entradas** | **648,4 kg** | **694,6 kg** | **719,8 kg** |
| Volumen envasado | 615,8 L | 655,4 L | 678,0 L |
| Masa envasada (1,05 kg/L) | 646,6 kg | 688,2 kg | 711,9 kg |
| Pérdidas de proceso | 1,8 kg (0,3 %) | 6,4 kg (0,9 %) | 7,9 kg (1,1 %) |
| Rendimiento | 1,12 L de yogur por L de leche | 1,19 L por L | 1,23 L por L |

Las pérdidas corresponden a evaporación durante la pasteurización, producto retenido en paredes, tuberías, filtro e intercambiador, y llenado inicial de la máquina. Son mayores en los vasos porque el preparado de fruta pasa por la bomba P-403 y el mezclador MX-403, que retienen producto al final del lote. El producto rechazado por peso no se cuenta aquí: se registra aparte como producto no conforme (sección 8.4).

### 4.3 Función y especificación de los insumos

| Insumo | Función en el producto | Especificación de compra | Almacenamiento y control |
| --- | --- | --- | --- |
| Leche cruda | Base del yogur; aporta grasa, proteína y lactosa | Decreto 616 de 2006; acidez de 14 a 17 °D, densidad de 1,030 a 1,033 g/mL, prueba de alcohol negativa y sin antibióticos | Análisis por cantina; se procesa el mismo día |
| Leche en polvo descremada | Sube los sólidos no grasos y la proteína; da firmeza al gel y reduce la separación de suero | Grado alimentario, humedad ≤ 4 %, proteína ≥ 34 % | Bodega seca; tolva de DS-206 cerrada; lote registrado |
| Azúcar | Endulza y aporta sólidos | Azúcar refinado, grado alimentario | Bodega seca; tolva de DS-201 |
| Estabilizante | Retiene agua y mantiene la textura durante la vida útil | Hidrocoloide autorizado por la Resolución 2310 de 1986 | Envase cerrado; microdosificador DS-202 |
| Cultivo láctico | Fermenta la lactosa a ácido láctico y forma el gel | Cultivo DVS liofilizado de S. thermophilus y L. bulgaricus | Congelador a −18 °C; pesaje y lectura del lote en BL-205 |
| Saborizante y colorante | Dan el sabor y el color de la referencia | Autorizados para derivados lácteos | Bidones con bomba P-203 y P-204 |
| Preparado o trozos de fruta | Diferencian las referencias en vaso | Preparado pasteurizado de mora y trozos de melocotón en almíbar, listos para dosificar en frío | Refrigerado a 4 °C; bomba P-403 |
| Material de envase | Contiene y protege el producto | Película para bolsa; vasos y tapas termosellables aptos para alimentos | Bodega de envases; lote registrado por orden |

### 4.4 Escalado de la fórmula

Cuando la leche disponible es menor de 550 L, el MES escala cada insumo en proporción a la leche cargada, medida por WT-101 y FT-101:

cantidad del insumo = cantidad de la fórmula × (litros reales ÷ 550)

Por ejemplo, un lote de YB-200 con 480 L de leche lleva 66,1 kg de azúcar y 4,97 kg de leche en polvo, y produce unas 2.687 bolsas. Los parámetros de proceso (temperaturas, tiempos y pH) no se escalan. El rango de operación es de 480 a 550 L; un lote menor exige verificar que el electrodo de pH AT-301 y la hélice del agitador queden sumergidos.

## 5. Parámetros de procedimiento

### 5.1 Parámetros por fase

La tabla sigue los procedimientos de unidad del modelo procedimental. El tiempo actual es el tiempo estándar medido en el caso de estudio para un lote de 550 L; el propuesto es la estimación de diseño, que se valida con la simulación y la puesta en marcha.

| Procedimiento de unidad y fase | Consigna | Condición de fin | Tiempo actual (min) | Tiempo propuesto (min) |
| --- | --- | --- | --- | --- |
| PU1 · Recibir y analizar la leche | Acidez, pH, densidad y sólidos por cantina | Leche aprobada por laboratorio | 19,6 | 19,6 |
| PU1 · Cargar el tanque de proceso | 550 L a 3 m³/h | Volumen de receta en T-301 (LT-301 y FT-101) | 28,4 | 12 |
| PU2 · Alistar y dosificar insumos | Cantidades de la fórmula, ± 1 % | Dosis completas (WT-201, WT-202, WT-206) | 10,2 | 2 |
| PU2 · Precalentar y disolver | 25 °C con agitación de 40–60 rpm | Temperatura alcanzada y azúcar disuelto | 13,9 | 12 |
| PU2 · Estandarizar y homogeneizar | Leche en polvo según la fórmula; 150–200 bar a 60–65 °C, en recirculación | Dos pasos del volumen del lote (PT-302 en rango) | No se hace | En paralelo con el calentamiento |
| PU2 · Pasteurizar | 85–90 °C, sostenimiento de 5 a 10 min | Tiempo de sostenimiento cumplido y curva registrada | 77,4 (sostenimiento de 15) | 60 |
| PU2 · Enfriar a inoculación | 43 °C (42–45 °C) | Temperatura estable durante 2 min | 26,2 | 15 |
| PU3 · Inocular | 7 g de cultivo; agitación de 5 min y parada | Lote del cultivo leído y peso verificado en BL-205 | Incluido en el anterior | Incluido en el anterior |
| PU3 · Incubar | 43 °C (41–45 °C), sin agitación | pH 4,4–4,6 en AT-301; máximo 300 min con alarma | 240 | 240 |
| PU4 · Romper el coágulo y saborizar | 30–40 rpm (bolsa) o 15–20 rpm (vaso); saborizante y colorante de la fórmula | Textura homogénea y dosis completas | 10,0 | 5 |
| PU4 · Enfriar y transferir | Salida de E-301 a 15–20 °C; P-301 a 1.500 L/h | T-301 vacío (LT-301) y producto en T-302 | 23,6, más la noche | 25 |
| PU5 · Envasar | Dosis, velocidad y codificado de la referencia | Tanque pulmón en nivel mínimo | 148,9 | 102 (YB-200), 97 (YV-150), 65 (YV-300) |
| PU6 · Empacar y almacenar | 120 bolsas, 24 o 20 vasos por empaque; cuarto frío a 4 °C | Lote completo en CF-501 | 2,9 | En paralelo con el envasado |
| Limpieza CIP | Enjuague o ciclo completo según el cambio | Conductividad de enjuague verificada con CT-901 | Manual, no medida | 15 o 40 |
| **Total por lote (YB-200)** | | | **601,3** | **≈ 493** |

La homogeneización se hace en recirculación por H-301 mientras la chaqueta calienta la mezcla entre 60 y 65 °C; a 1.500 L/h, dos pasos de los 600 L de mezcla toman unos 48 min, que se cubren dentro del calentamiento hacia la pasteurización.

### 5.2 Parámetros que cambian con la propuesta

| Fase | Situación actual | Propuesta |
| --- | --- | --- |
| Carga al tanque de proceso | 28 min con una bomba subdimensionada | 11 a 12 min con bomba sanitaria de 3 m³/h |
| Pesaje y adición de insumos | Manual, en dos cuartos | Dosificación automática por peso, ± 1 % de la fórmula |
| Sólidos de la leche | Sin ajuste | Leche en polvo descremada: 1 % en bolsa y 1,25 % en vaso |
| Homogeneización | No se hace | 150–200 bar a 60–65 °C, en recirculación durante el calentamiento previo a la pasteurización |
| Pasteurización | 85 °C con 15 min de sostenimiento; válvulas manuales | 85–90 °C con 5 a 10 min de sostenimiento y control automático; el tiempo final se valida con pruebas |
| Fin de la incubación | Muestra y acidómetro: 80–90 °Th | pH en línea: 4,4–4,6, equivalente a 80–90 °Th |
| Enfriamiento | Natural, durante la noche | Intercambiador de placas hasta 15–20 °C en unos 25 min, con agitación para romper el coágulo |
| Control de peso | Una de cada cinco bolsas, en gramera | 100 % de las unidades, en línea, con rechazo automático |
| Codificado | Sin codificado automático | Lote y fecha de vencimiento impresos en cada unidad, con los datos que envía el MES |
| Registro | Papel | Registro electrónico de lote en el MES |

Los valores de la propuesta siguen la referencia de proceso industrial del yogur: tratamiento térmico de 85–95 °C durante 5 a 10 minutos, que desnaturaliza la mayor parte de la β-lactoglobulina y da un gel más firme y con menos separación de suero; inoculación a 42–45 °C; pH final de 4,4 a 4,6, punto en el que la caseína coagula; y enfriamiento rápido para detener la fermentación.

### 5.3 Parámetros que cambian con la referencia

| Parámetro | YB-200 | YV-150 | YV-300 |
| --- | --- | --- | --- |
| Adición de fruta | No aplica | 8 %, dosificada en línea antes de la llenadora | 12 %, dosificada en línea antes de la llenadora |
| Leche en polvo | 1 % | 1,25 % | 1,25 % |
| Estabilizante | 0,206 kg | 0,412 kg | 0,412 kg |
| Agitación tras la incubación | 30–40 rpm (producto bebible) | 15–20 rpm (yogur de cuchara) | 15–20 rpm (yogur de cuchara) |
| Destino desde el tanque pulmón | Empacadora de bolsas (XV-401) | Llenadora de vasos (XV-402) | Llenadora de vasos (XV-402) |
| Volumen nominal | 200 ml | 150 ml | 300 ml |
| Tolerancia de llenado | 195–205 ml | 146–154 ml | 293–307 ml |
| Velocidad de envasado | 30 bolsas/min | 45 vasos/min | 35 vasos/min |
| Inspección | Peso del 100 %; hermeticidad por muestreo | Peso del 100 %; presencia y sellado de tapa (ZS-403) | Peso del 100 %; presencia y sellado de tapa (ZS-403) |
| Unidades por empaque | 120 por canasta | 24 por caja | 20 por caja |
| Patrón de estiba | Canastas apiladas | Patrón A | Patrón B |

Las velocidades de envasado son valores de diseño de la propuesta. La empacadora actual entrega 3.052 bolsas en 149 min, unas 20,5 bolsas/min, porque las paradas y el control de peso manual le quitan cerca de un tercio de su velocidad nominal.

### 5.4 Límites de alarma y acciones

| Variable | Límite | Instrumento | Acción automática | Acción del operador |
| --- | --- | --- | --- | --- |
| Temperatura de pasteurización | Baja: 85 °C | TT-301 | Reinicia el conteo del sostenimiento; el lote no avanza | Revisar la presión de vapor de CAL-901 |
| Temperatura de inoculación | Alta: 46 °C | TT-301 | Bloquea la inoculación | Esperar a que el lazo TIC-301 estabilice |
| Temperatura de incubación | ± 2 °C de la consigna | TT-301 | Alarma de prioridad media | Verificar TV-301 y TV-302 |
| Tiempo de incubación | 300 min sin llegar a pH 4,6 | AT-301 y temporizador | Alarma de prioridad alta | Confirmar con acidez de laboratorio; evaluar el cultivo |
| Presión de homogeneización | Menor de 150 bar | PT-302 | Prolonga la recirculación | Revisar H-301 |
| Salida del enfriador | Alta: 20 °C | TT-302 | Reduce el caudal de P-301 | Revisar el agua helada (TT-901) |
| Dosificación de insumos | Desviación mayor de 1 % | WT-201, WT-202, WT-206 | Detiene la fase y pide confirmación | Completar o justificar la dosis |
| Peso de la unidad | Fuera de tolerancia | WT-401 o WT-402 | Expulsa la unidad (XY-401 o XY-402) | Ajustar la dosis si los rechazos superan el 2 % en 10 min |
| Cuarto frío | Alta: 6 °C | TT-501 | Alarma de prioridad alta | Retener el producto y revisar el equipo de frío |

Las prioridades de alarma siguen ANSI/ISA-18.2: alta para lo que afecta la inocuidad, media para lo que afecta la calidad y baja para lo que afecta la eficiencia.

## 6. Estructura de recetas según ISA-88

### 6.1 Tipos de receta y responsables

| Tipo de receta | Contenido | Dónde se gestiona | Responsable |
| --- | --- | --- | --- |
| Receta general | Define cada producto sin referirse a equipos: ingredientes, proporciones y condiciones de proceso | Calidad y desarrollo de producto (ERP) | Jefatura de calidad |
| Receta de sitio | Adapta la receta general a la planta: insumos disponibles y normativa | Jefatura de producción | Jefatura de producción |
| Receta maestra | Una por referencia (RM-YB-200, RM-YV-150, RM-YV-300), ligada a los equipos de la línea | MES | Ingeniería de procesos |
| Receta de control | Copia de la receta maestra para un lote concreto, con el tamaño real y los equipos asignados | MES y PLC | Se genera al liberar la orden |

### 6.2 Contenido de la receta maestra

Cada receta maestra tiene cinco partes:

1. **Encabezado:** código, versión, producto, tamaño nominal y rango de lote, vida útil, fecha de aprobación y responsable.
2. **Fórmula:** insumos y cantidades de la sección 4, parámetros de proceso con su consigna, mínimo y máximo, y unidades esperadas.
3. **Requisitos de equipo:** tanque de proceso, homogeneizador, intercambiador, tanque pulmón y la máquina de envasado que corresponde a la presentación.
4. **Procedimiento:** procedimientos de unidad, operaciones y fases en el orden del modelo procedimental, con la condición de fin de cada fase.
5. **Otra información:** rótulo, empaque secundario, patrón de estiba, plan de muestreo y criterios de liberación.

### 6.3 Ejemplo: receta maestra RM-YV-150

| Parámetro | Fase | Consigna | Mínimo | Máximo | Unidad |
| --- | --- | --- | --- | --- | --- |
| Leche del lote | Cargar el tanque | 550 | 480 | 550 | L |
| Azúcar | Dosificar insumos | 63,1 | 62,5 | 63,7 | kg |
| Estabilizante | Dosificar insumos | 0,412 | 0,408 | 0,416 | kg |
| Leche en polvo | Estandarizar | 7,1 | 7,03 | 7,17 | kg |
| Temperatura de precalentamiento | Precalentar | 25 | 22 | 28 | °C |
| Temperatura de homogeneización | Homogeneizar | 62 | 60 | 65 | °C |
| Presión de homogeneización | Homogeneizar | 175 | 150 | 200 | bar |
| Temperatura de pasteurización | Pasteurizar | 87 | 85 | 90 | °C |
| Tiempo de sostenimiento | Pasteurizar | 7 | 5 | 10 | min |
| Temperatura de inoculación | Inocular | 43 | 42 | 45 | °C |
| Cultivo | Inocular | 7 | 6,5 | 7,5 | g |
| Temperatura de incubación | Incubar | 43 | 41 | 45 | °C |
| pH de fin de incubación | Incubar | 4,5 | 4,4 | 4,6 | pH |
| Tiempo máximo de incubación | Incubar | 300 | — | 300 | min |
| Velocidad de ruptura del coágulo | Romper el coágulo | 18 | 15 | 20 | rpm |
| Saborizante de mora | Saborizar | 0,206 | 0,204 | 0,208 | kg |
| Colorante | Saborizar | 0,090 | 0,089 | 0,091 | kg |
| Temperatura de salida de E-301 | Enfriar y transferir | 18 | 15 | 20 | °C |
| Relación de preparado de mora | Envasar | 8,0 | 7,8 | 8,2 | % |
| Dosis por vaso | Envasar | 150 | 146 | 154 | ml |
| Velocidad de la llenadora | Envasar | 45 | 30 | 45 | vasos/min |
| Vasos por caja | Empacar | 24 | 24 | 24 | und |

Requisitos de equipo de RM-YV-150: U1 a U5 (T-301, H-301, E-301, P-301, T-302) y la ruta U7 (P-403, MX-403, LL-402, CD-402, CK-402 y CV-402), más la estación de encanastado (la celda R-501 en una etapa posterior). Las recetas RM-YB-200 y RM-YV-300 tienen la misma estructura con los valores de las secciones 4 y 5.

### 6.4 Ciclo de vida y control de versiones

| Estado de la receta | Quién actúa | Qué se permite |
| --- | --- | --- |
| En elaboración | Ingeniería de procesos | Editar fórmula y parámetros; no se puede usar en producción |
| En revisión | Calidad y producción | Comentar y devolver; no se puede usar en producción |
| Aprobada | Jefatura de calidad | Firmar electrónicamente; queda lista para liberar |
| Liberada | MES | Generar recetas de control para órdenes nuevas |
| Obsoleta | MES | Consultar en registros históricos; no genera órdenes nuevas |

Cada cambio de fórmula o de límites crea una versión nueva (por ejemplo, RM-YV-150 v1.1) con el usuario, la fecha, el valor anterior y el motivo. Los lotes en curso terminan con la versión con la que empezaron. Este control responde a la Resolución 2674 de 2013, que exige registros del control de procesos, y a la segmentación de usuarios del documento de arquitectura ISA-95.

### 6.5 De la receta maestra a la receta de control

1. El ERP envía al MES el plan semanal con las cantidades por referencia.
2. El MES crea la orden de producción y la asocia a la versión liberada de la receta maestra.
3. Al recibir la leche, WT-101 y FT-101 informan el volumen real; el MES escala la fórmula (sección 4.4) y asigna los equipos: la ruta U6 o U7 según la referencia.
4. El MES genera el código de lote y la fecha de vencimiento y los envía al codificador de la máquina asignada.
5. La receta de control se descarga al PLC-01 a través del SCADA; el PLC ejecuta las fases y devuelve el inicio, el fin, las cantidades reales y las alarmas de cada una.
6. Al cerrar el lote, la receta de control queda guardada con el registro del lote y no se puede modificar.

### 6.6 Diferencias entre recetas por fase y equipo

Las tres recetas comparten el procedimiento y los equipos de preparación y fermentación (PU1 a PU4 en U1 a U5); cambian las cantidades de la fórmula, la velocidad de ruptura del coágulo, la fruta y la ruta de envasado.

| Procedimiento y fase | Unidad y equipos | YB-200 | YV-150 | YV-300 |
| --- | --- | --- | --- | --- |
| PU1 · Recibir y cargar | U1: TK-101, P-101 | 550 L | 550 L | 550 L |
| PU2 · Estandarizar sólidos | U2: DS-206 | 5,7 kg de leche en polvo | 7,1 kg | 7,1 kg |
| PU2 · Dosificar azúcar y estabilizante | U2: DS-201, DS-202 | 75,7 kg y 0,206 kg | 63,1 kg y 0,412 kg | 56,7 kg y 0,412 kg |
| PU2 · Homogeneizar y pasteurizar | U3: H-301, T-301 | 150–200 bar; 85–90 °C, 5–10 min | Igual | Igual |
| PU3 · Inocular e incubar | U3: BL-205, T-301, AT-301 | 7 g; 43 °C hasta pH 4,4–4,6 | Igual | Igual |
| PU4 · Romper el coágulo y saborizar | U3: M-301, P-203, P-204 | 30–40 rpm; fresa y 0,110 kg de colorante | 15–20 rpm; mora y 0,090 kg | 15–20 rpm; melocotón y 0,060 kg |
| PU4 · Enfriar y transferir | U4 y U5: E-301, T-302 | 15–20 °C | Igual | Igual |
| PU5 · Dosificar fruta | U7: P-403, MX-403 | No aplica | 8 % (57,2 kg) | 12 % (88,8 kg) |
| PU5 · Envasar | U6: EMP-401 · U7: LL-402 | XV-401 a la empacadora: 200 ml, 30 bolsas/min, 102 min | XV-402 a la llenadora: 150 ml, 45 vasos/min, 97 min | XV-402 a la llenadora: 300 ml, 35 vasos/min, 65 min |
| PU5 · Pesar y codificar | U6: CK-401, CD-401 · U7: CK-402, CD-402, ZS-403 | Peso del 100 % y código en la película | Peso del 100 %, tapa verificada y código en la tapa | Igual que YV-150 |
| PU6 · Empacar y almacenar | U8: CV-501, CF-501 | 26 canastas de 120 bolsas | 183 cajas de 24 vasos | 113 cajas de 20 vasos |

## 7. Lotes de producción

### 7.1 Definición e identificación del lote

- Un lote es una carga del tanque de proceso T-301: entre 480 y 550 L de leche, según la disponibilidad en la zona.
- Cada lote corresponde a una sola referencia, porque el saborizante y el colorante se adicionan en el tanque de proceso.
- Identificación: REF-AAAAMMDD-N, donde REF es la referencia sin guion, AAAAMMDD la fecha de fabricación y N el consecutivo del día. Ejemplo: YV150-20270510-2.
- El lote de leche se identifica por separado, con el proveedor y las cantinas recibidas, y se asocia al lote de yogur.
- En cada unidad se imprime el código del lote y la fecha de vencimiento (fecha de fabricación más 21 días), como exige la Resolución 5109 de 2005. Ejemplo de impresión: L YV150-20270510-2 · V 02/11/2026.

### 7.2 Estados del lote

| Estado | Se alcanza cuando | Quién lo registra |
| --- | --- | --- |
| Creado | El MES libera la orden y genera la receta de control | MES |
| Leche aprobada | Las cantinas pasan el análisis y se cargan al tanque | Operario en HMI-01 |
| Base preparada | Las dosis están completas y la homogeneización registrada | PLC |
| Pasteurizado | El sostenimiento se cumple sin interrupciones | PLC e historiador |
| Fermentado conforme | AT-301 llega a pH 4,4–4,6 y laboratorio confirma la acidez | PLC y calidad |
| Acondicionado | El producto está en T-302 a 15–20 °C | PLC |
| Envasado | La máquina termina el lote y las controladoras reportan conformes y rechazos | PLC y MES |
| Retenido | El lote está en el cuarto frío a la espera de los análisis | MES |
| Liberado | Calidad aprueba los resultados y el registro del lote | Calidad en el MES |
| Cerrado | El lote se despacha y el registro queda bloqueado | MES |

Una desviación de parámetro no cambia el estado en silencio: genera una alarma, un registro de causa y una decisión de calidad, que puede ser continuar, segregar o reprocesar con autorización.

### 7.3 Capacidad y tiempo de ciclo

| Indicador | Situación actual | Propuesta |
| --- | --- | --- |
| Lotes por día | 1 | 2 |
| Leche procesada por día | 550 L | 1.100 L |
| Yogur producido por día | 610 L | ≈ 1.230 a 1.360 L, según la mezcla de referencias |
| Referencias | 1 (bolsa de 200 ml) | 3 |
| Tiempo estándar por lote | 601 min | ≈ 493 min (YB-200) |
| Ocupación del tanque de proceso por lote | Desde la carga hasta la mañana siguiente | ≈ 369 min de proceso más 40 min de CIP |
| Producto no conforme | 5,06 % | Meta: 1,5 % o menos |

La ocupación del tanque de proceso en la propuesta es la suma de carga (12 min), precalentamiento y dosificación (12), pasteurización con homogeneización (60), enfriamiento a inoculación (15), incubación (240), ruptura y saborizado (5) y transferencia por el intercambiador (25). Con el CIP, cada lote ocupa el tanque unos 409 min, de modo que dos lotes caben en una jornada extendida de dos turnos. El envasado ya no limita: la empacadora termina un lote de bolsas en 102 min y la llenadora un lote de vasos en 65 a 97 min.

### 7.4 Programa diario de dos lotes

| Hora | Lote 1 | Lote 2 |
| --- | --- | --- |
| 7:30–9:15 | — | Transferencia y envasado del lote 2 del día anterior |
| 8:00–8:40 | Limpieza CIP del tanque de proceso | — |
| 8:40–10:40 | Carga, dosificación, homogeneización, pasteurización e inoculación | — |
| 10:40–14:40 | Incubación con control automático de pH | — |
| 14:40–15:05 | Enfriamiento en placas y transferencia al tanque pulmón | — |
| 15:05–16:50 | Envasado | Limpieza CIP y carga del tanque de proceso (15:05–16:15) |
| 16:15–18:15 | — | Pasteurización e inoculación |
| 18:15–22:15 | — | Incubación sin operario, con control automático y alarmas remotas |
| 22:15–7:30 | — | Enfriamiento automático con agua fría en la chaqueta (TIC-301 sobre TV-302) hasta 15–20 °C |

El segundo lote es posible porque el enfriamiento deja de depender de la noche: el lote 1 se enfría en el intercambiador de placas y libera el tanque a las 15:05. El lote 2 termina la incubación a las 22:15, sin operario: el agua fría de la chaqueta lo baja a 15–20 °C durante la noche y a las 7:30 pasa por el intercambiador hacia el tanque pulmón y se envasa.

### 7.5 Programa semanal de referencia

| Día | Lote 1 | Lote 2 |
| --- | --- | --- |
| Lunes | YB-200 | YB-200 |
| Martes | YV-150 | YB-200 |
| Miércoles | YB-200 | YV-300 |
| Jueves | YV-150 | YB-200 |
| Viernes | YV-300 | YV-150 |
| **Total semanal** | **5 lotes de YB-200, 3 de YV-150 y 2 de YV-300** | **15.395 bolsas, 13.107 vasos de 150 ml y 4.520 vasos de 300 ml** |

La mezcla de referencias es un supuesto de diseño y se ajusta con el plan de ventas del cliente. La secuencia agrupa lotes iguales cuando es posible, para reemplazar el CIP completo por un enjuague.

### 7.6 Requerimiento semanal de insumos

| Insumo | YB-200 (5 lotes) | YV-150 (3 lotes) | YV-300 (2 lotes) | Total semanal |
| --- | --- | --- | --- | --- |
| Leche cruda | 2.750 L | 1.650 L | 1.100 L | 5.500 L |
| Azúcar | 378,5 kg | 189,3 kg | 113,4 kg | 681,2 kg |
| Leche en polvo descremada | 28,5 kg | 21,3 kg | 14,2 kg | 64,0 kg |
| Estabilizante | 1,03 kg | 1,24 kg | 0,82 kg | 3,09 kg |
| Cultivo láctico | 35 g | 21 g | 14 g | 70 g |
| Saborizante | 1,03 kg | 0,62 kg | 0,41 kg | 2,06 kg |
| Colorante | 0,55 kg | 0,27 kg | 0,12 kg | 0,94 kg |
| Preparado o trozos de fruta | — | 171,6 kg | 177,6 kg | 349,2 kg |
| Envases | 15.395 bolsas | 13.107 vasos y tapas | 4.520 vasos y tapas | — |
| Empaque secundario | 130 canastas | 549 cajas | 226 cajas | — |

El MES calcula este requerimiento a partir del plan semanal y lo envía al ERP para las compras; el ERP devuelve al MES la disponibilidad de insumos antes de liberar cada orden.

### 7.7 Cambios entre lotes

| Cambio | Actividad | Tiempo estimado |
| --- | --- | --- |
| Entre lotes de la misma referencia | Enjuague del tanque de proceso y de la línea | 15 min |
| Cambio de sabor | Limpieza CIP del tanque de proceso, el tanque pulmón y la línea: preenjuague, lavado alcalino, enjuague, lavado ácido y enjuague final | 40 min |
| Cambio entre vasos de 150 y 300 ml | Ajuste de dosis y de altura en la llenadora | 10 min |
| Cambio entre bolsa y vaso | Conmutación de válvulas XV-401 y XV-402 hacia la otra máquina | 5 min |
| Fin del día | CIP completo de toda la línea, incluida la llenadora y la bomba de fruta | 40 min |

## 8. Calidad y liberación del lote

### 8.1 Puntos críticos de control

| PCC | Peligro | Límite crítico | Vigilancia | Acción correctiva |
| --- | --- | --- | --- | --- |
| Pasteurización | Supervivencia de microorganismos patógenos de la leche cruda | 85 °C o más durante todo el sostenimiento | TT-301 con registro continuo en el historiador | Reiniciar el sostenimiento; el lote no avanza sin cumplirlo |
| Enfriamiento y almacenamiento | Crecimiento microbiano y sobreacidificación | Envasado a 20 °C o menos; cuarto frío a 4 °C | TT-302, TT-303 y TT-501 | Retener el lote y evaluar |

### 8.2 Controles en proceso

| Control | Frecuencia | Criterio | Registro |
| --- | --- | --- | --- |
| Análisis de la leche | Cada cantina | Decreto 616 de 2006 | HMI-01 y MES |
| Dosis de insumos | Cada dosificación | Fórmula ± 1 % | PLC y MES |
| Curva de pasteurización | Continua | 85–90 °C durante el sostenimiento | Historiador |
| pH de fin de incubación | Continua | 4,4–4,6 | AT-301 e historiador |
| Acidez de confirmación | Una vez por lote | 80–90 °Th | Laboratorio en HMI-01 |
| Peso de cada unidad | 100 % | Tolerancia de la referencia | CK-401 o CK-402 |
| Hermeticidad del sellado | Muestreo cada 15 min | Sin fugas | Estación de registro en HMI-01 |
| Presencia de tapa | 100 % | Tapa presente y sellada | ZS-403 |
| Código impreso | Arranque y cada cambio de rollo o de lote | Lote y vencimiento legibles | Operario en HMI-02 |

### 8.3 Liberación del lote

El lote queda retenido en el cuarto frío hasta que calidad revisa tres cosas: el registro electrónico del lote completo y sin desviaciones abiertas, los análisis fisicoquímicos de la sección 3.2 y los análisis microbiológicos con el plan de muestreo de la Resolución 1407 de 2022 para leches fermentadas. Con todo conforme, calidad libera el lote en el MES y el ERP lo habilita para despacho. Los límites microbiológicos de referencia están en el documento de estado del arte.

### 8.4 Producto no conforme

- Las unidades rechazadas por peso se separan en la máquina y se cuentan por lote y por causa.
- Un lote con una desviación de un punto crítico no se libera hasta que calidad evalúa el registro.
- El yogur con pH por fuera del rango o con defectos de textura no se reprocesa en la base de un lote nuevo: se destina a otro uso o se descarta, según la decisión de calidad.
- La meta de producto no conforme es de 1,5 % o menos, frente al 5,06 % actual.

## 9. Registro y trazabilidad

### 9.1 Registro electrónico del lote

| Dato | Origen | Momento |
| --- | --- | --- |
| Orden de producción, referencia, versión de la receta y tamaño real del lote | MES | Al liberar la orden |
| Lote de leche, proveedor y resultados de laboratorio | HMI-01 | En la recepción |
| Lotes de leche en polvo, azúcar, estabilizante, cultivo, saborizante, colorante, fruta y envase | Lectura de código en HMI-01 y BL-205 | Al dosificar |
| Cantidades dosificadas frente a la fórmula | WT-201, WT-202, FQ-203, FQ-204, WT-205, WT-206 | En cada dosificación |
| Presión y temperatura de homogeneización | PT-302 y TT-301 | Continuo |
| Curva de pasteurización e incubación | TT-301 | Continuo |
| pH al final de la incubación | AT-301 | Continuo y al cierre de la fase |
| Temperatura de salida del enfriador | TT-302 | Continuo |
| Unidades conformes, rechazadas y causa | CK-401 o CK-402 | Cada unidad |
| Código y fecha de vencimiento impresos | CD-401 o CD-402 | Al arrancar el envasado |
| Inicio y fin de cada fase, alarmas y paradas | PLC-01 | Por evento |
| Canastas, cajas y estibas del lote, ubicación en el cuarto frío | Estación de encanastado y MES | Al encanastar |
| Ciclo CIP previo y su verificación | CIP-901 y CT-901 | Antes de cargar el lote |

### 9.2 Genealogía del lote

La trazabilidad va en las dos direcciones. Hacia atrás, desde una unidad en el mercado se llega al lote de yogur por el código impreso, y desde el lote a las cantinas de leche, al proveedor y a los lotes de cada insumo. Hacia adelante, desde un lote de leche o de insumo se llega a todos los lotes de yogur que lo usaron, a sus estibas y a sus despachos. Esta cadena es la que permite un retiro de producto acotado a los lotes afectados y no a toda la producción.

### 9.3 Indicadores por lote

| Indicador | Cálculo | Referencia |
| --- | --- | --- |
| Rendimiento | Litros envasados conformes ÷ litros de leche | 1,12 (YB-200), 1,19 (YV-150), 1,23 (YV-300) |
| Desviación de dosificación | Cantidad real ÷ cantidad de la fórmula − 1 | ± 1 % |
| Producto no conforme | Unidades rechazadas ÷ unidades producidas | 1,5 % o menos |
| Tiempo de ciclo del lote | Fin del envasado − inicio de la carga | ≈ 493 min (YB-200) |
| Disponibilidad del tanque de proceso | Tiempo en producción ÷ tiempo programado | Dos lotes por día |
| OEE de la máquina de envasado | Disponibilidad × rendimiento × calidad | Se calcula en el MES por lote |

## 10. Origen de los datos

| Dato | Origen |
| --- | --- |
| Tamaño de lote, fórmula de YB-200, tiempos estándar y producto no conforme | Caso de estudio de La Hacienda (Grimaldo, Moreno y Salamanca, 2015) |
| Tres referencias: bolsa de 200 ml y vasos de 150 y 300 ml, con tres sabores | Decisión del equipo, reunión del 11 de octubre de 2026 |
| Fórmulas de YV-150 y YV-300, velocidades de envasado, tiempos de cambio y composición estimada | Estimaciones de diseño de la propuesta |
| Leche en polvo, homogeneización y codificado | Modelo ISA-88 de la línea y referencia de proceso industrial del yogur |
| Segundo lote diario con enfriamiento en intercambiador de placas | Decisión del equipo, reunión del 11 de octubre de 2026, y programa de tiempos y capacidades |
| Requisitos sanitarios y de rotulado | Normativa colombiana citada en la sección 2.2 |

## Referencias

- ANSI/ISA-88.00.01-2010. Batch Control Part 1: Models and Terminology. International Society of Automation.
- ANSI/ISA-88.00.02-2001. Batch Control Part 2: Data Structures and Guidelines for Languages. International Society of Automation.
- ANSI/ISA-18.2-2016. Management of Alarm Systems for the Process Industries. International Society of Automation.
- Decreto 616 de 2006. Reglamento técnico sobre los requisitos que debe cumplir la leche para el consumo humano. Ministerio de la Protección Social.
- Grimaldo, G., Moreno, D. y Salamanca, M. (2015). Medición del trabajo de una línea de producción de yogurt – Empresa La Hacienda. Revista I3+, 2(2), 62–81.
- ICONTEC (2017). NTC 805: Productos lácteos. Leches fermentadas.
- Resolución 2310 de 1986. Procesamiento, composición, requisitos y comercialización de los derivados lácteos. Ministerio de Salud.
- Resolución 2674 de 2013. Requisitos sanitarios para fabricar, procesar, envasar y comercializar alimentos. Ministerio de Salud y Protección Social.
- Resolución 5109 de 2005. Reglamento técnico de rotulado o etiquetado de alimentos envasados. Ministerio de la Protección Social.
- Resolución 810 de 2021 y Resolución 2492 de 2022. Etiquetado nutricional y frontal de alimentos. Ministerio de Salud y Protección Social.
- Resolución 1407 de 2022. Criterios microbiológicos de los alimentos y bebidas para consumo humano. Ministerio de Salud y Protección Social.
- Tamime, A. Y. y Robinson, R. K. (2007). Tamime and Robinson's Yoghurt: Science and Technology (3.ª ed.). Woodhead Publishing.
- Tetra Pak (2015). Dairy Processing Handbook, capítulo 11: Fermented milk products.
