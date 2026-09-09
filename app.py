
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/churn_model.pkl")

# Load model feature columns
model_columns = joblib.load("models/model_columns.pkl")

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊"
)

st.title("📊 Customer Churn Prediction")
st.write("Enter customer information to predict the likelihood of churn.")

st.subheader("Customer Information")

senior_citizen = st.selectbox("Senior Citizen", [0, 1])
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=840.0)

gender = st.selectbox("Gender", ["Female", "Male"])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])
phone_service = st.selectbox("Phone Service", ["No", "Yes"])

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["No phone service", "No", "Yes"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["No internet service", "No", "Yes"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["No internet service", "No", "Yes"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["No internet service", "No", "Yes"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["No internet service", "No", "Yes"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["No internet service", "No", "Yes"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["No internet service", "No", "Yes"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ]
)

if st.button("Predict Churn"):

    input_data = pd.DataFrame([{
        "SeniorCitizen": senior_citizen,
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,

        "gender_Male": int(gender == "Male"),
        "Partner_Yes": int(partner == "Yes"),
        "Dependents_Yes": int(dependents == "Yes"),
        "PhoneService_Yes": int(phone_service == "Yes"),

        "MultipleLines_No phone service": int(
            multiple_lines == "No phone service"
        ),
        "MultipleLines_Yes": int(
            multiple_lines == "Yes"
        ),

        "InternetService_Fiber optic": int(
            internet_service == "Fiber optic"
        ),
        "InternetService_No": int(
            internet_service == "No"
        ),

        "OnlineSecurity_No internet service": int(
            online_security == "No internet service"
        ),
        "OnlineSecurity_Yes": int(
            online_security == "Yes"
        ),

        "OnlineBackup_No internet service": int(
            online_backup == "No internet service"
        ),
        "OnlineBackup_Yes": int(
            online_backup == "Yes"
        ),

        "DeviceProtection_No internet service": int(
            device_protection == "No internet service"
        ),
        "DeviceProtection_Yes": int(
            device_protection == "Yes"
        ),

        "TechSupport_No internet service": int(
            tech_support == "No internet service"
        ),
        "TechSupport_Yes": int(
            tech_support == "Yes"
        ),

        "StreamingTV_No internet service": int(
            streaming_tv == "No internet service"
        ),
        "StreamingTV_Yes": int(
            streaming_tv == "Yes"
        ),

        "StreamingMovies_No internet service": int(
            streaming_movies == "No internet service"
        ),
        "StreamingMovies_Yes": int(
            streaming_movies == "Yes"
        ),

        "Contract_One year": int(
            contract == "One year"
        ),
        "Contract_Two year": int(
            contract == "Two year"
        ),

        "PaperlessBilling_Yes": int(
            paperless_billing == "Yes"
        ),

        "PaymentMethod_Credit card (automatic)": int(
            payment_method == "Credit card (automatic)"
        ),
        "PaymentMethod_Electronic check": int(
            payment_method == "Electronic check"
        ),
        "PaymentMethod_Mailed check": int(
            payment_method == "Mailed check"
        )
    }])

    # Make sure columns are in exactly the same order
    # as the columns used during model training.
    input_data = input_data.reindex(
        columns=model_columns,
        fill_value=0
    )

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Get probability of churn
    probability = model.predict_proba(input_data)[0][1]

    if prediction == "Yes":
        st.error("⚠️ Customer is likely to churn.")
    else:
        st.success("✅ Customer is unlikely to churn.")

    st.metric(
        "Churn Probability",
        f"{probability:.2%}"
    )
