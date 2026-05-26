import json
from pathlib import Path


def save_report(report: dict, output_path: str = "reports/report.json") -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)