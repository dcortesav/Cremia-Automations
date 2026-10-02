# P&ID — Línea 2: Queso Campesino

> **Plano:** P&ID-L2-001 · Rev. A · Norma ANSI/ISA-5.1
> **Alcance:** recepción y almacenamiento de leche (área 100, compartida), tratamiento térmico (área 150, compartida), quesería (área 200) y manejo de suero (área 300). Desde el desmoldeo, las operaciones son discretas (oreo, porcionado, empaque, inspección y paletizado) y se representan en el diagrama de flujo del proceso.
> **Archivos:** `PID_Queso.svg` (plano) · `generar_pid.js` (fuente del plano; se regenera con `node generar_pid.js`).

![P&ID Línea 2 Queso campesino](PID_Queso.svg)

---

## 1. Lista de equipos

| Tag | Equipo | Área | Especificación de referencia |
|---|---|---|---|
| TK-100 | Carrotanque de leche cruda | 100 | 10.000 L, ≤ 6 °C |
| P-101 | Bomba sanitaria de recepción | 100 | Centrífuga, 20–30 m³/h |
| F-101 | Filtro de línea | 100 | Malla de 100–200 µm |
| E-101 | Enfriador de placas | 100 | Agua helada a 1 °C; salida ≤ 4 °C |
| T-101 | Silo de leche cruda | 100 | 25.000 L, isotérmico, agitador M-101 |
| P-102 | Bomba de alimentación a tratamiento | 100 | Centrífuga, 10 m³/h |
| CF-101 | Clarificadora / bactofugadora | 100 | 10.000 L/h |
| SE-101 | Separadora-estandarizadora | 100 | 10.000 L/h; grasa 3,0 % |
| BT-101 | Tanque de balance del pasteurizador | 150 | 200 L |
| P-150 | Bomba de alimentación del pasteurizador | 150 | Centrífuga, 10 m³/h |
| PA-101 | Pasteurizador HTST de placas | 150 | 10.000 L/h; secciones de regeneración, calentamiento y enfriamiento |
| HT-101 | Tubo de retención | 150 | 15–20 s a caudal nominal |
| T-102 | Tanque pulmón de leche pasteurizada | 150 | 10.000 L |
| P-201 | Bomba de llenado de tinas | 200 | Centrífuga, 10 m³/h |
| V-201 / V-202 | Tinas queseras de doble camisa | 200 | 5.000 L; liras de corte y agitación con motor M-201 y VFD |
| P-204 / P-205 | Bombas dosificadoras de CaCl₂ y cuajo | 200 | Peristálticas / de diafragma |
| P-202 | Bomba de suero | 300 | Centrífuga, 15–20 m³/h |
| T-301 | Tanque de suero refrigerado | 300 | 10.000 L, ≤ 6 °C |
| P-203 | Bomba de cuajada | 200 | De lóbulos, 8–12 m³/h |
| ML-201 | Moldeadora por peso | 200 | Multicabezal con celdas de carga; moldes de 1 kg (QC-1K) o 3 kg (QC-250, QC-3K) |
| PR-201…204 | Prensas neumáticas con volteo automático | 200 | 200 kg por ciclo cada una; 1,5–3 bar |

---

## 2. Índice de instrumentos

