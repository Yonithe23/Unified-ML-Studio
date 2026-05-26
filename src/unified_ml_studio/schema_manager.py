from pathlib import Path

import pandas as pd
import yaml


def generate_schema(df: pd.DataFrame, output_path: str = "config/schema.yaml") -> dict:
    schema = {
        "columns": {
            column: str(dtype)
            for column, dtype in df.dtypes.items()
        },
        "column_order": list(df.columns),
        "column_count": len(df.columns),
    }

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        yaml.dump(schema, file, sort_keys=False)

    return schema