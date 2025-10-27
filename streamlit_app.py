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

# === Custom CSS for Black Theme ===
st.markdown("""
    <style>
    /* === GLOBAL BACKGROUND === */
    .stApp {
        background-color: #000000 !important; /* solid black background */
        background-image: none !important;
    }

    /* Remove Streamlit's white content background */
    .main, .block-container {
        background: transparent !important;
        color: #FFFFFF !important;
    }

    /* === CONTENT CONTAINER === */
    .block-container {
        background-color: #121212; /* dark gray card background */
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 10px rgba(255, 255, 255, 0.05);
    }

    /* === HEADERS === */
    h1 {
        color: #4FC3F7; /* light teal-blue */
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        text-align: center;
        margin-bottom: 0.5rem !important;
    }

    h2 {
        color: #81D4FA;
        font-size: 1.8rem !important;
        margin-top: 2rem !important;
    }

    h3 {
        color: #4FC3F7;
        font-size: 1.3rem !important;
    }

    /* === DESCRIPTION BOX === */
    .description-box {
        background: linear-gradient(135deg, #0D47A1 0%, #1976D2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1.5rem 0;
        box-shadow: 0 6px 15px rgba(0,0,0,0.5);
    }

    /* === FOOTER === */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem 0;
        color: #AAA;
        border-top: 1px solid #333;
        margin-top: 3rem;
    }

    /* === BUTTONS === */
    .stButton>button {
        background: linear-gradient(135deg, #1565C0 0%, #1E88E5 100%);
        color: white;
        font-size: 1.2rem;
        font-weight: 600;
        padding: 0.75rem 2rem;
        border-radius: 10px;
        border: none;
        width: 100%;
        margin-top: 2rem;
        box-shadow: 0 4px 12px rgba(30,136,229,0.3);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(30,136,229,0.6);
    }

    /* === SUCCESS/ERROR BOXES === */
    .stSuccess, .stError {
        padding: 1rem;
        border-radius: 10px;
        font-weight: 600;
        background-color: #121212 !important;
        color: #FFFFFF !important;
    }

    /* === TEXT + LABELS === */
    label, p, .stMarkdown, .stSelectbox, .stSlider {
        color: #EEEEEE !important;
    }

    /* === SLIDER TRACK COLOR === */
    div[data-baseweb="slider"] > div {
        background-color: #4FC3F7 !important;
    }

    /* === REMOVE EXCESS WHITE SPACE === */
    header, footer {visibility: hidden !important;}
    </style>
""", unsafe_allow_html=True)

# === MODEL LOADING ===
filename = 'decision_tree_model.pkl'
data_info_filename = 'data_info.pkl'

with open(filename, 'rb') as file:
    model = pickle.load(file)

with open(data_info_filename, 'rb') as file:
    data_info = pickle.load(file)

expected_columns = data_info['expected_columns']
categorical_unique_values = data_info['categorical_unique_values']

# === HEADER ===
st.markdown("# 💳 Credit Default Prediction System")

# === NAVIGATION BAR ===
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.markdown("### 📊 Model")
with col2:
    st.markdown("### 🔍 Analysis")
with col3:
    st.markdown("### ℹ️ About")

st.markdown("---")

# === DESCRIPTION ===
st.markdown("""
    <div class="description-box">
        <h2 style="color: white; margin-top: 0;">🎯 Predict Loan Default Risk with Confidence</h2>
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

# === INPUT FORM ===
st.markdown("## 📝 Enter Customer Details")

st.markdown("### 💰 Financial Information")
col1, col2 = st.columns(2)

with col1:
    months_loan_duration = st.slider('🗓️ Months Loan Duration', min_value=6, max_value=72, value=12)
    amount = st.slider('💵 Amount', min_value=250, max_value=18424, value=1000)
    percent_of_income = st.slider('📊 Percent of Income', min_value=1, max_value=4, value=2)

with col2:
    years_at_residence = st.slider('🏠 Years at Residence', min_value=1, max_value=4, value=2)
    age = st.slider('👤 Age', min_value=18, max_value=75, value=30)

st.markdown("---")

st.markdown("### 📋 Categorical Features")
col1, col2, col3 = st.columns(3)

with col1:
    checking_balance = st.selectbox('💳 Checking Balance', categorical_unique_values['checking_balance'])
    credit_history = st.selectbox('📜 Credit History', categorical_unique_values['credit_history'])
    purpose = st.selectbox('🎯 Purpose', categorical_unique_values['purpose'])

with col2:
    savings_balance = st.selectbox('💰 Savings Balance', categorical_unique_values['savings_balance'])
    employment_duration = st.selectbox('💼 Employment Duration', categorical_unique_values['employment_duration'])
    other_credit = st.selectbox('🏦 Other Credit', categorical_unique_values['other_credit'])

with col3:
    housing = st.selectbox('🏡 Housing', categorical_unique_values['housing'])
    job = st.selectbox('👔 Job', categorical_unique_values['job'])
    phone = st.selectbox('📞 Phone', categorical_unique_values['phone'])

# === INPUT DATAFRAME ===
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

# === ONE-HOT ENCODING ===
input_encoded = pd.get_dummies(input_df, drop_first=True, dtype=int)

for col in expected_columns:
    if col not in input_encoded.columns:
        input_encoded[col] = 0

input_encoded = input_encoded[expected_columns]

# === PREDICTION ===
if st.button('🔮 Predict Default Risk'):
    prediction = model.predict(input_encoded)
    prediction_proba = model.predict_proba(input_encoded)
    
    st.markdown("---")
    st.markdown("## 📊 Prediction Results")
    
    result_col1, result_col2 = st.columns([2, 1])
    
    with result_col1:
        if prediction[0] == 0:
            st.success('✅ Prediction: No Default - Low Risk Customer')
            st.markdown(f"**Probability of No Default:** `{prediction_proba[0][0]:.1%}`")
            st.markdown(f"**Probability of Default:** `{prediction_proba[0][1]:.1%}`")
        else:
            st.error('⚠️ Prediction: Default - High Risk Customer')
            st.markdown(f"**Probability of Default:** `{prediction_proba[0][1]:.1%}`")
            st.markdown(f"**Probability of No Default:** `{prediction_proba[0][0]:.1%}`")
    
    with result_col2:
        if prediction[0] == 0:
            st.markdown("""
                <div style="background-color: #1B5E20; padding: 2rem; border-radius: 10px; text-align: center;">
                    <h1 style="color: #C8E6C9; font-size: 4rem; margin: 0;">✓</h1>
                    <p style="color: #C8E6C9; font-weight: 600; margin: 0;">APPROVED</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="background-color: #B71C1C; padding: 2rem; border-radius: 10px; text-align: center;">
                    <h1 style="color: #FFCDD2; font-size: 4rem; margin: 0;">✗</h1>
                    <p style="color: #FFCDD2; font-weight: 600; margin: 0;">DECLINED</p>
                </div>
            """, unsafe_allow_html=True)

# === FOOTER ===
st.markdown("""
    <div class="footer">
        <p><strong>Credit Default Prediction System</strong></p>
        <p>Powered by Machine Learning | German Credit Dataset</p>
        <p style="font-size: 0.9rem; color: #888;">© 2025 | Built with Streamlit 🎈</p>
    </div>
""", unsafe_allow_html=True)
