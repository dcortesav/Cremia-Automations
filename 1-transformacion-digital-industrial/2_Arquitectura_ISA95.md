# Arquitectura ISA-95 y flujo de información entre OT e IT

**Línea de yogur de la planta La Hacienda**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Módulo 1 · Transformación Digital Industrial

## 1. Alcance

Este documento define la arquitectura de automatización e información de la línea de yogur según los niveles de ANSI/ISA-95 y describe qué información circula entre la planta (OT) y la gestión de la empresa (IT). Las etiquetas de equipos e instrumentos son las del inventario de equipos, sensores y actuadores. El diseño, el despliegue y el costo del software están en el documento de la plataforma Cremia MES/ERP y el SCADA en Node-RED.

Hoy la planta no tiene ningún nivel conectado: las mediciones se toman con instrumentos manuales y los registros se llevan en papel. La arquitectura propuesta cubre los cinco niveles.

## 2. Arquitectura por niveles

| Nivel ISA-95 | Función | Elementos de la línea de yogur | Dónde corre | Horizonte de tiempo |
| --- | --- | --- | --- | --- |
| 4 · Gestión empresarial | Planeación del negocio y logística | ERP ligero de la plataforma Cremia MES/ERP: pedidos, plan semanal, requerimiento de materiales, compras de leche e insumos, inventario por lote y vencimiento, despacho y costo por lote. Exporta los pedidos despachados al facturador electrónico que ya usa la planta | Huawei Cloud | Días y semanas |
| 3 · Gestión de operaciones | Programación y seguimiento de la producción | MES de la plataforma Cremia MES/ERP: recetas maestras y de control, órdenes, registro electrónico de lote, genealogía, calidad y liberación, OEE, paradas y horas de equipo | Huawei Cloud, con caché de recetas y cola de mensajes en el nodo de borde | Turnos y horas |
| 2 · Control y supervisión | Control automático, monitoreo y mando del proceso | PLC-01 (CompactLogix 5380), que también controla el homogeneizador H-301; máquinas con controlador propio (controladoras de peso CK-401 y CK-402, codificadores CD-401 y CD-402, llenadora LL-402 y empacadora EMP-401) y la unidad de frío de TK-102; la celda robotizada R-501 se integra en una etapa posterior. SCADA en Node-RED con historiador local, HMI-01 en preparación y HMI-02 en envasado | Planta | Segundos y minutos |
| 1 · Medición y actuación | Medición y manipulación del proceso | 25 sensores (temperatura, nivel, pH, caudal, peso, presión y conductividad), 22 actuadores (válvulas, bombas, motores y expulsores), 68 señales de E/S en dos estaciones remotas y 20 nodos EtherNet/IP | Planta | Milisegundos |
| 0 · Proceso | Proceso físico | Unidades U1 a U8: tanques TK-101, TK-102, T-301 y T-302, intercambiador E-301, bombas, dosificadores y máquinas de envasado | Planta | Continuo |

ISA-95 ubica el control automático en el nivel 2, junto con la supervisión, y deja el nivel 1 para la medición y la actuación. El modelo Purdue dibuja el PLC en el nivel 1 con el nombre de control básico; las dos representaciones describen la misma arquitectura. Este documento y el de equipos siguen la definición de ISA-95.

**Qué queda en la planta y qué en la nube.** Todo lo que se necesita para producir un lote queda en la planta: el PLC ejecuta las fases y los enclavamientos, y el nodo de borde (un PC industrial con Node-RED) muestra las HMI, guarda el historiador, atiende las alarmas y tiene en caché las recetas de control de las órdenes de las 48 h siguientes. La gestión (MES y ERP) corre en Huawei Cloud, de modo que sigue disponible aunque la planta pierda energía o se dañe un equipo: ventas, inventario, despacho y consulta de trazabilidad no se detienen, y la nube avisa al jefe de producción si deja de recibir la señal de vida de la planta, lo que protege el lote 2 que incuba de noche sin operario.

El MES y el ERP son una sola aplicación con una sola base de datos. Su modelo de datos sigue los objetos de ISA-95 parte 2 (material, equipo, personal, segmento de proceso, programa y respuesta de producción), lo que facilita que otro integrador lo entienda y que la planta pueda conectar otro sistema en el futuro.

### 2.1 Plataformas seleccionadas

Como integradora, Cremia selecciona y justifica cada plataforma. El criterio común es que una planta pequeña pueda pagarla y mantenerla: pocos proveedores, sin licencias por usuario, tecnologías abiertas y estándares abiertos (ISA-88, ISA-95, OPC UA y MQTT) en las fronteras entre sistemas.

