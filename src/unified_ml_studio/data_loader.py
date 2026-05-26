from pathlib import Path
import pandas as pd


def load_dataset(file_path: str) -> pd.DataFrame:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix == ".csv":
        return pd.read_csv(path)

    if path.suffix in [".xlsx", ".xls"]:
        return pd.read_excel(path)

    if path.suffix == ".json":
        return pd.read_json(path)

    if path.suffix == ".parquet":
        return pd.read_parquet(path)

    raise ValueError(f"Unsupported file type: {path.suffix}")