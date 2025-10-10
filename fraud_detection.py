### Creating Wed App
import streamlit as st # streamlit creates the interactive web app (UI elements, buttons, inputs).
import pandas as pd
import joblib # load pre-trained pipeline from pkl (store machine learning model)

### Loading the machine leanrning pipeline
model = joblib.load("fraud_detection_pipeline_pkl")

### Designing the web features and input
st.title("Fraud Detection Prediction App")

st.markdown("Please enter the transaction details and use the predict button")

st.divider()

transaction_type = st.selectbox("Transaction Type",["PAYMENT","TRANSFER","CASH_OUT","DEPOSIT"])
amount = st.number_input("Amount",min_value = 0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)",min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)",min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)",min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)",min_value=0.0, value=0.0)

### Define prediction button
if st.button("Predict"):
    input_data = pd.DataFrame({
        "type": [transaction_type],
        "amount": [amount],
        "oldbalanceOrg": [oldbalanceOrg],
        "newbalanceOrig": [newbalanceOrig],
        "oldbalanceDest": [oldbalanceDest],
        "newbalanceDest": [newbalanceDest]
     })
    
    # Conduct prediction and produce output
    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction : '{int(prediction)}'")

    # Print output
    if prediction == 1:
        st.error("This transaction can be fraud.")
    else:
        st.success("This transaction looks like it is not a fraud.")

### Terminal run, streamlit run file name