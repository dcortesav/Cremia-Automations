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
| Receta de control | Copia de la receta maestra para un lote concreto, con su tamaño real y sus equipos asignados | YV150-20270920-2: 520 L de leche, fórmula escalada, LL-402 asignada |
| Fórmula | Lista de entradas, parámetros de proceso y salidas esperadas | Insumos por lote, consignas de fase y unidades esperadas |
| Requisitos de equipo | Clases o unidades que puede usar la receta | Tanque de proceso con chaqueta, homogeneizador y máquina de la presentación |
| Procedimiento | Secuencia de procedimientos de unidad, operaciones y fases | PU1 a PU6 del modelo procedimental |

La parte 2 de la norma (ANSI/ISA-88.00.02) define las estructuras de datos de las recetas y la parte 4 (ANSI/ISA-88.00.04) las de los registros de producción de lote; la plataforma Cremia MES/ERP de la propuesta usa esas estructuras para que las recetas se puedan versionar, aprobar y ligar al inventario y a las compras sin reescribir el programa del PLC. En este documento, MES y ERP se refieren a los dos módulos de esa plataforma, que corre en Huawei Cloud; la receta de control llega al PLC a través del nodo de borde con el SCADA en Node-RED.

### 2.2 Requisitos sanitarios y de identidad del producto

| Norma | Exigencia que afecta la receta o el lote | Cómo se atiende |
| --- | --- | --- |
| Decreto 616 de 2006 | Requisitos de la leche cruda para consumo humano: temperatura, densidad, acidez, grasa, sólidos, prueba de alcohol y ausencia de antibióticos | Análisis por cantina en LAB-101 y registro en HMI-01 antes de aceptar la leche |
| Resolución 2310 de 1986 | Define el yogur como leche higienizada fermentada por Streptococcus thermophilus y Lactobacillus delbrueckii subsp. bulgaricus, con o sin fruta, edulcorantes y estabilizantes autorizados | Cultivo termófilo DVS en las tres referencias; aditivos declarados en la fórmula |
| NTC 805 | Requisitos fisicoquímicos de las leches fermentadas: grasa, proteína láctea, sólidos no grasos, acidez y recuento de bacterias lácticas | Especificación de la sección 3.2 y verificación por lote |
| Resolución 2674 de 2013 | Buenas prácticas de manufactura: diseño sanitario, limpieza, control de procesos y registros | Equipos en acero inoxidable AISI 316L, CIP con registro y registro electrónico de lote |
| Resolución 1407 de 2022 | Criterios microbiológicos de los alimentos, con planes de muestreo por clases | Verificación periódica por muestreo en laboratorio externo (1 de cada 5 lotes, sección 8.3; no condiciona la liberación de cada lote) |
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
| Temperatura de envasado | 20 °C o menos: 15–20 °C en el lote 1 y 12–15 °C en el lote 2 | 20 °C o menos | 20 °C o menos | TT-302 y TT-303 |
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

El balance compara la masa de insumos con la masa envasada, calculada con las unidades por lote y una densidad de 1,033 kg/L para el yogur batido (la misma del balance del estado actual).

| Concepto | YB-200 | YV-150 | YV-300 |
| --- | --- | --- | --- |
| Leche cruda | 566,50 kg | 566,50 kg | 566,50 kg |
| Azúcar | 75,70 kg | 63,10 kg | 56,70 kg |
| Leche en polvo | 5,70 kg | 7,10 kg | 7,10 kg |
| Estabilizante, cultivo, saborizante y colorante | 0,53 kg | 0,72 kg | 0,69 kg |
| Preparado de fruta | — | 57,20 kg | 88,80 kg |
| **Total de entradas** | **648,4 kg** | **694,6 kg** | **719,8 kg** |
| Volumen envasado | 615,8 L | 655,4 L | 678,0 L |
| Masa envasada (1,033 kg/L) | 636,1 kg | 677,0 kg | 700,4 kg |
| Pérdidas de proceso | 12,3 kg (1,9 %) | 17,6 kg (2,5 %) | 19,4 kg (2,7 %) |
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

Cuando la leche disponible es menor de 550 L, el MES escala cada insumo en proporción a la leche cargada, medida por WT-101 y FT-101 en el lote 1 (desde TK-101) y por LT-102 y FT-101 en el lote 2 (desde TK-102):

cantidad del insumo = cantidad de la fórmula × (litros reales ÷ 550)

Por ejemplo, un lote de YB-200 con 480 L de leche lleva 66,1 kg de azúcar y 4,97 kg de leche en polvo, y produce unas 2.687 bolsas. Los parámetros de proceso (temperaturas, tiempos y pH) no se escalan. El rango de operación es de 480 a 550 L; un lote menor exige verificar que el electrodo de pH AT-301 y la hélice del agitador queden sumergidos.

## 5. Parámetros de procedimiento

### 5.1 Parámetros por fase

La tabla sigue los procedimientos de unidad del modelo procedimental. El tiempo actual es el tiempo estándar medido en el caso de estudio para un lote de 550 L; el propuesto es la estimación de diseño, que se valida con la simulación y la puesta en marcha.

