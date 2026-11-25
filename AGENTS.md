# Reglas de trabajo — Cremia Automations (`Cremia-Automations`)

Este archivo define las reglas permanentes (*always-on*) para cualquier agente o colaborador que modifique la documentación, el código de herramientas o la página web del proyecto.

## 1. Fuente única de verdad (SSOT)

- **Prohibido editar cifras directamente** en archivos `.md` o `docs/*.html` sin actualizar primero [`herramientas/parametros.yaml`](herramientas/parametros.yaml).
- Todo cambio numérico o de supuestos debe seguir estrictamente este flujo en Windows PowerShell (desde la raíz del repositorio):
  1. Editar `herramientas/parametros.yaml` (y `herramientas/balancear_carga.py --escribir` si cambian horas de la EDT).
  2. `.venv\Scripts\python.exe -X utf8 herramientas\modelo.py` (recalcula y regenera `herramientas/resultados.md`).
  3. `.venv\Scripts\python.exe -X utf8 herramientas\generar_tablas.py` (actualiza los bloques `<!-- tabla:... -->` en los `.md`).
  4. Propagar manualmente las cifras citadas en prosa y en `docs/*.html`, y actualizar `PROHIBIDOS` / `CANONICAS` en `herramientas/verificar_consistencia.py` si una cifra canónica cambió.
  5. `.venv\Scripts\python.exe -X utf8 herramientas\verificar_consistencia.py` (debe salir `Sin inconsistencias.`, código 0).
  6. `.venv\Scripts\python.exe -X utf8 herramientas\generar_tablas.py --verificar` (debe salir con código 0).
  7. `.venv\Scripts\python.exe -m pytest herramientas\tests -q` (deben pasar todas las pruebas).
- No editar `herramientas/resultados.md` a mano; es una salida generada por `modelo.py`.
- Las menciones históricas a versiones anteriores solo son válidas si la línea incluye un marcador de historial aceptado por `verificar_consistencia.py` (`versión de octubre de 2026`, `primera versión`, `descartad`).

## 2. Decisiones vigentes del proyecto

Toda modificación debe respetar sin contradicciones las decisiones vigentes:

- **(a) Alcance exclusivo en línea de yogur:** se implementa únicamente la línea de yogur (bolsa 200 ml `YB-200`, vaso 150 ml `YV-150`, vaso 300 ml `YV-300`). Las carpetas `0-estado-del-arte/queso/` y `0-estado-del-arte/kumis/` corresponden solo a la investigación inicial de estado del arte y no se modifican como parte del diseño vigente.
- **(b) Ubicación de la planta:** planta La Hacienda adaptada a **Guasca, Cundinamarca (2.600 msnm)** por requisito del caso reto.
- **(c) Supervisión local (SCADA):** implementado en **Node-RED** sobre el nodo de borde en planta, sin licencias de terceros en supervisión ni en gestión.
- **(d) Plataforma Cremia MES/ERP:** desarrollada a la medida en **FastAPI + PostgreSQL en el mismo servidor virtual ECS** de Huawei Cloud (sin RDS gestionado en la propuesta).
- **(e) Gemelo digital:** construido con **Tecnomatix Plant Simulation**, **Siemens NX Mechatronics Concept Designer (MCD)** y **FactoryTalk Logix Echo**, incluidos en los costos de administración de Cremia.
- **(f) Licencia de PLC y cifras financieras vigentes (D14):** la inversión incluye una licencia perpetua de **Studio 5000 Professional** a nombre de la planta. Cifras canónicas de referencia: inversión **COP 1.495,5 millones** (20 rubros), VPN al 15 % después de impuestos **COP 189,4 millones**, TIR **18,9 %**, recuperación **3,9 años**, punto de equilibrio **91,5 %**, cartas de intención por al menos el **90 % del volumen de vasos**, **4.780 h** de ingeniería en **26 semanas** (18 de enero al 16 de julio de 2027), lote de **563 min**, OEE actual **65 %** (meta **82 %**), **25 sensores**, **22 actuadores**, **68 señales** de E/S y tanque **TK-102** con enfriamiento nocturno del lote 2 en chaqueta.
- **(g) Celda robotizada R-501:** la celda de encanastado/paletizado **R-501** queda diseñada y reservada en plano para una etapa posterior (no se compra ni se instala en este alcance).
- **(h) Separación documental OT/IT e ISA-95:** mantener separados [`1-transformacion-digital-industrial/1_Flujo_Informacion_OT_IT.md`](1-transformacion-digital-industrial/1_Flujo_Informacion_OT_IT.md) y [`1-transformacion-digital-industrial/2_Arquitectura_ISA95.md`](1-transformacion-digital-industrial/2_Arquitectura_ISA95.md); no fusionarlos.

## 3. Gobernanza Git y estilo

- **Nunca trabajar directo sobre `main` ni ejecutar `git push` sin autorización explícita.** Usar siempre ramas independientes de trabajo (por ejemplo, `correccion_2_jesus`).
- Mantener un **tono ingenieril sobrio, directo y conciso**, respaldado por los modelos y datos del repositorio, sin relleno ni sobre-especificaciones artificiosas.
- Usar formato numérico colombiano en documentos (`1.495,5`, `18,9 %`) y codificación UTF-8 (`-X utf8` al invocar Python en Windows).
