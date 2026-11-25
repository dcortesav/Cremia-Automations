# Flujo de información entre OT e IT

**Línea de yogur de la planta La Hacienda**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Módulo 1 · Transformación Digital Industrial

## 1. Alcance

Este documento describe qué información circula entre la operación de la planta (OT: sensores, PLC y el SCADA en Node-RED del nodo de borde) y la gestión de la empresa (IT: la plataforma Cremia MES/ERP en Huawei Cloud), quién la produce, quién la usa y para qué decisión. La arquitectura, las redes y la ciberseguridad están en el documento de arquitectura ISA-95; el diseño del software, en el documento de la plataforma Cremia MES/ERP y el SCADA en Node-RED; los equipos y las etiquetas, en el inventario de equipos, sensores y actuadores.

Hoy la información de la línea se programa de forma verbal y se registra en papel. Con la propuesta, cada lote queda registrado de forma electrónica y los datos de la planta llegan a la gestión sin transcripción.

## 2. Niveles que intercambian información

| Nivel ISA-95 | Sistema | Dónde corre | Qué produce | Qué recibe |
| --- | --- | --- | --- | --- |
| 1 · Medición y actuación | 25 sensores y 22 actuadores | Planta | Mediciones y estados | Mandos del PLC |
| 2 · Control y supervisión | PLC-01, controladores de máquina, nodo de borde con SCADA en Node-RED, HMI-01 y HMI-02 | Planta | Fases ejecutadas, alarmas, conteos, pesos y curvas | Recetas de control y consignas |
| Zona desmilitarizada | Cortafuegos industrial y equipo de salto | Planta | Conexiones salientes autorizadas | — |
| 3 · Gestión de operaciones | MES de la plataforma Cremia MES/ERP | Huawei Cloud | Órdenes, recetas de control, registro de lote, trazabilidad e indicadores | Eventos de lote, consumos y alarmas |
| 4 · Gestión empresarial | ERP ligero de la plataforma Cremia MES/ERP | Huawei Cloud (misma base de datos) | Plan semanal, compras, inventarios y costos | Producción, consumos y lotes liberados |

## 3. Matriz de flujos principales

| ID | Información | Origen | Destino | Medio | Frecuencia | Uso |
| --- | --- | --- | --- | --- | --- | --- |
| F-01 | Plan de producción semanal por referencia | ERP de la plataforma | MES de la plataforma | Misma base de datos | Semanal | Programar los lotes |
| F-02 | Disponibilidad de leche, insumos y envases | ERP | MES | Misma base de datos | Diaria y al liberar cada orden | Liberar solo órdenes con materiales |
| F-03 | Orden de producción y receta de control | MES | Nodo de borde (caché) y PLC-01 | MQTT sobre TLS hasta el nodo; OPC UA hasta el PLC | Al liberar el lote | Ejecutar las fases con la fórmula escalada |
| F-04 | Código de lote y fecha de vencimiento | MES | CD-401 y CD-402 | MQTT hasta el nodo; EtherNet/IP por el PLC | Al arrancar el envasado | Imprimir lote y vencimiento en cada unidad |
| F-05 | Análisis de la leche por cantina | HMI-01 | MES | MQTT | Por cantina | Aceptar la leche y asociarla al lote |
| F-06 | Peso, nivel y caudal de leche cargada | WT-101 y FT-101 (lote 1); LT-102 y FT-101 (lote 2) | PLC-01 y MES | 4–20 mA; MQTT | Por lote | Escalar la fórmula |
| F-07 | Cantidades dosificadas y lote de cada insumo | WT-201, WT-202, WT-205, WT-206, FQ-203 y FQ-204 | MES | OPC UA y MQTT | Por dosificación | Consumo real y trazabilidad de insumos |
| F-08 | Temperatura del tanque (TT-301) | Sensor y PLC-01 | Historiador local; curva del punto crítico al MES | OPC UA; MQTT al cerrar la fase | Cada segundo | Curva de pasteurización, punto crítico |
| F-09 | pH de fin de incubación (AT-301) | Sensor y PLC-01 | Historiador local y MES | OPC UA y MQTT | Cada 5 s | Terminar la incubación y liberar el lote |
| F-10 | Presión de homogeneización (PT-302) | Sensor y PLC-01 | Historiador local y MES | OPC UA y MQTT | Cada segundo; curva al cerrar la fase | Registro de lote |
| F-11 | Temperatura de salida del enfriador (TT-302) y del enfriamiento nocturno (TT-301) | Sensores y PLC-01 | Historiador local y MES | OPC UA y MQTT | Cada segundo | Segundo punto crítico |
| F-12 | Inicio y fin de fases, alarmas y desviaciones | PLC-01 | Nodo de borde y MES | OPC UA y MQTT | Por evento | Seguimiento del lote y análisis de paradas |
| F-13 | Unidades conformes y rechazadas, con causa | CK-401 y CK-402 | MES | EtherNet/IP, OPC UA y MQTT | Por unidad, agregado cada minuto | Producto no conforme y OEE |
| F-14 | Estado y paradas de EMP-401 y LL-402 | Máquinas y PLC-01 | MES | OPC UA y MQTT | Por evento | Disponibilidad de la máquina |
| F-15 | Ciclo CIP y conductividad de enjuague | CIP-901 y CT-901 | MES | OPC UA y MQTT | Por ciclo | Verificar limpieza antes del lote |
| F-16 | Temperatura del cuarto frío (TT-501), de TK-102 (TT-102) y del tanque pulmón T-302 (TT-303) | Sensores y PLC-01 | Nodo de borde y MES | OPC UA y MQTT | Cada minuto | Cadena de frío de la leche y del producto, y alarma de temperatura del tanque pulmón (> 20 °C; TT-303 es alarma operativa, no punto crítico de control) |
| F-17 | Lote liberado por calidad | MES | ERP | Misma base de datos | Por lote | Habilitar el despacho |
| F-18 | Producción terminada, consumos e inventario | MES | ERP | Misma base de datos | Al cerrar el lote | Inventarios, costos y compras |
| F-19 | Indicadores del día | Plataforma | Tablero de la gerencia | HTTPS | Diaria | Decisiones de producción y compras |
| F-20 | Señal de vida del nodo de borde y alarmas de prioridad alta | Nodo de borde | Vigilancia en la nube; SMS y correo al jefe de producción | MQTT; SMS por el router 4G como respaldo | Cada minuto y por evento | Atender el lote nocturno sin operario |
| F-21 | Pedidos despachados | ERP | Facturador electrónico de la planta | Exportación de archivo o API | Diaria | Facturación electrónica ante la DIAN |