| Tag | Descripción | Variable | Rango / punto de ajuste | Ubicación | Función |
|---|---|---|---|---|---|
| FT-101 | Caudalímetro másico (Coriolis) de recepción | Flujo | 0–30 m³/h | Campo | Medición de leche recibida |
| FQI-101 | Totalizador de leche recibida | Flujo | L por carrotanque | PLC / SCADA | Registro de volumen por proveedor (trazabilidad) |
| TT-101 | Temperatura a la salida del enfriador | Temperatura | 0–20 °C; SP 4 °C | Campo (PT100) | Lazo TIC-101 |
| TIC-101 | Control de temperatura de enfriamiento | Temperatura | SP 4 °C | PLC | PID sobre TV-101 |
| TV-101 | Válvula de control de agua helada | — | 0–100 % | Campo | Elemento final del lazo 101 |
| LT-101 | Nivel del silo | Nivel | 0–25.000 L | Campo (radar) | Inventario |
| LAHL-101 | Alarma de nivel alto y bajo del silo | Nivel | 95 % / 10 % | PLC / SCADA | Protege contra rebose y cavitación |
| TT-102 | Temperatura del silo | Temperatura | 0–20 °C; alarma > 6 °C | Campo (PT100) | Cadena de frío |
| AT-101 | Analizador de grasa en línea | Análisis | 0–5 % grasa | Campo | Lazo AIC-101 |
| AIC-101 | Control de estandarización | Análisis | SP 3,0 % | PLC | Ajusta FV-101 (salida de crema) |
| FV-101 | Válvula de control de crema | — | 0–100 % | Campo | Elemento final del lazo AIC-101 |
| LT-150 | Nivel del tanque de balance | Nivel | 0–200 L | Campo | Protege la bomba P-150 |
| TT-103 | Temperatura a la salida del tubo de retención | Temperatura | 50–100 °C; SP 73 °C | Campo (PT100 doble) | **PCC** |
| TIC-103 | Control de temperatura de pasteurización | Temperatura | SP 73 °C | PLC | PID sobre TV-103 |
| TR-103 | Registrador de pasteurización | Temperatura | — | SCADA / historiador | Evidencia del PCC (HACCP) |
| TSL-103 | Interruptor por baja temperatura | Temperatura | < 72 °C | PLC | Activa la desviación de flujo XV-101 |
| XV-101 | Válvula de desviación de flujo (FDV) | — | Abierta / cerrada | Campo | Devuelve la leche a BT-101 si T < 72 °C |
| TV-103 | Válvula de agua caliente / vapor | — | 0–100 % | Campo | Elemento final del lazo 103 |
| TT-104 | Temperatura de la leche pasteurizada a la salida | Temperatura | 0–50 °C; SP 32–35 °C | Campo | Verifica la temperatura de coagulación |
| LT-102 | Nivel del tanque pulmón | Nivel | 0–10.000 L | Campo | Programación del llenado de tinas |
| FQ-201 | Totalizador de llenado de tina | Flujo | 0–5.000 L | Campo / PLC | Carga por receta |
| TT-201 | Temperatura de la tina | Temperatura | 0–50 °C; SP 32–36 °C | Campo (PT100) | Lazo TIC-201 |
| TIC-201 | Control de temperatura de la camisa | Temperatura | SP según fase de la receta | PLC | PID sobre TV-201 |
| TV-201 | Válvula de agua caliente de la camisa | — | 0–100 % | Campo | Elemento final del lazo 201 |
| LT-201 | Nivel de la tina | Nivel | 0–5.000 L | Campo | Control de llenado y desuerado |
| SIC-201 | Control de velocidad de liras (VFD) | Velocidad | 0–15 rpm; perfil por fase | PLC | Premaduración, corte y agitación |
| FQ-204 / 205 | Totalizadores de dosificación de CaCl₂ y cuajo | Flujo | mL por lote | PLC | Dosis por receta (ISA-88) |
| XV-202 | Válvula de descarga de suero | — | Abierta / cerrada | Campo | Secuencia de desuerado |
| XV-203 | Válvula de descarga de cuajada | — | Abierta / cerrada | Campo | Secuencia de moldeo |
| LT-301 | Nivel del tanque de suero | Nivel | 0–10.000 L | Campo | Inventario de subproducto |
| TT-301 | Temperatura del tanque de suero | Temperatura | 0–20 °C | Campo | Conservación del suero |
| WT-201 | Celda de carga de la moldeadora | Peso | 0–5 kg por cabezal; SP 1,0 o 3,0 kg | Campo | Llenado por peso según la presentación |
| PIC-201 | Control de presión de prensado | Presión | 0–6 bar; SP 1,5–3 bar | PLC | Presión y tiempo por presentación (75 / 60 / 90 min) |

---

## 3. Lazos de control

| Lazo | Variable controlada | Variable manipulada | Tipo | Observación |
|---|---|---|---|---|
| 101 | Temperatura de la leche cruda (TT-101) | Agua helada (TV-101) | PID | Cadena de frío en la recepción |
| AIC-101 | % de grasa (AT-101) | Salida de crema (FV-101) | PID | Grasa objetivo 3,0 % (receta única) |
| 103 | Temperatura de pasteurización (TT-103) | Agua caliente / vapor (TV-103) | PID + enclavamiento TSL-103 → XV-101 | **PCC**, registro continuo TR-103 |
| 201 | Temperatura de la tina (TT-201) | Agua caliente de la camisa (TV-201) | PID con perfil por fase | Parte del procedimiento ISA-88 |
| SIC-201 | Velocidad de las liras | Frecuencia del VFD | Secuencial por fase | Premaduración, corte y agitación en rampa |
| PIC-201 | Presión de prensado | Regulador proporcional neumático | PID + temporizador | Tiempo y presión por presentación |
