---
name: cremia-coherence-audit
description: Procedimiento de auditoría multiagente en paralelo para Módulos 0–3, docs/ y herramientas/ en Cremia-Automations, verificando física del proceso, conteos E/S, finanzas, cronograma 2027 y enlaces.
---

# Cremia Coherence Audit — Auditoría multiagente en paralelo

Usa esta guía para auditar de forma exhaustiva la coherencia técnica, financiera, temporal y documental de `Cremia-Automations` antes de consolidar entregas o cerrar una rama de corrección.

## Arquitectura de la auditoría en paralelo

Lanza subagentes especializados en paralelo (en modo lectura/reporte primero) sobre los 6 frentes siguientes, comparando siempre contra `herramientas/parametros.yaml` y `herramientas/resultados.md`:

### 1. Módulo 0 (`0-estado-del-arte/`)
- Verifica `README.md` y `estado-del-arte-y-justificacion-de-eleccion.md`.
- Confirma que quede explícito que **únicamente se implementa la línea de yogur** (`YB-200`, `YV-150`, `YV-300`), mientras que `0-estado-del-arte/queso/` y `0-estado-del-arte/kumis/` son solo investigación inicial (excluidas del verificador vigente).
- Verifica que no haya enlaces rotos hacia documentos reorganizados.

### 2. Módulo 1 (`1-transformacion-digital-industrial/`)
- **Física y proceso:** 550 L de leche por lote, 2 lotes/día, 563 min/lote, planta adaptada a **Guasca, Cundinamarca (2.600 msnm)**, pasteurización en ventana **85–90 °C**, tanque **TK-102** y enfriamiento nocturno del lote 2 con agua helada en chaqueta.
- **Conteos E/S y arquitectura:** **25 sensores**, **22 actuadores**, **68 señales de E/S**, **20 nodos EtherNet/IP** (diseño completo).
- **Tecnología OT/IT:** PLC CompactLogix 5380, SCADA en **Node-RED** en el nodo de borde (sin licencias de terceros), plataforma **Cremia MES/ERP** en **FastAPI + PostgreSQL en el mismo servidor virtual ECS** de Huawei Cloud (sin RDS gestionado), licencia perpetua **Studio 5000 Professional** para la planta.
- **Gemelo digital y alcance:** Tecnomatix Plant Simulation, Siemens NX MCD y FactoryTalk Logix Echo (incluidos en administración de Cremia); celda robotizada **R-501** diseñada para etapa posterior.
- **Integridad estructural:** verificar que `1_Flujo_Informacion_OT_IT.md` y `2_Arquitectura_ISA95.md` permanezcan separados y consistentes entre sí.

### 3. Módulo 2 (`2-gestion-y-evaluacion-de-la-produccion/`)
- Verifica que `Insumo - Tiempos y capacidades de la línea de yogur.md`, los dos VSM (`actual` y `propuesto`) y `Necesidades de información y relación con MES y ERP - Línea de yogur.md` coincidan con `resultados.md`:
  - Actual: 1 lote/día, 601 min/lote, 3.052 llenadas / 2.898 conformes, 5,06 % no conforme, OEE 65 %, 724 u/operario/día, 155 COP/u.
  - Propuesta: 2 lotes/día, ≈ 563 min/lote, 6.505 conformes/día promedio, ≤ 1,5 % no conforme, OEE meta 82 %, 1.301 u/operario/día (+80 %), 95 COP/u (−39 %), operación L–S 7:00–19:00 + turno corto dominical.
- Valida consistencia de necesidades de información MES/ERP con la plataforma FastAPI + PostgreSQL y SCADA Node-RED del Módulo 1.

### 4. Módulo 3 (`3-planeacion-y-evaluacion-del-proyecto/`)
- **Finanzas (D14):** 20 rubros incluyendo licencia Studio 5000 Professional; inversión **COP 1.495,5 millones**; VPN al 15 % después de impuestos **COP 189,4 millones**; TIR **18,9 %**; recuperación **3,9 años**; punto de equilibrio **91,5 %**; cartas de intención **90 % del volumen de vasos**; ingeniería **4.780 h** / **COP 333,7 millones**.
- **Cronograma 2027:** **26 semanas** (18 de enero al 16 de julio de 2027), parada de planta de 5 días, equipos de largo plazo ordenados en semana 4 y nacionalizados en semana 18, estabilización en semanas 21–26, carga semanal ≤ 42 h por integrante.
- Verifica que `Cronograma_Proyecto_TDI_Yogur.md`, `4_EDT_Proyecto_TDI_Yogur.md`, `Propuesta_Economica_y_Comercial.md`, `Propuesta_de_valor_y_gestion_del_cambio.md` y `Propuesta_Empresarial.md` no conserven tablas desactualizadas ni marcas de borrador.

### 5. Web (`docs/*.html`) y enlaces internos
- Revisa los 7 HTML (`index.html`, `empresa.html`, `diagnostico.html`, `solucion.html`, `plan.html`, `valor.html`, `aprendizajes.html`) y `docs/styles.css`.
- Comprueba que todas las cifras, decisiones técnicas (Guasca 2.600 msnm, Node-RED, FastAPI + PostgreSQL en el mismo ECS, Studio 5000, R-501 etapa posterior) y fechas 2027 coincidan con `resultados.md` y `README.md`.
- Verifica enlaces relativos entre `.md` e imágenes/HTML en `docs/` (sin rutas rotas ni referencias a archivos movidos).

### 6. Herramientas (`herramientas/`)
Ejecuta desde la raíz del repositorio en Windows PowerShell:
```powershell
.venv\Scripts\python.exe -X utf8 herramientas\programa.py
.venv\Scripts\python.exe -X utf8 herramientas\generar_tablas.py --verificar
.venv\Scripts\python.exe -X utf8 herramientas\verificar_consistencia.py
.venv\Scripts\python.exe -m pytest herramientas\tests -q
```

## Consolidación de hallazgos

Reúne los reportes de todos los frentes en una matriz `Archivo | Línea | Categoría (Física / E-S / Finanzas / Cronograma / Enlaces / Arquitectura) | Hallazgo | Corrección requerida`, corrige primero en `herramientas/parametros.yaml` si aplica (siguiendo `cremia-ssot-sync`) y vuelve a ejecutar la verificación completa antes de dar el cierre.
