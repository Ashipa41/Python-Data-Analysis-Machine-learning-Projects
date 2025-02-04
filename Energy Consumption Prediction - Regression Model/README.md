# Energy Consumption Prediction - README

## 📌 Project Overview
This project focuses on predicting energy consumption in buildings based on various features such as square footage, number of occupants, appliances used, average temperature, and the day of the week. The goal is to build an accurate predictive model to optimize energy usage and efficiency.

## 🔗 Dataset
The dataset used for this project is available on Kaggle:
[Energy Consumption Dataset](https://www.kaggle.com/datasets/govindaramsriram/energy-consumption-dataset-linear-regression/data)

---
## 🛠️ 1️⃣ Data Exploration and Cleaning

### Data Overview:
- **Training Dataset**: 1,000 entries, 7 columns.
- **Testing Dataset**: 100 entries, 7 columns.
- **Columns** included both categorical (`Building Type`, `Day of Week`) and numerical variables (`Square Footage`, `Number of Occupants`, etc.).

### Findings:
- No missing values were found in the dataset.
- Outliers were detected in numerical features (e.g., `Square Footage`, `Number of Occupants`), but these were retained for model training.

---
## 🛠️ 2️⃣ Data Preprocessing
✔ Load dataset  
✔ Handle missing values (if any)  
✔ Exploratory Data Analysis (EDA)  
✔ One-Hot Encoding for categorical variables  
✔ Feature Engineering  
✔ Normalize numerical features using **StandardScaler**  

---
## 🛠️ 3️⃣ Tools and Libraries Used

### **Python Libraries:**
- **pandas, numpy**: For data manipulation and preprocessing.
- **seaborn, matplotlib**: For data visualization.
- **scikit-learn**: For model building, evaluation, and optimization.

---
## 🤖 4️⃣ Model Building
Multiple regression models were trained and evaluated:
✔ **Linear Regression**
✔ **Ridge Regression** (L2 Regularization)
✔ **Lasso Regression** (L1 Regularization)

### 📊 Model Evaluation Metrics:
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score**
- **Cross-Validation**

---
## 📈 Model Performance

| Model               | Mean Squared Error | Root Mean Squared Error | R² Score |
|---------------------|-------------------|-------------------------|----------|
| **Linear Regression** | 0.000188          | 0.013728                | 1.000000 |
| **Ridge Regression** | 12.486473         | 3.533620                | 0.999985 |
| **Lasso Regression** | 0.046544          | 0.215741                | 1.000000 |

**Best Model:** Linear Regression

---
## 🔄 Cross-Validation Results

| Model               | Cross-Validation R² Scores                            | Mean CV Score | Performance Comment |
|---------------------|-----------------------------------------------------|--------------|---------------------|
| **Linear Regression** | [1. 1. 1. 1. 1.]                                   | 0.9999999998 | May indicate overfitting due to perfect scores despite being the Best model |
| **Ridge Regression** | [0.99997129 0.99997955 0.9999795  0.99997216 0.99998234] | 0.9999769673 | Slight regularization helps reduce overfitting |
| **Lasso Regression** | [0.99999994 0.99999996 0.99999995 0.99999995 0.99999994] | 0.9999999500 | Maintains high accuracy while reducing complexity |

---
## 🚀 Conclusion
- The **Lasso Regression** model was found to be the best in terms of accuracy and complexity reduction.
- The model can be further improved by incorporating additional environmental factors such as humidity and real-world data validation.
- Future work may include **time-series forecasting** for long-term energy demand prediction.

---
## 📁 Repository Structure
```
📂 Energy-Consumption-Prediction
 ├── 📄 energy_consumption_analysis.docx  # Detailed project documentation
 ├── 📄 README.md                         # Project summary and setup guide
 ├── 📂 data/                             # Dataset files
 ├── 📂 models/                           # Trained model files
 ├── 📂 notebooks/                        # Jupyter notebooks for analysis & training
 ├── 📂 scripts/                          # Python scripts for data preprocessing & modeling
```

---
## 📝 Author
Developed by **Paul**

For any inquiries, feel free to reach out!
