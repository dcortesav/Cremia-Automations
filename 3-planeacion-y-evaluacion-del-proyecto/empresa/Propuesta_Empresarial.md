# Propuesta empresarial

**Empresa, roles, principal contribución de cada integrante, salarios, margen y modelo de negocio**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Empresa

## 1. La empresa

Cremia Automations es una empresa integradora de soluciones de Transformación Digital Industrial para el sector lácteo. Diseña, integra y pone en marcha soluciones de automatización que conectan el proceso, el control, la supervisión y la gestión de la producción, con base en ISA-88 e ISA-95, y acompaña a las personas de la planta para que adopten la nueva forma de trabajar. Además de integrar equipos de terceros, desarrolla su propio software para pymes: un SCADA en Node-RED y la plataforma Cremia MES/ERP, que corre en Huawei Cloud.

Cliente del proyecto: La Hacienda Productos Alimenticios, una planta pequeña que produce un lote diario de yogur de 550 L de leche (3.052 bolsas de 200 ml llenadas, 2.898 conformes) con cuatro operarios y bajo nivel de automatización.

Propuesta de valor: una sola empresa entrega la solución completa, desde el instrumento hasta el indicador de gestión, con recetas y trazabilidad por lote y con software de supervisión y gestión hecho a la escala de la planta, sin licencias de terceros, y con una licencia propia de Studio 5000 para que la planta pueda abrir y diagnosticar el programa del PLC; la valida en un gemelo digital antes de intervenir la planta y prepara al personal con capacitación por rol y seis semanas de estabilización con producción. Para los dueños, la propuesta significa duplicar la producción con la misma planta, pasar de una a tres referencias, bajar el producto no conforme de 5,06 % a 1,5 % o menos y contar con información diaria para decidir, disponible aunque falle la planta.

### 1.1 Mercado objetivo

Cremia se dirige a las plantas pequeñas y medianas de derivados lácteos de Colombia (yogur, kumis, quesos frescos y postres lácteos) que cumplen estas condiciones:

| Criterio | Cliente objetivo |
| --- | --- |
| Tamaño | Entre unos 500 y 20.000 L de leche por día, con una a cinco líneas de producción |
| Nivel de automatización | Operación mayormente manual, registros en papel y sin MES ni ERP de manufactura |
| Necesidad | Crecer sin construir una planta nueva, ampliar el portafolio, bajar pérdidas y demostrar trazabilidad ante cadenas de supermercados y ante el INVIMA |
| Quién decide | El dueño o gerente de una empresa familiar, que busca una inversión que su flujo pueda pagar y una solución que su personal pueda mantener, sin licencias que no puede costear |
| Región inicial | Cundinamarca y Boyacá, cerca de Bogotá; después Antioquia y Nariño, las otras cuencas lecheras grandes del país |

**Por qué este segmento.** Las grandes procesadoras ya trabajan con integradores internacionales y sistemas corporativos. Las pymes, en cambio, no tienen un departamento de ingeniería, y las plataformas licenciadas de MES y ERP cuestan más de lo que una línea puede pagar. Necesitan un solo proveedor que entregue la solución completa a su escala y prepare a su gente. La Hacienda es un cliente típico del segmento: una línea, cuatro operarios, un lote diario y ningún sistema de información.

**Portafolio para el segmento.** (1) Diagnóstico con VSM y gemelo digital; (2) automatización de una línea con recetas ISA-88, como en La Hacienda; (3) plataforma Cremia MES/ERP en Huawei Cloud y SCADA en Node-RED, con licencia perpetua por sitio; (4) plan de servicio recurrente: nube, soporte, evolución y analítica. El cliente puede empezar por el diagnóstico y avanzar por etapas. Los canales comerciales son los gremios del sector lácteo, los proveedores de equipos de proceso y las referencias de clientes.

## 2. Roles y principal contribución

