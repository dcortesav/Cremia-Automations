# EDT de Proceso— Proceso Productivo de una Línea de Yogur Saborizado con Fruta

> **Alcance:** Proceso productivo de una línea de yogur batido saborizado con fruta.

---

## 1. Resumen de la EDT

| Código | Entregable | Paquetes |
|---|---|---|
| 1.1 | Materias primas recepcionadas y almacenadas | 4 |
| 1.2 | Leche acondicionada (mezcla normalizada y homogeneizada) | 4 |
| 1.3 | Mezcla pasteurizada y enfriada | 2 |
| 1.4 | Yogur fermentado (coágulo cortado) | 4 |
| 1.5 | Yogur saborizado con fruta y envasado | 3 |
| 1.6 | Control de calidad y almacenamiento | 3 |
| 1.7 | Sistema de gestión de la producción | 2 |
| | **Total** | **22** |

---

## 2. Diagrama de la EDT

![Diagrama de la EDT](./EDT%20Yogurt.png)

---

## 3. Árbol de la EDT

### 1.0 Proceso productivo de la línea de yogur saborizado con fruta

**1.1 Materias primas recepcionadas y almacenadas**
- 1.1.1 Recepción y control de la leche cruda
- 1.1.2 Almacenamiento refrigerado de la leche cruda
- 1.1.3 Recepción y control de insumos
- 1.1.4 Almacenamiento y acondicionamiento de insumos

**1.2 Leche acondicionada (mezcla normalizada y homogeneizada)**
- 1.2.1 Estandarización de materia grasa
- 1.2.2 Normalización de sólidos totales
- 1.2.3 Homogeneización
- 1.2.4 Formulación y dosificación de azúcar y estabilizantes (incluyendo colorantes, saborizantes y cultivos)

**1.3 Mezcla pasteurizada y enfriada**
- 1.3.1 Pasteurización
- 1.3.2 Enfriamiento a temperatura de inoculación

**1.4 Yogur fermentado (coágulo cortado)**
- 1.4.1 Inoculación con cultivos starter
- 1.4.2 Fermentación controlada
- 1.4.3 Corte de fermentación por enfriamiento
- 1.4.4 Control de la coagulación

**1.5 Yogur saborizado con fruta y envasado**
- 1.5.1 Preparación y dosificación de la preparación de fruta y saborizante
- 1.5.2 Envasado del yogur
- 1.5.3 Etiquetado, codificación y control de sellado

**1.6 Control de calidad y Almacenamiento**
- 1.6.1 Inspección de producto
- 1.6.2 Encanastado y paletizado
- 1.6.3 Transporte hasta cuarto de refrigeración a 4°C

**1.7 Sistema de gestión de la producción**
- 1.7.1 CIP (Cleaning In Place) entre lotes
- 1.7.2 Documentación, trazabilidad de lotes y registros

---

## 4. Diccionario de la EDT

Cada paquete indica qué incluye, qué **no** incluye, cómo se sabe que está terminado, quién responde, la estimación y de qué depende.

