## 5. Defensa directa ante objeciones de evaluación (Preguntas y Respuestas)

### P1. Si la celda `R-501` no se compra en este proyecto, ¿por qué invertir `120 horas` de ingeniería en diseñarla (`1.3.4`) y simularla en RobotStudio (`1.7.2`)?

**Respuesta:** El paquete `1.3.4` (`60 h`) y el paquete `1.7.2` (`60 h`) cubren principalmente la estación manual vigente (`MA-501`, análisis de riesgos de `U8` y simulación del envasado en Tecnomatix); la fracción dedicada a reservar `R-501` y validar su envolvente en **RobotStudio** representa apenas unas decenas de horas de ingeniería (menos de `COP 3 millones` dentro de los `COP 333,7 millones` totales). En contraste, **omitir esa reserva hoy obligaría en el futuro a reubicar tableros, romper o reencaminar bandas, ampliar el conmutador de red, modificar la lógica base del `PLC-01` y asumir una nueva parada de planta**. Validar el modelo en RobotStudio hoy deja un activo de ingeniería listo (*ready-to-procure*) y demuestra cuantitativamente que la decisión de diferir se tomó con rigor técnico, no por improvisación.

### P2. ¿Por qué especificar un robot industrial vallado (`ABB IRB 460`, ISO 10218-1/-2) y no un robot colaborativo (cobot, ISO/TS 15066) que ahorre el vallado?

**Respuesta:** Por tres restricciones físicas y normativas concretas:
1. **Carga útil y momento de inercia:** Una canasta de `120` bolsas `YB-200` pesa **`~26,8 kg`** (cerca de `29 kg` con herramienta de fin de brazo). La mayoría de cobots industriales estándar tienen cargas útiles de `5` a `20 kg`, y los modelos pesados de `25–30 kg` cuestan tanto como un paletizador dedicado con menor rigidez y velocidad.
2. **Límites biomecánicos de ISO/TS 15066:** En modo colaborativo sin resguardos (*Power and Force Limiting*), la energía cinética de una masa de `~27 kg` obliga a limitar drásticamente la velocidad lineal del brazo, anulando la ventaja de cadencia ante un futuro escalamiento a `3–4 lotes/día`.
3. **Higiene y ambiente húmedo lácteo:** En zona de lavado de planta de alimentos, un robot industrial con protección IP adecuada y vallado perimetral **PL d** lavable protege al operador de proyecciones y resguarda la celda frente a golpes de estibadores o agua de limpieza.

### P3. Manipular canastas de `~27 kg` y cajas cada `39 s` de forma manual, ¿no representa un riesgo ergonómico inaceptable bajo la normativa de SST?

**Respuesta:** El análisis ergonómico depende tanto del **peso** como de la **frecuencia** y la **duración acumulada**. Con `2 lotes/día`:
- En bolsas (`YB-200`), solo salen `26 canastas` por lote (`1` cada **`4,8 min`** efectivos durante `124 min`), permitiendo apilar en estiba baja sobre plataforma rodante o transpaleta a la altura de la banda `CV-501` sin levantamientos por encima de los hombros.
- En vasos (`YV-150` y `YV-300`), las cajas pesan apenas **`4,0 kg`** y **`6,2 kg`**, muy por debajo del límite de referencia de carga manual (`25 kg` en levantamiento ideal según guías SST/NIOSH), y la mesa acumuladora **`MA-501`** evita posturas forzadas al mantener un búfer de `2 min` a altura ergonómica (`~850–900 mm`).
- Además, si en una auditoría de SST se deseara reducir aún más el esfuerzo al manipular canastas de `YB-200`, un apilador/elevador neumático de canastas o mesa tijera cuesta menos de `COP 10 millones`, frente a los **`COP 210 millones`** de `R-501`.

### P4. ¿Cómo garantiza `R-501` el cumplimiento sanitario (Resolución 2674 de 2013) y qué efecto tiene la altitud de Guasca (`2.600 msnm`) sobre la celda?

**Respuesta:**
- **Inocuidad alimentaria:** En `U8` no existe producto abierto; el robot manipula exclusivamente **empaque secundario** (bolsas selladas dentro de canastas y cajas cerradas de vasos previamente verificados por `CK-401/402` y `ZS-403`). Por tanto, no requiere acero 316L en contacto con alimento ni limpieza CIP ácida/alcalina. No obstante, el diseño contempla materiales lavables, lubricante grado alimentario **NSF H1** en articulaciones, ventosas de silicona grado alimentario y aire comprimido filtrado y libre de aceite/humedad.
- **Altitud (`2.600 msnm`, `~74 kPa`):** Así como se verificó el `NPSH` de la bomba `P-101` en `U1`, la menor presión atmosférica reduce el vacío diferencial disponible aproximadamente en un `27 %`. En el diseño de `1.3.4` esto se compensa sobredimensionando el diámetro/número de ventosas y seleccionando generadores de vacío multietapa de alto caudal para asegurar la retención segura de cajas húmedas por condensación.

### P5. ¿Cuál es el costo de oportunidad de invertir esos `COP 210 millones` en `R-501` frente a otras prioridades de La Hacienda?

**Respuesta:** El dinero invertido en `R-501` hoy tiene un **costo de oportunidad directo contra la capacidad de proceso**. La restricción maestra de La Hacienda está en **`U3` (`T-301` ocupado 24 h con dos lotes)**. Destinar `COP 210 millones` a paletizar un flujo que hoy atiende un solo operario en medio turno genera **`0` litros adicionales de yogur** y **`0` pesos de ahorro en nómina**, mientras destruye **`COP 144,9 millones`** de VPN y deja el proyecto al borde de la pérdida (`98,0 %` de equilibrio). En una futura fase de expansión, ese mismo capital aporta mucho mayor retorno si se destina primero a ampliar capacidad de fermentación (`segundo tanque de proceso`) y solo después a robotizar el final de línea.

### P6. Cuando la planta alcance los `3–4 lotes/día` y decida comprar `R-501`, ¿cómo se integra sin detener la producción de la línea?

**Respuesta:** La integración está diseñada para ejecutarse con **cero parada prolongada** en producción gracias a las reservas construidas durante el proyecto actual:
1. **Obra civil y mecánica en paralelo:** La huella de `3,8 m × 3,4 m` junto a `CF-501` ya queda despejada; el anclaje del `IRB 460`, el vallado perimetral y las cortinas de luz se montan fuera del horario de envasado (antes de las `10:30` o después de las `17:30`).
2. **Interfaz eléctrica y OT preexistente:** El tablero de envasado ya cuenta con reserva del `20 %` y las `3 DI` asignadas (`ZS-501`, puerta y paro de emergencia); el conmutador **`Stratix 5700`** ya tiene el puerto reservado para el nodo **`#20` EtherNet/IP**.
3. **Software abierto propiedad de la planta:** Con la licencia perpetua de **Studio 5000** (`rubro 20`) incluida para La Hacienda, se habilita la subrutina de celda en `PLC-01` (probada previamente en **RobotStudio** + gemelo digital) y se empalma la salida de `CV-501` desplazando `MA-501` en una ventana dominical de tarde (`después de las 10:30`), sin interrumpir el programa semanal de lotes.

---