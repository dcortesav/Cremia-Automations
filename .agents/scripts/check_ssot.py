"""Hook no bloqueante de verificación rápida SSOT para Cremia-Automations.

Lee JSON por stdin desde hooks de Antigravity/IDE:
- Si ``continuationActive`` es true, omite la verificación.
- En ``Stop``, responde siempre ``{"decision": "allow"}``.
- En ``PostToolUse`` (``write_file`` / ``edit_file``), si el archivo tocado está
  dentro de ``Cremia-Automations`` y tiene extensión ``.md``, ``.html``, ``.py``
  o ``.yaml``/``.yml``, ejecuta ``herramientas/verificar_consistencia.py`` con
  timeout corto y registra hallazgos en ``.agents/last_ssot_check.log``.
- Siempre escribe JSON válido a stdout (``{}`` en ``PostToolUse``) y sale con
  código 0 para no bloquear ni entrar en bucle.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys
from pathlib import Path

AGENTS_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = AGENTS_DIR.parent
LOG_FILE = AGENTS_DIR / "last_ssot_check.log"
EXTENSIONES_RELEVANTES = {".md", ".html", ".py", ".yaml", ".yml"}
HERRAMIENTAS_PERMITIDAS = {"write_file", "edit_file"}


def _leer_payload() -> dict:
    try:
        bruto = sys.stdin.read()
    except Exception:
        return {}
    if not bruto or not bruto.strip():
        return {}
    try:
        data = json.loads(bruto)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _evento(payload: dict) -> str:
    return str(
        payload.get("hookEventName")
        or payload.get("hook_event_name")
        or payload.get("event")
        or ""
    )


def _extraer_tool_y_ruta(payload: dict) -> tuple[str, str | None]:
    tool_call = payload.get("toolCall") or payload.get("tool_call") or {}
    if not isinstance(tool_call, dict):
        tool_call = {}

    tool_name = str(
        payload.get("toolName")
        or payload.get("tool_name")
        or tool_call.get("name")
        or tool_call.get("toolName")
        or ""
    )

    args = (
        payload.get("toolInput")
        or payload.get("tool_input")
        or tool_call.get("arguments")
        or tool_call.get("args")
        or tool_call.get("input")
        or {}
    )
    if isinstance(args, str):
        try:
            args = json.loads(args)
        except Exception:
            args = {}
    if not isinstance(args, dict):
        args = {}

    for clave in ("Path", "path", "file_path", "filePath", "TargetFile", "target_file"):
        val = args.get(clave)
        if isinstance(val, str) and val.strip():
            return tool_name, val.strip()

    return tool_name, None


def _es_archivo_objetivo(ruta_str: str | None) -> Path | None:
    if not ruta_str:
        return None
    try:
        ruta = Path(ruta_str)
        if not ruta.is_absolute():
            ruta = (REPO_ROOT / ruta).resolve()
        else:
            ruta = ruta.resolve()
        ruta.relative_to(REPO_ROOT.resolve())
    except Exception:
        return None
    if ruta.suffix.lower() not in EXTENSIONES_RELEVANTES:
        return None
    return ruta


def _python_ejecutable() -> str:
    venv_py = REPO_ROOT / ".venv" / "Scripts" / "python.exe"
    if venv_py.is_file():
        return str(venv_py)
    return sys.executable or "python"


def _registrar_log(ruta: Path, rc: int, salida: str) -> None:
    marca = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rel = ruta.relative_to(REPO_ROOT.resolve()).as_posix()
    estado = "OK" if rc == 0 else f"INCONSISTENCIAS (exit {rc})"
    cuerpo = salida.strip() or "(sin salida)"
    contenido = f"[{marca}] archivo={rel} estado={estado}\n{cuerpo}\n"
    try:
        LOG_FILE.write_text(contenido, encoding="utf-8")
    except Exception:
        pass


def main() -> int:
    payload = _leer_payload()
    evento = _evento(payload)

    if evento == "Stop":
        sys.stdout.write('{"decision": "allow"}\n')
        return 0

    continuation = payload.get("continuationActive")
    if continuation is None:
        continuation = payload.get("continuation_active")
    if bool(continuation):
        sys.stdout.write("{}\n")
        return 0

    tool_name, ruta_str = _extraer_tool_y_ruta(payload)
    if tool_name and tool_name not in HERRAMIENTAS_PERMITIDAS:
        sys.stdout.write("{}\n")
        return 0

    ruta = _es_archivo_objetivo(ruta_str)
    if ruta is None:
        sys.stdout.write("{}\n")
        return 0

    verificador = REPO_ROOT / "herramientas" / "verificar_consistencia.py"
    if verificador.is_file():
        env = os.environ.copy()
        env["PYTHONUTF8"] = "1"
        try:
            proc = subprocess.run(
                [_python_ejecutable(), "-X", "utf8", str(verificador)],
                cwd=str(REPO_ROOT),
                env=env,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=8,
            )
            salida = (proc.stdout or "") + (("\n" + proc.stderr) if proc.stderr else "")
            if proc.returncode != 0 or LOG_FILE.exists():
                _registrar_log(ruta, proc.returncode, salida)
        except Exception as exc:
            _registrar_log(ruta, -1, f"Error ejecutando verificador: {exc}")

    sys.stdout.write("{}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