## 4. Recorrido de un lote

1. El ERP genera el plan semanal a partir de los pedidos; el MES programa los dos lotes del día y verifica la disponibilidad de leche, insumos y envases.
2. El operario registra el análisis de cada cantina en HMI-01; el MES asocia la leche aprobada al lote 1 (TK-101) o al lote 2 (TK-102).
3. Al liberar la orden, hasta con 48 h de anticipación, el MES envía al nodo de borde la receta de control con las cantidades planificadas para 550 L. Al cargar el lote, la cantidad real de leche (WT-101 y FT-101 en el lote 1, desde TK-101; LT-102 y FT-101 en el lote 2, desde TK-102) llega al MES, que escala la fórmula en proporción (sin internet, el nodo de borde hace el mismo escalado con la receta en caché), y el nodo de borde descarga la receta escalada al PLC.
4. El PLC ejecuta las fases y reporta cada inicio, fin, cantidad y alarma; el historiador local guarda las curvas y el nodo de borde envía a la nube las del registro de lote.
5. Los codificadores imprimen el lote y el vencimiento; las controladoras de peso reportan conformes y rechazos.
6. Calidad revisa el registro electrónico y los análisis, y libera el lote en la plataforma.
7. La plataforma actualiza el inventario disponible, el costo real del lote y los pedidos listos para despachar.

## 5. Validación de los mensajes

La API de la plataforma y el nodo de borde revisan cada mensaje antes de aceptarlo:

| Validación | Ejemplo | Qué pasa si falla |
| --- | --- | --- |
| Estructura | El mensaje cumple el esquema de la orden, del evento o del reporte | Se rechaza y queda registrado |
| Rangos | Una orden no pide más de 550 L de leche por lote ni una referencia que no existe | Se retiene para revisión del jefe de producción |
| Duplicados | El mismo evento de lote no entra dos veces, aunque el nodo de borde lo reenvíe después de una caída de internet | Se descarta la copia por su identificador único |
| Origen | El mensaje viene firmado con el certificado del nodo de borde autorizado | Se rechaza y se registra como incidente |
| Coherencia | Los consumos reportados corresponden a la fórmula del lote, con tolerancia de ± 1 % | Se marca para revisión de calidad |

## 6. Información para decidir

| Quién | Qué ve | Dónde | Qué decide |
| --- | --- | --- | --- |
| Operario | Fase en curso, alarmas, peso y temperatura | HMI-01 y HMI-02 | Atender alarmas y cambios de referencia |
| Jefe de producción | Avance de los lotes, paradas, OEE, no conformes y alarmas del lote nocturno | Plataforma y teléfono | Programación del día y prioridades |
| Calidad | Curvas de los puntos críticos, pH final, análisis y desviaciones | Plataforma | Liberar, retener o rechazar un lote |
| Mantenimiento | Horas de trabajo, paradas por causa y calibraciones | Plataforma | Mantenimiento preventivo |
| Compras | Requerimiento de materiales, inventario por lote y vencimiento | Plataforma | Qué comprar y cuándo |
| Gerencia | Producción, costo real por lote, margen por referencia e inventario | Tablero de la plataforma | Qué producir, cuánta leche comprar y qué invertir |

## 7. Continuidad

El PLC y el nodo de borde están en la planta; la plataforma está en Huawei Cloud. Si se cae internet, la línea sigue produciendo con las recetas en caché y el nodo de borde guarda hasta 72 h de mensajes, que reenvía cuando vuelve la conexión. Si falla la planta, la plataforma sigue disponible para ventas, inventario, despacho y trazabilidad, y avisa al jefe de producción cuando deja de recibir la señal de vida del nodo de borde. El detalle está en la sección 4 del documento de la plataforma.

## Referencias

- ANSI/ISA-95.00.01-2010 y ANSI/ISA-95.00.02. Enterprise-Control System Integration, Parts 1 and 2.
- ANSI/ISA-95.00.03-2013. Activity Models of Manufacturing Operations Management.
- ANSI/ISA-88.00.01-2010. Batch Control Part 1: Models and Terminology.
- IEC 62443. Security for industrial automation and control systems.
- OASIS. MQTT Version 5.0.
- OPC Foundation. OPC Unified Architecture (IEC 62541).
