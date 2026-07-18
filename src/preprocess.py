import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/products.csv")

def load_data():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"{DATA_PATH} not found.")

    df = pd.read_csv(DATA_PATH)

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove rows with missing values
    df = df.dropna()

    # Clean text columns
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
                .str.replace(r"\s+", " ", regex=True)
            )

    return df


if __name__ == "__main__":
    df = load_data()

    print("=" * 50)
    print("Dataset Loaded Successfully")
    print("=" * 50)
    print(df.head())
    print(f"\nTotal Records: {len(df)}")