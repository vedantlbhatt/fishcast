from pathlib import Path
import pandas as pd

CLEAN_FILE = Path("data/processed/noaa_sst_sample_clean.csv")


def load_noaa_sample() -> None: # loads  sample from the path defined earlier
    if not CLEAN_FILE.exists():
        raise FileNotFoundError(f"Missing cleaned file: {CLEAN_FILE}")

    df = pd.read_csv(CLEAN_FILE)
    print("Load stage check:")
    print(f"Rows ready for DB load: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    print(df.head(3))


if __name__ == "__main__":
    load_noaa_sample()