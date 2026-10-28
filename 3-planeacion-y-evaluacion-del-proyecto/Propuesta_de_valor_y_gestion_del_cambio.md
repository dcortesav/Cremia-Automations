# Propuesta de valor y gestión del cambio

**Beneficios para los dueños de La Hacienda y plan para que las personas adopten la nueva forma de trabajar**

**Proyecto:** Transformación Digital Industrial de la planta La Hacienda  
**Módulo:** Módulo 3 · Planeación y Evaluación de Proyectos

## 1. Alcance

Este documento responde dos preguntas. La primera es qué ganan los dueños de La Hacienda con la transformación digital de la línea de yogur, en productividad, costos, calidad, trazabilidad, disponibilidad de información y toma de decisiones. La segunda es cómo se prepara a las personas de la planta para que la nueva línea funcione como se diseñó: quién cambia de tareas, qué procedimientos se reescriben, cómo se capacita a cada rol, cómo se maneja la resistencia y cómo sigue la transformación después de la entrega.

La transformación digital de la planta no termina con la puesta en marcha. El proyecto de 16 semanas instala la tecnología y deja a las personas preparadas; la mejora continua con los datos que entrega el sistema es lo que mantiene y amplía los beneficios.

### 1.1 Qué entendemos por Transformación Digital Industrial

La Transformación Digital Industrial no es comprar tecnología: es cambiar la forma en que la empresa produce y decide, con cuatro componentes que avanzan juntos. Si solo cambia la tecnología, la planta queda con equipos que nadie usa como se diseñaron.

| Componente | Qué significa | Cómo se aplica en La Hacienda |
| --- | --- | --- |
| Estrategia | Para qué se transforma la empresa | Duplicar la producción con el mismo tanque y entrar al mercado de yogur en vaso, de mayor margen |
| Tecnología | Con qué herramientas | Instrumentación, PLC, SCADA, MES y ERP, integrados según ISA-88 e ISA-95 |
| Procesos | Cómo cambia el trabajo | Nueve procedimientos reescritos con los operarios: programación, dosificación, liberación de lotes, CIP y mantenimiento (sección 4) |
| Personas y cultura | Quién lo hace y cómo decide | Nadie sale de la planta: cada tarea automatizada tiene una nueva función para quien la hacía (sección 3.3), capacitación por rol y decisiones con datos en la reunión diaria |

### 1.1 Qué entendemos por Transformación Digital Industrial

La Transformación Digital Industrial no es comprar tecnología: es cambiar la forma en que la empresa produce y decide, con cuatro componentes que avanzan juntos. Si solo cambia la tecnología, la planta queda con equipos que nadie usa como se diseñaron.

| Componente | Qué significa | Cómo se aplica en La Hacienda |
| --- | --- | --- |
| Estrategia | Para qué se transforma la empresa | Duplicar la producción con el mismo tanque y entrar al mercado de yogur en vaso, de mayor margen |
| Tecnología | Con qué herramientas | Instrumentación, PLC, SCADA, MES y ERP, integrados según ISA-88 e ISA-95 |
| Procesos | Cómo cambia el trabajo | Nueve procedimientos reescritos con los operarios: programación, dosificación, liberación de lotes, CIP y mantenimiento (sección 4) |
| Personas y cultura | Quién lo hace y cómo decide | Nadie sale de la planta: cada tarea automatizada tiene una nueva función para quien la hacía (sección 3.3), capacitación por rol y decisiones con datos en la reunión diaria |

## 2. Propuesta de valor para los dueños

### 2.1 Beneficios medibles

