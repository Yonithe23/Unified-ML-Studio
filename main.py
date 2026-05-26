from src.unified_ml_studio.data_loader import load_dataset
from src.unified_ml_studio.validator import validate_dataset
from src.unified_ml_studio.report_generator import save_report


def main():
    dataset_path = "data/sample.csv"

    df = load_dataset(dataset_path)
    report = validate_dataset(df)
    save_report(report)

    print("Validation completed.")
    print("Report saved to reports/report.json")


if __name__ == "__main__":
    main()