| Procedimiento de unidad y fase | Consigna | Condición de fin | Tiempo actual (min) | Tiempo propuesto (min) |
| --- | --- | --- | --- | --- |
| PU1 · Recibir y analizar la leche | Acidez, pH, densidad y sólidos por cantina | Leche aprobada por laboratorio | 19,6 | 19,6 |
| PU1 · Cargar el tanque de proceso | 550 L a 3 m³/h desde TK-101 (lote 1) o TK-102 (lote 2) | Volumen de receta en T-301 (LT-301 y FT-101) | 28,4 | 12 |
| PU2 · Alistar y dosificar insumos | Cantidades de la fórmula, ± 1 % | Dosis completas (WT-201, WT-202, WT-206) | 10,2 | En paralelo con el precalentamiento (el azúcar toma unos 8 min a 10 kg/min) |
| PU2 · Precalentar y disolver | 25 °C con agitación de 40–60 rpm | Temperatura alcanzada y azúcar disuelto | 13,9 | 12 (18 en el lote 2, que parte de leche a 4 °C) |
| PU2 · Estandarizar, homogeneizar y pasteurizar | Leche en polvo según la fórmula; calentar a 62 °C (26 min), recircular por H-301 a 150–200 bar (45 min), calentar a 87 °C (17 min) y sostener 5 a 10 min | Recirculación cumplida con PT-302 en rango; sostenimiento cumplido y curva registrada | 77,4 (sin homogeneizar; sostenimiento de 15) | 95 |
| PU2 · Enfriar a inoculación | 43 °C (42–45 °C) con agua de red en la chaqueta | Temperatura estable durante 2 min | 26,2 (incluye la inoculación) | 25 |
| PU3 · Inocular | 7 g de cultivo; agitación de 5 min y parada | Lote del cultivo leído y peso verificado en BL-205 | Incluido en el anterior | 5 |
| PU3 · Incubar | 43 °C (41–45 °C), sin agitación | pH de corte en AT-301: 4,5 en el lote 1 y 4,6 en el lote 2; máximo 300 min con alarma | 240 | 240 |
| PU4 · Romper el coágulo y saborizar | 30–40 rpm (bolsa) o 15–20 rpm (vaso); saborizante y colorante de la fórmula | Textura homogénea y dosis completas | 10,0 | 5 |
| PU4 · Enfriar y transferir | Lote 1: salida de E-301 a 15–20 °C, P-301 a 1.500 L/h. Lote 2: agua helada en la chaqueta hasta 15 °C y mantenimiento a 12–15 °C; transferencia a las 7:00 | T-301 vacío (LT-301) y producto en T-302 | 23,6, más la noche | 25 |
| PU5 · Envasar | Dosis, velocidad y codificado de la referencia, con la meta de OEE de 82 % | Tanque pulmón en nivel mínimo | 148,9 | 124 (YB-200), 117 (YV-150), 78 (YV-300) |
| PU6 · Empacar y almacenar | 120 bolsas, 24 o 20 vasos por empaque; cuarto frío a 4 °C | Lote completo en CF-501 | 2,9 | En paralelo con el envasado |
| **Total por lote (YB-200)** | | | **601,3** | **≈ 563** |
| Limpieza CIP (no se suma al tiempo estándar) | Enjuague o ciclo completo según el cambio | Conductividad de enjuague verificada con CT-901 | Manual, no medida | 15 o 40 |

La homogeneización se hace en recirculación por H-301 con la mezcla a 60–65 °C: 45 min a 1.500 L/h recirculan unos 1,9 volúmenes del lote, de modo que cerca del 85 % del producto pasa al menos una vez por el homogeneizador. La textura se valida en el arranque; si no basta, la recirculación se extiende hasta 60 min.

El tiempo estándar baja solo 6 %, de 601 a 563 min, porque la incubación (240 min) no cambia y la pasteurización con homogeneización es más larga que la actual. El beneficio de la propuesta no está en el tiempo por lote sino en la ocupación del tanque: el lote 1 se enfría en placas y libera T-301 a las 15:05, y así caben dos lotes por día.

### 5.2 Parámetros que cambian con la propuesta

| Fase | Situación actual | Propuesta |
| --- | --- | --- |
| Carga al tanque de proceso | 28 min con una bomba subdimensionada | 11 a 12 min con bomba sanitaria de 3 m³/h |
| Pesaje y adición de insumos | Manual, en dos cuartos | Dosificación automática por peso, ± 1 % de la fórmula |
| Sólidos de la leche | Sin ajuste | Leche en polvo descremada: 1 % en bolsa y 1,25 % en vaso |
| Homogeneización | No se hace | 150–200 bar a 60–65 °C, en recirculación de 45 min antes de terminar el calentamiento hacia la pasteurización |
| Pasteurización | 85 °C con 15 min de sostenimiento; válvulas manuales | 85–90 °C con 5 a 10 min de sostenimiento y control automático; el tiempo final se valida con pruebas |
| Fin de la incubación | Muestra y acidómetro: 80–90 °Th | pH en línea, con pH de corte de 4,5 en el lote 1 y 4,6 en el lote 2; acidez de confirmación de 80–90 °Th en laboratorio |
| Enfriamiento | Natural, durante la noche | Lote 1: intercambiador de placas hasta 15–20 °C en unos 25 min. Lote 2: agua helada en la chaqueta de T-301, de 43 a 15 °C en unas 3 h, con agitación lenta intermitente, y mantenimiento a 12–15 °C hasta las 7:00 |
| Leche del lote 2 | No existe | Conservada a 4 °C en TK-102 desde la recepción hasta la carga |
| Control de peso | Una de cada cinco bolsas, en gramera | 100 % de las unidades, en línea, con rechazo automático |
| Codificado | Sin codificado automático | Lote y fecha de vencimiento impresos en cada unidad, con los datos que envía el MES |
| Registro | Papel | Registro electrónico de lote en el MES |

