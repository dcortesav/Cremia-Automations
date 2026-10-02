# Cuello de Botella — Línea de Queso Campesino

> **Línea:** 2 – Quesos · **Lote base:** 5.000 L de leche → 666,7 kg de queso campesino
> **Referencias:** QC-250 (cuña de 250 g), QC-1K (1 kg) y QC-3K (bloque de 3 kg)
> **Base documental:** `Receta_y_Parametros_Queso.md`
> **Situación inicial supuesta:**
> - 2 tinas de 5.000 L trabajando escalonadas.
> - 2 prensas neumáticas de 200 kg por ciclo, con carga y volteo manual.
> - Moldeo manual.
> - Un pasteurizador HTST de 10.000 L/h compartido con las líneas de yogur y kumis.
> - Un cuarto de oreo con capacidad para 4 lotes.
>
> Estos supuestos forman parte de la propuesta inicial y se contrastarán con la visita técnica a Alpina Sopó (27 y 28 de octubre de 2026).

---

## 1. Ocupación de cada recurso por lote (situación inicial)

### 1.1 Tina quesera (igual para las tres referencias)

| Actividad | min |
|---|---:|
| Llenado | 30 |
| Premaduración | 15 |
| Coagulación y verificación del punto de corte | 40 |
| Corte | 8 |
| Reposo y agitación | 20 |
| Desuerado | 12 |
| Salado | 12 |
| Desuerado final y descarga a moldeo | 25 |
| CIP de la tina | 50 |
| **Ciclo de la tina** | **212** |

Con 2 tinas escalonadas sale un lote cada **212 / 2 = 106 min**.

### 1.2 Prensado

Capacidad actual: 2 prensas × 200 kg = 400 kg por ciclo. Un lote de 666,7 kg necesita **2 ciclos** en las tres presentaciones.

| Referencia | Prensado (min) | Carga y volteo manual (min) | Ciclos | **Total por lote (min)** |
|---|---:|---:|---:|---:|
| QC-250 (moldes de 3 kg) | 75 | 20 | 2 | **190** |
| QC-1K (moldes de 1 kg) | 60 | 15 | 2 | **150** |
| QC-3K (moldes de 3 kg) | 90 | 20 | 2 | **220** |

### 1.3 Resto de estaciones

| Recurso | QC-250 (min) | QC-1K (min) | QC-3K (min) | Base de cálculo |
|---|---:|---:|---:|---|
| Pasteurizador (compartido) | 30 | 30 | 30 | 5.000 L a 10.000 L/h, más 30 min de cambio si viene de yogur o kumis |
| Moldeo manual | 25 | 35 | 25 | 222, 666 y 222 moldes |
| Porcionado | 53 | — | — | 2.664 cuñas a 50 cortes/min |
| Empaque | 95 | 33 | 37 | 28, 20 y 6 und/min |
| Etiquetado de peso variable | — | — | 13 | 222 und a 17 und/min |
| Paletizado (compartido) | 11 | 6 | 6 | 10 cajas/min |
| Oreo | 600 | 480 | 720 | Demora; el cuarto admite 4 lotes a la vez |

---

## 2. Identificación del cuello de botella

| Recurso (min/lote) | QC-250 | QC-1K | QC-3K |
|---|---:|---:|---:|
| Tina (2 escalonadas) | 106 | 106 | 106 |
| **Prensado** | **190** | **150** | **220** |
| Empaque | 95 | 33 | 37 |
| Porcionado | 53 | — | — |
| Moldeo | 25 | 35 | 25 |
| Pasteurizador | 30 | 30 | 30 |

**El cuello de botella es el prensado** en las tres presentaciones. Los bloques de 3 kg (QC-250 y QC-3K) necesitan prensados largos, y cada ciclo exige cargar y voltear a mano entre 222 y 666 moldes por lote. Eso limita la capacidad, introduce variabilidad y genera riesgo ergonómico.

