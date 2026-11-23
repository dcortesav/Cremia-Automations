# Parámetros de proceso de la línea de yogur

**Temperaturas, tiempos, velocidades y límites de control**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Módulo 1 · Transformación Digital Industrial

## 1. Alcance

Este documento reúne los parámetros de proceso de la línea de yogur: los que usa hoy la planta, según el caso de estudio, y los de la propuesta. Para cada parámetro se indica la consigna, el límite de alarma y el instrumento que lo mide. Los tiempos propuestos salen de los cálculos de dimensionamiento del documento de equipos (sección 4.3) y del modelo `herramientas/modelo.py`; el programa diario de los dos lotes está en la sección 7.4 del documento de recetas y lotes.

## 2. Temperaturas

| Etapa | Valor actual | Consigna propuesta | Alarma | Instrumento |
| --- | --- | --- | --- | --- |
| Leche en recepción | Ambiente; se procesa al recibirla | Lote 1: sin cambio. Lote 2: 4 °C en TK-102 hasta la carga | Alta: 6 °C en TK-102 | Termómetro de laboratorio y TT-102 |
| Precalentamiento | 25 °C | 25 °C | ± 3 °C | TT-301 |
| Homogeneización | No se hace | 60–65 °C (consigna de 62 °C) | ± 3 °C | TT-301 |
| **Pasteurización** | **85 °C** | **85–90 °C (consigna de 87 °C)** | **Baja: 85 °C (reinicia el sostenimiento)** | TT-301, con registro |
| Inoculación | 42–45 °C | 43 °C | Alta: 46 °C | TT-301 |
| Incubación | 41–45 °C | 43 °C | ± 2 °C | TT-301 |
| Salida del enfriador de placas (lote 1) | No existe | 15–20 °C | Alta: 20 °C | TT-302 |
| Enfriamiento nocturno en la chaqueta (lote 2) | Natural, sin control | 15 °C o menos dentro de las 4 h siguientes al fin de la incubación; mantenimiento a 12–15 °C | Alta: 30 °C a los 90 min | TT-301, con registro |
| Agua helada | No existe | 2 °C | Alta: 5 °C | TT-901 |
| Tanque pulmón durante el envasado | Sin control | 20 °C o menos, máximo 6 h | Alta: 20 °C | TT-303 |
| Cuarto frío | 4 °C | 4 °C | Alta: 6 °C | TT-501 |

## 3. Tiempos

| Etapa | Tiempo actual (min) | Tiempo propuesto (min) | Observación |
| --- | --- | --- | --- |
| Descarga y análisis de la leche | 19,6 | 19,6 | Análisis manual por cantina; con dos lotes se reciben 28 cantinas en unos 40 min |
| Transferencia de 550 L al tanque de proceso | 28,4 | 12 | Bomba de 3 m³/h |
| Alistamiento y pesaje de insumos | 10,2 | En paralelo con el precalentamiento | Dosificación automática; el azúcar toma unos 8 min a 10 kg/min |
| Precalentamiento y adición de azúcar | 13,9 | 12 (18 en el lote 2) | El lote 2 parte de leche a 4 °C |
| Homogeneización y pasteurización | 77,4 (sin homogeneizar; sostenimiento de 15) | 95 | Calentar a 62 °C (26), recircular por H-301 (45), calentar a 87 °C (17) y sostener (7); el sostenimiento final se valida con pruebas |
| Enfriamiento hasta la inoculación | 26,2 (incluye la inoculación) | 25 | Agua de red en la chaqueta con control automático |
| Inoculación | Incluida en el anterior | 5 | Agitación de 5 min y parada |
| **Incubación** | **240** | **240 (termina por pH)** | Tiempo de diseño; la fase termina cuando AT-301 llega al pH de corte, con un máximo de 300 min y alarma |
| Ruptura del coágulo, acidez y saborizado | 10,0 | 5 | La acidez de confirmación se toma en paralelo |
| Enfriamiento, filtrado y transferencia | 23,6, más el enfriamiento nocturno | 25 en el lote 1 | Intercambiador de placas a 1.500 L/h. El lote 2 se enfría de noche en la chaqueta y se transfiere a las 7:00 |
| Envasado y control de peso | 148,9 (YB-200) | 124 (YB-200), 117 (YV-150), 78 (YV-300) | Velocidad nominal con la meta de OEE: disponibilidad de 92 % y rendimiento de 90 % |
| Traslado al cuarto frío | 2,9 | En paralelo con el envasado | Banda transportadora |
| **Total por lote (YB-200)** | **601,3** | **≈ 563** | 563 min, −6 %; el beneficio está en liberar el tanque a las 15:05, no en el tiempo por lote |
| Limpieza CIP (no se suma al total) | Manual, no medida | 15 o 40 | Enjuague entre lotes iguales; ciclo completo en cada cambio de sabor y al final del día |

