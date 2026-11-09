"""Export the original workbook's cached cell values using only the standard library."""

import argparse
import csv
from pathlib import Path
import posixpath
import re
import unicodedata
from xml.etree import ElementTree as ET
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Plano_PoC_StuStaPay_Cashless_OpenSource(1).xlsx"
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"


def export(destination):
    destination.mkdir(parents=True, exist_ok=True)
    files = []
    with ZipFile(SOURCE) as archive:
        strings = []
        if "xl/sharedStrings.xml" in archive.namelist():
            strings = ["".join(t.text or "" for t in cell.findall(".//m:t", NS))
                       for cell in ET.fromstring(archive.read("xl/sharedStrings.xml")).findall("m:si", NS)]
        relationships = {r.attrib["Id"]: r.attrib["Target"] for r in
                         ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))}
        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        for number, sheet in enumerate(workbook.findall("m:sheets/m:sheet", NS), 1):
            name = unicodedata.normalize("NFKD", sheet.attrib["name"]).encode("ascii", "ignore").decode()
            slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
            filename = f"{number:02d}-{slug}.csv"
            target = relationships[sheet.attrib[REL]]
            path = target.lstrip("/") if target.startswith("/") else posixpath.normpath("xl/" + target)
            rows = []
            for row in ET.fromstring(archive.read(path)).findall("m:sheetData/m:row", NS):
                values = []
                for cell in row.findall("m:c", NS):
                    column = 0
                    for char in re.match(r"[A-Z]+", cell.attrib["r"]).group():
                        column = column * 26 + ord(char) - ord("A") + 1
                    values.extend([""] * (column - len(values)))
                    value = cell.find("m:v", NS)
                    text = value.text or "" if value is not None else ""
                    if cell.attrib.get("t") == "s":
                        text = strings[int(text)]
                    elif cell.attrib.get("t") == "inlineStr":
                        text = "".join(t.text or "" for t in cell.findall(".//m:t", NS))
                    values[column - 1] = text
                rows.append(values)
            with (destination / filename).open("w", encoding="utf-8", newline="") as stream:
                csv.writer(stream, lineterminator="\n").writerows(rows)
            files.append(filename)
    return files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "docs/planejamento")
    args = parser.parse_args()
    print(f"{len(export(args.output))} abas exportadas para {args.output}.")
