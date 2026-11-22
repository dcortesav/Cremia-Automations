# **CREMIA AUTOMATIONS Necesidades de información para la gestión de la producción** 

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda **Módulo:** Módulo 2 · Gestión y Evaluación de la Producción **Fecha:** 11 de octubre de 2026 

## **1. Alcance** 

El presente apartado tiene como propósito estructurar la estrategia de gestión de la información para la línea de yogur de la planta La Hacienda. Si bien el rediseño físico y la automatización de los equipos permiten incrementar la capacidad productiva a dos lotes diarios, esta transformación operativa exige un ecosistema digital capaz de planificar, ejecutar y monitorear la producción sin depender de registros manuales. 

actualmente la mayoría de las empresas pequeñas y medianas mantienen un orden jerárquico bastante rígido para la recolección de la información de las plantas de producción dando informes de la planta cada x intervalos de tiempo siendo estos una tarea bastante manual ya que suele depender de que una persona realice las respectivas inspecciones de forma manual para saber cosas como la cantidad de materia prima disponibles, el control de acidez o de otras características medidas durante el proceso. esto limita en gran medida la información en un nivel más gerencial dificultando algunos cálculos que requieren de información precisa directamente de la planta pero que se hacen en niveles superiores de la pirámide de automatización creando una falta de trazabilidad en tiempo real del funcionamiento de la planta por todo esto y como parte de la propuesta de automatización y transformación digital se planteó un sistema integrado de gestión empresarial (el ERP Odoo en la nube, por suscripción: ventas, compras, inventario, fabricación y contabilidad) y de manufactura (un MES con módulos Sepasoft sobre la plataforma Ignition, instalado en la planta junto con el SCADA)  que busque responder: 

   - ¿Cuánto se produjo y se vendió por referencia? 

   - ¿Cuál es el costo por unidad? 

   - ¿Qué lotes se programan hoy? 

   - ¿Hay leche, insumos y envases? 

   - ¿Se cumplió el plan? 

   - ¿El lote cumplió la pasteurización y el pH? 

   - ¿Qué leche e insumos lleva? ¿Se puede liberar? 

   - ¿En qué fase está el lote? 

   - ¿Qué equipo se detuvo, cuánto tiempo y por qué? 

   - ¿Cuánta leche, azúcar, fruta y envase se consumió y cuánto queda? 

- garantizando respuestas rápidas y actualizaciones frecuentes de las distintas variables que se encuentran en la planta 

para esto se espera crear dos apartados principales diferentes uno para el MES y otro para el ERP 

## **Funciones del Sistema ERP** 

para este apartado se tiene el nivel más alto en la pirámide de automatización del ISA 95 correspondiente a el Nivel Estratégico y de Negocio , donde sus principales funciones serán: 

- Registro de ventas y pedidos por cliente y referencia. 

- Ayudar con el plan de producción semanal y plan de requerimiento de materiales. 

- Compras de leche, azúcar, cultivo, fruta, saborizantes y material de envase. 

- Manejo de Inventarios de insumos y de producto terminado, con fecha de vencimiento. 

- Costos de producción, margen por referencia y visualización de indicadores de la planta. 

- Brindar información sobre facturación y despacho. 

## **Funciones del Sistema MES** 

- pasando a la parte del nivel de ejecución de planta se espera poder visualizar desde el sistema: ● Secuencia de los dos lotes diarios por referencia, con los cambios de sabor y de formato 

   - Liberación de la orden y descarga de la receta de control al PLC 

   - Registro electrónico de lote con mediciones, consumos y eventos 

   - Relación entre el lote de leche, los lotes de insumos y el lote de yogur 

   - Verificación de la pasteurización, del pH y del peso; liberación o retención del lote 

   - OEE, rendimiento, producto no conforme, tiempos por fase y cumplimiento del plan 

- Registro de paradas y horas de operación para el mantenimiento preventivo 

- todo esto obtenido de la información de distintos sensores y registros en la planta 

## **Intercambio entre MES y ERP** 