| Integrante | Rol | Principal contribución |
| --- | --- | --- |
| David Santiago Cortés Ávila | Gerente de proyecto | Coordinación del equipo, análisis del caso de estudio, modelos físico y procedimental ISA-88, programa de fases del PLC, repositorio y página web |
| Ana María Orozco Reyes | Líder de simulación y mejora | VSM, indicadores productivos, simulación en Tecnomatix, gemelo digital en Siemens NX Mechatronics Concept Designer, OEE y pruebas del software |
| Jesús Alberto Rivera Molina | Líder de arquitectura digital | Estado del arte de las tres líneas, arquitectura ISA-95, red OT/IT, ciberseguridad, infraestructura en Huawei Cloud y nodo de borde |
| David Felipe Cárdenas Cubides | Líder de gestión de producción | Tiempos y capacidades, necesidades de información, SCADA en Node-RED y núcleo y registro de lote de la plataforma Cremia MES/ERP |
| Cristian Stiven Hoyos Peralta | Líder financiero y comercial | Salarios, margen, presupuesto, análisis económico, modelo de negocio, gestión del cambio y ERP ligero de la plataforma (inventario, compras y costos) |
| José Andrés Zapata Piñeros | Líder de procesos e instrumentación | Recetas y lotes según ISA-88; equipos, sensores, actuadores, variables, estrategia de control y comunicaciones; recetas y calidad en la plataforma |

### 2.1 Líder técnico por módulo

Cada módulo tiene un líder técnico que coordina su desarrollo, revisa la calidad de sus entregables y responde por su coherencia con los demás módulos. El gerente de proyecto integra los cuatro módulos. Todos los integrantes conocen la propuesta completa y pueden sustentarla.

| Módulo | Líder técnico | Apoyo | Entregables que revisa |
| --- | --- | --- | --- |
| 0 · Estado del arte | Jesús Alberto Rivera Molina | Cristian Hoyos | Estado del arte de las tres líneas y justificación de la línea de yogur |
| 1 · Transformación Digital Industrial | José Andrés Zapata Piñeros | Jesús Rivera (arquitectura ISA-95 y nube), David Cortés (modelos ISA-88) y David Cárdenas (plataforma y SCADA) | Parámetros, recetas y lotes, modelos ISA-88, equipos e instrumentación, estrategia de control, arquitectura ISA-95, flujo OT/IT y plataforma Cremia MES/ERP |
| 2 · Gestión y evaluación de la producción | David Felipe Cárdenas Cubides | Ana Orozco (VSM y simulación) | Tiempos y capacidades, VSM actual y propuesto, gemelo digital, necesidades de información del MES y del ERP |
| 3 · Planeación y evaluación del proyecto | Cristian Stiven Hoyos Peralta | David Cortés (EDT y cronograma) | EDT del proyecto y del proceso, cronograma, presupuesto, análisis económico, propuesta de valor y gestión del cambio |
| Integración | David Santiago Cortés Ávila | Todos | Coherencia entre el repositorio, la página web y la presentación, con el verificador de `herramientas/` |

## 3. Salarios (costo interno de Cremia)

El equipo es de seis ingenieros mecatrónicos con un año de experiencia. Para los líderes de área se toma un salario de COP 4.000.000 (2,22 salarios mínimos) y para el gerente de proyecto uno de COP 6.000.000 (3,33 salarios mínimos), de acuerdo con las bandas de enganche del Observatorio Laboral para la Educación, el escalafón 1 de ACIEM y la guía salarial de Michael Page Colombia.

| Cargo | Cantidad | Salario mensual (COP) | Costo empresa mensual (COP) | Costo por hora (COP) |
| --- | --- | --- | --- | --- |
| Gerente de proyecto | 1 | 6.000.000 | 9.120.000 | 50.110 |
| Líder de área | 5 | 4.000.000 | 6.080.000 | 33.407 |
| Nómina mensual | 6 | 26.000.000 | 39.520.000 | — |

