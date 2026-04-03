from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[2]
DATASET_PATH = ROOT_DIR / "data" / "raw" / "punts_exemple.csv"


def main() -> None:
    df = pd.read_csv(DATASET_PATH)

    print(f"Dataset: {DATASET_PATH}")
    print(f"Files: {len(df)}")
    print("Primeres files:")
    print(df.head())


if __name__ == "__main__":
    main()
