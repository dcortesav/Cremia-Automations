# Diagramas de instrumentación — Línea 3: Kumis

Planos P&ID de la línea de kumis (ANSI/ISA-5.1), en dos hojas, junto con su documentación de ingeniería.

## Estructura

| Ruta | Contenido |
|---|---|
| [`PID_Kumis.md`](PID_Kumis.md) | Documentación: equipos, índice de instrumentos, lazos de control y notas de diseño |
| [`imagenes/`](imagenes) | Planos vectoriales: `PID_Kumis_Hoja1.svg` (hoja 1) y `PID_Kumis_Hoja2.svg` (hoja 2) |
| [`scripts/`](scripts) | Código fuente (Python + matplotlib) que genera los planos |

## Regenerar los planos

```bash
cd scripts
python generar_pid.py
```

Requiere `matplotlib`. Los SVG se escriben en `../imagenes/`.
