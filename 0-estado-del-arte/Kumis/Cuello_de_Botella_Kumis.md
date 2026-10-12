# Cuello de Botella — Línea de Kumis

> **Línea:** 3 – Kumis · **Lote base:** 2.000 L (2.060 kg) por fermentador
> **Referencias:** KU-200 (vaso de 200 g), KU-1L (botella de 1 L) y KU-NAT (bolsa de 1 kg natural)
> **Base documental:** `Receta_y_Parametros_Kumis.md`
> **Situación inicial supuesta:**
> - 3 fermentadores de 2.000 L en una sala aislada con presión positiva.
> - Formulación en un solo tanque de 2.500 L con dosificación manual de sacos y un Triblender.
> - Un skid HTST de 2.500 L/h y un homogeneizador, con el CIP en tiempos fijos.
> - Una envasadora por formato (botella, vaso y bolsa), con cambio de formato manual.
> - Punto final de la fermentación verificado por muestreo y titulación manual.
> - Encajonado y paletizado manual (5 cajas/min).
> - Cámara de maduración con estibas sin enfriamiento previo.
>
> Estos supuestos forman parte de la propuesta inicial y se contrastarán con la visita técnica a Alpina Sopó (27 y 28 de octubre de 2026).

---

## 1. Ocupación de cada recurso por lote (situación inicial)

### 1.1 Fermentador (la ocupación cambia con la referencia)

La fermentación no ocupa turnos: sigue durante la noche. Pero el llenado y la descarga se hacen dentro de los dos turnos de 8 h, y la ocupación total del fermentador (18 a 21 h) no permite un segundo lote el mismo día. **Cada fermentador completa un lote por día.**

**KU-1L (botella de 1 L):**

| Actividad | min |
|---|---:|
| Llenado desde el HTST | 48 |
| Inoculación y ajuste de temperatura | 20 |
| Fermentación | 960 |
| Verificación del punto de corte (manual) | 15 |
| Rotura y choque frío | 45 |
| Descarga al envasado | 30 |
| CIP del fermentador | 60 |
| **Ocupación del fermentador** | **1.178** |

| Ocupación del fermentador (min) | KU-200 | KU-1L | KU-NAT |
|---|---:|---:|---:|
| Situación inicial | 1.251 | 1.178 | 1.080 |
| Horas | 20,9 | 19,6 | 18,0 |

Con 3 fermentadores y un lote por día cada uno, la capacidad máxima es de **3 lotes por día**. El intervalo entre arranques de lote es de 900 / 3 = **300 min**.

### 1.2 Resto de estaciones

| Recurso | KU-200 (min) | KU-1L (min) | KU-NAT (min) | Base de cálculo |
|---|---:|---:|---:|---|
| Estandarización (compartida) | 12 | 12 | 12 | 2.000 L a 10.000 L/h |
| Formulación (ciclo del tanque, con CIP de 40 min) | 178 | 178 | 163 | Proceso 90/90/75 min + 48 min de transferencia al HTST |
| HTST | 48 | 48 | 48 | 2.000 L a 2.500 L/h |
| Envasado | 103 | 30 | 52 | 10.300 vasos, 2.000 botellas y 2.060 bolsas |
| Cambio de formato | 40 | 45 | 30 | Manual |
| Encajonado y paletizado manual | 86 | 33 | 34 | 429, 167 y 172 cajas a 5 cajas/min |
| Maduración fría | 1.800 | 2.160 | 1.920 | Enfriamiento al núcleo (6, 12 y 8 h) + 24 h de reposo |

---

## 2. Identificación del cuello de botella

Se compara el intervalo mínimo entre lotes que admite cada recurso con el takt de la línea (900 min / 4 lotes = **225 min/lote**).

| Recurso (min/lote) | KU-200 | KU-1L | KU-NAT |
|---|---:|---:|---:|
| **Fermentación (3 fermentadores, 1 lote/día cada uno)** | **300** | **300** | **300** |
| Formulación | 178 | 178 | 163 |
| Envasado con cambio de formato | 143 | 75 | 82 |
| Encajonado y paletizado | 86 | 33 | 34 |
| HTST | 48 | 48 | 48 |

**El cuello de botella es la fermentación** en las tres referencias. La fermentación mesófila dura de 14 a 18 horas y se hace en reposo absoluto: no se puede acelerar sin cambiar el producto (por encima de 30 °C se inhibe el diacetilo). Con 3 fermentadores solo se arrancan 3 lotes por día, frente a los 4 que pide la demanda.

El **envasado del vaso de 200 g** es el segundo recurso más cargado (143 min por lote con el cambio de formato): hoy no limita, pero conviene vigilarlo si crece la demanda de vasos. La **maduración** (30 a 36 h) no limita la capacidad mientras la cámara tenga espacio, pero es la mayor demora del flujo de valor: representa entre el 56 % y el 63 % del MLT.