| Dimensión | Hoy | Con la propuesta | Cómo se mide |
| --- | --- | --- | --- |
| Productividad | 3.052 bolsas por día con 4 operarios: 763 unidades por operario al día | 6.604 unidades por día en promedio con 5 operarios: 1.321 por operario al día (+73 %) | Unidades conformes por día y por operario, en el MES |
| Capacidad | Un lote de 550 L por día; el tanque queda ocupado toda la noche | Dos lotes por día (1.100 L de leche); el tanque queda libre a las 15:05 | Lotes por día y ocupación del tanque T-301 |
| Ingresos | Ventas de COP 1.098,7 millones al año, una sola referencia | Ventas de COP 3.074,6 millones al año con tres referencias | Ventas por referencia en el ERP |
| Costos | Mano de obra de 147 COP por unidad; sin costo real por lote | Mano de obra de 85 COP por unidad (−42 %); costo real de leche, insumos y envase por lote | Costo por lote en el MES y el ERP |
| Calidad | 5,06 % de producto no conforme; se pesa una de cada cinco bolsas | 1,5 % o menos; se pesa el 100 % y los puntos críticos tienen registro continuo | Producto no conforme por lote y por causa |
| Eficiencia de la empacadora (OEE) | ≈ 68 % estimado: disponibilidad 90 %, rendimiento 80 % y calidad 95 % | 82 %: disponibilidad 92 %, rendimiento 90 % y calidad 98,5 % | OEE por turno en el MES |
| Trazabilidad | Registros en papel; un retiro de producto afecta varios días de producción | Registro electrónico de cada lote, desde la cantina de leche hasta la estiba | Tiempo para reconstruir la genealogía de un lote: de horas a minutos |
| Disponibilidad de información | No hay datos: la programación es verbal y los registros son manuales | Tablero diario con OEE, rendimiento, no conformes, consumos, paradas y alarmas | Indicadores disponibles el mismo día |
| Toma de decisiones | Por experiencia del operario y sin datos | Qué referencia producir según su margen, cuánta leche comprar según el plan semanal y cuándo intervenir un equipo según sus horas de trabajo | Reunión semanal de indicadores con la gerencia |
| Resultado financiero | Margen de contribución de COP 494,4 millones al año | Beneficio neto adicional de COP 738 millones al año; VPN al 15 % de COP 617 millones, TIR de 30,6 % y recuperación en 2,7 años | Flujo de caja real frente al proyectado |

Las cifras de producción salen del documento de recetas y lotes (semana de referencia de 10 lotes) y las financieras, de la propuesta económica. El costo de mano de obra por unidad usa un costo de COP 33,6 millones al año por operario: 4 operarios para 915.600 unidades hoy y 5 operarios para 1.981.320 unidades con la propuesta.

### 2.2 Qué tecnología produce cada beneficio

| Beneficio | Tecnología que lo produce | Por qué |
| --- | --- | --- |
| Segundo lote diario | Intercambiador de placas E-301 con agua helada | Enfría el yogur en 25 min y libera el tanque, que hoy espera toda la noche |
| Tiempo por lote de 601 a 493 min | Bomba de leche de 3 m³/h, dosificación por peso y control automático de temperatura | Quita transportes, pesajes manuales y el exceso de sostenimiento en la pasteurización |
| Menos producto no conforme | Controladoras de peso del 100 %, pH en línea y control PID de temperatura | Cada unidad fuera de peso se rechaza y cada lote termina en el pH correcto |
| Tres referencias con los mismos equipos | Recetas maestras ISA-88 en el MES y llenadora de vasos | Cambiar de referencia es cambiar datos, no programas |
| Trazabilidad | MES con registro electrónico de lote y codificadores de lote y fecha | Cada unidad lleva su lote y cada lote guarda su leche, insumos, parámetros y resultados |
| Información para decidir | SCADA con historiador, MES e integración con el ERP | Los datos de planta llegan a la gestión sin transcripción |

### 2.3 Qué no cambia

- El análisis de la leche por cantina sigue siendo manual: es una decisión de calidad que se registra en el sistema.
- La inspección del sellado de la bolsa sigue por muestreo, con registro en HMI-01.
- La incubación dura 240 min, porque depende del cultivo. Lo que cambia es el enfriamiento: el lote 1 se enfría en placas y libera el tanque a las 15:05, y el lote 2 se enfría en la chaqueta, con control automático, durante la noche.
- No hay despidos: los cuatro operarios siguen en la línea y se crea un puesto para el segundo lote.

## 3. Las personas en la nueva línea

### 3.1 Partes interesadas

