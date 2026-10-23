# Arquitectura ISA-95 y flujo de información entre OT e IT

**Línea de yogur de la planta La Hacienda**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Módulo 1 · Transformación Digital Industrial

## 1. Alcance

Este documento define la arquitectura de automatización e información de la línea de yogur según los niveles de ANSI/ISA-95 y describe qué información circula entre la planta (OT) y la gestión de la empresa (IT). Las etiquetas de equipos e instrumentos son las del inventario de equipos, sensores y actuadores.

Hoy la planta no tiene ningún nivel conectado: las mediciones se toman con instrumentos manuales y los registros se llevan en papel. La arquitectura propuesta cubre los cinco niveles.

## 2. Arquitectura por niveles

| Nivel ISA-95 | Función | Elementos de la línea de yogur | Horizonte de tiempo |
| --- | --- | --- | --- |
| 4 · Gestión empresarial | Planeación del negocio y logística | ERP en la nube para pymes: pedidos, compras de leche e insumos, inventarios, costos y despacho | Días y semanas |
| 3 · Gestión de operaciones | Programación y seguimiento de la producción | MES con base de datos SQL: órdenes de producción, recetas maestras y de control, registro de lote, trazabilidad, calidad, paradas e indicadores | Turnos y horas |
| 2 · Control y supervisión | Control automático, monitoreo y mando del proceso | PLC-01 (CompactLogix 5380) y máquinas con controlador propio (homogeneizador H-301, controladoras de peso CK-401 y CK-402, codificadores CD-401 y CD-402, llenadora LL-402 y empacadora EMP-401; la celda robotizada R-501 se integra en una etapa posterior); SCADA (Ignition) con historiador, HMI-01 en preparación y HMI-02 en envasado | Segundos y minutos |
| 1 · Medición y actuación | Medición y manipulación del proceso | 23 sensores (temperatura, nivel, pH, caudal, peso, presión y conductividad), 19 actuadores (válvulas, bombas, motores y expulsores), E/S remotas y variadores | Milisegundos |
| 0 · Proceso | Proceso físico | Unidades U1 a U8: tanques TK-101, T-301 y T-302, intercambiador E-301, bombas, dosificadores y máquinas de envasado | Continuo |

ISA-95 ubica el control automático en el nivel 2, junto con la supervisión, y deja el nivel 1 para la medición y la actuación. El modelo Purdue dibuja el PLC en el nivel 1 con el nombre de control básico; las dos representaciones describen la misma arquitectura. Este documento y el de equipos siguen la definición de ISA-95.

La planta no tiene hoy ningún sistema de información, así que la arquitectura no supone un ERP corporativo: usa un ERP en la nube para pymes, por suscripción (contabilidad, compras, inventarios y ventas). El MES, el SCADA y el historiador quedan en la planta, en el nivel 3, para que la línea siga trabajando aunque se caiga internet. La integración con el ERP se hace con servicios web y mensajes según ISA-95 parte 2 (B2MML), de modo que cambiar de ERP no obliga a cambiar el MES.

## 3. Redes y protocolos

| Enlace | Medio y protocolo | Uso |
| --- | --- | --- |
| Instrumento a E/S remota | 4–20 mA, IO-Link y señales de 24 V DC | Mediciones y mandos de campo |
| E/S remota, variadores y máquinas a PLC | EtherNet/IP en anillo DLR con un conmutador administrable de celda (Stratix 5700); el anillo se recupera en menos de 3 ms si se corta un cable | Control en tiempo real |
| PLC a SCADA | OPC UA cifrado y autenticado con certificados | Variables, alarmas, receta activa y estado de fases |
| SCADA a MES | OPC UA o MQTT; base de datos SQL para el historiador y el registro de lote | Eventos de lote, consumos, conteos y paradas |
| MES a ERP | Servicios web (API REST sobre HTTPS) con mensajes según ISA-95 parte 2 (B2MML), a través de la pasarela de la zona desmilitarizada | Órdenes, consumos, producción e inventario |

**Zona desmilitarizada (nivel 3.5).** Entre la red de planta (niveles 0 a 3) y la red administrativa y la nube (nivel 4) hay una zona desmilitarizada industrial entre dos cortafuegos. Ningún sistema de la nube ni de la oficina habla de forma directa con el MES o con el PLC: todo pasa por la zona desmilitarizada, que tiene tres servicios:

- **Pasarela de integración.** Recibe los mensajes del ERP y del MES y los valida antes de dejarlos pasar: estructura B2MML, rangos permitidos (por ejemplo, que una orden no pida más de 550 L de leche por lote), mensajes duplicados y origen autenticado. Así se evitan órdenes o reportes en falso entre los dos sistemas.
- **Réplica de consulta.** Copia de solo lectura de los indicadores y del registro de lote para la gerencia y para el tablero web, que se publica detrás de un cortafuegos de aplicaciones web.
- **Acceso remoto.** El soporte de Cremia entra por VPN con doble factor hasta un equipo de salto en la zona desmilitarizada, nunca hasta la red de control.

## 4. Estrategia de control

El PLC-01 ejecuta dos capas de control. La primera es el control secuencial por fases según ISA-88, que sigue el procedimiento de la receta. La segunda es el control regulatorio con PID: TIC-301 con rango dividido sobre vapor y agua fría, TIC-302 con prealimentación del caudal de yogur, FFC-403 como control de relación de la fruta, PIC-302 para la presión del homogeneizador y la dosificación por peso en dos velocidades.