Los valores de la propuesta siguen la referencia de proceso industrial del yogur: tratamiento térmico de 85–90 °C durante 5 a 10 minutos, que desnaturaliza la mayor parte de la β-lactoglobulina y da un gel más firme y con menos separación de suero; inoculación a 42–45 °C; pH final de 4,4 a 4,6, punto en el que la caseína coagula; y enfriamiento rápido para detener la fermentación. El lote 2 se enfría más despacio que el lote 1 y sigue acidificando mientras baja de 43 a unos 30 °C; por eso su pH de corte es 4,6, el límite superior del rango, y la acidez se confirma a las 7:00 en paralelo con la transferencia a T-302, donde el producto queda retenido (sin habilitar envasado) hasta confirmar 80–90 °Th. El enfriamiento en el tanque con agitación lenta es la práctica habitual en plantas pequeñas sin intercambiador; su efecto en la textura se valida en el arranque con producto (paquete 1.9.3 de la EDT).

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

Las velocidades de envasado son valores nominales de diseño. Con la meta de OEE (disponibilidad de 92 % y rendimiento de 90 %), un lote se envasa en 124 min en bolsas, 117 min en vasos de 150 ml y 78 min en vasos de 300 ml. La empacadora actual llena 3.052 bolsas en 149 min, unas 20,5 bolsas/min, porque las paradas y el control de peso manual le quitan cerca de un tercio de su velocidad nominal.

### 5.4 Límites de alarma y acciones

| Variable | Límite | Instrumento | Acción automática | Acción del operador |
| --- | --- | --- | --- | --- |
| Temperatura de la leche del lote 2 | Alta: 6 °C | TT-102 | Alarma de prioridad alta; la carga del lote 2 espera decisión de calidad | Revisar la unidad de frío de TK-102 |
| Temperatura de pasteurización | Baja: 85 °C | TT-301 | Reinicia el conteo del sostenimiento; el lote no avanza | Revisar la presión de vapor de CAL-901 |
| Temperatura de inoculación | Alta: 46 °C | TT-301 | Bloquea la inoculación | Esperar a que el lazo TIC-301 estabilice |
| Temperatura de incubación | ± 2 °C de la consigna | TT-301 | Alarma de prioridad media | Verificar TV-301 y TV-302 |
| Tiempo de incubación | 300 min sin llegar al pH de corte | AT-301 y temporizador | Alarma de prioridad alta; en el lote 2 llega por SMS al jefe de producción | Confirmar con acidez de laboratorio; evaluar el cultivo |
| Enfriamiento nocturno del lote 2 | TT-901 mayor de 5 °C, o TT-301 mayor de 30 °C a los 90 min del fin de la incubación | TT-301 y TT-901 | Cierra TV-304, pasa el retorno de XV-904 a drenaje y abre TV-302 (agua de red) como respaldo; alarma de prioridad alta por SMS | El jefe de producción verifica el enfriador CH-901 |
| Señal de vida del nodo de borde | Sin señal durante 5 min | Vigilancia en la nube | SMS y correo al jefe de producción | Revisar la planta; el PLC sigue controlando el lote |
| Presión de homogeneización | Menor de 150 bar | PT-302 | Prolonga la recirculación | Revisar H-301 |
| Salida del enfriador | Alta: 20 °C | TT-302 | Reduce el caudal de P-301 | Revisar el agua helada (TT-901) |
| Tanque pulmón | Alta: 20 °C, o más de 6 h desde la transferencia | TT-303 y temporizador | Alarma de prioridad alta | Envasar de inmediato o retener el lote |
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
| pH de fin de incubación, lote 1 | Incubar | 4,5 | 4,4 | 4,6 | pH |
| pH de fin de incubación, lote 2 (enfriamiento en la chaqueta) | Incubar | 4,6 | 4,5 | 4,6 | pH |
| Tiempo máximo de incubación | Incubar | 300 | — | 300 | min |
| Velocidad de ruptura del coágulo | Romper el coágulo | 18 | 15 | 20 | rpm |
| Saborizante de mora | Saborizar | 0,206 | 0,204 | 0,208 | kg |
| Colorante | Saborizar | 0,090 | 0,089 | 0,091 | kg |
| Temperatura de salida de E-301 (lote 1) | Enfriar y transferir | 18 | 15 | 20 | °C |
| Temperatura de mantenimiento en la chaqueta (lote 2) | Enfriar en el tanque | 13 | 12 | 15 | °C |
| Relación de preparado de mora | Envasar | 8,0 | 7,8 | 8,2 | % |
| Dosis por vaso | Envasar | 150 | 146 | 154 | ml |
| Velocidad de la llenadora | Envasar | 45 | 30 | 45 | vasos/min |
| Vasos por caja | Empacar | 24 | 24 | 24 | und |

