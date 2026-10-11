# Análisis Económico — Línea 2: Queso Campesino

> **Alcance:** flujo de caja e indicadores financieros (VPN, TIR, periodo de recuperación y relación beneficio/costo) de la automatización de la línea de queso campesino. Es el aporte de la línea 2 al análisis económico general del proyecto.

> **Base documental:** `Presupuesto_Linea_Queso.md` (inversión) y `VSM_e_Indicadores_Queso.md` (producción antes y después).

> **Nota:** el margen por kilogramo, la rampa de ventas y la tasa de descuento son supuestos de la propuesta inicial. La sección 5 muestra cómo cambian los resultados al variarlos.

---

## 1. Supuestos

| Supuesto | Valor | Fuente |
|---|---|---|
| Inversión total | COP 2.832,5 millones | `Presupuesto_Linea_Queso.md` |
| Producción conforme actual | 2.544 kg/día (2.650 kg con 96 % de calidad) | `VSM_e_Indicadores_Queso.md` |
| Producción conforme propuesta | 4.597 kg/día (4.667 kg con 98,5 % de calidad) | `VSM_e_Indicadores_Queso.md` |
| Producción adicional | 2.053 kg/día → **615.900 kg/año** (300 días) | Diferencia |
| Margen de contribución por kg adicional | COP 5.000 | Supuesto conservador |
| Rampa de ventas del volumen adicional | 40 %, 60 %, 80 %, 100 % y 100 % en los años 1 a 5 | Supuesto |
| Ahorro en mano de obra | 6 operarios por turno × 2 turnos × COP 2,8 millones/mes = COP 403,2 millones/año | VSM: de 14 a 8 operarios por turno |
| Operación y mantenimiento | COP 141,6 millones/año (5 % de la inversión) | `Presupuesto_Linea_Queso.md` |
| Horizonte de evaluación | 5 años | |
| Tasa de descuento | 15 % anual | Supuesto |

El análisis es antes de impuestos y no incluye valor de salvamento. Los 12 operarios liberados se reubican en otras áreas de la planta; el ahorro corresponde al costo que la línea deja de cargar.

---

## 2. Flujo de caja (millones de COP)

| Concepto | Año 0 | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 |
|---|---:|---:|---:|---:|---:|---:|
| Inversión | −2.832,5 | | | | | |
| Margen por producción adicional | | 1.231,8 | 1.847,7 | 2.463,7 | 3.079,6 | 3.079,6 |
| Ahorro en mano de obra | | 403,2 | 403,2 | 403,2 | 403,2 | 403,2 |
| Operación y mantenimiento | | −141,6 | −141,6 | −141,6 | −141,6 | −141,6 |
| **Flujo neto** | **−2.832,5** | **1.493,4** | **2.109,3** | **2.725,2** | **3.341,1** | **3.341,1** |
| Flujo acumulado | −2.832,5 | −1.339,1 | 770,2 | 3.495,4 | 6.836,5 | 10.177,6 |

---

## 3. Indicadores financieros

| Indicador | Valor | Criterio |
|---|---:|---|
| **VPN (15 %)** | **COP 5.424 millones** | Mayor que cero: viable |
| **TIR** | **69,2 %** | Mayor que la tasa de descuento |
| **Periodo de recuperación** | **1,6 años** | Dentro del horizonte |
| **Relación beneficio/costo** | **2,9** | Mayor que 1 |

---

## 4. Origen del beneficio

El 88 % del beneficio del año 5 viene de vender la producción adicional y el 12 % del ahorro en mano de obra. La inversión se justifica por el aumento de capacidad: pasar del 57 % al 100 % de cumplimiento de la demanda.

---

## 5. Análisis de sensibilidad

| Escenario | Margen (COP/kg) | Volumen adicional vendido | VPN (millones de COP) | TIR | Recuperación |
|---|---:|---:|---:|---:|---:|
| Base | 5.000 | 100 % (con rampa) | 5.424 | 69,2 % | 1,6 años |
| Conservador | 3.000 | 100 % (con rampa) | 2.472 | 42,8 % | 2,3 años |
| Pesimista | 3.000 | 50 % (con rampa) | 258 | 18,4 % | 3,3 años |
| Solo ahorro de mano de obra | — | 0 % | −1.956 | Negativa | No se recupera |

El proyecto es viable mientras exista demanda para el volumen adicional. Si la línea no vende más queso del que produce hoy, el ahorro de mano de obra no alcanza para pagar la inversión. Por eso la demanda de 7 lotes diarios es el supuesto que más conviene validar con el cliente.