La propuesta no usa control avanzado (control predictivo por modelo, control difuso o adaptativo). Cada lazo tiene un actuador dominante, las dinámicas son lentas y conocidas y el proceso es por lotes, de modo que el PID cumple las tolerancias y el personal de la planta lo puede mantener. La justificación completa está en la sección 8.1 del documento de equipos, sensores, actuadores, variables y comunicaciones.

## 5. Flujo de información entre OT e IT

### 5.1 De IT hacia OT

| Información | Origen | Destino | Momento |
| --- | --- | --- | --- |
| Plan de producción semanal: referencias y cantidades | ERP | MES | Semanal y cuando cambia la demanda |
| Disponibilidad de leche, insumos y material de envase | ERP | MES | Diaria |
| Orden de producción: referencia, tamaño de lote y fecha | MES | SCADA | Al programar el lote |
| Receta de control: fórmula escalada y parámetros de cada fase | MES | PLC, a través del SCADA | Al liberar el lote |
| Código de lote y fecha de vencimiento | MES | Codificadores CD-401 y CD-402 | Al arrancar el envasado |
| Consignas y mandos del operador | SCADA y HMI | PLC | Durante el lote |

### 5.2 De OT hacia IT

| Información | Origen | Destino | Uso |
| --- | --- | --- | --- |
| Mediciones de proceso: temperatura, pH, nivel, caudal, peso y presión de homogeneización | Sensores y PLC | SCADA e historiador | Control, tendencias y registro de lote |
| Inicio y fin de cada fase, y alarmas | PLC | SCADA y MES | Seguimiento del lote y análisis de paradas |
| Cantidades dosificadas frente a la fórmula | PLC | MES | Consumo real y trazabilidad de insumos |
| Curva de pasteurización y pH final | Historiador | MES | Liberación del lote por calidad |
| Unidades producidas y rechazadas por peso | CK-401 y CK-402 | MES | Rendimiento, producto no conforme y OEE |
| Estado y paradas de EMP-401 y LL-402 | PLC | MES | Disponibilidad y mantenimiento |
| Resultados de laboratorio de la leche por cantina | Registro en HMI-01 | MES | Aceptación de la leche y pago al proveedor |
| Producción terminada, consumos e inventario en cuarto frío | MES | ERP | Inventarios, costos y despacho |

### 5.3 Recorrido de un lote

1. El ERP envía al MES el plan semanal con las cantidades por referencia.
2. El MES programa los lotes del día y verifica que haya leche, insumos y envase.
3. Al liberar el lote, el MES crea la receta de control a partir de la receta maestra y la descarga al PLC.
4. El PLC ejecuta las fases: carga, dosificación, estandarización y homogeneización, pasteurización, inoculación, incubación, enfriamiento, saborizado y transferencia.
5. El SCADA muestra el avance y guarda las mediciones en el historiador.
6. Los codificadores imprimen el lote y la fecha de vencimiento en cada unidad, y las controladoras de peso reportan las unidades conformes y rechazadas.
7. El MES cierra el lote con el registro completo y calcula los indicadores.
8. El MES reporta al ERP la producción, los consumos y el inventario disponible para despacho.

## 6. Funciones por sistema

| Sistema | Funciones |
| --- | --- |
| PLC-01 | Lógica de fases según ISA-88, lazos PID de temperatura TIC-301 y TIC-302, presión de homogeneización, control de relación de fruta, enclavamientos y alarmas |
| SCADA | Pantallas de proceso según ISA-101, alarmas según ISA-18.2, tendencias, selección de receta, estado del lote e historiador |
| MES | Órdenes de producción, gestión de recetas, registro electrónico de lote, trazabilidad, calidad, paradas e indicadores (OEE, rendimiento y producto no conforme) |
| ERP | Plan de producción, compras, inventarios, costos, ventas y despacho |

## 7. Ciberseguridad

- Segmentación por zonas y conductos según IEC 62443: zona de control (niveles 0 a 2), zona de operaciones (nivel 3), zona desmilitarizada (nivel 3.5) y zona empresarial con la nube (nivel 4).
- Usuarios con roles: operador, supervisor, calidad, mantenimiento y administrador.
- Cambios de receta y de consignas con registro de usuario, fecha y valor anterior.
- Copias de respaldo diarias del programa del PLC, del proyecto del SCADA y de la base de datos del MES, cifradas y guardadas en la nube, para recuperar el sistema si falla un servidor de la planta.
- Si se cae la conexión con la nube, el MES sigue registrando los lotes y envía los mensajes pendientes al ERP cuando vuelve la conexión.

## 8. Las personas en la arquitectura

La arquitectura cambia la forma de trabajar de cada rol. El operador deja de anotar en papel y opera desde la HMI; el jefe de producción programa y sigue los lotes en el MES; calidad libera los lotes con el registro electrónico; la gerencia decide con un tablero diario. La capacitación por rol, los procedimientos y el plan de gestión del cambio están en el documento Propuesta de valor y gestión del cambio.

## Referencias

- ANSI/ISA-95.00.01-2010 (IEC 62264-1). Enterprise-Control System Integration, Part 1: Models and Terminology.
- ANSI/ISA-95.00.02. Enterprise-Control System Integration, Part 2: Objects and Attributes for Enterprise-Control System Integration.
- ANSI/ISA-88.00.01-2010. Batch Control Part 1: Models and Terminology.
- IEC 62443. Security for industrial automation and control systems.
- ANSI/ISA-101.01-2015. Human Machine Interfaces for Process Automation Systems.
- ANSI/ISA-18.2-2016. Management of Alarm Systems for the Process Industries.
- ANSI/ISA-5.1-2009. Instrumentation Symbols and Identification.
