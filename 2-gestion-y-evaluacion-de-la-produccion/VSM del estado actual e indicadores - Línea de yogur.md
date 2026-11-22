## **CREMIA AUTOMATIONS** 

# **VSM del estado actual e indicadores productivos** 

Línea de yogur de la planta La Hacienda 

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda **Módulo:** Módulo 2 · Gestión y Evaluación de la Producción Pendiente de revisión por: Ana María Orozco 

### **1. Alcance** 

Este documento contiene los datos del mapa de flujo de valor (VSM) del estado actual de la línea de yogur, los indicadores productivos calculados a partir de ellos y los datos de entrada para el modelo de simulación. La fuente de los tiempos es el estudio de La Hacienda (Grimaldo, Moreno y Salamanca, 2015) para un lote de 550 L de leche. 

### **2. Datos generales del flujo** 

|**Dato**|**Valor**|
|---|---|
|**Producto**|Yogur saborizado en bolsa de 200 ml|
|**Demanda atendida**|3.052 bolsas por día (un lote diario)|
|**Proveedor**|Ganaderos de la zona: 14 cantinas de 40 L, entrega diaria|
|**Cliente**|Distribución desde el cuarto frío, en canastas|
|**Operarios**|4|
|**Jornada**|Un turno de 8 h (480 min); inicio a las 7:30 a. m.|
|**Flujo de**<br>**información**|Programación verbal y registros en papel; no hay sistema de<br>información|



### **3. Cajas de proceso** 

|**N.**<br>**º**|**Proceso**|**Tiempo**<br>**de ciclo**<br>**(min/lote**<br>**)**|**Operario**<br>**s**|**Valor**<br>**agregad**<br>**o (min)**|**Sin valor**<br>**agregad**<br>**o (min)**|**Observacione**<br>**s**|
|---|---|---|---|---|---|---|
|**1**|Recepción de la<br>leche cruda|48,07|2|0|48,07|Descarga 3,05;<br>análisis 16,59;<br>transporte por<br>tubería 28,43|



|**2**|Alistamiento de<br>materias primas|10,21|1|0|10,21|Cálculo y<br>pesaje manual<br>6,50; transporte<br>entre cuartos<br>3,71|
|---|---|---|---|---|---|---|
|**3**|Tratamiento<br>térmico|117,55|1|117,55|0|Precalentar<br>11,08;<br>adicionar 2,84;<br>pasteurizar<br>77,43; inocular<br>26,20. Válvulas<br>manuales|
|**4**|Incubación|240,00|0|240,00|0|Tiempo fijo; el<br>tanque queda<br>ocupado|
|**—**|Espera:<br>enfriamiento<br>natural|1.024<br>≈|0|0|1.024<br>≈|Desde el fin de<br>la incubación<br>(cerca de las<br>2:26 p. m.)<br>hasta las 7:30<br>a. m. del día<br>siguiente|
|**5**|Acondicionamient<br>o|33,64|1|31,06|2,58|Romper el<br>coágulo 2,36;<br>prueba de<br>acidez 2,58;<br>saborizar 5,07;<br>filtrar 23,63|
|**6**|Empaque y control<br>de calidad|148,93|2|148,93|0|20,5<br>bolsas/min;<br>pesaje de una<br>de cada cinco<br>bolsas; 5,06 %<br>no conforme|
|**7**|Traslado al cuarto<br>frío|2,92|1|0|2,92|Canastas<br>llevadas a<br>mano|
||**Total**|**601,32**<br>**de**||**537,54**|**63,78 de**<br>**proceso**||
|||**proceso**|||**y**<br>**1.024**<br>**≈**||





**y ≈ 1.024 de de espera espera** 



La asignación de operarios por proceso es una estimación a partir de la descripción del caso. La incubación se cuenta como valor agregado porque transforma el producto. 

### **4. Línea de tiempo** 

