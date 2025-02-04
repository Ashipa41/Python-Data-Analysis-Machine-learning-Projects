# **Heart Disease Prediction Project** 🏥

## **1. Introduction** 📌
Cardiovascular diseases (CVDs) are the leading cause of death globally. This project aims to predict the likelihood of heart disease using machine learning models. The dataset consists of 11 features that represent various health metrics.

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

### **Model Comparison Results:**
| Model                 | Accuracy | Precision (Macro Avg) | Recall (Macro Avg) | F1-Score (Macro Avg) |
|----------------------|----------|----------------------|----------------------|----------------------|
| **Random Forest**         | 86.4%  | 0.860   | 0.861   | 0.861  |
| **Logistic Regression**   | 86.4%  | 0.860   | **0.867**   | **0.862**  |
| Gradient Boosting        | 85.3%  | 0.849   | 0.852   | 0.850  |
| SVM                      | 85.9%  | 0.854   | 0.860   | 0.856  |
| Decision Tree            | 78.3%  | 0.778   | 0.784   | 0.779  |

### **Best Model:** 🏆
- **Logistic Regression** performed the best with **86.4% accuracy** and the highest recall (86.7%), making it the most suitable model for identifying heart disease cases.

## **6. Hyperparameter Tuning** 🎛️
- Grid Search performed to optimize `C` (regularization strength) and solver type.
- Best parameters found:
  - `C = 0.1`
  - `solver = 'liblinear'`
- Tuned model improved generalization and maintained high accuracy.

## **7. Conclusion and Next Steps** 🚀
- **Key Takeaway:** Logistic Regression is the best-performing model.
- **Potential Improvements:**
  - Further hyperparameter tuning.
  - Feature engineering to extract more predictive information.
  - Deployment as a web-based application for real-time predictions.

This project successfully built a predictive model for heart disease using machine learning techniques and data preprocessing strategies.

