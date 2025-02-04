# **Heart Disease Prediction Project** 🏥

## **1. Introduction** 📌
Cardiovascular diseases (CVDs) have led to the deaths of over **18 million people globally**. This project aims to predict heart failure using machine learning models. The dataset consists of 11 features that represent various health metrics.

## **2. Dataset Overview** 📊
- **Number of Records:** 918
- **Number of Features:** 11 (Independent variables)
- **Target Variable:** `HeartDisease` (Binary classification: 0 = No, 1 = Yes)
- **Feature Types:**
  - **Numerical:** Age, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak
  - **Categorical:** Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope

## **3. Data Preprocessing** 🛠️
- **Handling Missing Values:** No missing values detected.
- **Handling Anomalies:**
  - `Cholesterol = 0` replaced with median cholesterol.
  - `RestingBP = 0` replaced with median blood pressure.
- **Feature Encoding:**
  - One-hot encoding applied to categorical variables.
- **Feature Scaling:**
  - Standardization applied to numerical features.

## **4. Exploratory Data Analysis (EDA)** 📈
- Distribution of heart disease cases analyzed using visualizations.
- Correlation analysis revealed key insights:
  - `MaxHR` and `Cholesterol` negatively correlated with heart disease.
  - `Age`, `FastingBS`, and `Oldpeak` positively correlated with heart disease.

## **5. Model Training and Evaluation** 🤖
### **Models Trained:**
1. **Random Forest Classifier**
2. **Logistic Regression**
3. **Decision Tree Classifier**
4. **Gradient Boosting Classifier**
5. **Support Vector Machine (SVM)**

### **Evaluation Metrics:**
- **Accuracy**
- **Precision, Recall, F1-Score**
- **Confusion Matrix Analysis**

### **Model Performance Results:** 📊
| Model                 | Accuracy | Precision (Macro Avg) | Recall (Macro Avg) | F1-Score (Macro Avg) |
|----------------------|----------|----------------------|----------------------|----------------------|
| **Random Forest**         | **85.87%**  | **85.42%**   | **85.67%**   | **85.53%**  |
| **Logistic Regression**   | 83.69%  | 83.35%   | 84.16%   | 83.50%  |
| Gradient Boosting        | 83.69%  | 83.21%   | 83.80%   | 83.41%  |
| SVM                      | 82.61%  | 82.26%   | 83.04%   | 82.40%  |
| Decision Tree            | 77.17%  | 77.08%   | 77.83%   | 77.00%  |

### **Confusion Matrix Analysis:** 🔍
#### **Key Observations:**
1. **Random Forest (Best Model)**
   - **True Positives (93) and True Negatives (65)**: The model correctly predicted heart disease in 93 cases and correctly classified non-heart disease cases in 65 cases.
   - **False Negatives (14)**: These cases were actually heart disease but misclassified as non-disease.
   - **False Positives (12)**: These cases were incorrectly classified as heart disease.
   - **Conclusion**: **Balanced model with high accuracy and low false negatives.**

2. **Logistic Regression**
   - **More False Negatives (20) than Random Forest**: This suggests it misses more cases of heart disease.
   - **Better True Negative (67)** than Random Forest but **lower recall**.
   - **Conclusion**: **Decent model but slightly weaker than Random Forest in recall.**

3. **Decision Tree (Worst Performance)**
   - **Most False Negatives (28) and False Positives (14)**: High misclassification rate.
   - **Conclusion**: **Overfitting issue likely. Performs worse than other models.**

4. **Gradient Boosting**
   - **Performance close to Random Forest** but slightly **higher false negatives (18)**.
   - **Conclusion**: **Good alternative model, but Random Forest still outperforms it.**

5. **SVM**
   - **False Negatives (21) and False Positives (11)**.
   - **Slightly weaker recall** compared to Gradient Boosting and Random Forest.
   - **Conclusion**: **Performs decently, but not the best.**

### **Best Model:** 🏆
- **Random Forest** performed the best with **85.87% accuracy** and the highest recall (85.67%), making it the most suitable model for identifying heart disease cases.

## **6. Hyperparameter Tuning** 🎛️
- Grid Search performed to optimize `C` (regularization strength) and solver type for Logistic Regression.
- Best parameters found:
  - `C = 0.1`
  - `solver = 'liblinear'`
- Tuned model improved generalization and maintained high accuracy.

## **7. Conclusion and Next Steps** 🚀
- **Key Takeaway:** Random Forest is the best-performing model.
- **Potential Improvements:**
  - Further hyperparameter tuning.
  - Feature engineering to extract more predictive information.
  - Deployment as a web-based application for real-time predictions.

This project successfully built a predictive model for heart disease using machine learning techniques and data preprocessing strategies.