| Capa | Plataforma seleccionada | Función en la línea | Por qué |
| --- | --- | --- | --- |
| Control (nivel 2) | Allen-Bradley CompactLogix 5380, programado en Studio 5000 Logix Designer | Fases ISA-88 con PhaseManager, lazos PID, enclavamientos y alarmas de proceso; servidor OPC UA | Fases ISA-88 nativas, EtherNet/IP con anillo DLR, repuestos y soporte local; un solo controlador cubre las 68 señales con reserva |
| Red de control | Conmutador Stratix 5700, dos estaciones de E/S remotas EtherNet/IP y variadores PowerFlex | Anillo DLR entre PLC, E/S remotas, variadores y máquinas | Mismo fabricante del PLC: diagnóstico de toda la red desde Studio 5000 |
| Supervisión (nivel 2) | SCADA desarrollado por Cremia en Node-RED, con InfluxDB como historiador local, en un PC industrial (nodo de borde) con un PC de repuesto | HMI-01 y HMI-02, alarmas según ISA-18.2, tendencias, historiador, descarga de recetas al PLC y alarmas remotas de la incubación nocturna | Sin licencias; las pantallas son páginas web que se ven en cualquier panel o navegador; Node-RED es de código abierto y conocido por muchos integradores |
| Gestión de operaciones y empresarial (niveles 3 y 4) | Plataforma Cremia MES/ERP (Python, Django y PostgreSQL), desarrollada por Cremia | Recetas, órdenes, registro de lote, genealogía, calidad, OEE, inventario, compras, pedidos, despacho y costo por lote | Hecha a la escala de la planta; la planta tiene licencia perpetua, el código está en depósito con un tercero y los datos se exportan completos |
| Nube | Huawei Cloud, región de Ciudad de México: servidor virtual (ECS), PostgreSQL gestionado (RDS) principal y en espera, almacenamiento de respaldos (OBS) y avisos (SMN) | Aloja la plataforma y vigila el nodo de borde | Servicios gestionados que reducen la administración; México tiene nivel adecuado de protección de datos según la SIC |
| Integración | MQTT sobre TLS entre el nodo de borde y la nube; OPC UA entre el nodo de borde y el PLC | Mensajes de lote, consumos, alarmas, recetas y señal de vida, con almacenamiento y reenvío | La planta solo abre conexiones salientes; MQTT tolera conexiones intermitentes |
| Gemelo digital | Siemens Tecnomatix Plant Simulation y FactoryTalk Logix Echo (emulador del CompactLogix), conectados por OPC UA | Capacidad de la línea y puesta en marcha virtual del programa del PLC, del SCADA y de la plataforma | El mismo programa que va a la planta se prueba contra el modelo antes de la parada |

Las licencias de Studio 5000, Logix Echo y Tecnomatix son herramientas de ingeniería de Cremia, incluidas en su costo de administración; la planta no las necesita para operar.

### 2.2 La arquitectura en cifras

| Nivel ISA-95 | Hoy | Con la propuesta |
| --- | --- | --- |
| 4 · Gestión empresarial | Sin sistema: pedidos y compras en papel; la planta solo tiene su facturador electrónico | ERP ligero de la plataforma Cremia MES/ERP en Huawei Cloud |
| 3 · Gestión de operaciones | Programación verbal | MES de la plataforma Cremia MES/ERP en Huawei Cloud, con caché y cola en la planta |
| 2 · Control y supervisión | Ninguno: válvulas manuales | 1 PLC (PLC-01), 6 máquinas con controlador propio (CK-401, CK-402, CD-401, CD-402, LL-402 y EMP-401), la unidad de frío de TK-102, 1 nodo de borde con SCADA en Node-RED (más 1 de repuesto) y 2 HMI |
| 1 · Medición y actuación | Termómetro, acidómetro y gramera | 25 sensores y 22 actuadores: 15 entradas analógicas, 4 salidas analógicas, 3 entradas de pulsos, 4 puertos IO-Link, 23 entradas y 19 salidas digitales (68 señales; 83 con reserva del 20 %) y 20 nodos EtherNet/IP, de ellos 11 variadores. El proyecto compra 24 sensores, 20 actuadores y 19 nodos; la celda R-501 tiene sus señales reservadas |
| 0 · Proceso | 9 equipos, un lote diario | 28 equipos en 8 unidades ISA-88: 9 existentes y 19 nuevos, de los cuales el proyecto compra 18 |
| Robots | Ninguno | 1 robot de paletizado de cuatro ejes (R-501) que encanasta, encajona y estiba; diseñado en el proyecto y comprado en una etapa posterior |

