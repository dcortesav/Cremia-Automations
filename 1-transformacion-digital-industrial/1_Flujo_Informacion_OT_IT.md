# Flujo de información entre OT e IT

**Línea de yogur de la planta La Hacienda**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Módulo 1 · Transformación Digital Industrial

## 1. Alcance

Este documento describe qué información circula entre la operación de la planta (OT: sensores, PLC, SCADA y MES) y la gestión de la empresa (IT: ERP en la nube), quién la produce, quién la usa y para qué decisión. La arquitectura, las redes y la ciberseguridad están en el documento de arquitectura ISA-95; los equipos y las etiquetas, en el inventario de equipos, sensores y actuadores.

Hoy la información de la línea se programa de forma verbal y se registra en papel. Con la propuesta, cada lote queda registrado de forma electrónica y los datos de la planta llegan al ERP sin transcripción.

## 2. Niveles que intercambian información

| Nivel ISA-95 | Sistema | Qué produce | Qué recibe |
| --- | --- | --- | --- |
| 1 · Medición y actuación | 23 sensores y 19 actuadores | Mediciones y estados | Mandos del PLC |
| 2 · Control y supervisión | PLC-01, controladores de máquina, SCADA, HMI-01 y HMI-02 | Fases ejecutadas, alarmas, conteos y pesos | Recetas de control y consignas |
| 3 · Gestión de operaciones | MES e historiador | Registro de lote, trazabilidad e indicadores | Plan de producción y disponibilidad de materiales |
| 3.5 · Zona desmilitarizada | Pasarela de integración | Mensajes validados | Mensajes del MES y del ERP |
| 4 · Gestión empresarial | ERP en la nube | Plan semanal, compras e inventarios | Producción, consumos y lotes liberados |

## 3. Matriz de flujos principales

| ID | Información | Origen | Destino | Medio | Frecuencia | Uso |
| --- | --- | --- | --- | --- | --- | --- |
| F-01 | Plan de producción semanal por referencia | ERP | MES | API REST, B2MML | Semanal | Programar los lotes |
| F-02 | Disponibilidad de leche, insumos y envases | ERP | MES | API REST, B2MML | Diaria | Liberar solo órdenes con materiales |
| F-03 | Orden de producción y receta de control | MES | PLC-01 | OPC UA | Al liberar el lote | Ejecutar las fases con la fórmula escalada |
| F-04 | Código de lote y fecha de vencimiento | MES | CD-401 y CD-402 | EtherNet/IP | Al arrancar el envasado | Imprimir lote y vencimiento en cada unidad |
| F-05 | Análisis de la leche por cantina | HMI-01 | MES | OPC UA | Por cantina | Aceptar la leche y asociarla al lote |
| F-06 | Peso y caudal de leche cargada | WT-101 y FT-101 | PLC-01 y MES | 4–20 mA, OPC UA | Por lote | Escalar la fórmula |
| F-07 | Cantidades dosificadas y lote de cada insumo | WT-201, WT-202, WT-205, WT-206, FQ-203 y FQ-204 | MES | OPC UA | Por dosificación | Consumo real y trazabilidad de insumos |
| F-08 | Temperatura del tanque (TT-301) | Sensor y PLC-01 | SCADA e historiador | OPC UA | Cada segundo | Curva de pasteurización, punto crítico |
| F-09 | pH de fin de incubación (AT-301) | Sensor y PLC-01 | SCADA y MES | OPC UA | Cada 5 s | Terminar la incubación y liberar el lote |
| F-10 | Presión de homogeneización (PT-302) | Sensor y PLC-01 | Historiador | OPC UA | Cada segundo | Registro de lote |
| F-11 | Temperatura de salida del enfriador (TT-302) | Sensor y PLC-01 | Historiador | OPC UA | Cada segundo | Segundo punto crítico |
| F-12 | Inicio y fin de fases, alarmas y desviaciones | PLC-01 | SCADA y MES | OPC UA | Por evento | Seguimiento del lote y análisis de paradas |
| F-13 | Unidades conformes y rechazadas, con causa | CK-401 y CK-402 | MES | EtherNet/IP, OPC UA | Por unidad | Producto no conforme y OEE |
| F-14 | Estado y paradas de EMP-401 y LL-402 | Máquinas y PLC-01 | MES | OPC UA | Por evento | Disponibilidad de la máquina |
| F-15 | Ciclo CIP y conductividad de enjuague | CIP-901 y CT-901 | MES | OPC UA | Por ciclo | Verificar limpieza antes del lote |
| F-16 | Temperatura del cuarto frío (TT-501) | Sensor y PLC-01 | SCADA y MES | OPC UA | Cada minuto | Cadena de frío |
| F-17 | Lote liberado por calidad | MES | ERP | API REST, B2MML | Por lote | Habilitar el despacho |
| F-18 | Producción terminada, consumos e inventario | MES | ERP | API REST, B2MML | Al cerrar el lote | Inventarios, costos y compras |
| F-19 | Indicadores del día | MES | Tablero de la gerencia | Réplica en la zona desmilitarizada | Diaria | Decisiones de producción y compras |

