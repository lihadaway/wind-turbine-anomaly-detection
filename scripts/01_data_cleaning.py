#%% md
# # Wind Turbine Anomaly Detection: Data Cleaning

#%%
# Import libraries
import json
import os
import pandas as pd
import requests
from datetime import datetime

# Print start time
print(f"{datetime.now()} - SCRIPT STARTED")

#%% md
# ## Data Acquisition

#%%
# Define file URLs
file_links = {
    "SCADA_Data.csv": "https://zenodo.org/records/8192149/files/Aventa_AV7_IET_OST_SCADA.csv?download=1",
    "WT_Metadata.json": "https://zenodo.org/records/8192149/files/Aventa_AV_7_IET_OST_WT_metadata.json?download=1",
    "SCADA_Channels_Metadata.csv": "https://zenodo.org/records/8192149/files/SCADA_Channels_Metadata.csv?download=1"
}

# Download and save each file
for filename, url in file_links.items():
    response = requests.get(url)
    if response.status_code == 200:
        filepath = os.path.join("./data", filename)
        with open(filepath, "wb") as file:
            file.write(response.content)
        print(f"\n{filename} downloaded successfully!")
    else:
        print(f"\nFailed to download {filename}. Status Code: {response.status_code}")

#%% md
# ## Data Exploration

#%%
# Load SCADA Time Series Data
scada_df = pd.read_csv("./data/SCADA_Data.csv")
print("\nSCADA Data Overview:")
print(scada_df.info())
print("\nHead of dataset:")
print(scada_df.head())

#%%
# Load SCADA Channels Metadata
scada_meta_df = pd.read_csv("./data/SCADA_Channels_Metadata.csv")
print("\nSCADA Channels Metadata Overview:")
print(scada_meta_df.info())
print("\nHead of metadata:")
print(scada_meta_df.head())

#%%
# Load Wind Turbine Metadata (JSON)
with open("./data/WT_Metadata.json", "r") as file:
    wt_metadata = json.load(file)

print("\nWind Turbine Metadata:")
print(json.dumps(wt_metadata, indent=4))  # Pretty-print JSON data

#%%
# Check for missing values
print(f"\nNull count:")
print(scada_df.isnull().sum())

#%%
# Check for duplicate rows
print(f"\nDuplicate rows: {scada_df.duplicated().sum()}")

#%%
# Check for unrealistic values
print(f"\nDataset description:")
print(scada_df.describe())

#%%
# Check for gaps in timestamps
scada_df["Datetime"] = pd.to_datetime(scada_df["Datetime"])
scada_df = scada_df.sort_values(by="Datetime")
scada_df["Time_Gap"] = scada_df["Datetime"].diff().dt.total_seconds()
print(f"\nTime Data Overview:")
print(scada_df[["Datetime", "Time_Gap"]].describe())

#%% md
# ## Data Cleaning

#%%
# Convert Datetime to proper format
scada_df["Datetime"] = pd.to_datetime(scada_df["Datetime"])

# Step 1: Handle Missing Values (Interpolation)
print("\nInterpolating missing data")
scada_df.interpolate(method="linear", inplace=True)

# Step 2: Clip/Filter Unrealistic Values
print("\nFiltering out unrealistic values")
# Define realistic thresholds based on known physical constraints
scada_df["GeneratorTemperature"] = scada_df["GeneratorTemperature"].clip(lower=-30, upper=100)  # Fix sensor errors
scada_df["WindSpeed"] = scada_df["WindSpeed"].clip(lower=0, upper=60)  # Wind speeds above 60m/s are rare
scada_df["PowerOutput"] = scada_df["PowerOutput"].clip(lower=0)  # Negative power is unrealistic
scada_df["MaxWindHeute"] = scada_df["MaxWindHeute"].clip(lower=0, upper=100)  # Remove extreme values

# Step 3: Check for Time Gaps and Resample
print("\nChecking for time gaps and resampling")
scada_df = scada_df.sort_values(by="Datetime")
scada_df.set_index("Datetime", inplace=True)

# Resample to 1-second intervals and interpolate missing time points
scada_df = scada_df.resample("1s").interpolate()

#%%
# Check for missing values
print(f"\nNull count:")
print(scada_df.isnull().sum())

#%%
# Get indices where any column has null values
null_dates = scada_df[scada_df.isnull().any(axis=1)].index

if not null_dates.empty:
    # Convert Index to Series
    null_dates_series = pd.Series(null_dates)

    # Detect gaps in consecutive dates
    gaps = null_dates_series.diff().gt(pd.Timedelta(days=1))

    # Assign group numbers to consecutive periods
    groups = gaps.cumsum()

    # Group by the detected groups and find min/max for each period
    date_ranges = null_dates_series.groupby(groups).agg(["min", "max"])

    print("\nNull value date ranges:")
    print(date_ranges)
else:
    print("\nNo null value dates found.")

#%%
# Filter out missing values
print("\nDropping null data")
scada_df = scada_df.dropna()
scada_df = scada_df.drop(columns=["Time_Gap"])

# Save the cleaned dataset
scada_df.to_parquet("./data/SCADA_Cleaned.parquet")
print("\nData cleaned and exported successfully!")

#%%
# Check for unrealistic values
print(f"\nCleaned dataset description:")
print(scada_df.describe())

# Print end time
print(f"\n{datetime.now()} - SCRIPT ENDED")