| Grupo | Qué cambia para ellos | Qué necesitan | Nivel de impacto |
| --- | --- | --- | --- |
| Dueños y gerencia | Deciden con indicadores diarios; invierten COP 1.325,8 millones | Ver el retorno y entender el tablero | Medio |
| Jefe de producción | Programa lotes en el MES, sigue el avance en el SCADA y lidera la reunión diaria | Dominio del MES y de los indicadores | Alto |
| Operarios (hoy 4) | Dejan de pesar insumos y abrir válvulas a mano; operan desde la HMI y atienden alarmas | Capacitación práctica y seguridad sobre su puesto | Alto |
| Operario nuevo del segundo lote | Se integra con la línea ya automatizada | Inducción completa | Alto |
| Calidad | Libera lotes en el MES con el registro electrónico y verifica la calibración de los instrumentos críticos | Criterios de liberación y manejo del MES | Medio |
| Mantenimiento (contratado o interno) | Atiende instrumentos, variadores, PLC y máquinas de envasado | Formación técnica y repuestos | Alto |
| Ventas y distribución | Venden dos referencias nuevas en vaso | Fichas de producto y plan de lanzamiento | Medio |
| Proveedores de leche | Reciben resultados de laboratorio por cantina registrados en el sistema | Información clara sobre la calidad de su leche | Bajo |

### 3.2 Roles de operación

| Rol | Tareas en la nueva línea | Personas | Origen |
| --- | --- | --- | --- |
| Operador de recepción y laboratorio | Descarga y análisis de cantinas, registro en HMI-01, carga del tanque | 1 | Operario actual |
| Operador de preparación | Arranque de la receta, dosificación, seguimiento de fases y alarmas en HMI-01, CIP | 1 | Operario actual |
| Operador de envasado | Empacadora y llenadora, cambios de referencia, codificado, control de peso en HMI-02 | 1 | Operario actual |
| Operador de empaque y cuarto frío | Encanastado de bolsas y encajonado de vasos, estibas, cuarto frío y despacho; muestreo del sellado | 1 | Operario actual |
| Operador del segundo lote | Carga, pasteurización e inoculación del lote 2 (15:05 a 18:15) y verificación de las alarmas de la incubación nocturna | 1 | Contratación nueva |
| Técnico de mantenimiento de primer nivel | Mantenimiento autónomo, calibraciones de rutina y primer diagnóstico; el soporte de segundo nivel lo da Cremia | 1 de los operarios, con formación adicional | Operario actual |

La incubación del lote 2 ocurre sin operario, con control automático y alarmas remotas al jefe de producción.

### 3.3 Qué pasa con cada tarea que se automatiza

Ningún puesto se elimina. El tiempo que la automatización libera se dedica a lo que la nueva línea necesita: el segundo lote, la llenadora de vasos, los cambios de referencia, la calidad y el mantenimiento autónomo.

| Tarea que hoy es manual | Qué la reemplaza | Nueva función de quien la hacía | Capacitación |
| --- | --- | --- | --- |
| Cálculo y pesaje de insumos en dos cuartos | Dosificación automática por peso desde la receta | Operador de preparación: arranca la receta, vigila las fases y las alarmas en HMI-01 y ejecuta el CIP | 24 h por rol y certificación |
| Apertura de válvulas de vapor y agua y lectura del termómetro | Control PID de temperatura (TIC-301) | El mismo operador supervisa el lazo y verifica con el técnico la calibración de TT-301 y AT-301 | Incluida en las 24 h |
| Prueba de acidez para decidir el fin de la incubación | pH en línea (AT-301) | Calidad confirma la acidez una vez por lote y libera el lote en el MES | 12 h para calidad |
| Pesaje de una de cada cinco bolsas | Controladora de peso con rechazo automático | Operador de envasado: cambios de referencia, ajuste de dosis y operación de la nueva llenadora de vasos | 24 h y certificación |
| Registros en papel | Registro electrónico en el MES | Todos registran en la HMI; el jefe de producción usa el tablero en la reunión diaria | Incluida en cada rol |
| Mantenimiento solo correctivo | Mantenimiento autónomo y preventivo por horas | Uno de los operarios se forma como técnico de primer nivel | 32 h |
| Encanastado manual (etapa posterior) | Celda robotizada R-501, cuando el volumen la justifique | El operador de empaque pasa a operar la celda (cargue de cajas, cambio de patrón de estiba y recuperación de paradas) y a atender el cuarto frío y el despacho, que crecen con el volumen | 16 h con el fabricante del robot, según ISO 10218 |