| Código | Paquete de trabajo | Descripción (incluye / no incluye) | Criterio de aceptación | Responsable (rol) | Depende de |
|---|---|---|---|---|---|
| 1.1.1 | Recepción y control de leche cruda | **Incluye:** descarga, pesaje en WT-101, muestreo y análisis de temperatura, pH, acidez, densidad, grasa, proteína, sólidos y antibióticos. **No incluye:** pago a proveedor ni gestión comercial del rechazo. | Leche aprobada por calidad, a <6 °C, pH 6.6–6.8 y densidad 1.028–1.034; registro de recepción completo. | Jefe de Recepción / Calidad | — |
| 1.1.2 | Almacenamiento refrigerado de leche cruda | **Incluye:** transferencia al tanque, control continuo de temperatura, inventario y rotación FIFO. **No incluye:** CIP, incluido en 1.7.1. | Leche conservada a <6 °C, con nivel y temperatura registrados y sin desviaciones durante el almacenamiento. | Operador de Planta | 1.1.1 |
| 1.1.3 | Recepción y control de insumos | **Incluye:** recepción y verificación de azúcar, leche en polvo, estabilizante, cultivos, saborizantes, colorantes, fruta y materiales de envase; control de lote, certificado y condición. **No incluye:** control de leche cruda. | Insumos identificados, conformes y liberados para la receta correspondiente. | Jefe de Recepción / Calidad | — |
| 1.1.4 | Almacenamiento y acondicionamiento de insumos | **Incluye:** almacenamiento seco o refrigerado, control de inventario y alistamiento de cultivos y fruta. **No incluye:** dosificación de proceso. | Insumos disponibles, identificados y conservados dentro de las condiciones especificadas. | Jefe de Almacén | 1.1.3 |
| 1.2.1 | Estandarización de materia grasa | **Incluye:** ajuste de materia grasa mediante separación y mezcla hasta 3.0–3.5 % para yogur entero, 1.5–1.8 % para semidescremado o <0.5 % para descremado. **No incluye:** homogeneización. | Materia grasa dentro del rango de la receta, con resultado registrado. | Supervisor de Producción | 1.1.4 |
| 1.2.2 | Normalización de sólidos totales | **Incluye:** adición de leche en polvo y ajuste de sólidos no grasos a 12–14 % y sólidos totales a 14–16 %. **No incluye:** dosificación de azúcar y estabilizante. | SNG y sólidos totales dentro de especificación, sin evidencia de separación. | Supervisor de Producción | 1.2.1 |
| 1.2.3 | Homogeneización | **Incluye:** homogeneización en dos etapas a 150–200 bar y 60–65 °C para reducir los glóbulos de grasa. **No incluye:** pasteurización. | Presión y temperatura registradas; producto sin separación visible de grasa y glóbulos objetivo menores de 1 µm. | Operador de Planta | 1.2.2 |
| 1.2.4 | Formulación y dosificación de azúcar y estabilizantes | **Incluye:** pesaje y dosificación de azúcar, estabilizante, saborizante, colorante y cultivo según la receta seleccionada. **No incluye:** preparación de fruta de 1.5.1. | Ingredientes pesados y verificados; fórmula YB-200, YV-150 o YV-300 cargada sin desviación mayor al ±1 % en la dosificación automática. | Supervisor de Producción | 1.2.2 |
| 1.3.1 | Pasteurización | **Incluye:** tratamiento en el tanque de proceso con chaqueta de vapor a 85–90 °C con sostenimiento de 5–10 min, después de homogeneizar a 150–200 bar, sujeto a validación de pruebas. **No incluye:** esterilización UHT. | Curva tiempo-temperatura registrada, tratamiento cumplido y producto habilitado para enfriamiento. | Operador de Planta | 1.2.3, 1.2.4 |
| 1.3.2 | Enfriamiento a temperatura de inoculación | **Incluye:** enfriamiento controlado de la mezcla a 42–45 °C ±0.5 °C mediante agua helada y preparación para inoculación. **No incluye:** adición del cultivo. | Temperatura estable dentro del rango de inoculación y transferencia autorizada a fermentación. | Operador de Planta | 1.3.1 |
| 1.4.1 | Inoculación con cultivos starter | **Incluye:** dosificación del cultivo DVS de *S. thermophilus* y *L. delbrueckii* subsp. *bulgaricus* según receta, sin propagación previa. **No incluye:** preparación de cultivo madre. | Cultivo dosificado y mezclado uniformemente; lote y cantidad registrados. | Microbiólogo / QA | 1.3.2, 1.1.4 |
| 1.4.2 | Fermentación controlada | **Incluye:** incubación sin agitación a 40–45 °C durante aproximadamente 240 min, con seguimiento de pH y acidez. **No incluye:** enfriamiento de corte. | pH final 4.4–4.6 y acidez 80–90 °Th alcanzados dentro del procedimiento. | Supervisor de Producción | 1.4.1 |
| 1.4.3 | Corte de fermentación por enfriamiento | **Incluye:** enfriamiento rápido a 15–20 °C para detener la fermentación, ruptura controlada del coágulo y posterior acondicionamiento a 4 °C. **No incluye:** envasado. | Fermentación detenida, temperatura de transferencia conforme y textura homogénea para envasado. | Operador de Planta | 1.4.2 |
| 1.4.4 | Control de la coagulación | **Incluye:** verificación de pH, acidez, firmeza, textura y sinéresis; decisión documentada de continuar al corte. **No incluye:** modificación de la fórmula. | Lote conforme o desviación documentada antes de continuar el proceso. | Microbiólogo / QA | 1.4.2 |
| 1.5.1 | Preparación y dosificación de fruta y saborizante | **Incluye:** preparación y dosificación de fruta, saborizante y colorante según referencia: sin fruta para YB-200, preparado de mora al 8 % para YV-150 y trozos de melocotón al 12 % para YV-300. **No incluye:** compra de insumos. | Preparación dosificada según receta, con temperatura de operación ≤20 °C y registro de lote. | Supervisor de Producción | 1.4.3 |
| 1.5.2 | Envasado del yogur | **Incluye:** llenado y sellado de bolsa de 200 ml para YB-200 o de vaso de 150 ml/300 ml para YV-150/YV-300, usando los equipos definidos. **No incluye:** etiquetado. | Peso o volumen conforme, envase íntegro y sellado correcto en el formato de la referencia. | Operador de Envasado | 1.5.1 |
| 1.5.3 | Etiquetado y codificación | **Incluye:** identificación de referencia, lote, fecha, vida útil y control de hermeticidad o tapa. **No incluye:** diseño gráfico de la etiqueta. | Código legible y trazable; etiqueta, tapa o sello conformes al formato del producto. | Operador de Envasado | 1.5.2 |
| 1.6.1 | Inspección de producto | **Incluye:** inspección de peso, volumen, presentación, sellado, tapa, apariencia y condiciones de liberación del producto. **No incluye:** validación comercial de aceptación del mercado. | Muestras conformes y lote identificado para almacenamiento; desviaciones segregadas y registradas. | Microbiólogo / QA | 1.5.3 |
| 1.6.2 | Encanastado y paletizado | **Incluye:** empaque secundario y organización de 120 bolsas por canasta, 24 vasos YV-150 por caja o 20 vasos YV-300 por caja. **No incluye:** transporte. | Unidades agrupadas sin daño, con identificación de lote y patrón de almacenamiento aprobado. | Jefe de Almacén | 1.6.1 |
| 1.6.3 | Transporte hasta cuarto de refrigeración | **Incluye:** traslado del producto terminado a la cámara, control de temperatura y rotación de inventario. **No incluye:** despacho comercial al cliente. | Producto ingresado a refrigeración a 4 °C, con registro de ubicación y temperatura. | Jefe de Almacén | 1.6.2 |
| 1.7.1 | CIP entre lotes | **Incluye:** limpieza y sanitización de tanques y tuberías mediante la estación CIP-901, con verificación de eficacia entre lotes. **No incluye:** limpieza manual de áreas comunes. | Ciclo CIP ejecutado, parámetros registrados y resultado de verificación conforme antes del siguiente lote. | Coordinador de Saneamiento | 1.6.3 |
| 1.7.2 | Documentación, trazabilidad de lotes y registros | **Incluye:** identificación ISA-88 del lote, receta, fases, parámetros, consumos, registros de proceso, controles y trazabilidad hacia atrás y adelante. **No incluye:** contabilidad de costos ni gestión general del proyecto. | Expediente de lote completo, trazable y consistente con la receta y los registros de producción. | Microbiólogo / QA | 1.7.1 |

