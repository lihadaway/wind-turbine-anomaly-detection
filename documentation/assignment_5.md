# CS-633: Data Mining Final Project Assignment 5

## Task 4.1: Selecting Modeling Techniques

**Deliverable 1: Defined Modeling Technique(s)**

**Selected Technique:** Isolation Forest – an unsupervised anomaly detection algorithm based on isolating outliers in high-dimensional feature space.

**Justification:**
- **Nature of the problem:** Anomaly detection in time-series sensor data without labeled failure cases.
- **Business need:** Early identification of abnormal turbine behavior using only historical operational data.
- **Data characteristics:** Large volume of continuous sensor data with outliers and missing values, which Isolation Forest handles well.
- **Scalability:** Isolation Forest is efficient for large datasets and can be updated incrementally.
- **Interpretability:** Outputs anomaly scores that can be monitored and thresholded, supporting actionable alerts.

**Alternative Techniques Considered:**
- **One-Class SVM:** Effective but computationally expensive and sensitive to hyperparameters.
- **Autoencoders:** Good for complex patterns but require more data preprocessing and tuning.
- **Statistical models (e.g., z-score, ARIMA):** Not well-suited for multivariate high-dimensional sensor data.

**Deliverable 2: Defined Modeling Assumptions**

**Key Assumptions of Isolation Forest:**
1. **Data contains anomalies:** Assumes a small fraction of data points are outliers (controlled via contamination parameter).
2. **Features are independent:** While not strictly required, better performance is expected when irrelevant or redundant features are removed.
3. **Continuous numerical features:** Works best with scaled, continuous numeric input, which is satisfied via standardization.
4. **Balanced variance among features:** StandardScaler ensures that all features contribute equally to tree splits.

**Additional Notes:**
- **No label dependency:** Suitable for unsupervised scenarios with no ground truth on failures.
- **Anomalies are isolatable:** Model assumes anomalies are easier to separate via recursive splits due to their rarity and feature value distinctiveness.

## Task 4.3: Building Model

**Deliverable 1: Parameter Definitions**

**Model:** IsolationForest

**Library:** sklearn.ensemble.IsolationForest

**Parameter Configuration:**

| Parameter       | Value  | Description                                                                               |
|-----------------|--------|-------------------------------------------------------------------------------------------|
| `n_estimators`  | 100    | Number of base estimators in the ensemble. Default value used.                            |
| `contamination` | 0.01   | Estimated proportion of anomalies in the data (1%). Set based on domain knowledge.        |
| `max_samples`   | 'auto' | Number of samples to draw for training each base estimator. Default: min(256, n_samples). |
| `max_features`  | 1.0    | Fraction of features used to train each base estimator. Default (all features).           |
| `bootstrap`     | False  | Whether to bootstrap samples. Default (no bootstrapping).                                 |
| `random_state`  | 42     | Seed for reproducibility.                                                                 |
| `verbose`       | 0      | Controls verbosity of output. Default (silent).                                           |
| `n_jobs`        | None   | Number of parallel jobs. Default (single-threaded).                                       |

**Deliverable 2: Model Descriptions**

**Type of Model:** Isolation Forest

**Why Chosen:**
- Designed specifically for anomaly detection.
- Handles high-dimensional, large-scale, and unlabeled data efficiently.
- Well-suited to the characteristics of SCADA data and business goals (early detection of faults).

**Features Used (scaled):**
- RotorSpeed
- GeneratorTemperature
- WindSpeed
- PowerOutput
- MaxWindHeute
- PitchDeg

**Why These Features:** They directly reflect turbine operational and environmental conditions. Sudden or unusual changes in these values may precede equipment failure or abnormal operation.

**Model Interpretation:**
- Outputs an anomaly score for each data point.
- Points with scores above the threshold (determined by contamination=0.01) are labeled as anomalies.
- Higher scores indicate a higher likelihood of the point being anomalous.

**Difficulties Encountered:**
- Large dataset: Over 39 million rows required memory-efficient techniques and batch processing.
- Irregular sampling: Missing time intervals required resampling and interpolation to stabilize modeling input.
- Feature engineering: Needed to validate sensor behavior (e.g., unrealistic wind speed or temperature values were clipped).

**Deliverable 3: Data Models**