## 4. Recorrido de un lote

1. El ERP envía el plan semanal; la pasarela de la zona desmilitarizada valida el mensaje y lo entrega al MES.
2. El MES programa los lotes del día y verifica la disponibilidad de leche, insumos y envases.
3. El operario registra el análisis de cada cantina en HMI-01; el MES asocia la leche aprobada al lote.
4. Al liberar el lote, el MES escala la fórmula con el peso real de la leche y descarga la receta de control al PLC.
5. El PLC ejecuta las fases y reporta cada inicio, fin, cantidad y alarma; el historiador guarda las curvas.
6. Los codificadores imprimen el lote y el vencimiento; las controladoras de peso reportan conformes y rechazos.
7. Calidad revisa el registro electrónico y los análisis, y libera el lote en el MES.
8. El MES reporta al ERP el lote liberado, la producción, los consumos y el inventario.

## 5. Validación en la zona desmilitarizada

La pasarela de integración revisa cada mensaje entre el MES y el ERP antes de dejarlo pasar:

| Validación | Ejemplo | Qué pasa si falla |
| --- | --- | --- |
| Estructura | El mensaje cumple el esquema B2MML de la orden o del reporte | Se rechaza y se avisa al remitente |
| Rangos | Una orden no pide más de 550 L de leche por lote ni una referencia que no existe | Se retiene para revisión del jefe de producción |
| Duplicados | La misma orden o el mismo reporte de lote no entra dos veces | Se descarta la copia |
| Origen | El mensaje viene firmado por el ERP o el MES autorizados | Se rechaza y se registra como incidente |
| Coherencia | Los consumos reportados corresponden a la fórmula del lote, con tolerancia de ± 1 % | Se marca para revisión de calidad |

## 6. Información para decidir

| Quién | Qué ve | Qué decide |
| --- | --- | --- |
| Operario | Fase en curso, alarmas, peso y temperatura | Atender alarmas y cambios de referencia |
| Jefe de producción | Avance de los lotes, paradas, OEE y no conformes | Programación del día y prioridades |
| Calidad | Curvas de los puntos críticos, pH final, análisis y desviaciones | Liberar, retener o rechazar un lote |
| Mantenimiento | Horas de trabajo, paradas por causa y calibraciones | Mantenimiento preventivo |
| Gerencia | Producción, costo real por lote, margen por referencia e inventario | Qué producir, cuánta leche comprar y qué invertir |

## 7. Continuidad

El MES, el SCADA y el historiador están en la planta. Si se cae la conexión con el ERP en la nube, la línea sigue produciendo y registrando los lotes, y la pasarela envía los mensajes pendientes cuando vuelve la conexión. Las copias de respaldo diarias se guardan cifradas en la nube.

## Referencias

- ANSI/ISA-95.00.01-2010 y ANSI/ISA-95.00.02. Enterprise-Control System Integration, Parts 1 and 2.
- ANSI/ISA-95.00.03-2013. Activity Models of Manufacturing Operations Management.
- ANSI/ISA-88.00.01-2010. Batch Control Part 1: Models and Terminology.
- IEC 62443. Security for industrial automation and control systems.
- MESA International. B2MML: Business To Manufacturing Markup Language.
