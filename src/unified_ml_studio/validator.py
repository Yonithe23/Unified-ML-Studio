import pandas as pd


def validate_dataset(df: pd.DataFrame) -> dict:
    row_count, column_count = df.shape

    missing_count = df.isnull().sum()
    missing_percentage = (missing_count / row_count * 100).round(2) if row_count > 0 else missing_count

    duplicate_columns = df.columns[df.columns.duplicated()].tolist()

    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
    categorical_columns = df.select_dtypes(include=["object", "category"]).columns.tolist()

    report = {
        "status": "passed",
        "dataset_shape": {
            "rows": row_count,
            "columns": column_count,
        },
        "columns": list(df.columns),
        "numeric_columns": numeric_columns,
        "categorical_columns": categorical_columns,
        "duplicate_columns": duplicate_columns,
        "missing_values": missing_count.to_dict(),
        "missing_percentage": missing_percentage.to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "data_types": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "memory_usage_mb": round(df.memory_usage(deep=True).sum() / (1024 * 1024), 4),
        "issues": [],
    }

    if row_count == 0:
        report["status"] = "failed"
        report["issues"].append("Dataset is empty.")

    if duplicate_columns:
        report["status"] = "failed"
        report["issues"].append("Dataset has duplicate column names.")

    if report["duplicate_rows"] > 0:
        report["status"] = "warning"
        report["issues"].append("Dataset has duplicate rows.")

    if any(value > 0 for value in report["missing_values"].values()):
        report["status"] = "warning"
        report["issues"].append("Dataset has missing values.")

    if not report["issues"]:
        report["issues"].append("No major issues found.")

    return report