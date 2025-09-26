# CONTENT-MONETIZATION-MODELER


Content Monetization Prediction Tool
-
This project is a Content Monetization Prediction tool that estimates ad revenue (USD) for online content using machine learning and real-time YouTube data.

The system predicts revenue based on content performance metrics such as views, likes, comments, watch time, subscribers, and audience engagement. A Streamlit web app allows users to interact with the model in real time.

Features
-
Predict ad revenue using 13 input features:

views

likes

comments

watch_time_minutes

video_length_minutes

subscribers

category

device

country

engagement_rate (auto-calculated)

avg_watch_time (auto-calculated)

Streamlit interface for real-time predictions.

Handles categorical inputs: category, device, country, day_of_week.

Automatically calculates:

engagement_rate = (likes + comments) / views

avg_watch_time = watch_time_minutes / views

Supports live ad revenue prediction using YouTube API key.

Preprocessing
-
All preprocessing steps are implemented in notebooks/preprocessing.ipynb:

Handle missing values in numeric and categorical columns.

Encode categorical variables using OneHotEncoder.

Feature scaling for models that require it (e.g., SVR).

Feature engineering for engagement rate and average watch time.

Model Building
-
Several machine learning models were trained and evaluated:

Linear Regression (LR)

Decision Tree Regressor (DT)

K-Nearest Neighbors Regressor (KNN)

Random Forest Regressor (RF)

Gradient Boosting Regressor (GBR)

Support Vector Regression (SVR)

Evaluation & Model Selection

Models were evaluated using R² score on the test dataset.

Linear Regression was selected for deployment because:

Fast predictions suitable for front-end use.

Provides stable and interpretable results.

Other models like Random Forest, Gradient Boosting, and Decision Tree can also be used for improved accuracy.

The trained LR model is saved as models/linear_regression_model.pkl.
