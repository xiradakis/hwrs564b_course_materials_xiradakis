## HydroFrame Precip download Demo
## This script downloads historical precipitation data for a grid cell in the Verde River
## Note that forecasted precip is not available through HydroFrame  
## You can learn more aobut this here: https://hf-hydrodata.readthedocs.io

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import hf_hydrodata as hf          # HydroFrame data access package


# =============================================================================
# STEP 1 — Authenticate with the HydroFrame platform
# =============================================================================

HYDROFRAME_EMAIL = "your_email@domain.org"   # <-- replace with your email
HYDROFRAME_PIN   = "1234"            # <-- replace with your PIN
hf.register_api_pin(email=HYDROFRAME_EMAIL, pin=HYDROFRAME_PIN)

# =============================================================================
# STEP 2 — Define the study domain and time period
# =============================================================================

LATLNG_BOUNDS = [33.5, -113.0, 35.0, -111.0]   # Verde River watershed

# Time range for the data request.
DATE_START = "2019-01-21"
DATE_END   = "2019-01-26"

# =============================================================================
# STEP 3 — Download daily PRECIPITATION data
# =============================================================================

precip = hf.get_gridded_data(
    dataset            = "CW3E",          # atmospheric forcing dataset
    variable           = "precipitation", # total precipitation
    temporal_resolution= "daily",         # daily values
    aggregation        = "sum",           # sum over the day (for precip)
    date_start         = DATE_START,
    date_end           = DATE_END,
    latlng_bounds      = LATLNG_BOUNDS,
)

np.save("precip_data.npy", precip)  # save the downloaded data to a local file