La compra del robot se justifica por el crecimiento del volumen, no por reducir personal. Las competencias nuevas se reconocen con una certificación interna por rol (operador, operador certificado y técnico de primer nivel), que la planta puede usar como ruta de crecimiento para sus trabajadores.

### 3.3 Qué pasa con cada tarea que se automatiza

Ningún puesto se elimina. El tiempo que la automatización libera se dedica a lo que la nueva línea necesita: el segundo lote, la llenadora de vasos, los cambios de referencia, la calidad y el mantenimiento autónomo.

| Tarea que hoy es manual | Qué la reemplaza | Nueva función de quien la hacía | Capacitación |
| --- | --- | --- | --- |
| Cálculo y pesaje de insumos en dos cuartos | Dosificación automática por peso desde la receta | Operador de preparación: arranca la receta, vigila las fases y las alarmas en HMI-01 y ejecuta el CIP | 24 h por rol y certificación |
| Apertura de válvulas de vapor y agua y lectura del termómetro | Control PID de temperatura (TIC-301) | El mismo operador supervisa el lazo y verifica con el técnico la calibración de TT-301 y AT-301 | Incluida en las 24 h |
| Prueba de acidez para decidir el fin de la incubación | pH en línea (AT-301) | Calidad confirma la acidez una vez por lote y libera el lote en el MES | 12 h para calidad |
| Pesaje de una de cada cinco bolsas | Controladora de peso con rechazo automático | Operador de envasado: cambios de referencia, ajuste de dosis y operación de la nueva llenadora de vasos | 24 h y certificación |
| Registros en papel | Registro electrónico en el MES | Todos registran en la HMI; el jefe de producción usa el tablero en la reunión diaria | Incluida en cada rol |
| Mantenimiento solo correctivo | Mantenimiento autónomo y preventivo por horas | Uno de los operarios se forma como técnico de primer nivel | 32 h |
| Encanastado manual (etapa posterior) | Celda robotizada R-501, cuando el volumen la justifique | El operador de empaque pasa a operar la celda (cargue de cajas, cambio de patrón de estiba y recuperación de paradas) y a atender el cuarto frío y el despacho, que crecen con el volumen | 16 h con el fabricante del robot, según ISO 10218 |

La compra del robot se justifica por el crecimiento del volumen, no por reducir personal. Las competencias nuevas se reconocen con una certificación interna por rol (operador, operador certificado y técnico de primer nivel), que la planta puede usar como ruta de crecimiento para sus trabajadores.

## 4. Adaptación de los procesos

| Proceso | Hoy | Con la propuesta | Procedimiento que se escribe |
| --- | --- | --- | --- |
| Recepción de la leche | Análisis por cantina y anotación en papel | Análisis por cantina y registro en HMI-01; el MES asocia la leche al lote | Recepción y aceptación de leche |
| Programación de la producción | Verbal, un lote diario de bolsa | Plan semanal del ERP; el jefe de producción libera las órdenes en el MES | Programación y liberación de órdenes |
| Dosificación | Cálculo y pesaje manual en dos cuartos | Dosificación automática por peso desde la receta, con lectura del lote de cada insumo | Arranque de lote y dosificación |
| Pasteurización e incubación | Válvulas manuales, termómetro y acidómetro | Control PID de temperatura, pH en línea y alarmas | Operación del tanque de proceso y atención de alarmas |
| Enfriamiento | Natural, durante la noche | Intercambiador de placas a 15–20 °C | Transferencia y enfriamiento |
| Envasado | Una de cada cinco bolsas en gramera | Peso del 100 %, rechazo automático y codificado de lote y fecha | Cambio de referencia y control de peso |
| Liberación del lote | Sin criterio documentado | Calidad revisa el registro electrónico, los fisicoquímicos y los microbiológicos y libera en el MES | Liberación de lote |
| Limpieza | Manual, sin registro | CIP con verificación de conductividad y registro | Limpieza CIP |
| Mantenimiento | Correctivo | Autónomo diario, preventivo por horas y calibración programada | Mantenimiento autónomo y calibración |