Requisitos de equipo de RM-YV-150: U1 a U5 (T-301, H-301, E-301, P-301, T-302) y la ruta U7 (P-403, MX-403, LL-402, CD-402, CK-402 y CV-402), más la mesa acumuladora MA-501 y la estación de encanastado (la celda R-501 en una etapa posterior). Las recetas RM-YB-200 y RM-YV-300 tienen la misma estructura con los valores de las secciones 4 y 5.

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

1. El ERP genera el plan semanal con las cantidades por referencia a partir de los pedidos.
2. El MES crea la orden de producción y la asocia a la versión liberada de la receta maestra.
3. Al liberar la orden, hasta con 48 h de anticipación, la receta de control sale con las cantidades planificadas para 550 L. Al cargar el lote, WT-101 y FT-101 (lote 1, desde TK-101) o LT-102 y FT-101 (lote 2, desde TK-102) informan la cantidad real; el MES escala la fórmula (sección 4.4; sin internet, el nodo de borde hace el mismo escalado con la receta en caché) y asigna los equipos: el tanque de origen (TK-101 o TK-102) y la ruta U6 o U7 según la referencia.
4. El MES genera el código de lote y la fecha de vencimiento y los envía al codificador de la máquina asignada.
5. La receta de control llega al nodo de borde, que la guarda en caché y la descarga al PLC-01 cuando el operador arranca el lote; el PLC ejecuta las fases y devuelve el inicio, el fin, las cantidades reales y las alarmas de cada una.
6. Al cerrar el lote, la receta de control queda guardada con el registro del lote y no se puede modificar.

### 6.6 Diferencias entre recetas por fase y equipo

Las tres recetas comparten el procedimiento y los equipos de preparación y fermentación (PU1 a PU4 en U1 a U5); cambian las cantidades de la fórmula, la velocidad de ruptura del coágulo, la fruta y la ruta de envasado.

| Procedimiento y fase | Unidad y equipos | YB-200 | YV-150 | YV-300 |
| --- | --- | --- | --- | --- |
| PU1 · Recibir y cargar | U1: TK-101 (lote 1) o TK-102 (lote 2), P-101 | 550 L | 550 L | 550 L |
| PU2 · Estandarizar sólidos | U2: DS-206 | 5,7 kg de leche en polvo | 7,1 kg | 7,1 kg |
| PU2 · Dosificar azúcar y estabilizante | U2: DS-201, DS-202 | 75,7 kg y 0,206 kg | 63,1 kg y 0,412 kg | 56,7 kg y 0,412 kg |
| PU2 · Homogeneizar y pasteurizar | U3: H-301, T-301 | 150–200 bar; 85–90 °C, 5–10 min | Igual | Igual |
| PU3 · Inocular e incubar | U2–U3: BL-205, T-301, AT-301 | 7 g; 43 °C hasta pH 4,5 (lote 1) o 4,6 (lote 2) | Igual | Igual |
| PU4 · Romper el coágulo y saborizar | U2–U3: M-301, P-203, P-204 | 30–40 rpm; fresa y 0,110 kg de colorante | 15–20 rpm; mora y 0,090 kg | 15–20 rpm; melocotón y 0,060 kg |
| PU4 · Enfriar y transferir | U3, U4 y U5: E-301 o chaqueta con TV-304, T-302 | Lote 1: 15–20 °C en placas; lote 2: 12–15 °C en la chaqueta | Igual | Igual |
| PU5 · Dosificar fruta | U7: P-403, MX-403 | No aplica | 8 % (57,2 kg) | 12 % (88,8 kg) |
| PU5 · Envasar | U6: EMP-401 · U7: LL-402 | XV-401 a la empacadora: 200 ml, 30 bolsas/min nominales, 124 min | XV-402 a la llenadora: 150 ml, 45 vasos/min nominales, 117 min | XV-402 a la llenadora: 300 ml, 35 vasos/min nominales, 78 min |
| PU5 · Pesar y codificar | U6: CK-401, CD-401 · U7: CK-402, CD-402, ZS-403 | Peso del 100 % y código en la película | Peso del 100 %, tapa verificada y código en la tapa | Igual que YV-150 |
| PU6 · Empacar y almacenar | U8: CV-501, MA-501, CF-501 | 26 canastas de 120 bolsas | 183 cajas de 24 vasos | 113 cajas de 20 vasos |

## 7. Lotes de producción

### 7.1 Definición e identificación del lote

- Un lote es una carga del tanque de proceso T-301: entre 480 y 550 L de leche. La leche del lote 1 se carga desde TK-101 y la del lote 2 desde el tanque refrigerado TK-102.
- Cada lote corresponde a una sola referencia, porque el saborizante y el colorante se adicionan en el tanque de proceso.
- Identificación: REF-AAAAMMDD-N, donde REF es la referencia sin guion, AAAAMMDD la fecha de fabricación y N el consecutivo del día. Ejemplo: YV150-20270920-2.
- El lote de leche se identifica por separado, con el proveedor y las cantinas recibidas, y se asocia al lote de yogur.
- En cada unidad se imprime el código del lote y la fecha de vencimiento (fecha de fabricación más 21 días), como exige la Resolución 5109 de 2005. Ejemplo de impresión: L YV150-20270920-2 · V 11/10/2027.