La interoperabilidad entre el nivel estratégico y la planta de producción se rige por un intercambio bidireccional de datos. Esta arquitectura garantiza que las órdenes de fabricación se ejecuten con los materiales correctos y que el inventario se descuente según el consumo real en tiempo real. 

### **Flujo Descendente: Nivel de Planificación a Nivel de Ejecución (ERP MES)** 

El sistema ERP actúa como el planificador maestro, enviando a la planta los parámetros de negocio necesarios para operar. Los mensajes críticos en este sentido incluyen: 

- **Plan de producción:** Se envía con una frecuencia semanal e indica las referencias específicas a fabricar, las cantidades requeridas y las fechas de ejecución. 

- **Disponibilidad de materiales:** Se actualiza de manera diaria para informar al piso de planta sobre las existencias reales de insumos y materiales de envase disponibles. 

- **Definición de producto:** Transfiere la lista de materiales exacta por cada referencia de yogur, la cual se actualiza y envía únicamente cuando existe un cambio en la formulación. 

### **Flujo Ascendente: Nivel de Ejecución a Nivel de Planificación (MES ERP)** 

El sistema MES actúa como el recolector de datos en tiempo real, retroalimentando al ERP para el cierre contable, logístico y de calidad. Sus comunicaciones principales son: 

- **Recepción de leche:** Se transmite por cada recepción, detallando los datos del proveedor, la cantidad descargada y los parámetros de calidad evaluados. 

- ● **Estado de la orden:** Notifica en cada cambio de estado si una orden de fabricación se encuentra programada, en proceso, terminada o retenida. 

- **Consumo de materiales:** Se emite al cerrar el lote, reportando las cantidades reales de cada insumo gastado por lote. 

- **Reporte de producción:** Se envía al cerrar el lote, consolidando el número exacto de unidades conformes generadas por lote y referencia. 

obteniendo: 

|**Mensaje**|**Sentido**|**Contenido**|**Momento**|
|---|---|---|---|
|Plan de producción|ERP<br>MES<br>→|Referencias,<br>cantidades y fechas|Semanal|
|Disponibilidad de<br>materiales|ERP<br>MES<br>→|Existencias de<br>insumos y envase|Diaria|
|Definición de<br>producto|ERP<br>MES<br>→|Lista de materiales<br>por referencia|Cuando cambia|
|Recepción de leche|MES<br>ERP<br>→|Proveedor, cantidad<br>y calidad|Por recepción|
|Reporte de<br>producción|MES<br>ERP<br>→|Unidades conformes<br>por lote y referencia|Al cerrar el lote|
|Consumo de<br>materiales|MES<br>ERP<br>→|Cantidades reales<br>por insumo y lote|Al cerrar el lote|
|Estado de la orden|MES<br>ERP<br>→|Programada, en<br>proceso, terminada<br>o retenida|En cada cambio de<br>estado|



## **Indicadores de gestión** 

|**Indicador**|**Fórmula**|**Valor actual**|**Meta**|**Fuente del dato**|
|---|---|---|---|---|
|OEE de<br>envasado|Disponibilidad ×<br>rendimiento ×<br>calidad|68 %<br>≈|82 %|PLC y<br>controladoras de<br>peso|
|Producto no<br>conforme|Unidades<br>rechazadas /<br>unidades<br>llenadas|5,06 %|1,5 % o<br>menos|CK-401 y<br>CK-402|
|Rendimiento de<br>materiales|Masa de<br>producto / masa<br>de insumos|98,1 %|98,5 % o más|Dosificación y<br>conteo de<br>unidades|
|Lotes por día|Lotes<br>terminados /<br>días de<br>operación|1|2|MES|
|Tiempo<br>estándar por<br>lote|Suma de<br>tiempos de fase|601 min|493 min<br>≈|PLC y MES|
|Cumplimiento<br>del plan|Unidades<br>producidas /<br>unidades<br>programadas|No se mide|95 % o más|MES y ERP|
|Lotes liberados<br>a la primera|Lotes sin<br>retención / lotes<br>producidos|No se mide|98 % o más|MES|



