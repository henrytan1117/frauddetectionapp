# Fraud Detection Prediction App

## Problem Statement

Financial institutions lose billions annually to fraudulent credit transactions. The challenge lies in the class imbalance of transaction data—where legitimate transactions vastly outnumber fraudulent ones—and the need for interpretable models that allow risk officers to understand why a transaction was flagged.

This project develops an end-to-end pipeline to identify high-risk behavioral patterns and deploy a real-time prediction interface for fraud risk assessment.

## Methodology & Technical Stack

The project follows a rigorous data science lifecycle, emphasizing statistical validation and robust feature engineering.

(1) Data Processing: Utilized pandas and numpy for data cleaning and handling missing values.

(2) EDA: Conducted exploratory analysis to identify key fraud indicators (e.g., transaction amount spikes, geographical anomalies).

(3) Feature Engineering: Developed predictive features and utilized a scikit-learn pipeline for consistent data transformation.

(4) Modeling: Implemented a Logistic Regression classifier, chosen for its interpretability in a risk management context.

(5) Validation: Applied K-Fold Cross-Validation to ensure model reliability across different data segments.

## Results & Key Findings

(1) Accuracy: Achieved a 90% classification accuracy on the test set.

(2) Interpretability: Identified that transaction frequency and specific merchant categories were the strongest predictors of fraud risk.

(3) Deployment: Developed a responsive Streamlit dashboard that allows users to input transaction parameters and receive an instant risk score. To access the interactive app, please click the link here: https://frauddetectionapp-8uf2buj4bjwybctwj6nnlg.streamlit.app/

## Discussion

While the Logistic Regression model provides a strong baseline with high interpretability, future iterations could explore:

(1) SMOTE (Synthetic Minority Over-sampling Technique): To better address the inherent class imbalance in fraud datasets.

(2) Ensemble Methods: Testing Random Forests or XGBoost to capture non-linear relationships, while using SHAP values to maintain transparency.

(3) Real-time Latency: Optimizing the pipeline for sub-second inference in a production environment.

## How to Use

(1) Interactive App: Access the live dashboard here: https://frauddetectionapp-8uf2buj4bjwybctwj6nnlg.streamlit.app/

(2) Local Setup:

git clone https://github.com/henrytan1117/fraud-detection-project.git
pip install -r requirements.txt
streamlit run app.py


## Resources and Appendix

To access the original dataset, please download via this link: https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset

This is a learning project inspired by Data Science by Onur. 