Factor prestacional de 1,52 (seguridad social, parafiscales, cesantías, prima y vacaciones) y 182 horas laborables al mes con la jornada de 42 horas semanales.

## 4. Margen y precio de la ingeniería

| Componente | Porcentaje | Se aplica sobre |
| --- | --- | --- |
| Administración (oficina, licencias de las herramientas de ingeniería de Cremia, equipos de cómputo y pólizas) | 15 % | Costo directo de personal |
| Imprevistos | 5 % | Costo directo más administración |
| Utilidad | 15 % | Costo más administración e imprevistos |
| Factor multiplicador | 1,39 | Costo directo de personal |

| Cargo | Costo por hora (COP) | Tarifa mínima con el factor 1,39 (COP/h) |
| --- | --- | --- |
| Gerente de proyecto | 50.110 | 69.700 |
| Líder de área | 33.407 | 46.500 |

El factor de 1,39 es el mínimo que debe cubrir el conjunto de la ingeniería sobre la nómina completa del proyecto. Al cliente no se le cobra nómina: se le cobran servicios de ingeniería por actividad, con las horas de la EDT a una tarifa propia de cada integrante, según el tipo de valor que aporta.

<!-- tabla:tarifas -->
| Integrante | Tipo de valor | Horas | Tarifa (COP/h) | Factor sobre su costo | Millones de COP |
| --- | --- | --- | --- | --- | --- |
| David Santiago Cortés Ávila | Dirección y control | 775 | 90.000 | 1,80 | 69,75 |
| Ana María Orozco Reyes | Núcleo técnico de validación | 810 | 67.000 | 2,01 | 54,27 |
| Jesús Alberto Rivera Molina | Especialidad escasa y crítica | 805 | 71.000 | 2,13 | 57,16 |
| David Felipe Cárdenas Cubides | Especialidad escasa y crítica | 815 | 71.000 | 2,13 | 57,87 |
| José Andrés Zapata Piñeros | Núcleo técnico del proceso | 800 | 67.000 | 2,01 | 53,60 |
| Cristian Stiven Hoyos Peralta | Gestión y soporte | 775 | 53.000 | 1,59 | 41,08 |
| **Total** | | **4.780** | **69.815 en promedio** | | **333,71** |
<!-- /tabla:tarifas -->

| Integrante | Valor que aporta al proyecto |
| --- | --- |
| David Santiago Cortés Ávila | Dirige el proyecto, programa las fases ISA-88 del PLC y el lote nocturno, y responde por la puesta en marcha virtual, las pruebas SAT y la estabilización |
| Ana María Orozco Reyes | Construye el gemelo digital, valida el estado propuesto, desarrolla el módulo de OEE y el tablero, y dirige las pruebas del software |
| Jesús Alberto Rivera Molina | Diseña la red OT/IT, la ciberseguridad según IEC 62443, la infraestructura en Huawei Cloud y el nodo de borde, y programa el envasado del PLC |
| David Felipe Cárdenas Cubides | Desarrolla el SCADA en Node-RED y el núcleo y el registro de lote de la plataforma, de donde salen la trazabilidad y los indicadores |
| José Andrés Zapata Piñeros | Especifica equipos e instrumentos, diseña los tableros, configura las recetas y la calidad en la plataforma y lidera el montaje y el arranque con producto |
| Cristian Stiven Hoyos Peralta | Compras, contratos e importación, control de costos y gestión del cambio; desarrolla el ERP ligero (inventario, pedidos, compras y costo por lote) y apoya la integración borde–nube bajo la dirección de Jesús Rivera |

El proyecto de 26 semanas tiene 4.780 horas y vale COP 333,7 millones en dos contratos (diseño, procura y gestión de compras, 62,1 millones; implementación, software, puesta en marcha y adopción, 271,6 millones). Como comprobación interna, ese valor cubre la nómina de Cremia durante las 26 semanas (COP 237,1 millones) con un factor de 1,41 y deja COP 96,6 millones para administración, imprevistos y utilidad.

