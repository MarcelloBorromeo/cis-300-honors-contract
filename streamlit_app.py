import streamlit as st
import pickle
import pandas as pd
from PIL import Image

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
        background-color: #0a0a0a;
        padding: 2rem;
    }
    
    /* Content container */
    .block-container {
        background-color: #1a1a1a;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(220, 38, 38, 0.2);
        border: 1px solid #2a2a2a;
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
        color: #ef4444 !important;
        font-size: 1.8rem !important;
        margin-top: 2rem !important;
        border-bottom: 2px solid #dc2626;
        padding-bottom: 0.5rem;
    }
    
    h3 {
        color: #f87171 !important;
        font-size: 1.3rem !important;
        margin-top: 1.5rem !important;
    }
    
    /* Description box */
    .description-box {
        background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin: 1.5rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        border: 2px solid #dc2626;
    }
    
    /* Hero banner */
    .hero-banner {
        background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 6px 20px rgba(220, 38, 38, 0.4);
    }
    
    /* Image containers */
    .image-container {
        border-radius: 10px;
        overflow: hidden;
        border: 2px solid #3a3a3a;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    
    /* Input labels */
    label {
        color: #d1d5db !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
    }
    
    /* Sliders */
    .stSlider > div > div > div {
        background-color: #dc2626 !important;
    }
    
    .stSlider > div > div > div > div {
        background-color: #ef4444 !important;
    }
    
    /* Select boxes */
    .stSelectbox > div > div {
        background-color: #2a2a2a !important;
        color: white !important;
        border: 1px solid #3a3a3a !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem 0;
        color: #6b7280;
        border-top: 2px solid #dc2626;
        margin-top: 3rem;
    }
    
    /* Prediction result boxes */
    .stSuccess {
        background-color: #1a1a1a !important;
        border: 2px solid #10b981 !important;
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
        background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%) !important;
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
        border-radius: 10px !important;
        border: 2px solid #dc2626 !important;
        width: 100%;
        margin-top: 2rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #ef4444 0%, #b91c1c 100%) !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(220, 38, 38, 0.6);
        border-color: #ef4444 !important;
    }
    
    /* Divider */
    hr {
        border-color: #3a3a3a !important;
        margin: 2rem 0 !important;
    }
    
    /* Results card */
    .results-card {
        background-color: #2a2a2a;
        border: 2px solid #3a3a3a;
        border-radius: 10px;
        padding: 1.5rem;
        margin-top: 1rem;
    }
    
    .success-card {
        border-color: #10b981 !important;
        background: linear-gradient(135deg, #1a1a1a 0%, #064e3b 100%);
    }
    
    .error-card {
        border-color: #dc2626 !important;
        background: linear-gradient(135deg, #1a1a1a 0%, #450a0a 100%);
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

# Load and display images
try:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        default_img = Image.open('default_image.jpeg')
        st.image(default_img, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        loan_img = Image.open('loan_image.jpeg')
        st.image(loan_img, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        euro_img = Image.open('euro_image.jpeg')
        st.image(euro_img, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
except:
    pass  # If images aren't found, continue without them

st.markdown("---")

# MAIN SECTION - Description
st.markdown("""
    <div class="description-box">
        <h2 style="color: #ef4444; margin-top: 0;">Predict Loan Default Risk with Confidence</h2>
        <p style="font-size: 1.1rem; line-height: 1.6; color: #d1d5db;">
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
        st.markdown('<div class="results-card success-card">', unsafe_allow_html=True)
        st.success('Prediction: No Default - Low Risk Customer')
        st.markdown(f"<p style='font-size: 1.1rem;'><strong>Probability of No Default:</strong> <span style='color: #10b981; font-size: 1.3rem;'>{prediction_proba[0][0]:.1%}</span></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 1.1rem;'><strong>Probability of Default:</strong> <span style='color: #6b7280;'>{prediction_proba[0][1]:.1%}</span></p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="results-card error-card">', unsafe_allow_html=True)
        st.error('Prediction: Default - High Risk Customer')
        st.markdown(f"<p style='font-size: 1.1rem;'><strong>Probability of Default:</strong> <span style='color: #dc2626; font-size: 1.3rem;'>{prediction_proba[0][1]:.1%}</span></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 1.1rem;'><strong>Probability of No Default:</strong> <span style='color: #6b7280;'>{prediction_proba[0][0]:.1%}</span></p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# FOOTER SECTION
st.markdown("""
    <div class="footer">
        <p style="color: #9ca3af;"><strong>Credit Default Prediction System</strong></p>
        <p style="color: #6b7280;">Powered by Machine Learning | German Credit Dataset</p>
        <p style="font-size: 0.95rem; color: #9ca3af; margin-top: 1rem;">Marcello Borromeo | CIS 300 Honors Contract</p>
    </div>
""", unsafe_allow_html=True)
