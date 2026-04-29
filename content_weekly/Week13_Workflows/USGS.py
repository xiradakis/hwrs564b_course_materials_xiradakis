import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ── Define your 5 stations here ──────────────────────────────────────────────
stations = [
    "09498500",
    "09505800",
    "09506000",
    "09508500",
    "09510000",
]

params_base = {
    "format":      "json",
    "parameterCd": "00060",
    "startDT":     "2020-01-01",
    "endDT":       "2024-12-31",
    "siteStatus":  "all"
}

url = "https://waterservices.usgs.gov/nwis/dv/"

# ── Loop over stations ────────────────────────────────────────────────────────
for station in stations:
    print(f"Processing station {station}")

    # Add the station to the params for this request
    params = {**params_base, "sites": station}

    # Make the request
    response = requests.get(url, params=params)
    data = response.json()

    # Parse nested JSON
    try:
        records = data["value"]["timeSeries"][0]["values"][0]["value"]
    except (IndexError, KeyError):
        print(f"  No data found for station {station} — skipping")
        continue

    df = pd.DataFrame(records)
    df["dateTime"] = pd.to_datetime(df["dateTime"])
    df["value"]    = pd.to_numeric(df["value"], errors="coerce")
    df = df.set_index("dateTime")

    # Plot and save
    plt.figure(figsize=(10, 4))
    plt.plot(df.index, df["value"])
    plt.title(f"Daily Streamflow — Station {station}")
    plt.ylabel("Discharge (ft³/s)")
    plt.tight_layout()
    plt.close()

print("Done — all stations processed")