## 4. Velocidades y caudales

| Equipo | Parámetro | Valor |
| --- | --- | --- |
| Bomba de leche P-101 | Caudal | 3 m³/h |
| Dosificador de azúcar DS-201 | Caudal grueso y de afine | 10 kg/min y 1 kg/min |
| Homogeneizador H-301 | Presión y caudal | 150–200 bar; 1.500 L/h |
| Agitador M-301 | Mezcla y tratamiento térmico | 40–60 rpm |
| | Incubación | Detenido |
| | Ruptura del coágulo: producto bebible | 30–40 rpm |
| | Ruptura del coágulo: producto en vaso | 15–20 rpm |
| | Enfriamiento nocturno del lote 2 | 10 rpm durante 2 min cada 15 min |
| Bomba de lóbulos P-301 | Caudal de transferencia | 1.500 L/h |
| Bomba de fruta P-403 | Relación con el caudal de yogur | 8 % (YV-150) o 12 % (YV-300) |
| Empacadora de bolsas EMP-401 | Velocidad | 30 bolsas/min nominales (hoy, 20,5 con paradas y control manual) |
| Llenadora de vasos LL-402 | Velocidad | 45 vasos/min (150 ml) y 35 vasos/min (300 ml) nominales |
| Enfriador CH-901 | Agua helada | 6 m³/h a 2 °C, al intercambiador de día y a la chaqueta de noche |
| Celda de encanastado R-501 (etapa posterior al proyecto) | Cadencia | 10 ciclos/min |

Las velocidades del agitador y de los equipos nuevos son valores de diseño y se ajustan en la puesta en marcha.

## 5. Parámetros de calidad

| Parámetro | Especificación | Medición actual | Medición propuesta |
| --- | --- | --- | --- |
| Leche cruda | Acidez, pH, densidad y sólidos dentro de la especificación de recepción | Laboratorio, por cantina | Igual, con registro en el sistema |
| Fin de la incubación | Acidez de 80–90 °Th; pH de 4,4 a 4,6 | Muestra y acidómetro | pH en línea (AT-301), con pH de corte de 4,5 en el lote 1 y 4,6 en el lote 2; acidez de confirmación en laboratorio |
| Dosificación de insumos | Fórmula de la receta, ± 1 % | Gramera | Celdas de carga y conteo de pulsos |
| Contenido por unidad | 195–205 ml, 146–154 ml o 293–307 ml | Una de cada cinco bolsas | 100 % de las unidades |
| Hermeticidad | Sin fugas | Presión manual de cada bolsa | Manual por muestreo; sensor de tapa en los vasos |
| Producto no conforme | Meta: 1,5 % o menos | 5,06 % | Registro automático por lote |
| Vida útil | 21 a 28 días a 4 °C | — | — |

## 6. Puntos críticos de control

| PCC | Peligro | Límite crítico | Vigilancia | Acción correctiva |
| --- | --- | --- | --- | --- |
| Pasteurización | Supervivencia de microorganismos patógenos | 85 °C o más durante el sostenimiento | TT-301 con registro continuo | Reiniciar el sostenimiento; el lote no avanza sin cumplirlo |
| Enfriamiento y almacenamiento | Crecimiento microbiano y sobreacidificación | Lote 1: 20 °C o menos a la salida de E-301. Lote 2: 15 °C o menos dentro de las 4 h siguientes al fin de la incubación. Envasado a 20 °C o menos; cuarto frío a 4 °C | TT-301, TT-302, TT-303 y TT-501 | Retener el lote y evaluar |

## 7. Limpieza CIP

| Paso | Temperatura | Tiempo (ciclo completo) |
| --- | --- | --- |
| Preenjuague con agua | Ambiente | 5 min |
| Lavado alcalino (soda) | 75–80 °C | 15 min |
| Enjuague intermedio | Ambiente | 5 min |
| Lavado ácido | 60–65 °C | 10 min |
| Enjuague final, con conductividad verificada por CT-901 | Ambiente | 5 min |
| **Total** | | **40 min** |

Entre lotes de la misma referencia basta un enjuague de 15 min.

### Referencias

- Grimaldo, G., Moreno, D. y Salamanca, M. (2015). Medición del trabajo de una línea de producción de yogurt – Empresa La Hacienda. Revista I3+, 2(2), 62–81.
- Dairy Consultant. Proceso industrial del yogur: guía completa de producción. https://dairyconsultant.co.uk/proceso-industrial-yogurt.php
- Tetra Pak. Dairy Processing Handbook, capítulo 11: Fermented milk products.
