# Herramientas: fuente única de cifras

Esta carpeta mantiene consistentes las cifras de la propuesta entre todos los documentos y la página web.

| Archivo | Qué hace |
| --- | --- |
| `parametros.yaml` | Supuestos de entrada: producción, precios, tiempos de proceso, personal, horas y tarifas de la EDT, rubros de inversión, costos de operación y finanzas. Es el único lugar donde se cambia un supuesto. |
| `modelo.py` | Calcula producción y unidades conformes, OEE, tiempos por lote, horas y valor de la ingeniería, carga semanal del equipo, inversión, costos de operación, flujo de caja antes y después de impuestos, VPN, TIR, recuperación, sensibilidades y crédito. Escribe `resultados.md`. |
| `programa.py` | Arma el programa diario de los dos lotes y verifica que ningún equipo tenga dos usos a la vez y que cada tarea caiga en el turno de su responsable. |
| `balancear_carga.py` | Reparte las horas de los paquetes de la EDT entre los integrantes para que nadie pase de 42 h en ninguna semana (descontando festivos) ni del 80 % de su capacidad. Con `--escribir` actualiza `parametros.yaml`. |
| `generar_tablas.py` | Reemplaza las tablas marcadas con `<!-- tabla:nombre -->` en los documentos por las que calcula el modelo. Con `--verificar` solo informa si alguna está desactualizada. |
| `verificar_consistencia.py` | Busca en los documentos y en la web cifras y términos de versiones anteriores y comprueba que las cifras canónicas aparezcan donde deben. |
| `resultados.md` | Salida del modelo. No se edita a mano. |
| `tests/` | Pruebas del modelo, del programa diario y del verificador. |

## Flujo de trabajo

```powershell
# 1. Cambiar un supuesto en herramientas\parametros.yaml
# 2. Recalcular
.venv\Scripts\python.exe -X utf8 herramientas\modelo.py
# 3. Actualizar las tablas generadas de los documentos
cd herramientas; ..\.venv\Scripts\python.exe -X utf8 generar_tablas.py; cd ..
# 4. Actualizar a mano las cifras citadas en el texto y en docs\*.html, y agregar las cifras viejas a PROHIBIDOS
# 5. Verificar
.venv\Scripts\python.exe -X utf8 herramientas\verificar_consistencia.py
.venv\Scripts\python.exe -m pytest herramientas\tests -q
```

Las dependencias son PyYAML y pytest (`uv pip install --python .venv\Scripts\python.exe pyyaml pytest`).

Una línea de un documento queda exenta del verificador si contiene «versión de octubre de 2026», «primera versión» o «descartada»: así se puede citar el historial de la propuesta sin que cuente como cifra vigente. Las carpetas `0-estado-del-arte/queso`, `0-estado-del-arte/kumis` y las actas de reunión no se verifican, porque son investigación de otras líneas y registros históricos.