## 5. Modelo de negocio

| Criterio | A. Llave en mano clásico | B. Arrendamiento de equipos | C. Llave en mano con plan de servicio |
| --- | --- | --- | --- |
| Qué paga el cliente | La inversión, por hitos | Una cuota mensual | La inversión por hitos y un plan de servicio anual |
| Propiedad de los equipos | Cliente | Cremia | Cliente |
| Software de gestión | Licencias de terceros | Incluido en la cuota | Plataforma Cremia MES/ERP con licencia perpetua por sitio |
| Capital que necesita Cremia | Bajo | Muy alto | Bajo |
| Riesgo para Cremia | Bajo | Alto: cartera y obsolescencia | Bajo |
| Relación a largo plazo | Termina con el proyecto | Continua | Continua y colaborativa |

**Modelo recomendado: C.** Cremia no tiene capital para financiar equipos de proceso, lo que descarta el arrendamiento. El cliente queda como dueño de los equipos y recibe una licencia perpetua de la plataforma para su sitio. Cremia conserva la propiedad intelectual de la plataforma, que reutiliza en las siguientes plantas del segmento, y mantiene un ingreso recurrente con el plan de servicio (COP 36,0 millones al año, ya incluidos en los costos de operación del cliente): la nube Huawei (15,0) y el soporte y la evolución del PLC, el SCADA y la plataforma (21,0), con una revisión trimestral de indicadores con la gerencia de la planta.

**Protección del cliente frente a la dependencia.** El código fuente de la plataforma se deposita con un tercero y se entrega a La Hacienda si Cremia deja de prestar el servicio; la planta puede exportar sus datos completos en cualquier momento; el programa del PLC, los flujos de Node-RED y las recetas son del cliente, y la planta recibe su propia licencia perpetua de Studio 5000 (COP 28,7 millones en la inversión y COP 8,2 millones al año de mantenimiento) para abrir, diagnosticar y respaldar el programa del PLC sin depender de Cremia.

| Hito | Semana | Pago |
| --- | --- | --- |
| Firma del contrato, con las cartas de intención de los distribuidores | 1 | 30 % |
| Pruebas FAT aprobadas | 14 | 30 % |
| Puesta en marcha y pruebas SAT | 21 | 30 % |
| Cierre y entrega | 26 | 10 % |
| Plan de servicio Cremia | Después de la entrega | COP 36,0 millones al año |

## 6. Oferta para La Hacienda

| Elemento | Oferta |
| --- | --- |
| Alcance | Ingeniería, suministro, montaje, programación, licencia de Studio 5000 para la planta, SCADA en Node-RED, plataforma Cremia MES/ERP en Huawei Cloud, puesta en marcha, gestión del cambio, capacitación y estabilización para la línea de yogur |
| Resultado para el cliente | De uno a dos lotes diarios, de una a tres referencias y producto no conforme de 5,06 % a 1,5 % o menos |
| Valor | COP 1.495,5 millones, sin IVA, a precio fijo (incluye la contingencia del 8 %, a riesgo de Cremia) |
| Plazo | 26 semanas, del 18 de enero al 16 de julio de 2027 |
| Garantía | 12 meses sobre la integración y seis semanas de estabilización con producción dentro del proyecto |
| Indicadores financieros para el cliente | VPN al 15 % después de impuestos de COP 189,4 millones, TIR de 18,9 % y recuperación en 3,9 años |
| Etapa posterior opcional | Celda robotizada de encanastado y paletizado, con espacio e interfaz ya diseñados |

El detalle del presupuesto, el flujo de caja y los indicadores financieros está en la propuesta económica de la línea de yogur; el plan de trabajo, en la EDT y el cronograma del proyecto; el software, en el documento de la plataforma Cremia MES/ERP y el SCADA en Node-RED; y los beneficios para los dueños y el plan de gestión del cambio, en el documento Propuesta de valor y gestión del cambio.