---

## 5. Parámetros clave del proceso

| Etapa | Parámetro crítico | Valor |
|---|---|---|
| Recepción de leche cruda | Temperatura / pH / densidad | <6 °C / 6.6–6.8 / 1.028–1.034 |
| Estandarización | Materia grasa / SNG / sólidos totales | 3.0–3.5 % entero; 1.5–1.8 % semides.; <0.5 % descr. / 12–14 % / 14–16 % |
| Homogeneización | Presión / temperatura | 150–200 bar / 60–65 °C (glóbulos <1 µm) |
| Pasteurización | Temperatura / tiempo | 85–90 °C / 5–10 min (validar con pruebas) |
| Enfriamiento | Temperatura de inoculación | 42–45 °C ± 0.5 °C |
| Inoculación | Dosis / pH inicial | 0.02–0.05 % (DVS) / ~6.6 |
| Fermentación | Tiempo / pH final / acidez | 4–6 h / 4.4–4.6 / 0.85–0.95 % |
| Corte de fermentación | Temperatura | 15–20 °C en el intercambiador de placas, luego 4 °C en el cuarto frío |
| Adición de fruta y envasado | Temperatura ambiente máxima | ≤20 °C |
| Almacenamiento y distribución | Temperatura / vida útil | 4 °C constante / 21–28 días |

---

## 6. Referencias

- Watson Dairy Consulting - Proceso Industrial del Yogur: https://dairyconsultant.co.uk/proceso-industrial-yogurt.php
- Rock.so — *EDT (WBS): qué es, ejemplos y constructor* (estructura de tres niveles, regla del 100 % y regla 8–80, diccionario de la EDT): https://www.rock.so/es/blog/edt-estructura-desglose-trabajo
- Project Management Institute — *PMBOK Guide* (definición de EDT/WBS, cuenta de control y paquete de trabajo).
- FAO/OMS — *Codex Alimentarius: Norma para leches fermentadas* y principios de HACCP.
- Wikipedia — *Yogur* (tipos firme/batido/bebible, envasado, vida útil y cadena de frío): https://es.wikipedia.org/wiki/Yogur
