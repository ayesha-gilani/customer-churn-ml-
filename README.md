# Customer Churn Prediction

## 📌 Project Overview
This project is an end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn. Customer churn means a customer stops using a company's services. Predicting churn can help businesses identify customers who may leave and take preventive actions to improve customer retention. 

The project covers the complete Machine Learning workflow, from data cleaning and exploratory data analysis to model training, evaluation, model saving, and deployment using Streamlit.

---

## 🎯 Project Objectives
* Clean and preprocess customer data
* Perform Exploratory Data Analysis (EDA)
* Identify factors related to customer churn
* Prepare data for Machine Learning
* Train and compare multiple classification models
* Evaluate model performance
* Select the best-performing model
* Save the trained model for reuse
* Build an interactive Streamlit application
* Predict customer churn probability from user-provided information

---

## 🛠️ Technologies Used
* **Languages:** Python
* **Data Libraries:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-learn, Joblib
* **Deployment:** Streamlit
* **Environments & Tools:** Google Colab, Git & GitHub

---

## 📊 Dataset
The project uses the **Telco Customer Churn** dataset. The dataset contains customer information such as:
* Customer demographics
* Tenure
* Contract type
* Internet service
* Payment method
* Monthly charges
* Total charges
* Additional services
* Churn status

The target variable is:
```text
Churn (Yes = Customer churned, No = Customer did not churn)
```

---

## 🔄 Machine Learning Workflow
```text
Raw Dataset 
    ↓ 
Data Cleaning 
    ↓ 
Exploratory Data Analysis 
    ↓ 
Feature Engineering 
    ↓ 
Data Preparation 
    ↓ 
Train/Test Split 
    ↓ 
Model Training 
    ↓ 
Model Evaluation 
    ↓ 
Model Comparison 
    ↓ 
Best Model Selection 
    ↓ 
Model Saving 
    ↓ 
Streamlit Deployment
```

---

## 🧹 Data Cleaning
The following preprocessing steps were performed:
* Checked dataset shape and data types.
* Checked and handled missing values (specifically in `TotalCharges` by converting it to numeric format).
* Checked for duplicate records.
* Removed the `customerID` column as it does not provide useful predictive information.
* Converted categorical variables into numerical features using **One-Hot Encoding**.

---

## 📈 Exploratory Data Analysis
Several analyses were performed to understand customer churn patterns. Key insights include:

### 📄 Contract Type
Customers with **month-to-month contracts** showed considerably higher churn compared with customers having one-year or two-year contracts.

### ⏳ Tenure
Customers who churned generally had a **lower average tenure** than customers who stayed.

### 🌐 Internet Service
Churn patterns differed across internet service types, with **fiber-optic customers** showing a higher churn rate in this dataset.

### 🧓 Senior Citizens
**Senior citizens** showed a higher churn percentage compared with non-senior customers.

### 💰 Monthly and Total Charges
Customer charges were also analyzed to understand their relationship with churn, helping identify customer characteristics associated with higher churn risk.

---

## 🤖 Machine Learning Models
Two classification models were trained and compared:

### 1. Logistic Regression (Selected Model)
Logistic Regression was used as the primary classification model and achieved the best overall performance.
* **Accuracy:** 0.81
* **Churn Precision:** 0.66
* **Churn Recall:** 0.56
* **Churn F1-Score:** 0.61
* **ROC-AUC:** 0.84

### 2. Random Forest
Random Forest was trained to compare its performance with Logistic Regression.
* **Accuracy:** 0.78
* **Churn Precision:** 0.62
* **Churn Recall:** 0.50
* **Churn F1-Score:** 0.55

---

## 🏆 Model Selection
After comparing both models, **Logistic Regression** was selected as the final model because it achieved better overall performance on the test set:
* **Accuracy:** 81%
* **Churn F1-Score:** 61%
* **ROC-AUC:** 0.84

The Random Forest implementation remains in the notebook as part of the model comparison process.

---

## 💾 Model Saving
The trained Logistic Regression model and its associated feature columns were saved using **Joblib** to allow the Streamlit application to load them without retraining:
* `models/churn_model.pkl`
* `models/model_columns.pkl`

---

## 🌐 Streamlit Application
An interactive Streamlit application was developed to allow users to enter customer information and receive a real-time churn prediction and probability score.

### Input Features:
* Demographics (Gender, Senior Citizen, Partner, Dependents)
* Services (Phone Service, Internet Service, Online Security, Online Backup, Device Protection, Tech Support, Streaming TV/Movies)
* Account Info (Tenure, Contract Type, Paperless Billing, Payment Method, Monthly Charges, Total Charges)

---

## 📁 Project Structure
```text
customer-churn-ml/
│
├── models/
│   ├── churn_model.pkl
│   └── model_columns.pkl
│
├── notebooks/
│   └── churn_analysis.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/customer-churn-ml.git
cd customer-churn-ml
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application
```bash
streamlit run app.py
```

---

## 🚀 Future Improvements
* Hyperparameter tuning for both models.
* Handling class imbalance (e.g., using SMOTE).
* Testing additional algorithms like XGBoost or LightGBM.
* Adding model explainability using SHAP or LIME.
* Deploying the application online (e.g., Streamlit Community Cloud).
* Generating tailored customer retention recommendations based on predicted churn risk.

---

## 👩‍💻 Author
**Ayesha Gilani**  
*BS Computer Science Student*  
This project was developed as a Machine Learning portfolio project to demonstrate an end-to-end ML workflow from data preprocessing to deployment.
