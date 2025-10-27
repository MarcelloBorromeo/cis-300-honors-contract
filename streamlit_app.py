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
    /* Main background with gradient */
    .main {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        padding: 0 !important;
    }
    
    /* Content container with larger horizontal margins */
    .block-container {
        max-width: 1400px;
        padding: 3rem 6rem !important;
        margin: 0 auto;
    }
    
    /* All text white by default */
    .main * {
        color: white !important;
    }
    
    /* HEADER SECTION */
    .header-section {
        background: linear-gradient(135deg, #dc2626 0%, #7c2d12 50%, #991b1b 100%);
        padding: 3rem 6rem;
        margin: 0 -6rem 3rem -6rem;
        border-bottom: 4px solid #fbbf24;
        box-shadow: 0 8px 32px rgba(220, 38, 38, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .header-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="grid" width="100" height="100" patternUnits="userSpaceOnUse"><path d="M 100 0 L 0 0 0 100" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
        opacity: 0.3;
    }
    
    .header-section h1 {
        position: relative;
        z-index: 1;
    }
    
    /* Header styling */
    h1 {
        color: #fbbf24 !important;
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        text-align: center;
        margin: 0 !important;
        text-transform: uppercase;
        letter-spacing: 3px;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.5);
    }
    
    /* NAVIGATION SECTION */
    .navigation-section {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        padding: 1.5rem 6rem;
        margin: 0 -6rem 3rem -6rem;
        border-bottom: 2px solid #3b82f6;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    
    .nav-content {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 2rem;
    }
    
    .nav-item {
        color: #93c5fd !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        transition: all 0.3s ease;
        text-decoration: none;
    }
    
    .nav-item:hover {
        background-color: rgba(59, 130, 246, 0.2);
        color: #60a5fa !important;
    }
    
    /* MAIN SECTION */
    .main-section {
        background: linear-gradient(135deg, #1a1a2e 0%, #2d2d44 100%);
        border-radius: 20px;
        padding: 3rem;
        margin-bottom: 3rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        border: 2px solid #3b82f6;
    }
    
    h2 {
        color: #fbbf24 !important;
        font-size: 2rem !important;
        margin-top: 0 !important;
        margin-bottom: 1.5rem !important;
        border-bottom: 3px solid #dc2626;
        padding-bottom: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    
    h3 {
        color: #60a5fa !important;
        font-size: 1.5rem !important;
        margin-top: 2rem !important;
        margin-bottom: 1rem !important;
        padding-left: 1rem;
        border-left: 4px solid #3b82f6;
    }
    
    /* Description box */
    .description-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 6px 24px rgba(59, 130, 246, 0.3);
        border: 2px solid #3b82f6;
        position: relative;
        overflow: hidden;
    }
    
    .description-box::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.1) 0%, transparent 70%);
    }
    
    .description-box h2 {
        border-bottom: 3px solid #fbbf24 !important;
    }
    
    /* Image containers */
    .image-container {
        border-radius: 15px;
        overflow: hidden;
        border: 3px solid #3b82f6;
        box-shadow: 0 6px 24px rgba(59, 130, 246, 0.4);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        padding: 0.5rem;
    }
    
    .image-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 32px rgba(59, 130, 246, 0.6);
    }
    
    /* Input labels */
    label {
        color: #93c5fd !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Sliders */
    .stSlider > div > div > div {
        background-color: #3b82f6 !important;
    }
    
    .stSlider > div > div > div > div {
        background-color: #60a5fa !important;
    }
    
    /* Number inputs */
    .stNumberInput > div > div > input {
        background-color: #1e293b !important;
        color: white !important;
        border: 2px solid #3b82f6 !important;
        border-radius: 8px !important;
    }
    
    /* Select boxes */
    .stSelectbox > div > div {
        background-color: #1e293b !important;
        color: white !important;
        border: 2px solid #3b82f6 !important;
        border-radius: 8px !important;
    }
    
    /* Input fields section */
    .input-section {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 1.5rem 0;
        border: 2px solid #475569;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
    }
    
    /* FOOTER SECTION */
    .footer-section {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 100%);
        padding: 2.5rem 6rem;
        margin: 3rem -6rem 0 -6rem;
        border-top: 4px solid #fbbf24;
        box-shadow: 0 -8px 32px rgba(251, 191, 36, 0.2);
    }
    
    .footer {
        text-align: center;
        color: #93c5fd;
    }
    
    .footer p {
        margin: 0.5rem 0;
    }
    
    /* Prediction result boxes */
    .results-section {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        border-radius: 20px;
        padding: 3rem;
        margin-top: 3rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        border: 3px solid #3b82f6;
    }
    
    .results-card {
        background-color: #1e293b;
        border: 3px solid #475569;
        border-radius: 15px;
        padding: 2rem;
        margin-top: 1.5rem;
        box-shadow: 0 6px 24px rgba(0, 0, 0, 0.3);
    }
    
    .success-card {
        border-color: #10b981 !important;
        background: linear-gradient(135deg, #064e3b 0%, #065f46 100%);
        box-shadow: 0 6px 24px rgba(16, 185, 129, 0.4);
    }
    
    .error-card {
        border-color: #dc2626 !important;
        background: linear-gradient(135deg, #7f1d1d 0%, #991b1b 100%);
        box-shadow: 0 6px 24px rgba(220, 38, 38, 0.4);
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #dc2626 0%, #7c2d12 50%, #991b1b 100%) !important;
        color: #fbbf24 !important;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        padding: 1rem 3rem !important;
        border-radius: 15px !important;
        border: 3px solid #fbbf24 !important;
        width: 100%;
        margin-top: 2rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.3s ease;
        box-shadow: 0 6px 24px rgba(220, 38, 38, 0.4);
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #ef4444 0%, #92400e 50%, #b91c1c 100%) !important;
        transform: translateY(-3px);
        box-shadow: 0 12px 32px rgba(251, 191, 36, 0.6);
        border-color: #fcd34d !important;
    }
    
    /* Divider */
    hr {
        border: none !important;
        height: 2px !important;
        background: linear-gradient(90deg, transparent, #3b82f6, transparent) !important;
        margin: 2.5rem 0 !important;
    }
    
    /* Success/Error messages */
    .stSuccess, .stError {
        background-color: transparent !important;
        border: none !important;
        padding: 0 !important;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
    }
    
    /* Probability text styling */
    .prob-text {
        font-size: 1.2rem;
        margin: 1rem 0;
        padding: 1rem;
        background-color: rgba(0, 0, 0, 0.3);
        border-radius: 10px;
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

# ============================================
# HEADER SECTION
# ============================================
st.markdown("""
    <div class="header-section">
        <h1>Credit Default Prediction Tool</h1>
    </div>
""", unsafe_allow_html=True)

# ============================================
# NAVIGATION SECTION
# ============================================
st.markdown("""
    <div class="navigation-section">
        <div class="nav-content">
            <span class="nav-item">🏠 Home</span>
            <span class="nav-item">📊 Predict</span>
            <span class="nav-item">📈 Analytics</span>
            <span class="nav-item">ℹ️ About</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# ============================================
# MAIN SECTION
# ============================================

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

# Description
st.markdown("""
    <div class="description-box">
        <h2>Predict Loan Default Risk with Confidence!</h2>
        <p style="font-size: 1.15rem; line-height: 1.8; color: #e5e7eb;">
            This machine learning model brings the renowned German Credit Dataset to life — analyzing the creditworthiness of German citizens with data-driven precision.
By digging into key financial details like loan duration, credit history, employment background, and personal finances, it predicts the probability of loan default with remarkable accuracy.
Just tweak the parameters below and watch as real-time insights unfold, giving you an instant risk profile to power smarter lending decisions!
Whether you’re a financial institution assessing applicants, a credit analyst exploring trends, or a researcher experimenting with predictive modeling, this tool transforms credit risk analysis into an engaging, intuitive experience.
        </p>
    </div>
""", unsafe_allow_html=True)

# Input Form
st.markdown('<div class="main-section">', unsafe_allow_html=True)
st.markdown("## 📝 Enter Customer Details")

# Numerical Features Section
st.markdown('<div class="input-section">', unsafe_allow_html=True)
st.markdown("### 💰 Financial Information")

months_loan_duration = st.slider('Months Loan Duration', min_value=6, max_value=72, value=12)
amount = st.slider('Amount', min_value=250, max_value=18424, value=1000)
percent_of_income = st.slider('Percent of Income', min_value=1, max_value=4, value=2)
years_at_residence = st.slider('Years at Residence', min_value=1, max_value=4, value=2)
age = st.slider('Age', min_value=18, max_value=75, value=30)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Categorical Features Section
st.markdown('<div class="input-section">', unsafe_allow_html=True)
st.markdown("### 📋 Categorical Features")

col1, col2, col3 = st.columns(3)

with col1:
    checking_balance = st.selectbox('Checking Balance', categorical_unique_values['checking_balance'])
    credit_history = st.selectbox('Credit History', categorical_unique_values['credit_history'])
    purpose = st.selectbox('Purpose', categorical_unique_values['purpose'])

with col2:
    savings_balance = st.selectbox('Savings Balance', categorical_unique_values['savings_balance'])
    employment_duration = st.selectbox('Employment Duration', categorical_unique_values['employment_duration'])
    other_credit = st.selectbox('Other Credit', categorical_unique_values['other_credit'])

with col3:
    housing = st.selectbox('Housing', categorical_unique_values['housing'])
    job = st.selectbox('Job', categorical_unique_values['job'])
    phone = st.selectbox('Phone', categorical_unique_values['phone'])

st.markdown('</div>', unsafe_allow_html=True)

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
if st.button('🔮 Predict Default Risk'):
    prediction = model.predict(input_encoded)
    prediction_proba = model.predict_proba(input_encoded)
    
    st.markdown('<div class="results-section">', unsafe_allow_html=True)
    st.markdown("## 📊 Prediction Results")
    
    if prediction[0] == 0:
        st.markdown('<div class="results-card success-card">', unsafe_allow_html=True)
        st.success('✅ Prediction: No Default - Low Risk Customer')
        st.markdown(f"""
            <div class="prob-text">
                <strong>Probability of No Default:</strong> 
                <span style='color: #10b981; font-size: 1.5rem; font-weight: 800;'>{prediction_proba[0][0]:.1%}</span>
            </div>
            <div class="prob-text">
                <strong>Probability of Default:</strong> 
                <span style='color: #6b7280;'>{prediction_proba[0][1]:.1%}</span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="results-card error-card">', unsafe_allow_html=True)
        st.error('⚠️ Prediction: Default - High Risk Customer')
        st.markdown(f"""
            <div class="prob-text">
                <strong>Probability of Default:</strong> 
                <span style='color: #fca5a5; font-size: 1.5rem; font-weight: 800;'>{prediction_proba[0][1]:.1%}</span>
            </div>
            <div class="prob-text">
                <strong>Probability of No Default:</strong> 
                <span style='color: #6b7280;'>{prediction_proba[0][0]:.1%}</span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# FOOTER SECTION
# ============================================
st.markdown("""
    <div class="footer-section">
        <div class="footer">
            <p style="color: #fbbf24; font-size: 1.3rem; font-weight: 700;">💳 Credit Default Prediction System</p>
            <p style="color: #93c5fd; font-size: 1.1rem;">Powered by Machine Learning | German Credit Dataset</p>
            <p style="font-size: 1rem; color: #60a5fa; margin-top: 1.5rem;">Marcello Borromeo | CIS 300 Honors Contract</p>
        </div>
    </div>
""", unsafe_allow_html=True)