En QC-250 el **empaque** (95 min) es el segundo recurso más cargado, casi al nivel de la tina. Si se elimina el cuello del prensado, hay que vigilarlo.

**Producción por turno (8 h = 480 min) en la situación inicial:**

| | QC-250 | QC-1K | QC-3K |
|---|---:|---:|---:|
| Lotes por turno (480 / 190, 150, 220) | 2,5 | 3,2 | 2,2 |
| kg de queso por turno | 1.684 | 2.133 | 1.455 |
| Unidades por turno | 6.730 cuñas | 2.131 bloques | 484 bloques |

El **oreo** (8–12 h) no limita la capacidad mientras el cuarto admita 4 lotes. Aun así, es la mayor demora del flujo de valor: representa entre el 60 % y el 75 % del MLT, que va de 10 a 16 h.

---

## 3. Propuesta de solución

### 3.1 Prensado automático con volteo automático (ataca el cuello de botella)

- Pasar de 2 a **4 prensas neumáticas de túnel con volteo automático**, cargadas desde la moldeadora por transportador. Así la capacidad sube a 800 kg por ciclo y cada lote se prensa en **1 solo ciclo**.
- La carga y el volteo automáticos bajan a unos 5 min por ciclo.
- El PLC gestiona la presión (PIC-201), el tiempo de prensado y la secuencia de volteo según la presentación (receta ISA-88: 75, 60 o 90 min).

| Recurso (min/lote) | QC-250 | QC-1K | QC-3K |
|---|---:|---:|---:|
| Prensado propuesto (1 ciclo + 5 min) | 80 | 65 | 95 |
| Tina (nuevo recurso limitante) | 106 | 106 | 106 |
| Empaque | 95 | 33 | 37 |

Con esto el cuello de botella pasa a la tina, que tiene el mismo ritmo para las tres presentaciones, y la línea queda balanceada. En QC-250 el empaque (95 min) queda cerca del ritmo de la tina. Si la demanda de cuñas crece, la siguiente mejora es una termoformadora de 6 cavidades (unos 42 und/min, 63 min/lote).

### 3.2 Moldeadora automática multicabezal

La moldeadora dosifica la cuajada por peso con celdas de carga (WT-201) en moldes de 1 kg o de 3 kg según la receta. El moldeo de QC-1K baja de 35 a unos 15 min y los moldes llegan a la prensa sin manipulación manual.

### 3.3 Túnel de enfriamiento rápido (reduce el MLT)

Un túnel de aire forzado a 0–2 °C reduce el oreo de 8–12 h a 2–3 h. Esto baja el MLT de 10–16 h a 5–7 h y reduce el WIP en el cuarto frío.

### 3.4 Programación del pasteurizador compartido

Los lotes de queso se agrupan en campañas para minimizar los cambios de temperatura entre queso (72–75 °C) y yogur o kumis (85–95 °C). El tanque pulmón T-102 desacopla el pasteurizador de las tinas.

---

## 4. Resultado esperado

| Indicador | QC-250 actual → propuesto | QC-1K actual → propuesto | QC-3K actual → propuesto |
|---|---|---|---|
| Tiempo en el recurso limitante (min/lote) | 190 → 106 | 150 → 106 | 220 → 106 |
| Lotes por turno | 2,5 → 4,5 | 3,2 → 4,5 | 2,2 → 4,5 |
| kg por turno | 1.684 → 3.019 | 2.133 → 3.019 | 1.455 → 3.019 |
| Aumento de throughput | +79 % | +42 % | +108 % |
| MLT (h) | 11–15 → 5–7 | 10–14 → 5–7 | 12–16 → 6–8 |
| Moldes manipulados a mano por lote | 222 → 0 | 666 → 0 | 222 → 0 |

Estos resultados se verificarán con la simulación de eventos discretos en Siemens Tecnomatix y se reflejarán en el VSM "antes y después".
