"""Generate local-only development credentials without overwriting existing files."""

import json
import os
from pathlib import Path
import secrets

ROOT = Path(__file__).resolve().parents[1]
local = ROOT / ".local"
local.mkdir(mode=0o700, exist_ok=True)
config_path = local / "config.yaml"
env_path = local / "postgres.env"
if config_path.exists() or env_path.exists():
    if not (config_path.is_file() and env_path.is_file()):
        raise SystemExit("Configuração parcial em .local/: revisar os arquivos antes de continuar.")
    print("Configuração existente preservada em .local/.")
else:
    password = secrets.token_hex(24)
    config = {
        "database": {
            "host": "127.0.0.1", "port": 5433, "user": "stustapay",
            "password": password, "dbname": "stustapay",
        },
        "core": {
            "test_mode": True, "test_mode_message": "LibreCode Cashless — PoC",
            "secret_key": secrets.token_hex(32), "sumup_enabled": False,
        },
    }
    for name, port in [("administration", 8081), ("customerportal", 8082), ("terminalserver", 8083)]:
        config[name] = {"base_url": f"http://localhost:{port}", "host": "localhost", "port": port}
    # JSON is a YAML subset, readable by the upstream YAML configuration loader.
    for path, content in [
        (config_path, json.dumps(config, ensure_ascii=False, indent=2) + "\n"),
        (env_path, f"POSTGRES_USER=stustapay\nPOSTGRES_DB=stustapay\nPOSTGRES_PASSWORD={password}\n"),
    ]:
        with open(path, "x", encoding="utf-8", opener=lambda p, flags: os.open(p, flags, 0o600)) as stream:
            stream.write(content)
    print("Configuração de desenvolvimento criada em .local/ (permissão 0600).")