## 3. Redes y protocolos

| Enlace | Medio y protocolo | Uso |
| --- | --- | --- |
| Instrumento a E/S remota | 4–20 mA, IO-Link y señales de 24 V DC | Mediciones y mandos de campo |
| E/S remota, variadores y máquinas a PLC | EtherNet/IP en anillo DLR con un conmutador administrable de celda (Stratix 5700); el anillo se recupera en menos de 3 ms si se corta un cable | Control en tiempo real |
| PLC a nodo de borde | OPC UA cifrado y autenticado con certificados | Variables, alarmas, receta activa, estado de fases y descarga de la receta de control |
| Nodo de borde a plataforma | MQTT sobre TLS, conexión saliente, con certificado por dispositivo; cola local de 72 h | Eventos de lote, consumos, conteos, paradas, curvas de los puntos críticos, alarmas, recetas y señal de vida |
| Usuarios a plataforma | HTTPS desde un navegador, con doble factor para los roles que aprueban | Gestión, calidad, compras, ventas y tablero gerencial |
| Plataforma a facturador | Exportación de pedidos despachados (archivo o API del facturador) | Facturación electrónica, que sigue en el sistema de la planta |

**Zona desmilitarizada.** Entre la red de control y internet hay una zona desmilitarizada con un cortafuegos industrial. Tiene dos funciones:

- **Salida controlada.** Solo deja pasar las conexiones salientes del nodo de borde hacia el intermediario MQTT de la nube (puerto 8883) y las actualizaciones firmadas. No hay puertos abiertos hacia la planta.
- **Acceso remoto.** El soporte de Cremia entra por una VPN saliente que abre el equipo de salto solo cuando el jefe de producción la autoriza, con doble factor; nunca llega directo a la red de control.

## 4. Estrategia de control

El PLC-01 ejecuta dos capas de control. La primera es el control secuencial por fases según ISA-88, que sigue el procedimiento de la receta. La segunda es el control regulatorio con PID: TIC-301 con rango dividido sobre vapor y agua fría, y con agua helada en el enfriamiento nocturno del lote 2; TIC-302 con prealimentación del caudal de yogur; FFC-403 como control de relación de la fruta; PIC-302 para la presión del homogeneizador y la dosificación por peso en dos velocidades.

La propuesta no usa control avanzado (control predictivo por modelo, control difuso o adaptativo). Cada lazo tiene un actuador dominante, las dinámicas son lentas y conocidas y el proceso es por lotes, de modo que el PID cumple las tolerancias y el personal de la planta lo puede mantener. La justificación completa está en la sección 8.1 del documento de equipos, sensores, actuadores, variables y comunicaciones.

El PLC no depende del nodo de borde ni de la nube para terminar una fase: si se pierde la comunicación, la fase en curso termina con sus enclavamientos y el lote queda en espera segura antes de la fase siguiente que necesite un operario.

## 5. Flujo de información entre OT e IT

### 5.1 De IT hacia OT

| Información | Origen | Destino | Momento |
| --- | --- | --- | --- |
| Plan de producción semanal: referencias y cantidades | ERP de la plataforma | MES de la plataforma | Semanal y cuando cambia la demanda |
| Disponibilidad de leche, insumos y material de envase | ERP | MES | Diaria y antes de liberar cada orden |
| Orden de producción y receta de control | MES | Nodo de borde (caché) y PLC | Al liberar el lote, con 48 h de anticipación como máximo |
| Código de lote y fecha de vencimiento | MES | Codificadores CD-401 y CD-402, a través del nodo de borde | Al arrancar el envasado |
| Consignas y mandos del operador | HMI-01 y HMI-02 | PLC | Durante el lote |

### 5.2 De OT hacia IT

| Información | Origen | Destino | Uso |
| --- | --- | --- | --- |
| Mediciones de proceso: temperatura, pH, nivel, caudal, peso y presión de homogeneización | Sensores y PLC | Historiador local y, para los puntos críticos, el registro de lote | Control, tendencias y registro de lote |
| Inicio y fin de cada fase, y alarmas | PLC | Nodo de borde y MES | Seguimiento del lote y análisis de paradas |
| Cantidades dosificadas frente a la fórmula | PLC | MES | Consumo real y trazabilidad de insumos |
| Curva de pasteurización, pH final y temperatura del enfriamiento nocturno | Historiador local | MES | Liberación del lote por calidad |
| Unidades producidas y rechazadas por peso | CK-401 y CK-402 | MES | Rendimiento, producto no conforme y OEE |
| Estado y paradas de EMP-401 y LL-402 | PLC | MES | Disponibilidad y mantenimiento |
| Resultados de laboratorio de la leche por cantina | HMI-01 | MES | Aceptación de la leche y pago al proveedor |
| Temperatura y nivel de TK-102 | Unidad de frío y PLC | MES | Conservación de la leche del lote 2 |
| Producción terminada, consumos e inventario en cuarto frío | MES | ERP (misma base de datos) | Inventarios, costos y despacho |
| Señal de vida del nodo de borde | Nodo de borde | Vigilancia en la nube | Aviso al jefe de producción si se pierde la planta |

