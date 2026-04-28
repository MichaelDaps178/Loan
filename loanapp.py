import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("my_model.pkl", "rb"))

def main():
    st.title("Loan Approval Prediction")

    # User inputs
    fico = st.number_input("FICO Score", min_value=300, max_value=850)
    income = st.number_input("Monthly Income", min_value=0)
    housing = st.number_input("Monthly Housing Payment", min_value=0)
    loan = st.number_input("Loan Amount", min_value=0)

    employment_status = st.selectbox("Employment Status", ["Employed", "Unemployed"])
    employment_sector = st.selectbox("Employment Sector", ["Private", "Public"])
    reason = st.selectbox("Loan Reason", ["Debt Consolidation", "Home", "Other"])
    lender = st.selectbox("Lender", ["A", "B", "C"])
    bankrupt = st.selectbox("Ever Bankrupt?", ["Yes", "No"])
    bankrupt = 1 if bankrupt == "Yes" else 0

    # Predict button
    if st.button("Predict"):
        input_data = pd.DataFrame([{
            "FICO_score": fico,
            "Monthly_Gross_Income": income,
            "Monthly_Housing_Payment": housing,
            "Granted_Loan_Amount": loan,
            "Employment_Status": employment_status,
            "Employment_Sector": employment_sector,
            "Reason": reason,
            "Lender": lender,
            "Ever_Bankrupt_or_Foreclose": bankrupt
        }])

        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.success("Loan Approved")
        else:
            st.error("Loan Denied")


if __name__ == "__main__":
    main()