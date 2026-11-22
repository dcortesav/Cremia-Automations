# **CREMIA AUTOMATIONS Parámetros de proceso de la línea de yogur** 

Temperaturas, tiempos, velocidades y límites de control 

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda **Módulo:** Módulo 1 · Transformación Digital Industrial Pendiente de revisión por: David Santiago Cortés 

## **1. Alcance** 

Este documento reúne los parámetros de proceso de la línea de yogur: los que usa hoy la planta, según el caso de estudio, y los de la propuesta. Para cada parámetro se indica la consigna, el límite de alarma y el instrumento que lo mide. 

## **2. Temperaturas** 

|**Etapa**|**Valor**<br>**actual**|**Consigna**<br>**propuesta**|**Alarma**|**Instrumento**|
|---|---|---|---|---|
|Leche en<br>recepción|Ambiente;<br>se procesa<br>al recibirla|Sin cambio|—|Termómetro<br>de laboratorio|
|Precalentamiento|25 °C|25 °C|± 3 °C|TT-301|
|Homogeneización|No se hace|60–65 °C|± 3 °C|TT-301|
|**Pasteurización**|**85 °C**|**85–90 °C**|**Baja: 85 °C**<br>**(reinicia el**<br>**sostenimiento)**|TT-301, con<br>registro|
|Inoculación|42–45 °C|43 °C|Alta: 46 °C|TT-301|
|Incubación|41–45 °C|43 °C|± 2 °C|TT-301|
|Salida del enfriador<br>de placas|No existe|15–20 °C|Alta: 20 °C|TT-302|
|Agua helada|No existe|2 °C|Alta: 5 °C|TT-901|
|Tanque pulmón<br>durante el<br>envasado|Sin control|20 °C o<br>menos|Alta: 20 °C|TT-303|
|Cuarto frío|4 °C|4 °C|Alta: 6 °C|TT-501|



## **3. Tiempos** 

|**Etapa**|**Tiempo actual**<br>**(min)**|**Tiempo propuesto**<br>**(min)**|**Observación**|
|---|---|---|---|
|Descarga y análisis<br>de la leche|19,6|19,6|Análisis manual por<br>cantina|
|Transferencia de 550<br>L al tanque de<br>proceso|28,4|12|Bomba de 3 m³/h|
|Alistamiento y pesaje<br>de insumos|10,2|2|Dosificación<br>automática|
|Precalentamiento y<br>adición de azúcar|13,9|12||
|Estandarización y<br>homogeneización|No se hace|En paralelo con el<br>calentamiento|Leche en polvo<br>dosificada por peso<br>y recirculación por<br>H-301|
|Pasteurización:<br>calentamiento y<br>sostenimiento|77,4 (sostenimiento<br>de 15)|60 (sostenimiento<br>de 5 a 10)|El sostenimiento<br>final se valida con<br>pruebas|
|Enfriamiento hasta la<br>inoculación|26,2|15|Control automático<br>del agua fría|
|**Incubación**|**240**|**240 (termina por**<br>**pH)**|Tiempo fijo del<br>proceso; máximo<br>de 300 min con<br>alarma|
|Ruptura del coágulo,<br>acidez y saborizado|10,0|5||
|Enfriamiento, filtrado<br>y transferencia|23,6, más el<br>enfriamiento<br>nocturno|25|Intercambiador de<br>placas a 1.500 L/h|
|Envasado y control<br>de peso (YB-200)|148,9|102|30 bolsas/min con<br>control de peso en<br>línea|
|Traslado al cuarto frío|2,9|En paralelo con el<br>envasado|Banda<br>transportadora|
|Limpieza CIP|Manual, no medida|40|En cada cambio de<br>sabor|
|**Total por lote**|**601,3**|**493**<br>**≈**||



## **4. Velocidades y caudales** 

|**Equipo**|**Parámetro**|**Valor**|
|---|---|---|
|Bomba de leche P-101|Caudal|3 m³/h|
|Dosificador de azúcar<br>DS-201|Caudal grueso y de afine|10 kg/min y 1 kg/min|
|Homogeneizador H-301|Presión y caudal|150–200 bar; 1.500 L/h|
|Agitador M-301|Mezcla y tratamiento<br>térmico|40–60 rpm|
||Incubación|Detenido|
||Ruptura del coágulo:<br>producto bebible|30–40 rpm|
||Ruptura del coágulo:<br>producto en vaso|15–20 rpm|
|Bomba de lóbulos P-301|Caudal de transferencia|1.500 L/h|
|Bomba de fruta P-403|Relación con el caudal de<br>yogur|8 % (YV-150) o 12 %<br>(YV-300)|
|Empacadora de bolsas<br>EMP-401|Velocidad|30 bolsas/min (hoy, 20,5<br>con paradas y control<br>manual)|
|Llenadora de vasos LL-402|Velocidad|45 vasos/min (150 ml) y<br>35 vasos/min (300 ml)|
|Celda de encanastado<br>R-501 (etapa posterior al<br>proyecto)|Cadencia|10 ciclos/min|



_Las velocidades del agitador y de los equipos nuevos son valores de diseño y se ajustan en la puesta en marcha._ 

## **5. Parámetros de calidad** 

|**Parámetro**|**Especificación**|**Medición actual**|**Medición**<br>**propuesta**|
|---|---|---|---|
|Leche cruda|Acidez, pH, densidad<br>y sólidos dentro de la<br>especificación de<br>recepción|Laboratorio, por<br>cantina|Igual, con registro<br>en el sistema|
|Fin de la incubación|Acidez de 80–90 °Th;<br>pH de 4,4 a 4,6|Muestra y<br>acidómetro|pH en línea<br>(AT-301)|



|Dosificación de<br>insumos|Fórmula de la receta,<br>± 1 %|Gramera|Celdas de carga y<br>conteo de pulsos|
|---|---|---|---|
|Contenido por<br>unidad|195–205 ml, 146–154<br>ml o 293–307 ml|Una de cada cinco<br>bolsas|100 % de las<br>unidades|
|Hermeticidad|Sin fugas|Presión manual de<br>cada bolsa|Manual por<br>muestreo; sensor<br>de tapa en los<br>vasos|
|Producto no<br>conforme|Meta: 1,5 % o menos|5,06 %|Registro<br>automático por<br>lote|
|Vida útil|21 a 28 días a 4 °C|—|—|



## **6. Puntos críticos de control** 

|**PCC**|**Peligro**|**Límite crítico**|**Vigilancia**|**Acción**<br>**correctiva**|
|---|---|---|---|---|
|Pasteurización|Supervivencia de<br>microorganismos<br>patógenos|85 °C o más<br>durante el<br>sostenimiento|TT-301 con<br>registro<br>continuo|Reiniciar el<br>sostenimiento;<br>el lote no<br>avanza sin<br>cumplirlo|
|Enfriamiento y<br>almacenamiento|Crecimiento<br>microbiano y<br>sobreacidificación|Envasado a 20<br>°C o menos;<br>cuarto frío a 4<br>°C|TT-302,<br>TT-303 y<br>TT-501|Retener el lote<br>y evaluar|



### **Referencias** 

- Grimaldo, G., Moreno, D. y Salamanca, M. (2015). Medición del trabajo de una línea de producción de yogurt – Empresa La Hacienda. Revista I3+, 2(2), 62–81. 

- Dairy Consultant. Proceso industrial del yogur: guía completa de producción. https://dairyconsultant.co.uk/proceso-industrial-yogurt.php 

- Tetra Pak. Dairy Processing Handbook, capítulo 11: Fermented milk products. 

