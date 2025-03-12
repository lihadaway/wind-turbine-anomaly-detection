# CS-633: Data Mining Final Project Assignment 1

## Part 1: Team Information

* **Team Members:** Leslie Hadaway and Chang Liu

We will be working together as a team of two for this project, as recommended. Both of us are committed to contributing equally to ensure the successful completion of the final project.

## Part 2: Project Selection

### Original Project

* **Title:** Renewable Energy \- Tuning and Pipelining ML Models  
* **Link:** [ReneWind Energy: Tuning & Pipelining ML Models](https://www.kaggle.com/code/lilyhyseni/renewind-energy-tuning-pipelining-ml-models/notebook)

### Updated Project Proposal

We plan to adapt the original renewable energy project, which focuses on energy output prediction, to develop an anomaly detection system for equipment failures in renewable energy infrastructures, such as wind turbines. The core objective is to identify potential malfunctions or performance degradation in advance by analyzing patterns in sensor data. By shifting the focus to anomalies, the system will not only identify potential equipment failures but also improve the efficiency of maintenance schedules and operational reliability.  
Our approach involves modifying the machine learning pipeline to detect outliers and abnormal patterns rather than just predicting energy output. A combination of traditional anomaly detection techniques and deep learning methods to enhance detection capabilities:

* Traditional Methods: Isolation Forests, Z-score analysis, One-Class SVM, and local outlier Factor(LOF) will help identify statistical deviations from normal behavior.  
* Deep Learning Approaches: Autoencoders and Long Short-Term Memory Networks (LSTM) will be integrated to capture time-series sensor readings. 

By combining traditional anomaly detection techniques with deep learning methodologies, we aim to create a comprehensive and robust system for proactive identification of potential equipment failures in wind turbines.   
The updated project will maintain the original codebase’s structure, with enhancements focused on feature engineering, model selection, and evaluation metrics specific to anomaly detection tasks. This adaptation will provide a practical solution relevant to predictive maintenance, reducing downtime and maintenance costs in renewable energy operations, ultimately strengthening the reliability and efficiency of wind energy operations.