### 5.3 Recorrido de un lote

1. El ERP de la plataforma genera el plan semanal a partir de los pedidos.
2. El MES programa los dos lotes del día y verifica que haya leche, insumos y envase.
3. Al liberar el lote, el MES crea la receta de control a partir de la receta maestra y la envía al nodo de borde, que la guarda en caché y la descarga al PLC cuando el operador arranca el lote.
4. El PLC ejecuta las fases: carga, dosificación, estandarización y homogeneización, pasteurización, inoculación, incubación, ruptura, saborizado, enfriamiento y transferencia.
5. El nodo de borde muestra el avance, guarda las mediciones en el historiador local y envía a la nube los eventos del lote.
6. Los codificadores imprimen el lote y la fecha de vencimiento en cada unidad, y las controladoras de peso reportan las unidades conformes y rechazadas.
7. Calidad revisa el registro electrónico y los análisis, y libera el lote en la plataforma.
8. La plataforma actualiza el inventario disponible para despacho y el costo real del lote.

## 6. Funciones por sistema

| Sistema | Funciones |
| --- | --- |
| PLC-01 | Lógica de fases según ISA-88, lazos PID TIC-301 y TIC-302, presión de homogeneización, control de relación de fruta, enclavamientos y alarmas de proceso |
| Nodo de borde (SCADA en Node-RED) | Pantallas según ISA-101, alarmas según ISA-18.2, tendencias, historiador local, usuarios del piso de planta, caché de recetas, descarga al PLC, cola de mensajes y señal de vida |
| MES de la plataforma | Órdenes de producción, gestión de recetas, registro electrónico de lote, trazabilidad, calidad, paradas e indicadores (OEE, rendimiento y producto no conforme) |
| ERP ligero de la plataforma | Pedidos, plan de producción, requerimiento de materiales, compras, inventarios, costos por lote y despacho; exportación al facturador |

## 7. Ciberseguridad

- Segmentación por zonas y conductos según IEC 62443: zona de control (PLC, E/S, variadores y nodo de borde), zona desmilitarizada y zona de nube.
- Solo conexiones salientes desde la planta, con certificados por dispositivo.
- Usuarios con roles: operador, supervisor, calidad, compras, mantenimiento, gerencia y administrador; doble factor para aprobar recetas y liberar lotes.
- Cambios de receta y de consignas con registro de usuario, fecha y valor anterior.
- Copias de respaldo diarias y cifradas de la base de datos de la plataforma, y copia semanal del programa del PLC y de los flujos de Node-RED, guardadas en la nube.
- Si se cae la conexión con la nube, el nodo de borde sigue registrando los lotes y envía los mensajes pendientes cuando vuelve la conexión.

## 8. Las personas en la arquitectura

La arquitectura cambia la forma de trabajar de cada rol. El operador deja de anotar en papel y opera desde la HMI; el jefe de producción programa y sigue los lotes en la plataforma y recibe en su teléfono las alarmas del lote nocturno; calidad libera los lotes con el registro electrónico; compras pide insumos con el requerimiento de materiales; la gerencia decide con un tablero diario. La capacitación por rol, los procedimientos y el plan de gestión del cambio están en el documento Propuesta de valor y gestión del cambio.

## Referencias

- ANSI/ISA-95.00.01-2010 (IEC 62264-1). Enterprise-Control System Integration, Part 1: Models and Terminology.
- ANSI/ISA-95.00.02. Enterprise-Control System Integration, Part 2: Objects and Attributes for Enterprise-Control System Integration.
- ANSI/ISA-88.00.01-2010. Batch Control Part 1: Models and Terminology.
- IEC 62443. Security for industrial automation and control systems.
- ANSI/ISA-101.01-2015. Human Machine Interfaces for Process Automation Systems.
- ANSI/ISA-18.2-2016. Management of Alarm Systems for the Process Industries.
- ANSI/ISA-5.1-2009. Instrumentation Symbols and Identification.
- OASIS. MQTT Version 5.0.
