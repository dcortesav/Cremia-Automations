# Necesidades de información para la gestión de la producción

**Línea de yogur de la planta La Hacienda**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Módulo 2 · Gestión y Evaluación de la Producción

## 1. Alcance

Este documento define qué información necesita la planta para planear, ejecutar y controlar los dos lotes diarios de yogur, y qué funciones de MES y de ERP la producen. Es la especificación funcional de la plataforma Cremia MES/ERP; su diseño, despliegue en Huawei Cloud y costo están en el documento de la plataforma en el módulo 1.

Hoy la planta no tiene sistema de información: la programación es verbal, los registros son en papel y los datos de existencias, acidez o rendimiento dependen de que alguien los anote y los lleve a la gerencia. Con dos lotes por día, tres referencias y un lote que incuba de noche sin operario, esa forma de trabajar no alcanza.

## 2. Preguntas que el sistema debe responder

| Pregunta | Quién la hace | Cuándo | Módulo que responde |
| --- | --- | --- | --- |
| ¿Cuánto se produjo y se vendió por referencia? | Gerencia | Diario y mensual | ERP |
| ¿Cuál es el costo real por unidad y el margen por referencia? | Gerencia | Por lote y mensual | ERP |
| ¿Qué lotes se programan hoy y en qué orden? | Jefe de producción | Diario | MES |
| ¿Hay leche, insumos y envases para esos lotes? | Jefe de producción y compras | Antes de liberar cada orden | MES y ERP |
| ¿Se cumplió el plan? | Jefe de producción y gerencia | Diario y semanal | MES |
| ¿El lote cumplió la pasteurización, el pH y el enfriamiento? | Calidad | Al cerrar el lote | MES |
| ¿Qué leche e insumos lleva el lote? ¿Se puede liberar? | Calidad | Al cerrar el lote | MES |
| ¿En qué fase está el lote, incluido el lote 2 de noche? | Jefe de producción | En cualquier momento, desde el teléfono | MES |
| ¿Qué equipo se detuvo, cuánto tiempo y por qué? | Jefe de producción y mantenimiento | Diario | MES |
| ¿Cuánta leche, azúcar, fruta y envase se consumió y cuánto queda? | Compras | Diario | ERP |

## 3. Funciones del ERP

El ERP es el nivel 4 de ISA-95: planeación del negocio y logística. Sus funciones son:

- Registro de pedidos por cliente y referencia, y despacho de lotes liberados.
- Plan de producción semanal y requerimiento de materiales a partir de los pedidos y de las listas de materiales de las recetas.
- Compras de leche, azúcar, cultivo, fruta, saborizantes y material de envase.
- Inventario de insumos y de producto terminado por lote y fecha de vencimiento.
- Costo real por lote con los consumos que reporta el MES, margen por referencia e indicadores para la gerencia.
- Exportación de los pedidos despachados al facturador electrónico que la planta ya usa. La contabilidad y la facturación electrónica siguen en ese sistema.

## 4. Funciones del MES

El MES es el nivel 3 de ISA-95: ejecución de la producción en la planta. Sus funciones son:

- Secuencia de los dos lotes diarios por referencia, con los cambios de sabor y de formato.
- Gestión de recetas maestras con versiones y aprobación; liberación de la orden y envío de la receta de control al nodo de borde, que la descarga al PLC.
- Registro electrónico de lote con mediciones, consumos, eventos y alarmas.
- Genealogía: relación entre el lote de leche, el tanque de origen (TK-101 o TK-102), los lotes de insumos y el lote de yogur.
- Verificación de la pasteurización, del pH, del enfriamiento y del peso; liberación o retención del lote.
- OEE, rendimiento, producto no conforme, tiempos por fase y cumplimiento del plan.
- Registro de paradas y de horas de operación para el mantenimiento preventivo.

## 5. Intercambio entre el MES y el ERP

El MES y el ERP son dos módulos de la misma plataforma y comparten una base de datos, de modo que no necesitan una interfaz de mensajes entre ellos: una orden, su lote, sus consumos y su costo son registros relacionados. Los intercambios se definen por el dato que pasa de una función a otra y por el momento en que debe estar disponible.

| Dato | Sentido | Contenido | Momento |
| --- | --- | --- | --- |
| Plan de producción | ERP → MES | Referencias, cantidades y fechas | Semanal |
| Disponibilidad de materiales | ERP → MES | Existencias de insumos y envase | Diaria y al liberar cada orden |
| Definición de producto | ERP → MES | Lista de materiales por referencia, ligada a la versión de la receta maestra | Cuando cambia la formulación |
| Recepción de leche | MES → ERP | Proveedor, cantidad, tanque de destino y calidad por cantina | Por recepción |
| Estado de la orden | MES → ERP | Programada, en proceso, terminada, liberada o retenida | En cada cambio de estado |
| Consumo de materiales | MES → ERP | Cantidades reales por insumo y lote | Al cerrar el lote |
| Reporte de producción | MES → ERP | Unidades conformes y rechazadas por lote y referencia | Al cerrar el lote |

Entre la planta y la plataforma sí hay mensajes: el nodo de borde envía por MQTT los eventos, consumos y curvas del lote y recibe las recetas de control. Los flujos están en el documento de flujo de información entre OT e IT.

## 6. Indicadores de gestión

| Indicador | Fórmula | Valor actual | Meta | Fuente del dato |
| --- | --- | --- | --- | --- |
| OEE de envasado | Disponibilidad × rendimiento × calidad | ≈ 65 % | 82 % | PLC y controladoras de peso |
| Producto no conforme | Unidades rechazadas ÷ unidades llenadas | 5,06 % | 1,5 % o menos | CK-401 y CK-402 |
| Rendimiento de materiales | Masa de producto ÷ masa de insumos | 98,1 % (bolsas) | Bolsas ≥ 98 %; vasos ≥ 97 % (la fruta retiene producto) | Dosificación y conteo de unidades |
| Lotes por día | Lotes terminados ÷ días de operación | 1 | 2 | MES |
| Tiempo estándar por lote | Suma de tiempos de fase | 601 min | ≈ 563 min | PLC y MES |
| Cumplimiento del plan | Unidades conformes producidas ÷ unidades programadas | No se mide | 95 % o más | MES y ERP |
| Lotes liberados a la primera | Lotes sin retención ÷ lotes producidos | No se mide | 98 % o más | MES |
| Unidades conformes por operario al día | Unidades conformes ÷ operarios | 724 | 1.301 | MES |

## Referencias

- ANSI/ISA-95.00.01-2010 y ANSI/ISA-95.00.03-2013. Enterprise-Control System Integration, partes 1 y 3.
- Grimaldo, G., Moreno, D. y Salamanca, M. (2015). Medición del trabajo de una línea de producción de yogurt – Empresa La Hacienda. Revista I3+, 2(2), 62–81.
