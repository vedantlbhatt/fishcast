from pathlib import Path
import requests

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

NOAA_URL = (
    "https://coastwatch.pfeg.noaa.gov/erddap/griddap/"
    "jplMURSST41.csv?"
    "analysed_sst[(2024-01-01T09:00:00Z):1:(2024-01-03T09:00:00Z)]"
    "[(40.0):1:(45.0)][(-71.0):1:(-66.0)]"
)

OUT_FILE = RAW_DIR / "noaa_sst_sample.csv"

def download_noaa_sample() -> None:
    response = requests.get(NOAA_URL, timeout=60)
    response.raise_for_status()
    OUT_FILE.write_text(response.text)
    print(f"Saved NOAA sample to {OUT_FILE} ({OUT_FILE.stat().st_size} bytes)")


if __name__ == "__main__":
    download_noaa_sample()
