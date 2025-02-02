# **Detecting Breast Cancer Using Machine Learning Algorithms**

## **Introduction**
Breast cancer is one of the most prevalent and life-threatening diseases among women worldwide. Early detection and accurate diagnosis significantly improve survival rates. Machine learning (ML) algorithms have emerged as powerful tools for analyzing complex medical datasets, identifying patterns, and enabling precise classification of breast cancer cases as **malignant (cancerous)** or **benign (non-cancerous)**.

This project leverages ML techniques to develop a reliable classification model for breast cancer detection, providing a structured workflow from data preprocessing to model evaluation.

---

## **Dataset Overview**
The analysis is based on the **Breast Cancer Wisconsin Dataset**, which contains features extracted from breast biopsy images. The dataset includes:

- **Diagnosis (Target Variable)**: Labeled as `M` (Malignant) or `B` (Benign).
- **Features**: 30 numerical attributes derived from image analysis, such as **radius, texture, perimeter, area, and smoothness**.
- **ID Column**: A unique identifier for each sample (removed during preprocessing).

---

## **Workflow and Methodology**

### **1. Data Preprocessing**
Before training machine learning models, the dataset undergoes thorough preprocessing:

- **Data Cleaning**: Remove unnecessary columns (e.g., ID column) that do not contribute to prediction.
- **Feature Selection**: ANOVA F-Test was applied to retain only the most significant features (`p < 0.05`).
- **Normalization**: StandardScaler was used to normalize the features before PCA and model training.
- **Dimensionality Reduction**: PCA was applied to reduce multicollinearity and retain relevant information.

---

### **2. Exploratory Data Analysis (EDA)**
EDA provides insights into the dataset through visualizations and statistical analysis:

- **Target Distribution**: Assess the proportion of malignant vs. benign cases.
- **Feature Distributions**: Visualize feature variations using histograms and boxplots.
- **Pairwise Feature Relationships**: Use scatter plots to analyze interactions between key features.
- **Correlation Heatmap**: Identify strongly correlated features, guiding feature selection.

---

### **3. Model Development**
This project evaluates multiple machine learning models for breast cancer classification. The **HistGradientBoosting classifier** was ultimately chosen based on its high accuracy and generalization ability.

- **Train-Test Split**: The dataset was split into **training (80%)** and **testing (20%)** subsets to ensure unbiased model evaluation.
- **Model Training**: Various machine learning algorithms were trained and optimized, including:
  - **Logistic Regression**
  - **Random Forest**
  - **AdaBoost**
  - **HistGradientBoosting**
  - **K-Nearest Neighbors (KNN)**

---

## **📌 Model Performance Analysis After Feature Selection & Normalization**
Now that we have the accuracy, confusion matrices, and cross-validation scores, let's determine the best-performing model based on different criteria.

### **🚀 Step 1: Accuracy Comparison**

| Model | Accuracy |
|--------|---------------------|
| **Logistic Regression** | **95%** |
| **Random Forest** | **96%** |
| **AdaBoost** | **97%** |
| **HistGradientBoosting** | **97%** |
| **KNN** | **93%** |

✅ **Best Models (Highest Accuracy):** **AdaBoost & HistGradientBoosting (97%)**  
❌ **Weakest Model:** **KNN (93%)**

---

### **🚀 Step 2: Cross-Validation Scores (Model Generalizability)**

| Model | Mean CV Score |
|--------|------------------|
| **Logistic Regression** | **0.8872 (88.72%)** |
| **Random Forest** | **0.8024 (80.24%)** |
| **SVM** | **0.6323 (63.23%)** ❌ |
| **AdaBoost** | **0.7839 (78.39%)** |
| **HistGradientBoosting** | **0.8966 (89.66%)** ✅ |
| **KNN** | **0.8401 (84.01%)** |

✅ **Best Generalization (Highest CV Score):** **HistGradientBoosting (89.66%)**  
❌ **Weakest Model (Poor Generalization):** **SVM (63.23%)**

---

### **🚀 Step 3: Confusion Matrix Analysis (False Positives & False Negatives)**

| Model | False Positives (FP) | False Negatives (FN) |
|--------|------------------|------------------|
| **Logistic Regression** | 2 | **2** ✅ |
| **Random Forest** | 3 | **1** ✅ |
| **SVM** | 2 | **4** ❌ |
| **AdaBoost** | 3 | 2 |
| **HistGradientBoosting** | 3 | 3 |
| **KNN** | 2 | 3 |

✅ **Best Model (Lowest False Negatives - Avoids Missed Cancer Cases):** **Random Forest (1 FN) & Logistic Regression (2 FN)**  
❌ **Worst Model (Most False Negatives - Misses More Cancer Cases):** **SVM (4 FN)**

📌 **False negatives are critical in medical diagnoses because missing a malignant case could be dangerous.**

---

### **🚀 Final Model Recommendation**

| Criteria | Best Model |
|-------------|--------------|
| **Highest Accuracy** | ✅ **AdaBoost & HistGradientBoosting (97%)** |
| **Best Cross-Validation Score (Generalization)** | ✅ **HistGradientBoosting (89.66%)** |
| **Lowest False Negatives (Medical Criticality)** | ✅ **Random Forest (1 FN), Logistic Regression (2 FN)** |

🏆 **Final Best Model: HistGradientBoosting**
- **Highest accuracy (97%)**
- **Best generalization score (89.66%)**
- **Acceptable false negative rate (3 FN)**

🔥 **Alternative Choice: AdaBoost**
- **Same accuracy (97%)**
- **Slightly lower generalization score (78.39%)**
- **Similar false negative count (2 FN)**

📌 **If prioritizing high recall (minimizing false negatives), consider Random Forest or Logistic Regression.**  
📌 **If prioritizing generalization and stability, HistGradientBoosting is the best overall choice.**

---

## **Future Work**
- **Perform Hyperparameter Tuning** for further optimization.
- **Explore additional ML algorithms** (e.g., Support Vector Machines, XGBoost) for comparative analysis.
- **Expand the dataset** by incorporating external sources to improve generalizability.
- **Develop real-time diagnostic tools** to assist medical professionals in decision-making.

---

## **Conclusion**
This project demonstrates the potential of **machine learning** in breast cancer detection. With appropriate **feature selection, normalization, dimensionality reduction, and model tuning**, ML algorithms can deliver highly accurate classification results.

