# CS-633: Data Mining Final Project Assignment 4

# Task 3.1: Selecting Data

**Deliverable: Data Rationale Report**

## Overview of Data Selection

The dataset chosen for this project is a wind turbine SCADA dataset. The selection criteria were:

* **Relevance:** The dataset contains key operational parameters required for anomaly detection and performance assessment.
* **Completeness:** The dataset includes over 39 million records, providing a robust sample size.
* **Diversity:** It contains multiple attributes such as wind speed, rotor speed, power output, and generator temperature.
* **Availability:** The dataset is accessible and well-documented, making it suitable for analysis.

# Task 3.2: Cleaning Data

**Deliverable: Data Cleansing Report**

## Identified Issues

* **Missing Values:** Wind speed, power output, max wind today, and pitch degree had missing values.
* **Unrealistic Values:** Some values (generator temperature, wind speed, power output, and max wind today) showed extreme deviations that required further examination.

## Cleaning Process

* **Missing Values Handling:**
  * Imputed missing values using linear interpolation.
* **Outlier Detection and Treatment:**
  * Used statistical summaries to detect outliers in numerical fields.
  * Applied capping techniques to limit extreme values based on known physical constraints.
* **Standardization and Formatting:**
  * Converted timestamps to a standardized format.
  * Ensured consistency in numerical scales.

# Task 3.3: Constructing Data

**Deliverable 1: Data Attribute Report**

| Attribute            | Description                    | Type   | Handling Process                      |
|:---------------------|:-------------------------------|:-------|:--------------------------------------|
| Datetime             | Timestamp of record            | Object | Converted to datetime format          |
| RotorSpeed           | Rotor speed in RPM             | Float  | Checked for unrealistic values        |
| GeneratorSpeed       | Generator speed in RPM         | Float  | Checked for unrealistic values        |
| GeneratorTemperature | Temperature of generator in °C | Float  | Checked and cleaned outliers          |
| WindSpeed            | Wind speed in m/s              | Float  | Imputed missing values                |
| PowerOutput          | Power generated in kW          | Float  | Imputed missing values, checked range |
| SpeiseSpannung       | Supply voltage (24W)           | Float  | Verified consistency                  |
| StatusAnlage         | Turbine status code            | Float  | Categorical treatment if needed       |
| MaxWindHeute         | Maximum wind today             | Float  | Imputed missing values                |
| offsetWindDirection  | Wind direction offset          | Float  | Verified consistency                  |
| PitchDeg             | Blade pitch in degrees         | Float  | Imputed missing values                |

**Deliverable 2: Data Generation Report**

To enhance the dataset for anomaly detection, we generated the following new attributes:

1. Rolling Average Wind Speed (**WindSpeed\_10min\_avg**)
2. A 10 minute rolling mean of wind speed values to smooth fluctuations.
3. Anomaly Flags for Extreme Values (**Anomaly\_Flag**)
4. Flagged data points where:
    1. **MaxWindHeute** \> 50 m/s (realistic hurricane-force winds).
    2. **GeneratorTemperature** \< \-40°C or \> 80°C(beyond operational range).
    3. **PowerOutput** \< 0 (physically impossible for energy production).
5. Time Gap Indicator (**Time\_Gap**)
6. Calculated time differences between consecutive observations to detect missing data segments.

# Task 3.4: Integrating Data

**Deliverable: Merged Data Set**

The final dataset was created by merging:

* SCADA sensor data (**Aventa\_AV7\_IET\_OST\_SCADA.csv**)
* SCADA metadata (**SCADA\_Channels\_Metadata.csv**)
* Wind turbine specifications (**Aventa\_AV\_7\_IET\_OST\_WT\_metadata.json**)

**Merging Methodology**

* Merged SCADA data with metadata based on channel names to provide meaningful descriptions for each sensor variable.
* Integrated wind turbine specifications into the dataset to give context for operational limits.
* Key join conditions:
  * **Datetime** for SCADA data
  * **Internal Name** for sensor descriptions

# Task 3.5: Formatting Data

**Deliverable: Final Formatted Data Set**

The cleaned and processed dataset is stored in parquet format (SCADA\_Cleaned.parquet) for compatibility with modeling tools.

**Final Preprocessing Steps:**

* Normalized continuous variables (**MinMaxScaler)** to ensure uniform scaling for modeling training.
* Encoded categorical turbine statuses into numerical values for machine learning compatibility.
* Saved cleaned dataset with all engineered features, anomalies flagged, and missing values handled.

**Final Dataset Stats:**

* Rows: \~39.7 million
* Columns 14 (original 11 \+ 3 engineered features)
* Missing Data: Interpolated or flagged
* Outliers: Capped or flagged for anomaly detection