### 7.2 Estados del lote

| Estado | Se alcanza cuando | Quién lo registra |
| --- | --- | --- |
| Creado | El MES libera la orden y genera la receta de control | MES |
| Leche aprobada | Las cantinas pasan el análisis y se cargan al tanque | Operario en HMI-01 |
| Base preparada | Las dosis están completas y la homogeneización registrada | PLC |
| Pasteurizado | El sostenimiento se cumple sin interrupciones | PLC e historiador |
| Fermentado conforme | AT-301 llega al pH de corte y laboratorio confirma la acidez (en el lote 2, a las 7:00 mientras el lote queda retenido en T-302) | PLC y calidad |
| Acondicionado | El producto está en T-302 a 20 °C o menos | PLC |
| Envasado | La máquina termina el lote y las controladoras reportan conformes y rechazos | PLC y MES |
| Liberado | Calidad aprueba el registro electrónico del lote, sin desviaciones abiertas en los puntos críticos | Calidad en el MES |
| Retenido | Hay una desviación abierta o un análisis pendiente; el lote no se despacha | Calidad en el MES |
| Cerrado | El lote se despacha y el registro queda bloqueado | MES |

Una desviación de parámetro no cambia el estado en silencio: genera una alarma, un registro de causa y una decisión de calidad, que puede ser continuar, segregar o reprocesar con autorización.

### 7.3 Capacidad y tiempo de ciclo

| Indicador | Situación actual | Propuesta |
| --- | --- | --- |
| Lotes por día | 1 | 2 |
| Leche procesada por día | 550 L | 1.100 L |
| Yogur producido por día | 610 L | ≈ 1.230 a 1.360 L, según la mezcla de referencias |
| Unidades conformes por día | 2.898 bolsas | 6.505 unidades en promedio |
| Referencias | 1 (bolsa de 200 ml) | 3 |
| Tiempo estándar por lote | 601 min | ≈ 563 min (YB-200) |
| Ocupación del tanque de proceso | Desde la carga hasta la mañana siguiente | Lote 1: 419 min de proceso y 40 de CIP (7:25 a 15:05). Lote 2: de las 15:05 (CIP) y carga a las 15:45, hasta las 7:25 del día siguiente, porque se enfría en el tanque |
| Producto no conforme | 5,06 % | Meta: 1,5 % o menos |

La ocupación del lote 1 es la suma de carga (12 min), precalentamiento y dosificación (12), homogeneización y pasteurización (95), enfriamiento a inoculación (25), inoculación (5), incubación (240), ruptura y saborizado (5) y transferencia por el intercambiador (25). El lote 2 ocupa el tanque toda la noche, de modo que T-301 queda ocupado las 24 h: es la restricción de la línea y fija la capacidad en dos lotes diarios. El envasado no limita: con la meta de OEE, la empacadora termina un lote de bolsas en 124 min y la llenadora un lote de vasos en 78 a 117 min.

### 7.4 Programa diario de dos lotes

| Hora | Lote 1 | Lote 2 y lote 2 del día anterior |
| --- | --- | --- |
| 7:00–7:25 | — | Muestra y acidez de confirmación del lote 2 anterior (7:00–7:05) en paralelo con su transferencia por E-301 a T-302; el producto queda retenido en T-302 hasta confirmar la acidez (80–90 °Th) |
| 7:05–7:45 | Recepción y análisis de 14 cantinas hacia TK-101 (7:05–7:25) | Recepción y análisis de 14 cantinas hacia TK-102, que las enfría a 4 °C (7:25–7:45) |
| 7:25–8:05 | CIP de T-301 | El lote 2 anterior espera en T-302 a 12–15 °C hasta las 10:30 (retenido para envasado hasta confirmar la acidez) |
| 8:05–10:35 | Carga (12 min), precalentamiento y dosificación (12), homogeneización y pasteurización (95), enfriamiento a 43 °C (25) e inoculación (5) | — |
| 10:35–14:35 | Incubación hasta pH 4,5, con control automático | Envasado del lote 2 anterior (10:30–12:35 en bolsas; 117 min en vasos de 150 ml y 78 min en vasos de 300 ml) y CIP de T-302 y de la línea (12:35–13:15) |
| 14:35–15:05 | Ruptura, saborizado y muestra de acidez de confirmación (14:35–14:40); enfriamiento en placas y transferencia a T-302 (14:40–15:05), donde queda retenido hasta confirmar la acidez antes de envasar | — |
| 15:05–17:10 | Envasado | CIP de T-301 (15:05–15:45), carga desde TK-102 (15:45–15:55), precalentamiento desde 4 °C (15:55–16:15), homogeneización y pasteurización (16:15–17:50) |
| 17:10–17:50 | CIP de fin de día de T-302 y de la línea de envasado | Pasteurización |
| 17:50–18:20 | — | Enfriamiento a 43 °C (17:50–18:15) e inoculación (18:15–18:20) |
| 18:20–22:20 | — | Incubación sin operario hasta pH 4,6, con alarmas remotas |
| 22:20–7:00 | — | Ruptura y saborizado automáticos (22:20–22:25); agua helada en la chaqueta (TIC-301 sobre TV-304) hasta 15 °C hacia la 1:30 y mantenimiento a 12–15 °C |