Los procedimientos se escriben con los operarios durante las semanas 12 a 16 (paquete 1.9.3 de la EDT), se prueban en el gemelo digital y se ajustan en el arranque.

## 5. Plan de gestión del cambio

### 5.1 Modelo

El plan sigue el modelo ADKAR (conciencia, deseo, conocimiento, habilidad y refuerzo), porque mide el avance de cada persona y no solo el del proyecto. Cada etapa tiene actividades dentro del cronograma de 16 semanas y del acompañamiento posterior.

| Etapa | Objetivo | Actividades | Semanas |
| --- | --- | --- | --- |
| Conciencia | Que todos entiendan por qué cambia la línea | Reunión de lanzamiento con dueños y operarios; recorrido por el VSM y por los problemas actuales (noche de enfriamiento, 5,06 % de no conformes) | 1 y 2 |
| Deseo | Que las personas quieran participar | Compromiso escrito de los dueños de que no hay despidos; agentes de cambio entre los operarios; participación en la validación de recetas y alarmas | 2 a 10 |
| Conocimiento | Que cada rol sepa qué hacer | Capacitación por rol en aula y en el gemelo digital | 11 a 13 |
| Habilidad | Que cada persona lo haga bien en la planta | Práctica guiada en la puesta en marcha; certificación interna antes de operar sin acompañamiento | 14 a 16 |
| Refuerzo | Que la nueva forma de trabajar se mantenga | Reunión diaria con el tablero, reconocimiento de logros, acompañamiento de 8 semanas y revisión trimestral | 16 en adelante |

### 5.2 Roles del cambio

- **Patrocinador:** el dueño o gerente de La Hacienda. Comunica el porqué, aprueba los recursos y asiste a los hitos.
- **Líder del cambio:** el jefe de producción, con el apoyo de Cristian Hoyos y David Cortés por parte de Cremia (paquete 1.9.1).
- **Agentes de cambio:** dos operarios con experiencia, uno de preparación y uno de envasado. Participan en las pruebas FAT y SAT, revisan las pantallas y los procedimientos y apoyan a sus compañeros.

### 5.3 Plan de capacitación por rol

| Rol | Contenido | Horas | Dónde | Evaluación |
| --- | --- | --- | --- | --- |
| Operadores (5) | Nueva línea, recetas, HMI según ISA-101, alarmas, CIP, buenas prácticas y registro de lote | 24 por persona: 8 en aula, 8 en el gemelo digital y 8 en planta | Planta y gemelo digital | Práctica en el gemelo y certificación antes de operar solo |
| Técnico de mantenimiento | Instrumentación, calibración, variadores, diagnóstico básico del PLC, seguridad de las máquinas y mantenimiento autónomo | 32 | Planta y proveedores | Prueba práctica |
| Jefe de producción | MES: órdenes, recetas, registro de lote e indicadores; SCADA | 16 | Gemelo digital y planta | Programación de una semana real |
| Calidad | Liberación de lotes en el MES, puntos críticos y verificación de instrumentos | 12 | Planta | Liberación supervisada de lotes de prueba |
| Dueños y gerencia | Lectura del tablero de indicadores y uso de la información para decidir | 4 | Oficina | Reunión de indicadores |
| Operador de la celda robotizada (etapa posterior) | Operación segura según ISO 10218, cambio de patrón de estiba y recuperación de paradas | 16 | Planta, con el fabricante del robot | Certificación antes de operar la celda |
| Operador de la celda robotizada (etapa posterior) | Operación segura según ISO 10218, cambio de patrón de estiba y recuperación de paradas | 16 | Planta, con el fabricante del robot | Certificación antes de operar la celda |

La capacitación usa el gemelo digital antes del arranque: los operadores practican con la línea virtual sin riesgo para el producto ni para los equipos.

### 5.4 Comunicación

