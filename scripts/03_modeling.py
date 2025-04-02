# %% md
# # Wind Turbine Anomaly Detection: Data Modeling

# %%
# Import libraries
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Print start time
print(f"{datetime.now()} - SCRIPT STARTED")

# Set plot style
sns.set_style("whitegrid")

# %%
# Load cleaned dataset
df = pd.read_parquet("./data/SCADA_Cleaned.parquet")

# If datetime is in index, make sure it's parsed properly
df.index = pd.to_datetime(df.index, errors="coerce")
df = df[~df.index.isna()].sort_index()

# Select features based on EDA
features = ["RotorSpeed", "GeneratorTemperature", "WindSpeed", "PowerOutput", "MaxWindHeute", "PitchDeg"]
X = df[features]

# Scale features
print("\nScaling data...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# %% md
# ## Fit Isolation Forest
# %%
# Initialize Isolation Forest for anomaly detection
model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)

# Fit the model and predict anomalies (-1 for outliers, 1 for inliers)
print("\nFitting and predicting data...")
df["anomaly"] = model.fit_predict(X_scaled)

# Filter out detected anomalies (outliers)
df_anomaly = df[df["anomaly"] == -1]

# %% md
# ## Anomaly Detection Plot
# %%
# Create figure
print("\nPlotting anomaly detection in power output overtime")
plt.figure(figsize=(14, 5))

# Line plot for power output
plt.plot(df.index, df["PowerOutput"], label="PowerOutput")

# Scatter plot for anomalies
plt.scatter(x=df_anomaly.index, y=df_anomaly["PowerOutput"], color="red", label="Anomalies", s=12)

# Titles and labels
plt.title("Anomaly Detection in Power Output Over Time", fontsize=14)
plt.xlabel("Timestamp", fontsize=12)
plt.ylabel("Power Output", fontsize=12)

# Adjust layout and display the plot
plt.legend()
plt.tight_layout()
plt.savefig("./plots/Anomaly Detection in Power Output Over Time.png")
print("\nSaved plot: Anomaly Detection in Power Output Over Time.png")

# %% md
# ## Anomaly Score Distribution
# %%
# Scores: the lower, the more anomalous
df["anomaly_score"] = model.decision_function(X_scaled)

# %%
print("\nPlotting anomaly score...")
plt.figure(figsize=(14, 5))
# Create a histogram to visualize the distribution of anomaly scores
plt.figure(figsize=(8, 4))
plt.hist(x=df["anomaly_score"], bins=50, color="purple", edgecolor="black")

# Titles and labels
plt.title("Anomaly Score Distribution")
plt.xlabel("Score")
plt.ylabel("Count")

# Adjust layout and display the plot
plt.tight_layout()
plt.savefig("./plots/Anomaly Score Distribution.png")
print("\nSaved plot: Anomaly Score Distribution.png")

# %% md
# ## Anomaly Percentage

# %%
# Calculate the percentage of anomalies detected
anomaly_rate = df_anomaly.shape[0] / len(df) * 100

# Print the total number of anomalies and their percentage
print(f"\nAnomalies detected: {df_anomaly.shape[0]:,} out of {len(df):,} rows ({anomaly_rate:.2f}%)")

# %% md
# ## Compare Anomaly vs Normal Stats

# %%
# Display summary statistics for normal (non-anomalous) data
print("\nNormal (non-anomalous) summary:\n", df[df["anomaly"] == 1][features].describe())

# Display summary statistics for detected anomalies
print("\nAnomalies summary:\n", df_anomaly[features].describe())

# %% md
# ## Zoom into a Specific Date Range (May 2022)

# %%
# Filter data for the period between May 1, 2022, and June 1, 2022
df_may_22 = df["2022-05-01":"2022-06-01"]

# Extract anomalies from the filtered period
df_may_22_anomaly = df_may_22[df_may_22["anomaly"] == -1]

# %%
# Create figure
print("\nPlotting anomaly detection in power output in May 2022")
plt.figure(figsize=(14, 5))

# Line plot for power output
plt.plot(df_may_22.index, df_may_22["PowerOutput"], label="PowerOutput")

# Scatter plot for anomalies
plt.scatter(x=df_may_22_anomaly.index, y=df_may_22_anomaly["PowerOutput"], color="red", label="Anomalies", s=15)

# Titles and labels
plt.title("Anomaly Detection in Power Output (May 2022)", fontsize=14)
plt.xlabel("Timestamp", fontsize=12)
plt.ylabel("Power Output", fontsize=12)

# Adjust layout and display the plot
plt.legend()
plt.tight_layout()
plt.savefig("./plots/Anomaly Detection in Power Output (May 2022).png")
print("\nSaved plot: Anomaly Detection in Power Output (May 2022).png")

# %% md
# ## Summary Stats

# %%
# Calculate the percentage of anomalies detected
anomaly_rate = df_anomaly.shape[0] / len(df) * 100

# Print the total number of anomalies and their percentage
print(f"\nAnomalies detected: {df_anomaly.shape[0]:,} out of {len(df):,} rows ({anomaly_rate:.2f}%)")

# Print end time
print(f"\n{datetime.now()} - SCRIPT ENDED")