El segundo lote es posible porque el lote 1 se enfría en el intercambiador de placas y libera el tanque a las 15:05. El lote 2 termina la incubación a las 22:20, sin operario: el PLC rompe el coágulo, dosifica el saborizante y el colorante y lo enfría con el agua helada del enfriador CH-901, que de noche no atiende el intercambiador. A las 7:00 inicia en paralelo la muestra de laboratorio (7:00–7:05) y el paso del lote por E-301 al tanque pulmón T-302, donde el producto queda retenido (sin habilitar el envasado de las 10:30) a 12–15 °C hasta confirmar la acidez en 80–90 °Th. El tanque pulmón tiene alarma si el yogur supera 20 °C o lleva más de 6 h sin envasar.

Las horas de la tabla están redondeadas a 5 min; las exactas están en `herramientas/resultados.md`. El programa se verifica con `herramientas/programa.py`: ningún equipo (T-301, T-302, CIP-901 y E-301) tiene dos usos a la vez y cada tarea cae dentro del turno de su responsable. Con la incubación máxima de 300 min, el envasado del lote 1 termina 40 min después del fin del turno y el lote 2 se inocula 20 min después de las 19:00; esas horas extra están en el presupuesto de operación.

**Régimen de operación y turnos.** La planta produce de lunes a sábado, 50 semanas al año (300 días), con dos lotes por día: 12 lotes por semana y 600 al año. La jornada va de 7:00 a 19:00 en turnos escalonados de 7 h, que cumplen la jornada de 42 h semanales (Ley 2101 de 2021). La incubación, la ruptura y el enfriamiento del lote 2 son automáticos y no necesitan operario; las alarmas de prioridad alta y la pérdida de la señal de vida de la planta llegan por SMS al jefe de producción.

| Rol | Turno (lunes a sábado) | Tareas principales |
| --- | --- | --- |
| Operador de recepción y laboratorio | 7:00–14:00 | Acidez del lote 2 anterior (7:00), recepción y análisis de 28 cantinas (7:05–7:45), carga del lote 1 (8:05), registros y apoyo al encajonado (10:30–12:35) |
| Operador de preparación | 7:00–14:00 | Transferencia del lote 2 anterior (7:00), CIP, preparación del lote 1 hasta la inoculación (10:35), seguimiento de la incubación y mantenimiento autónomo |
| Operador de envasado | 10:30–17:30 | Envasado del lote 2 anterior (10:30–12:35), CIP de T-302, cambio de referencia y envasado del lote 1 (15:05–17:10) |
| Operador de empaque y cuarto frío | 10:30–17:30 | Encanastado de bolsas y encajonado de vasos con la mesa acumuladora, cuarto frío y despacho |
| Operador del segundo lote | 12:00–19:00 | Apoyo al empaque, ruptura, acidez y transferencia del lote 1 (14:35–15:05), CIP, carga y preparación del lote 2 hasta la inoculación (18:20) y CIP de fin de día |
| Turno corto del domingo | 7:00–10:30 | Dos operarios por rotación transfieren y envasan el lote 2 del sábado y hacen el CIP |

El lote 2 del sábado no espera al lunes: a 12–15 °C el yogur sigue acidificando y no debe pasar 32 h sin envasar. Por eso el domingo hay un turno corto de 3,5 h. Esas horas superan las 42 h semanales, así que se pagan como horas extra dominicales; cada operario cubre el domingo como máximo dos veces al mes. Su costo está en la propuesta económica.

### 7.5 Ciclo de programación de 10 lotes

La mezcla de referencias se programa en un ciclo de 10 lotes (5 días de producción) que se repite 60 veces en los 300 días del año. Como la planta trabaja 6 días por semana, el ciclo no coincide con la semana calendario: el plan semanal del ERP toma los 12 lotes siguientes del ciclo.

| Día del ciclo | Lote 1 | Lote 2 |
| --- | --- | --- |
| 1 | YB-200 | YB-200 |
| 2 | YV-150 | YB-200 |
| 3 | YB-200 | YV-300 |
| 4 | YV-150 | YB-200 |
| 5 | YV-300 | YV-150 |
| **Total del ciclo** | **5 lotes de YB-200, 3 de YV-150 y 2 de YV-300** | **15.395 bolsas, 13.107 vasos de 150 ml y 4.520 vasos de 300 ml** |

La mezcla de referencias es un supuesto de diseño y se ajusta con el plan de ventas del cliente. La secuencia agrupa lotes iguales cuando es posible, para reemplazar el CIP completo por un enjuague.

### 7.6 Requerimiento de insumos por ciclo de 10 lotes

| Insumo | YB-200 (5 lotes) | YV-150 (3 lotes) | YV-300 (2 lotes) | Total del ciclo |
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

El MES calcula el requerimiento real a partir del plan semanal y el ERP, que es parte de la misma plataforma, lo usa para las compras; antes de liberar cada orden, el MES verifica en el mismo inventario la disponibilidad de insumos.

