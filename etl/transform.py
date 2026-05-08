from pathlib import Path
import pandas as pd

RAW_FILE = Path("data/raw/noaa_sst_sample.csv")
OUT_FILE = Path("data/processed/noaa_sst_sample_clean.csv")
OUT_FILE.parent.mkdir(parents=True, exist_ok=True)


def transform_noaa_sample() -> None:
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Missing raw file: {RAW_FILE}")

    df = pd.read_csv(RAW_FILE, low_memory = False)
    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
    df["analysed_sst"] = pd.to_numeric(df["analysed_sst"], errors="coerce")

    # Keep rows where temperature is present
    if "analysed_sst" in df.columns:
        df = df.dropna(subset=["latitude", "longitude", "analysed_sst"])

    df.to_csv(OUT_FILE, index=False)
    print(f"Saved cleaned file to {OUT_FILE}")
    print(f"Rows: {len(df)}")
    print(f"Columns: {list(df.columns)}")


if __name__ == "__main__":
    transform_noaa_sample()