|**Concepto**|**Valor**|**Cálculo**|
|---|---|---|
|**Tiempo de proceso (suma de**<br>**tiempos estándar)**|601,3 min<br>(10,0 h)|Dato del caso|
|**Espera por enfriamiento nocturno**|1.024 min<br>≈<br>(17,1 h)|De las 2:26 p. m. a las 7:30 a.<br>m.|
|**Tiempo de entrega (lead time)**|**1.625 min**<br>**≈**<br>**(27,1 h)**|601,3 + 1.024|
|**Tiempo con valor agregado**|537,5 min|Operaciones de transformación<br>y empaque|
|**Relación de valor agregado**|**33 %**|537,5 / 1.625|



### **5. Indicadores** 

|**Indicador**|**Valor**|**Cálculo**|
|---|---|---|
|**Takt time**|**9,4 s por bolsa**|480 min × 60 / 3.052 bolsas|
|**Tiempo de ciclo del**<br>**empaque**|2,9 s por bolsa|148,93 min × 60 / 3.052|
|**Throughput**|**3.052 bolsas por día**<br>**(610 L de yogur)**|Un lote diario|
|**Índice de procesamiento**<br>**del cuello de botella**|468 bolsas/h|3.052 / (391,19 / 60)|
|**Tiempo total de**<br>**fabricación (MLT)**|601,3 min de proceso;<br>27,1 h con la espera|Sección 4|
|**Cuello de botella**|Preparación del yogur:<br>391,19 min (65 % del<br>tiempo)|La incubación de 240 min es el<br>61 % de la preparación|



|**Calidad**|94,9 %|100 %<br>5,06 % de producto<br>−<br>no conforme|
|---|---|---|
|**Velocidad real frente a la**<br>**nominal**|68,3 %|20,5 bolsas conformes/min<br>frente a 30 bolsas/min<br>nominales|
|**OEE de la empacadora**|**68 %**<br>**≈**|Disponibilidad 90 % ×<br>rendimiento 80 % × calidad 95<br>% (sección 6)|
|**Eficiencia de materiales**|98,1 %|630,5 kg de producto / 642,7 kg<br>de insumos|
|**Productividad de la**<br>**mano de obra**|763 bolsas por operario<br>y día|3.052 / 4|
|**Utilización del tanque de**<br>**proceso**|Un lote por día|El enfriamiento nocturno impide<br>una segunda carga|



La velocidad nominal de la empacadora (30 bolsas/min) es un valor de referencia para máquinas de este tipo; el caso no reporta el tiempo de paradas por separado, de modo que el OEE es una aproximación. 

**Lectura.** El takt time (9,4 s) es mayor que el tiempo de ciclo del empaque (2,9 s): la empacadora tiene capacidad de sobra. Lo que limita la producción es el tanque de proceso, que queda ocupado desde la carga hasta la mañana siguiente. Solo un tercio del tiempo de entrega agrega valor; el resto es, sobre todo, la espera del enfriamiento. 

### **6. Estimación del OEE del proceso manual** 

El OEE (eficiencia general de los equipos) mide qué parte del tiempo planeado se convierte en producto bueno a la velocidad nominal: OEE = disponibilidad × rendimiento × calidad. Se estima para la empacadora EMP-401, la única máquina de la línea con una velocidad nominal de referencia (30 bolsas/min). El caso no reporta las paradas por separado, así que la división entre disponibilidad y rendimiento es un supuesto; el OEE total no depende de él. 

|**Factor**|**Cálculo**|**Valor**|
|---|---|---|
|**Tiempo planeado**|Duración del empaque por lote|148,9<br>min|
|**Paradas por desajuste del corte**<br>**de la bolsa**|Supuesto: unos 15 min por lote|15,0<br>min|
|**Disponibilidad**|(148,9<br>15,0) ÷ 148,9<br>−|90 %|
|**Rendimiento**|3.215 bolsas llenadas ÷ (30|80 %|



||bolsas/min × 133,9 min)||
|---|---|---|
|**Calidad**|3.052 bolsas conformes ÷ 3.215<br>llenadas|95 %|
|**OEE**|0,90 × 0,80 × 0,95|**68 %**|



Comprobación sin el supuesto de paradas: 3.052 bolsas conformes ÷ (30 bolsas/min × 148,9 min) = 68,3 %. El 72 % que se mencionó en la presentación corresponde a la disponibilidad por el rendimiento (3.215 ÷ 4.467), sin descontar la calidad. 