| Mensaje | Audiencia | Medio | Momento |
| --- | --- | --- | --- |
| Por qué y para qué cambia la línea | Todo el personal | Reunión de lanzamiento con el patrocinador | Semana 1 |
| Avance del proyecto y próximos pasos | Todo el personal | Reunión mensual de 30 min y cartelera en planta | Cada mes |
| Cómo será cada puesto | Operarios | Reuniones por rol con los agentes de cambio | Semanas 4 a 10 |
| Demostración de la línea virtual | Operarios, calidad y jefe de producción | Sesión en el gemelo digital | Semana 12 |
| Parada de planta y arranque | Todo el personal y distribuidores | Reunión y comunicado | Semanas 13 y 15 |
| Resultados del arranque | Todo el personal | Tablero en planta y reconocimiento al equipo | Semana 16 |

### 5.5 Resistencia al cambio y respuesta

| Causa probable | Señal | Respuesta |
| --- | --- | --- |
| Miedo a perder el empleo | Poca participación o rechazo abierto | Compromiso escrito de no despidos; el segundo lote crea un puesto; los operarios pasan a tareas de supervisión |
| Desconfianza en la tecnología | Uso de procedimientos viejos en paralelo | Práctica en el gemelo digital; agentes de cambio que acompañan el arranque |
| Pérdida del valor de la experiencia | Comentarios del tipo «así siempre se ha hecho» | La experiencia de los operarios valida recetas, alarmas y procedimientos |
| Más carga durante la transición | Errores y cansancio en las primeras semanas | Arranque asistido, acompañamiento de 8 semanas y rampa de producción del 50 % y 75 % |

## 6. Indicadores de adopción

| Indicador | Meta | Fuente |
| --- | --- | --- |
| Operadores certificados antes de operar solos | 100 % | Registro de capacitación |
| Lotes con registro electrónico completo | 100 % desde la segunda semana de arranque | MES |
| Alarmas atendidas dentro del tiempo definido | 95 % o más | SCADA, según ANSI/ISA-18.2 |
| Producto no conforme | 3 % al final del acompañamiento y 1,5 % o menos al sexto mes | MES |
| OEE de la máquina de envasado | Seguimiento semanal desde el arranque | MES |
| Sugerencias de los operarios implementadas | Al menos una por mes | Reunión semanal |
| Reunión semanal de indicadores con la gerencia | 100 % de las semanas | Actas |

## 7. Transformación continua después del proyecto

| Etapa | Cuándo | Qué hace la planta con la información |
| --- | --- | --- |
| 1. Conectar | Proyecto (semanas 1 a 16) | Instrumentar la línea, registrar cada lote y poner en marcha el MES |
| 2. Estabilizar | Meses 1 a 6 después de la entrega | Cumplir las metas de no conformes y OEE con la reunión diaria y la semanal |
| 3. Analizar y mejorar | Año 1 a 2 | Control estadístico de proceso sobre el pH final y el peso, mantenimiento por condición de bombas y homogeneizador, análisis de costo por lote y por referencia, y compra de la celda robotizada de encanastado si el volumen la justifica |
| 4. Integrar la cadena | Año 2 a 3 | Pago de la leche por calidad con los resultados por cantina y planeación con los distribuidores según la demanda real |

La revisión trimestral de indicadores, incluida en el contrato de soporte de Cremia, decide qué mejoras se priorizan en cada etapa. La analítica de datos de las etapas 3 y 4 apoya las decisiones de producción, calidad y mantenimiento; el control de la línea sigue siendo el control regulatorio PID definido en el documento de equipos.

## Referencias

- Hiatt, J. (2006). ADKAR: A Model for Change in Business, Government and Our Community. Prosci.
- Kotter, J. P. (2012). Leading Change. Harvard Business Review Press.
- ANSI/ISA-95.00.03-2013. Enterprise-Control System Integration, Part 3: Activity Models of Manufacturing Operations Management.
- ANSI/ISA-18.2-2016. Management of Alarm Systems for the Process Industries.
- Grimaldo, G., Moreno, D. y Salamanca, M. (2015). Medición del trabajo de una línea de producción de yogurt – Empresa La Hacienda. Revista I3+, 2(2), 62–81.