### 7.7 Cambios entre lotes

| Cambio | Actividad | Tiempo estimado |
| --- | --- | --- |
| Entre lotes de la misma referencia | Enjuague del tanque de proceso y de la línea | 15 min |
| Cambio de sabor | Limpieza CIP del tanque de proceso, el tanque pulmón y la línea: preenjuague, lavado alcalino, enjuague, lavado ácido y enjuague final | 40 min |
| Cambio entre vasos de 150 y 300 ml | Ajuste de dosis y de altura en la llenadora | 10 min |
| Cambio entre bolsa y vaso | Conmutación de válvulas XV-401 y XV-402 hacia la otra máquina | 5 min |
| Fin del día | CIP completo de toda la línea, incluida la llenadora y la bomba de fruta | 40 min |

El programa diario reserva 40 min para cada CIP, de modo que funciona con cualquier secuencia de referencias; cuando dos lotes seguidos son de la misma referencia, el enjuague de 15 min deja holgura.

## 8. Calidad y liberación del lote

### 8.1 Puntos críticos de control

| PCC | Peligro | Límite crítico | Vigilancia | Acción correctiva |
| --- | --- | --- | --- | --- |
| Pasteurización | Supervivencia de microorganismos patógenos de la leche cruda | 85 °C o más durante todo el sostenimiento | TT-301 con registro continuo en el historiador | Reiniciar el sostenimiento; el lote no avanza sin cumplirlo |
| Enfriamiento y almacenamiento | Crecimiento microbiano y sobreacidificación | Lote 1: 20 °C o menos a la salida de E-301. Lote 2: 15 °C o menos dentro de las 4 h siguientes al fin de la incubación. Envasado a 20 °C o menos; cuarto frío a 4 °C | TT-301, TT-302 y TT-501 | Retener el lote y evaluar |

El transmisor TT-303 no hace parte de los puntos críticos de control: funciona como alarma operativa del tanque pulmón T-302 (> 20 °C) para avisar si el producto se calienta durante la espera antes del envasado.

### 8.2 Controles en proceso

| Control | Frecuencia | Criterio | Registro |
| --- | --- | --- | --- |
| Análisis de la leche | Cada cantina | Decreto 616 de 2006 | HMI-01 y MES |
| Temperatura de la leche del lote 2 | Continua | 4 °C o menos en TK-102 | TT-102 e historiador |
| Dosis de insumos | Cada dosificación | Fórmula ± 1 % | PLC y MES |
| Curva de pasteurización | Continua | 85–90 °C durante el sostenimiento | Historiador |
| pH de fin de incubación | Continua | pH de corte de la receta, dentro de 4,4–4,6 | AT-301 e historiador |
| Curva de enfriamiento del lote 2 | Continua | 15 °C o menos a las 4 h; 12–15 °C hasta las 7:00 | TT-301 e historiador |
| Acidez de confirmación | Una vez por lote; en el lote 2, a las 7:00 | 80–90 °Th | Laboratorio en HMI-01 |
| Peso de cada unidad | 100 % | Tolerancia de la referencia | CK-401 o CK-402 |
| Hermeticidad del sellado | Muestreo cada 15 min | Sin fugas | Estación de registro en HMI-02 |
| Presencia de tapa | 100 % | Tapa presente y sellada | ZS-403 |
| Código impreso | Arranque y cada cambio de rollo o de lote | Lote y vencimiento legibles | Operario en HMI-02 |

### 8.3 Liberación del lote

La liberación es por registro de proceso. Calidad libera el lote en el MES cuando el registro electrónico está completo y sin desviaciones abiertas en los puntos críticos (curva de pasteurización, pH de corte, curva de enfriamiento y temperatura de envasado), la acidez de confirmación está en 80–90 °Th, las controladoras de peso no reportan desviaciones y los instrumentos críticos tienen la calibración vigente. El MES no permite liberar un lote que incumpla alguna de esas condiciones, y el ERP solo despacha lotes liberados.

Los análisis microbiológicos verifican que el sistema de puntos críticos funciona; no son una condición para liberar cada lote. Un laboratorio externo analiza una muestra de uno de cada cinco lotes y de cada lote fabricado con un lote nuevo de cultivo o de fruta, unos 120 análisis al año, con el plan de muestreo de la Resolución 1407 de 2022 para leches fermentadas. Si un resultado no cumple, calidad retiene los lotes relacionados que sigan en la planta y, con la genealogía, ubica los despachados. El costo del laboratorio externo está en la propuesta económica. Los límites microbiológicos de referencia están en el documento de estado del arte.

Como la liberación no espera los resultados microbiológicos, el cuarto frío guarda cerca de dos días de producción (unas 52 canastas y 310 cajas, menos de 5 m³ de producto). La ingeniería básica verifica esa capacidad (paquete 1.2.1 de la EDT del proyecto).

### 8.4 Producto no conforme

- Las unidades rechazadas por peso se separan en la máquina y se cuentan por lote y por causa.
- Un lote con una desviación de un punto crítico no se libera hasta que calidad evalúa el registro.
- El yogur con pH por fuera del rango o con defectos de textura no se reprocesa en la base de un lote nuevo: se destina a otro uso o se descarta, según la decisión de calidad.
- La meta de producto no conforme es de 1,5 % o menos, frente al 5,06 % actual. La evaluación económica solo vende las unidades conformes.

