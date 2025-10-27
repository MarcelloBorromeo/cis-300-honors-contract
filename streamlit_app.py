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

# --- Enhanced Aesthetic Styling (Terracotta Theme) ---
st.markdown("""
    <style>
    /* === GLOBAL BACKGROUND === */
    .stApp {
        background-color: #E2725B !important; /* Terracotta */
        background-image: none !important;
    }

    /* === MAIN LAYOUT === */
    .main, .block-container {
        background: transparent !important;
    }

    /* === TYPOGRAPHY === */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
        color: #ffffff !important;
    }

    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 700 !important;
        text-align: center;
        text-shadow: 0 1px 4px rgba(0,0,0,0.2);
    }

    /* === INPUT SECTIONS === */
    .section-container {
        background-color: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 16px;
        padding: 2rem;
        margin-top: 1.5rem;
        backdrop-filter: blur(6px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }

    .section-container h3 {
        color: #ffffff !important;
        text-align: left !important;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    /* === SLIDERS + LABELS === */
    .stSlider label, .stSelectbox label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* Stack sliders vertically */
    div[data-testid="stHorizontalBlock"] {
        flex-direction: column !important;
    }

    /* === BUTTON === */
    .stButton>button {
        background: linear-gradient(135deg, #008080, #00a0a0);
        color: white !important;
        font-size: 1.2rem;
        font-weight: 600;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        width: 100%;
        border: none;
        box-shadow: 0 4px 12px rgba(0,128,128,0.4);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #00a0a0, #008080);
        transform: translateY(-2px);
        box-shadow: 0 8px 18px rgba(0,128,128,0.5);
    }

    /* === DESCRIPTION BOX === */
    .description-box {
        background-color: #008080;
        color: white;
        padding: 1.5rem 2rem;
        border-radius: 16px;
        margin: 2rem 0;
        box-shadow: 0 6px 18px rgba(0,0,0,0.25);
        line-height: 1.6;
    }

    /* === RESULT BOXES === */
    .result-card {
        background-color: rgba(255,255,255,0.1);
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
        text-align: center;
        color: white;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }

    .footer {
        text-align: center;
        color: rgba(255,255,255,0.8);
        padding: 2rem 0;
        border-top: 1px solid rgba(255,255,255,0.3);
        margin-top: 3rem;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOAD MODEL ---
filename = 'decision_tree_model.pkl'
data_info_filename = 'data_info.pkl'

with open(filename, 'rb') as file:
    model = pickle.load(file)

with open(data_info_filename, 'rb') as file:
    data_info = pickle.load(file)

expected_columns = data_info['expected_columns']
categorical_unique_values = data_info['categorical_unique_values']

# --- HEADER ---
st.markdown("<h1>💳 Credit Default Prediction System</h1>", unsafe_allow_html=True)

# --- DESCRIPTION ---
st.markdown("""
    <div class="description-box">
        <h2>🎯 Predict Loan Default Risk with Confidence</h2>
        <p>
            Our advanced machine learning model uses the renowned German Credit Dataset 
            to evaluate key financial indicators such as loan duration, income ratio, and 
            credit history. Simply input your data to receive an instant risk analysis and 
            make more informed lending decisions with confidence.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- INPUT FORM ---
st.markdown('<div class="section-container">', unsafe_allow_html=True)
st.markdown("### 📝 Customer Financial Details")

# All sliders stacked vertically (no columns)
months_loan_duration = st.slider('🗓️ Months Loan Duration', 6, 72, 12)
amount = st.slider('💵 Amount', 250, 18424, 1000)
percent_of_income = st.slider('📊 Percent of Income', 1, 4, 2)
years_at_residence = st.slider('🏠 Years at Residence', 1, 4, 2)
age = st.slider('👤 Age', 18, 75, 30)
st.markdown('</div>', unsafe_allow_html=True)

# --- CATEGORICAL INPUTS ---
st.markdown('<div class="section-container">', unsafe_allow_html=True)
st.markdown("### 📋 Categorical Features")

checking_balance = st.selectbox('💳 Checking Balance', categorical_unique_values['checking_balance'])
credit_history = st.selectbox('📜 Credit History', categorical_unique_values['credit_history'])
purpose = st.selectbox('🎯 Purpose', categorical_unique_values['purpose'])
savings_balance = st.selectbox('💰 Savings Balance', categorical_unique_values['savings_balance'])
employment_duration = st.selectbox('💼 Employment Duration', categorical_unique_values['employment_duration'])
other_credit = st.selectbox('🏦 Other Credit', categorical_unique_values['other_credit'])
housing = st.selectbox('🏡 Housing', categorical_unique_values['housing'])
job = st.selectbox('👔 Job', categorical_unique_values['job'])
phone = st.selectbox('📞 Phone', categorical_unique_values['phone'])
st.markdown('</div>', unsafe_allow_html=True)

# --- DATA PREP ---
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
for col in expected_columns:
    if col not in input_encoded.columns:
        input_encoded[col] = 0
input_encoded = input_encoded[expected_columns]

# --- PREDICTION ---
if st.button('🔮 Predict Default Risk'):
    prediction = model.predict(input_encoded)
    prediction_proba = model.predict_proba(input_encoded)

    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown("### 📊 Prediction Results")

    if prediction[0] == 0:
        st.markdown("""
            <div class="result-card" style="border-left: 5px solid #00c9a7;">
                <h3>✅ No Default - Low Risk</h3>
                <p><b>Probability of No Default:</b> {:.1%}</p>
                <p><b>Probability of Default:</b> {:.1%}</p>
            </div>
        """.format(prediction_proba[0][0], prediction_proba[0][1]), unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="result-card" style="border-left: 5px solid #ffb3a7;">
                <h3>⚠️ Default Likely - High Risk</h3>
                <p><b>Probability of Default:</b> {:.1%}</p>
                <p><b>Probability of No Default:</b> {:.1%}</p>
            </div>
        """.format(prediction_proba[0][1], prediction_proba[0][0]), unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        <p><strong>Credit Default Prediction System</strong></p>
        <p>Powered by Machine Learning | German Credit Dataset</p>
        <p>© 2025 | Built with Streamlit 🎈</p>
    </div>
""", unsafe_allow_html=True)
