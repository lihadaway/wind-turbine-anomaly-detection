# CS-633: Data Mining Final Project Assignment 3

## Task 2.1: Gathering Data

**Deliverable: Data Collection Report**

**Dataset Overview**  
For this project, we selected the supervisory control and data acquisition **(**SCADA) dataset from the Aventa AV-7 Research Wind Turbine, sourced from Zenodo. The dataset consists of time-series sensor data recorded at 1Hz from January 1, 2022, to July 20, 2023\. 

**Data Sources**  
The following files were collected:

* SCADA Data: [Aventa\_AV7\_IET\_OST\_SCADA.csv](https://zenodo.org/records/8192149/files/Aventa_AV7_IET_OST_SCADA.csv?download=1)  
* SCADA Metadata: [SCADA\_Channels\_Metadata.csv](https://zenodo.org/records/8192149/files/SCADA_Channels_Metadata.csv?download=1)  
* Wind Turbine Metadata: [Aventa\_AV\_7\_IET\_OST\_WT\_metadata.json](https://zenodo.org/records/8192149/files/Aventa_AV_7_IET_OST_WT_metadata.json?download=1)

**Data Collection Methodology** 

* The dataset was downloaded directly from Zendo using Python.  
* Metadata files were included to provide context for each SCADA measurement.  
* The data includes environmental and operational turbine parameters sampled at 1-second intervals.

## Task 2.2: Gathering Data

**Deliverable: Data Description Report**

**Data Structure**

* Size: \~39.7 million rows, 11 columns  
* Key Features:  
  * Datetime: Timestamp of measurements  
  * RotorSpeed: Rotor speed (RPM)  
  * GeneratorSpeed: Generator speed (RPM)  
  * GeneratorTemperature: Stator temperature (°C)  
  * WindSpeed: Wind speed (m/s)  
  * PowerOutput: Active power output (kW)  
  * offsetWindDirection: Wind direction relative to nacelle (°)  
  * PitchDeg: Blade pitch angle (°)  
  * StatusAnlage: Turbine status codes  
  * SpeiseSpannung: System supply voltage (24V)  
  * MaxWindHeute: Maximum wind speed recorded daily

**Data Types**

* **Timestamp (DateTime format):** Datetime  
* **Numeric Data (Continuous):** RotorSpeed (RPM), GeneratorSpeed (RPM), GeneratorTemperature (°C), WindSpeed (m/s), PowerOutput (kW), offsetWindDirection (°), PitchDeg (°), SpeiseSpannung (V), MaxWindHeute (m/s)  
* **Categorical Data (Discrete):** StatusAnlage

**Metadata Summary**

* SCADA Channels Metadata: Describes each SCADA measurement, including IEC 61400-25 compliance and reliability.  
* Wind Turbine Metadata: Provides technical specifications of the turbine (e.g., rotor diameter, drivetrain type, control systems).

## Task 2.3: Exploring Data

**Deliverable: Data Exploration Report**

**Initial Data Analysis & Observations**  
Missing Values:

* Very minimal impact: 5 missing values found across WindSpeed, PowerOutput, MaxWindHeute, and PitchDeg.

Outliers & Unrealistic Values:

* GeneratorTemperature had extreme values (-95.1°C to 107.3°C), it might be caused by sensor error.  
* PowerOutput had negative values (not physically possible).  
* MaxWindHeute had a max of 187,458 m/s which is a clear anomaly. 

Timestamp Gaps & Irregular Sampling:

* Data is mostly sampled at 1-second intervals, but some gaps exist (up to \~29 days). 

## Task 2.4: Verifying Data Quality

**Deliverable: Data Quality Report**

**Issues Identified & Resolutions**

| Issue          | Identified Problem                                    | Resolution                         |
|:---------------|:------------------------------------------------------|:-----------------------------------|
| Missing Values | 5 missing data points                                 | Interpolated values                |
| Outliers       | Unrealistic temperature, wind speed, and power output | Clipped extreme values             |
| Timestamp Gaps | Missing time intervals (up to 29 days)                | Resample timestamps & interpolated |

