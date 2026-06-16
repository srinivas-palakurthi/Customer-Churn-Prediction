import streamlit as st

st.title("Customer Churn Prediction")

tenure = st.slider(
    "Customer Tenure",
    1,
    72,
    12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    0,
    5000,
    500
)

if st.button("Predict"):

    if tenure < 12:
        st.error(
            "High Risk of Churn"
        )

    else:
        st.success(
            "Low Risk of Churn"
        )
