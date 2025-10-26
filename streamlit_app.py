import streamlit as st
import pickle
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Credit Default Predictor",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    /* Main background */
    .main {
        background-color: #000000;
        padding: 2rem;
    }
    
    /* Content container */
    .block-container {
        background-color: #1a1a1a;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(220, 38, 38, 0.3);
        border: 1px solid #dc2626;
    }
    
    /* All text white by default */
    .main * {
        color: white !important;
    }
    
    /* Header styling */
    h1 {
        color: #dc2626 !important;
        font-size: 3rem !important;
        font-weight: 700 !important;
        text-align: center;
        margin-bottom: 0.5rem !important;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    h2 {
        color: #ff4444 !important;
        font-size: 1.8rem !important;
        margin-top: 2rem !important;
        border-bottom: 2px solid #dc2626;
        padding-bottom: 0.5rem;
    }
    
    h3 {
        color: #ff6666 !important;
        font-size: 1.3rem !important;
    }
    
    /* Description box */
    .description-box {
        background-color: #dc2626;
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1.5rem 0;
        box-shadow: 0 4px 15px rgba(220, 38, 38, 0.4);
        border: 2px solid #ff4444;
    }
    
    /* Input labels */
    label {
        color: white !important;
        font-weight: 500 !important;
    }
    
    /* Sliders and inputs */
    .stSlider > div > div > div {
        background-color: #dc2626 !important;
    }
    
    /* Select boxes */
    .stSelectbox > div > div {
        background-color: #2a2a2a !important;
        color: white !important;
        border: 1px solid #dc2626 !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem 0;
        color: #999;
        border-top: 2px solid #dc2626;
        margin-top: 3rem;
    }
    
    /* Prediction result boxes */
    .stSuccess {
        background-color: #1a1a1a !important;
        border: 2px solid #22c55e !important;
        padding: 1rem;
        border-radius: 10px;
        font-weight: 600;
    }
    
    .stError {
        background-color: #1a1a1a !important;
        border: 2px solid #dc2626 !important;
        padding: 1rem;
        border-radius: 10px;
        font-weight: 600;
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #dc2626 !important;
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
        border-radius: 10px !important;
        border: 2px solid #ff4444 !important;
        width: 100%;
        margin-top: 2rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #ff4444 !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(220, 38, 38, 0.6);
    }
    
    /* Divider */
    hr {
        border-color: #dc2626 !important;
        margin: 2rem 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Define the filename for the pickle file
filename = 'decision_tree_model.pkl'
data_info_filename = 'data_info.pkl'

# Load the model from the pickle file
with open(filename, 'rb') as file:
    model = pickle.load(file)

# Load data info (including expected columns and categorical values)
with open(data_info_filename, 'rb') as file:
    data_info = pickle.load(file)

expected_columns = data_info['expected_columns']
categorical_unique_values = data_info['categorical_unique_values']

# HEADER SECTION
st.markdown("# Credit Default Prediction System")

st.markdown("---")

# MAIN SECTION - Description
st.markdown("""
    <div class="description-box">
        <h2 style="color: white; margin-top: 0;">Predict Loan Default Risk with Confidence</h2>
        <p style="font-size: 1.1rem; line-height: 1.6;">
            Our advanced machine learning model analyzes creditworthiness using the renowned German Credit Dataset. 
            By evaluating key financial indicators—including loan duration, credit history, employment background, 
            and personal financial status—this tool provides accurate predictions of loan default probability. 
            Simply configure your parameters below and receive instant risk assessment to make informed lending decisions. 
            Whether you're a financial institution, credit analyst, or researcher, this tool helps you understand 
            credit risk with precision and clarity.
        </p>
    </div>
""", unsafe_allow_html=True)

# MAIN SECTION - Input Form
st.markdown("## Enter Customer Details")

# Numerical Features Section
st.markdown("### Financial Information")

months_loan_duration = st.slider('Months Loan Duration', min_value=6, max_value=72, value=12)
amount = st.slider('Amount', min_value=250, max_value=18424, value=1000)
percent_of_income = st.slider('Percent of Income', min_value=1, max_value=4, value=2)
years_at_residence = st.slider('Years at Residence', min_value=1, max_value=4, value=2)
age = st.slider('Age', min_value=18, max_value=75, value=30)

st.markdown("---")

# Categorical Features Section
st.markdown("### Categorical Features")

checking_balance = st.selectbox('Checking Balance', categorical_unique_values['checking_balance'])
credit_history = st.selectbox('Credit History', categorical_unique_values['credit_history'])
purpose = st.selectbox('Purpose', categorical_unique_values['purpose'])
savings_balance = st.selectbox('Savings Balance', categorical_unique_values['savings_balance'])
employment_duration = st.selectbox('Employment Duration', categorical_unique_values['employment_duration'])
other_credit = st.selectbox('Other Credit', categorical_unique_values['other_credit'])
housing = st.selectbox('Housing', categorical_unique_values['housing'])
job = st.selectbox('Job', categorical_unique_values['job'])
phone = st.selectbox('Phone', categorical_unique_values['phone'])

# Collect user input into a dictionary
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

# Convert user input to DataFrame
input_df = pd.DataFrame([user_input])

# Apply one-hot encoding
input_encoded = pd.get_dummies(input_df, drop_first=True, dtype=int)

# Ensure all columns from training data are present and in the same order
for col in expected_columns:
    if col not in input_encoded.columns:
        input_encoded[col] = 0
input_encoded = input_encoded[expected_columns]

# Make prediction
if st.button('Predict Default Risk'):
    prediction = model.predict(input_encoded)
    prediction_proba = model.predict_proba(input_encoded)
    
    st.markdown("---")
    st.markdown("## Prediction Results")
    
    if prediction[0] == 0:
        st.success('Prediction: No Default - Low Risk Customer')
        st.markdown(f"**Probability of No Default:** `{prediction_proba[0][0]:.1%}`")
        st.markdown(f"**Probability of Default:** `{prediction_proba[0][1]:.1%}`")
    else:
        st.error('Prediction: Default - High Risk Customer')
        st.markdown(f"**Probability of Default:** `{prediction_proba[0][1]:.1%}`")
        st.markdown(f"**Probability of No Default:** `{prediction_proba[0][0]:.1%}`")

# FOOTER SECTION
st.markdown("""
    <div class="footer">
        <p><strong>Credit Default Prediction System</strong></p>
        <p>Powered by Machine Learning | German Credit Dataset</p>
        <p style="font-size: 0.9rem; color: #999;">Marcello Borromeo | CIS 300 Honors Contract</p>
    </div>
""", unsafe_allow_html=True)
