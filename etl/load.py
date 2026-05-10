from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

CLEAN_FILE = Path("data/processed/noaa_sst_sample_clean.csv")
DB_URL = "postgresql+psycopg2://fishcast:fishcast@localhost:5433/fishcast"
TABLE_NAME = "noaa_sst_clean"


def load_noaa_sample() -> None:
    if not CLEAN_FILE.exists():
        raise FileNotFoundError(f"Missing cleaned file: {CLEAN_FILE}") #pre-validation

    df = pd.read_csv(CLEAN_FILE)

    # Convert CSV time string to timestamp for Postgres
    df["time_utc"] = pd.to_datetime(df["time"], utc=True)
    df = df.drop(columns=["time"])

    engine = create_engine(DB_URL)

    # Append rows to target table in chunks for memory + speed  
    df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False, chunksize=10000, method="multi")
    print(f"Loaded {len(df)} rows into {TABLE_NAME}")


if __name__ == "__main__":
    load_noaa_sample()