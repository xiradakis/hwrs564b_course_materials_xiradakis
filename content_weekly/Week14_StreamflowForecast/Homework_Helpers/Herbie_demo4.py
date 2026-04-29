## Precipitaiton forecast download demo using Herbie
## This script downloads precipitation forecasts for the GFS model for a grid cell in the Verde River watershed
## It uses the Herbie package
## You can learn more aobut this here: https://herbie.readthedocs.io/en/stable/user_guide/install.html


import numpy as np
import pandas as pd
import datetime
from herbie import Herbie


def clip_and_reproject_verde(data_array):
    # Normalize longitudes to [-180, 180] and sort
    data_array = data_array.assign_coords({'longitude': ((data_array['longitude'] + 180) % 360) - 180}).sortby('longitude')
    LATLNG_BOUNDS = [33.5, -113.0, 35.0, -111.0] 

    # Clip directly to Verde watershed bounds [lat_min, lon_min, lat_max, lon_max]
    lat_min, lon_min, lat_max, lon_max = LATLNG_BOUNDS  # 33.5, -113.0, 35.0, -111.0
    data_verde = data_array.sel(
        latitude=slice(lat_max, lat_min),   # descending: N → S
        longitude=slice(lon_min, lon_max)
    )

    # Assign CRS (no reprojection needed — stays in WGS84)
    data_verde = data_verde.rio.write_crs("EPSG:4326")
    data_verde = data_verde.rio.set_spatial_dims(
        x_dim="longitude", y_dim="latitude", inplace=False
    )

    return data_verde


def collect_forcings_gfs(base_date, date):

    day_from_base_date = (date - base_date).days
    initial_hour = day_from_base_date * 24 + 1
    final_hour = initial_hour + 23
    
    precip_hourly_data = np.zeros((24, 7, 9), dtype='float64')  # time_steps, rows, cols
        
    for time_step in range(initial_hour, final_hour + 1):
        H = Herbie(base_date.strftime('%Y-%m-%d'), model="gfs", product='pgrb2.0p25', fxx=time_step, verbose=False)
        data = H.xarray(f":APCP:surface")
        data_reprojected = clip_and_reproject_verde(data)
        data_in_numpy_format = np.flipud(np.array(data_reprojected['tp'], dtype='float64'))
        precip_hourly_data[(time_step - 1) % 24, :, :] = data_in_numpy_format

    accumulated_daily_precipitation = np.sum(precip_hourly_data, axis=0)
    average_daily_precipitation = np.mean(accumulated_daily_precipitation)
    return average_daily_precipitation


base_date = datetime.datetime(2024, 1, 21)
n_days = 2
precip_data = []

# Collect precipitation - GFS
dates_list = [base_date + datetime.timedelta(days=i) for i in range(n_days)]
for date in dates_list:
    print(date)
    precip_data.append(collect_forcings_gfs(base_date, date))

# create df
df_precip = pd.DataFrame({
    'date': dates_list,
    'average_daily_precipitation': precip_data
})

df_precip.to_csv(f'precip_data_{base_date}.csv', index=False)