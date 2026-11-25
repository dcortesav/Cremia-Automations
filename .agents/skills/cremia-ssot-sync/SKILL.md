---
name: cremia-ssot-sync
description: Runbook paso a paso para modificar herramientas/parametros.yaml o decisiones de arquitectura y propagar cambios de forma consistente a Markdown, docs/*.html, herramientas/verificar_consistencia.py y pruebas pytest en Cremia-Automations.
---

# Cremia SSOT Sync — Runbook de actualización de parámetros y decisiones

Usa este procedimiento siempre que debas actualizar un supuesto numérico (producción, tiempos, EDT, inversión, OPEX, finanzas) o una decisión de arquitectura/alcance en `Cremia-Automations`.

## Reglas previas

1. **Nunca edites cifras a mano** en `.md` o `docs/*.html` sin partir de `herramientas/parametros.yaml` (salvo texto puramente cualitativo, que aun así debe pasar el verificador).
2. **No edites `herramientas/resultados.md` a mano**: se regenera automáticamente con `modelo.py`.
3. Ejecuta todos los comandos Python desde la raíz del repositorio (`Cremia-Automations`) usando `.venv\Scripts\python.exe -X utf8` en Windows PowerShell.

## Paso 1 — Actualizar la fuente única de verdad (`parametros.yaml`)

1. Abre `herramientas/parametros.yaml` y modifica únicamente los supuestos necesarios (si un rubro está en USD, usa `valor_usd`; `modelo.cargar()` lo convierte con `general.tasa_cambio_cop_usd`).
2. Si cambiaron horas o paquetes de la EDT, verifica o rebalancea la carga semanal para que ningún integrante supere 42 h/semana ni 80 % de ocupación:
   ```powershell
   .venv\Scripts\python.exe -X utf8 herramientas\balancear_carga.py
   # Si necesitas reescribir la distribución en parametros.yaml:
   .venv\Scripts\python.exe -X utf8 herramientas\balancear_carga.py --escribir
   ```

## Paso 2 — Recalcular modelos y programa diario

1. Recalcula el modelo maestro y regenera `herramientas/resultados.md`:
   ```powershell
   .venv\Scripts\python.exe -X utf8 herramientas\modelo.py
   ```
2. Si cambiaron tiempos de proceso, turnos o uso de equipos, valida el programa diario de dos lotes sin colisiones ni tareas fuera de turno:
   ```powershell
   .venv\Scripts\python.exe -X utf8 herramientas\programa.py
   ```

## Paso 3 — Regenerar tablas incrustadas en Markdown

Actualiza automáticamente todos los bloques delimitados por `<!-- tabla:nombre --> ... <!-- /tabla:nombre -->`:

```powershell
.venv\Scripts\python.exe -X utf8 herramientas\generar_tablas.py
```

Si también cambiaron nombres de paquetes, entregables o dependencias de la EDT en prosa tabular, revisa `ENTREGABLES` dentro de `herramientas/generar_tablas.py`.

## Paso 4 — Propagar cambios a prosa Markdown y `docs/*.html`

1. Revisa `herramientas/resultados.md` para obtener las cifras exactas con formato colombiano (punto de miles, coma decimal).
2. Busca todas las apariciones de las cifras anteriores en:
   - `README.md`
   - `1-transformacion-digital-industrial/*.md` (manteniendo separados `1_Flujo_Informacion_OT_IT.md` y `2_Arquitectura_ISA95.md`)
   - `2-gestion-y-evaluacion-de-la-produccion/*.md`
   - `3-planeacion-y-evaluacion-del-proyecto/*.md` (incluyendo `empresa/` y `EDTs/`)
   - `docs/*.html` (`index.html`, `empresa.html`, `diagnostico.html`, `solucion.html`, `plan.html`, `valor.html`, `aprendizajes.html`)
3. Si conservas una referencia histórica en un documento, la línea **debe** incluir un marcador aceptado (`versión de octubre de 2026`, `primera versión` o `descartad`).

## Paso 5 — Actualizar el verificador y las pruebas

1. En `herramientas/verificar_consistencia.py`:
   - Agrega las cifras o términos reemplazados al diccionario `PROHIBIDOS` con su motivo.
   - Actualiza las claves y rutas esperadas en `CANONICAS` para reflejar las nuevas cifras vigentes.
2. Revisa y actualiza si corresponde los tests en `herramientas/tests/`:
   - `test_modelo.py`
   - `test_programa.py`
   - `test_verificador.py`

## Paso 6 — Verificación final obligatoria

Ejecuta la cadena completa en Windows PowerShell y verifica que los tres comandos terminen con código de salida `0`:

```powershell
.venv\Scripts\python.exe -X utf8 herramientas\verificar_consistencia.py
.venv\Scripts\python.exe -X utf8 herramientas\generar_tablas.py --verificar
.venv\Scripts\python.exe -m pytest herramientas\tests -q
```

- `verificar_consistencia.py` debe imprimir `Sin inconsistencias.`.
- `generar_tablas.py --verificar` no debe reportar archivos desactualizados.
- `pytest` debe pasar el 100 % de las pruebas sin saltos ni fallos.
