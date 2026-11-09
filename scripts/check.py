"""Check the bootstrap repository without network, dependencies, or running services."""

import ast
from pathlib import Path
import re
from tempfile import TemporaryDirectory
from urllib.parse import unquote

from export_plan import export

ROOT = Path(__file__).resolve().parents[1]
for path in (ROOT / "scripts").glob("*.py"):
    ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
assert re.fullmatch(r"[0-9a-f]{40}\n?", (ROOT / "upstream.ref").read_text()), "SHA inválido"
documents = [ROOT / "README.md", ROOT / "CONTRIBUTING.md", *list((ROOT / "docs").glob("*.md"))]
for document in documents:
    for target in re.findall(r"\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
        if "://" in target or target.startswith("#"):
            continue
        target = unquote(target.split("#")[0])
        assert (document.parent / target).exists(), f"Link inexistente em {document}: {target}"
with TemporaryDirectory() as temporary:
    output = Path(temporary)
    files = export(output)
    assert len(files) == 9, "Esperadas nove abas do plano original"
    actual = {p.name for p in (ROOT / "docs/planejamento").glob("*.csv")}
    assert actual == set(files), "Lista de CSVs diverge da planilha"
    for filename in files:
        assert (output / filename).read_bytes() == (ROOT / "docs/planejamento" / filename).read_bytes(), filename
print("OK: sintaxe Python, SHA upstream, links locais e nove exportações da planilha.")