**Análisis.** La mayor pérdida está en el rendimiento (20 %): la empacadora trabaja más despacio que su velocidad nominal porque el operario pesa una de cada cinco bolsas y ajusta la máquina a mano. Le siguen las paradas por el corte de la bolsa (10 %) y las bolsas no conformes (5 %). Un OEE cercano a 68 % es normal en plantas pequeñas manuales, que suelen estar entre 55 y 70 %; la referencia de clase mundial es 85 %. Aun así, la empacadora no es el cuello de botella: lo es el tanque de proceso, ocupado hasta el día siguiente por el enfriamiento. 

|**Factor**|**Hoy**|**Meta con la**<br>**propuesta**|**Qué lo mejora**|
|---|---|---|---|
|**Disponibilida**<br>**d**|90<br>%|92 %|Registro automático de paradas y causas,<br>mantenimiento autónomo|
|**Rendimiento**|80<br>%|90 %|Controladora de peso en línea en lugar del<br>pesaje manual|
|**Calidad**|95<br>%|98,5 %|Peso del 100 % con rechazo automático y<br>dosificación por receta|
|**OEE**|**68**<br>**%**|**82 %**|El MES lo calcula por turno|



Si la demanda se toma como 15.000 bolsas por semana en seis días de 450 minutos, el takt sería de 10,8 s por bolsa. En los dos casos el takt es mayor que el tiempo de ciclo del empaque (2,9 s), de modo que la conclusión no cambia. 

### **7. Desperdicios identificados** 

|**Desperdicio**|**Dónde ocurre**|**Magnitud**|
|---|---|---|
|**Espera**|Enfriamiento natural en el tanque<br>de proceso|17 h por lote<br>≈|
|**Transporte**|Leche por 12 m de tubería;<br>insumos entre cuartos; canastas a<br>mano|35,1 min por lote|



|**Sobreprocesamiento**|Sostenimiento de 15 min en la<br>pasteurización y control manual de<br>válvulas|77,4 min de<br>pasteurización|
|---|---|---|
|**Defectos**|Bolsas con peso o sellado no<br>conforme|5,06 %|
|**Movimientos e**<br>**inspección manual**|Pesaje de insumos, prueba de<br>acidez y pesaje de una de cada<br>cinco bolsas|Parte de los 148,9<br>min de empaque|
|**Paradas**|Desajuste de la medida de corte<br>de la bolsa|No medidas|



### **8. Datos de entrada para la simulación** 

|**Elemento del**<br>**modelo**|**Tipo**|**Parámetro**|
|---|---|---|
|**Fuente**|Llegada de leche|Un lote de 550 L por día a las 7:30 a.<br>m.|
|**Recepción**|Estación|48,07 min por lote|
|**Alistamiento**|Estación en paralelo con<br>la recepción|10,21 min por lote|
|**Tanque de proceso**|Estación de capacidad 1<br>lote|117,55 min de tratamiento térmico,<br>240 min de incubación y enfriamiento<br>hasta el día siguiente|
|**Acondicionamiento**|Estación|33,64 min por lote|
|**Tanque pulmón**|Almacén intermedio|Capacidad de 650 L|
|**Empacadora**|Estación de<br>desensamble: 1 lote en<br>3.215 bolsas|2,9 s por bolsa; 5,06 % de rechazo<br>(3.052 conformes)|
|**Cuarto frío**|Sumidero|Canastas de 120 bolsas|
|**Recursos**|Operarios|4, en un turno de 8 h|



Las 3.215 bolsas llenadas resultan de 3.052 bolsas conformes y un 5,06 % de rechazo. 

#### **Referencias** 

- Grimaldo, G., Moreno, D. y Salamanca, M. (2015). Medición del trabajo de una 

- línea de producción de yogurt – Empresa La Hacienda. Revista I3+, 2(2), 62–81. 

- ● Rother, M. y Shook, J. (2003). Learning to See: Value Stream Mapping to Add Value and Eliminate Muda. Lean Enterprise Institute. 