**Producción por turno (8 h) en la situación inicial** (capacidad × disponibilidad × tasa de eficiencia = 2,51 lotes/día):

| | Valor |
|---|---:|
| Lotes por día | 2,51 |
| Lotes por turno | 1,25 |
| kg de kumis por día | 5.166 |
| kg de kumis por turno | 2.583 |
| Cumplimiento de la demanda (4 lotes/día) | 63 % |

Con otras pérdidas habituales: los lotes perdidos por bacteriófagos o acidez fuera de rango, y las paradas de la sala de fermentación, reducen la disponibilidad al 88 % (ver `VSM_e_Indicadores_Kumis.md`).

---

## 3. Propuesta de solución

### 3.1 Más fermentadores y control automático del punto final (ataca el cuello de botella)

- Pasar de 3 a **5 fermentadores de 2.000 L** en la misma sala aislada. La capacidad sube a 5 lotes por día y el intervalo entre arranques baja a 900 / 5 = **180 min**.
- Medir el pH en línea (AT-501) y cortar la fermentación al llegar a pH 4,55, con perfil de temperatura y rotura automática. Se elimina el muestreo manual y el margen de seguridad que alarga la fermentación (−60 min por lote).
- Inoculación automática por el puerto aséptico (de 20 a 10 min) y CIP de fermentador más corto (de 60 a 40 min) con sensores de conductividad y turbidez.

| Recurso (min/lote) | KU-200 | KU-1L | KU-NAT |
|---|---:|---:|---:|
| Ocupación del fermentador propuesta | 1.141 | 1.068 | 970 |
| Intervalo entre arranques propuesto (900 / 5) | 180 | 180 | 180 |
| Takt | 225 | 225 | 225 |

Con esto el intervalo del recurso limitante queda por debajo del takt y la línea llega a la demanda. El siguiente recurso más cargado pasa a ser la formulación o el envasado de vasos (ver 3.2 y 3.4).

### 3.2 Formulación automática

Dosificación gravimétrica de sacarosa y LPD con receta ISA-88, y dispersión en el Triblender mientras se llena el tanque. El proceso baja de 90 a 45 min por lote y el ciclo del tanque, de 178 a 123 min. Se elimina el manejo manual de sacos de 25 kg y el riesgo de grumos.

### 3.3 Túnel de enfriamiento rápido (reduce el MLT)

Un túnel de aire forzado a 0–2 °C lleva el núcleo del producto a ≤ 4 °C en 2–3 horas. Hoy los fardos y las estibas tardan de 6 a 12 horas en enfriarse dentro de la cámara. Como el reposo de 24 horas empieza cuando el núcleo llega a 4 °C, la maduración baja de 36 h a 27 h en KU-1L.

### 3.4 Cambio de formato rápido y paletizado robotizado

- Reducir el cambio de formato de 45/40/30 min a 20/20/15 min con kits de formato y pasos en paralelo.
- Encajonadora automática y celda robotizada compartida (10 cajas/min): el encajonado de KU-1L baja de 33 a 17 min por lote y se eliminan 3 operarios por turno.

### 3.5 Blindaje fágico y CIP inteligente (mejora la calidad)

Monitoreo de la presión de la sala (PDT-510), rotación de cepas DVS gestionada desde el MES y registro del lote de cultivo. Se espera reducir los lotes perdidos y subir la tasa de calidad del 95,5 % al 98,5 %.

---

## 4. Resultado esperado

| Indicador | KU-200 actual → propuesto | KU-1L actual → propuesto | KU-NAT actual → propuesto |
|---|---|---|---|
| Intervalo del recurso limitante (min/lote) | 300 → 180 | 300 → 180 | 300 → 180 |
| Ocupación del fermentador (min) | 1.251 → 1.141 | 1.178 → 1.068 | 1.080 → 970 |
| Lotes por día | 2,51 → 4,00 | 2,51 → 4,00 | 2,51 → 4,00 |
| kg por día | 5.166 → 8.240 | 5.166 → 8.240 | 5.166 → 8.240 |
| Aumento de throughput | +59 % | +59 % | +59 % |
| MLT (h) | 53,2 → 46,0 | 57,1 → 45,3 | 51,2 → 42,6 |
| Muestreos manuales de punto final por lote | 1 → 0 | 1 → 0 | 1 → 0 |

La producción por día es la de la línea completa con la mezcla de 2 lotes de KU-1L, 1 de KU-200 y 1 de KU-NAT; por eso es igual en las tres columnas.

Estos resultados se verificarán con la simulación de eventos discretos en Siemens Tecnomatix y se reflejarán en el VSM "antes y después".