## 9. Registro y trazabilidad

### 9.1 Registro electrónico del lote

| Dato | Origen | Momento |
| --- | --- | --- |
| Orden de producción, referencia, versión de la receta y tamaño real del lote | MES | Al liberar la orden |
| Lote de leche, proveedor, resultados de laboratorio y tanque de origen (TK-101 o TK-102, con su curva de temperatura) | HMI-01 y TT-102 | En la recepción y hasta la carga |
| Lotes de leche en polvo, azúcar, estabilizante, cultivo, saborizante, colorante, fruta y envase | Lectura de código en HMI-01 y BL-205 | Al dosificar |
| Cantidades dosificadas frente a la fórmula | WT-201, WT-202, FQ-203, FQ-204, WT-205, WT-206 | En cada dosificación |
| Presión y temperatura de homogeneización | PT-302 y TT-301 | Continuo |
| Curva de pasteurización, incubación y, en el lote 2, enfriamiento nocturno | TT-301 | Continuo |
| pH al final de la incubación | AT-301 | Continuo y al cierre de la fase |
| Temperatura de salida del enfriador y del tanque pulmón | TT-302 y TT-303 | Continuo |
| Unidades conformes, rechazadas y causa | CK-401 o CK-402 | Cada unidad |
| Código y fecha de vencimiento impresos | CD-401 o CD-402 | Al arrancar el envasado |
| Inicio y fin de cada fase, alarmas y paradas | PLC-01 | Por evento |
| Canastas, cajas y estibas del lote, ubicación en el cuarto frío | Estación de encanastado y MES | Al encanastar |
| Ciclo CIP previo y su verificación | CIP-901 y CT-901 | Antes de cargar el lote |

El nodo de borde guarda el registro mientras no hay internet y lo envía a la plataforma cuando vuelve la conexión, de modo que ningún lote queda sin registro.

### 9.2 Genealogía del lote

La trazabilidad va en las dos direcciones. Hacia atrás, desde una unidad en el mercado se llega al lote de yogur por el código impreso, y desde el lote a las cantinas de leche, al proveedor y a los lotes de cada insumo. Hacia adelante, desde un lote de leche o de insumo se llega a todos los lotes de yogur que lo usaron, a sus estibas y a sus despachos. Esta cadena es la que permite un retiro de producto acotado a los lotes afectados y no a toda la producción.

### 9.3 Indicadores por lote

| Indicador | Cálculo | Referencia |
| --- | --- | --- |
| Rendimiento | Litros envasados totales ÷ litros de leche (antes de rechazo por peso; sección 4.2) | 1,12 (YB-200), 1,19 (YV-150), 1,23 (YV-300) |
| Desviación de dosificación | Cantidad real ÷ cantidad de la fórmula − 1 | ± 1 % |
| Producto no conforme | Unidades rechazadas ÷ unidades llenadas | 1,5 % o menos |
| Tiempo de ciclo del lote 1 | Fin del envasado − inicio de la carga | ≈ 543 min (de 8:05 a 17:10, en YB-200) |
| Disponibilidad del tanque de proceso | Tiempo en producción ÷ tiempo programado | Dos lotes por día |
| OEE de la máquina de envasado | Disponibilidad × rendimiento × calidad | Se calcula en el MES por turno y por lote; meta de 82 % |

## 10. Origen de los datos

| Dato | Origen |
| --- | --- |
| Tamaño de lote, fórmula de YB-200, tiempos estándar y producto no conforme | Caso de estudio de La Hacienda (Grimaldo, Moreno y Salamanca, 2015) |
| Tres referencias: bolsa de 200 ml y vasos de 150 y 300 ml, con tres sabores | Decisión del equipo, reunión del 11 de octubre de 2026 |
| Fórmulas de YV-150 y YV-300, velocidades de envasado, tiempos de cambio y composición estimada | Estimaciones de diseño de la propuesta |
| Leche en polvo, homogeneización y codificado | Modelo ISA-88 de la línea y referencia de proceso industrial del yogur |
| Segundo lote diario con enfriamiento en intercambiador de placas | Decisión del equipo, reunión del 11 de octubre de 2026, y programa de tiempos y capacidades |
| Enfriamiento del lote 2 con agua helada en la chaqueta, tanque refrigerado TK-102 y liberación por registro de proceso | Revisión de la propuesta de noviembre de 2026 |
| Tiempos de pasteurización, enfriamiento y envasado de la propuesta | Cálculos de la sección 4.3 del documento de equipos y modelo `herramientas/modelo.py` |
| Requisitos sanitarios y de rotulado | Normativa colombiana citada en la sección 2.2 |

## Referencias

- ANSI/ISA-88.00.01-2010. Batch Control Part 1: Models and Terminology. International Society of Automation.
- ANSI/ISA-88.00.02-2001. Batch Control Part 2: Data Structures and Guidelines for Languages. International Society of Automation.
- ANSI/ISA-88.00.04-2006. Batch Control Part 4: Batch Production Records. International Society of Automation.
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
