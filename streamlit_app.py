import streamlit as st
import pickle
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Credit Default Prediction", layout="centered")

# --- LOAD MODEL AND DATA INFO ---
filename = 'decision_tree_model.pkl'
data_info_filename = 'data_info.pkl'

with open(filename, 'rb') as file:
    model = pickle.load(file)

with open(data_info_filename, 'rb') as file:
    data_info = pickle.load(file)

expected_columns = data_info['expected_columns']
categorical_unique_values = data_info['categorical_unique_values']

# --- TITLE SECTION ---
st.markdown(
    """
    <h1 style='text-align: center;'>Credit Default Prediction</h1>
    """,
    unsafe_allow_html=True
)

# --- DISPLAY IMAGE ---
st.image("loan.jpeg", use_container_width=True)

# --- TUTORIAL BUTTON (UPPER RIGHT) ---
st.markdown(
    """
    <style>
    .floating-btn {
        position: fixed;
        top: 25px;
        right: 30px;
        background-color: #FF0000;
        color: white;
        border: none;
        padding: 10px 16px;
        border-radius: 8px;
        font-size: 14px;
        cursor: pointer;
        z-index: 9999;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("🎓 Tutorial", key="tutorial_btn", help="Open the tutorial page"):
    st.switch_page("Tutorial")

# --- ABOUT SECTION ---
st.header("About This Tool")
st.markdown(
    """
    <div style='background-color:#2c2c2c; color:white; padding:18px; border-radius:10px; border:1px solid #444; text-align:justify; font-size:16px;'>
    Our advanced machine learning model analyzes creditworthiness using the renowned <b>German Credit Dataset</b>. 
    By evaluating key financial indicators—including loan duration, credit history, employment background, 
    and personal financial status—this tool provides accurate predictions of loan default probability. 
    Simply configure your parameters below and receive instant risk assessment to make informed lending decisions. 
    Whether you're a financial institution, credit analyst, or researcher, this tool helps you understand 
    credit risk with precision and clarity.
    </div>
    """,
    unsafe_allow_html=True
)

# --- INPUT SECTION ---
st.header('Enter Customer Details')

# --- NUMERICAL FEATURES ---
months_loan_duration = st.slider('Months Loan Duration', min_value=6, max_value=72, value=12)
amount = st.slider('Amount', min_value=250, max_value=18424, value=1000)
percent_of_income = st.slider('Percent of Income', min_value=1, max_value=4, value=2)
years_at_residence = st.slider('Years at Residence', min_value=1, max_value=4, value=2)
age = st.slider('Age', min_value=18, max_value=75, value=30)

# --- CATEGORICAL FEATURES ---
st.subheader('Categorical Features')
checking_balance = st.selectbox('Checking Balance', categorical_unique_values['checking_balance'])
credit_history = st.selectbox('Credit History', categorical_unique_values['credit_history'])
purpose = st.selectbox('Purpose', categorical_unique_values['purpose'])
savings_balance = st.selectbox('Savings Balance', categorical_unique_values['savings_balance'])
employment_duration = st.selectbox('Employment Duration', categorical_unique_values['employment_duration'])
other_credit = st.selectbox('Other Credit', categorical_unique_values['other_credit'])
housing = st.selectbox('Housing', categorical_unique_values['housing'])
job = st.selectbox('Job', categorical_unique_values['job'])
phone = st.selectbox('Phone', categorical_unique_values['phone'])

# --- DATA PROCESSING ---
user_input = {
    'months_loan_duration': months_loan_duration,
    'amount': amount,
    'percent_of_income': percent_of_income,
    'years_at_residence': years_at_residence,
    'age': age,
    'checking_balance': checking_balance,
    'credit_history': credit_history,
    'purpose': purpose,
    'savings_balance': savings_balance,
    'employment_duration': employment_duration,
    'other_credit': other_credit,
    'housing': housing,
    'job': job,
    'phone': phone,
    'existing_loans_count': 1,
    'dependents': 1
}

input_df = pd.DataFrame([user_input])
input_encoded = pd.get_dummies(input_df, drop_first=True, dtype=int)

# Ensure all expected columns are present
for col in expected_columns:
    if col not in input_encoded.columns:
        input_encoded[col] = 0

input_encoded = input_encoded[expected_columns]

# --- PREDICTION ---
if st.button('Predict'):
    prediction = model.predict(input_encoded)
    prediction_proba = model.predict_proba(input_encoded)

    st.subheader('Prediction Result:')
    if prediction[0] == 0:
        st.success('Prediction: No Default')
        st.write(f'Probability of No Default: {prediction_proba[0][0]:.2f}')
        st.write(f'Probability of Default: {prediction_proba[0][1]:.2f}')
    else:
        st.error('Prediction: Default')
        st.write(f'Probability of Default: {prediction_proba[0][1]:.2f}')
        st.write(f'Probability of No Default: {prediction_proba[0][0]:.2f}')

# --- FOOTER ---
st.markdown(
    """
    <hr style="border:1px solid #444; margin-top:40px; margin-bottom:10px;">
    <p style="text-align:center; color:gray; font-size:14px;">
    © Marcello Borromeo | CIS 300 Honors Contract
    </p>
    """,
    unsafe_allow_html=True
)
