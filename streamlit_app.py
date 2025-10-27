import streamlit as st
import pickle
import pandas as pd
from PIL import Image
# Page configuration
st.set_page_config(
    page_title="Credit Default Predictor",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Custom CSS for styling
st.markdown("""
  import streamlit as st import pickle import pandas as pd from PIL import Image # Page configuration st.set_page_config( page_title="Credit Default Predictor", layout="wide", initial_sidebar_state="expanded" ) # Custom CSS for styling st.markdown(""" <style> /* Import modern font */ @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap'); /* Main background with gradient */ .main { background: linear-gradient(180deg, #0a0a0a 0%, #1a0505 50%, #0a0a0a 100%); padding: 2rem; font-family: 'Inter', sans-serif; } /* Content container */ .block-container { background: linear-gradient(135deg, #1a1a1a 0%, #2a1a1a 100%); border-radius: 20px; padding: 3rem; box-shadow: 0 8px 32px rgba(220, 38, 38, 0.3), 0 0 80px rgba(220, 38, 38, 0.1); border: 1px solid rgba(220, 38, 38, 0.3); backdrop-filter: blur(10px); } /* All text white by default */ .main * { color: white !important; } /* Header styling - ALL WHITE */ h1 { color: #ffffff !important; font-size: 3.5rem !important; font-weight: 700 !important; text-align: center; margin-bottom: 1rem !important; text-transform: uppercase; letter-spacing: 3px; text-shadow: 0 0 30px rgba(220, 38, 38, 0.5); } h2 { color: #ffffff !important; font-size: 2rem !important; margin-top: 2.5rem !important; border-bottom: 3px solid #dc2626; padding-bottom: 0.8rem; font-weight: 600 !important; text-shadow: 0 0 20px rgba(220, 38, 38, 0.3); } h3 { color: #ffffff !important; font-size: 1.5rem !important; margin-top: 2rem !important; font-weight: 600 !important; position: relative; padding-left: 20px; } h3:before { content: ''; position: absolute; left: 0; top: 50%; transform: translateY(-50%); width: 4px; height: 24px; background: linear-gradient(180deg, #dc2626 0%, #ef4444 100%); border-radius: 2px; } /* Description box */ .description-box { background: linear-gradient(135deg, #2a1a1a 0%, #1a1a1a 100%); color: white; padding: 2.5rem; border-radius: 15px; margin: 2rem 0; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4), inset 0 0 0 2px rgba(220, 38, 38, 0.3); border: 2px solid transparent; background-clip: padding-box; position: relative; overflow: hidden; } .description-box:before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #dc2626 0%, #ef4444 50%, #dc2626 100%); } /* Image containers */ .image-container { border-radius: 15px; overflow: hidden; border: 2px solid rgba(220, 38, 38, 0.3); box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4), 0 0 40px rgba(220, 38, 38, 0.2); transition: all 0.3s ease; background: #1a1a1a; } .image-container:hover { transform: translateY(-5px); box-shadow: 0 12px 32px rgba(0, 0, 0, 0.6), 0 0 60px rgba(220, 38, 38, 0.4); border-color: rgba(220, 38, 38, 0.6); } /* Input labels */ label { color: #e5e7eb !important; font-weight: 500 !important; font-size: 1rem !important; margin-bottom: 0.5rem !important; } /* Sliders */ .stSlider > div > div > div { background: linear-gradient(90deg, #dc2626 0%, #ef4444 100%) !important; } .stSlider > div > div > div > div { background-color: #ffffff !important; box-shadow: 0 0 10px rgba(220, 38, 38, 0.5); } /* Select boxes */ .stSelectbox > div > div { background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%) !important; color: white !important; border: 2px solid rgba(220, 38, 38, 0.3) !important; border-radius: 10px !important; transition: all 0.3s ease; } .stSelectbox > div > div:hover { border-color: rgba(220, 38, 38, 0.6) !important; box-shadow: 0 0 20px rgba(220, 38, 38, 0.2); } /* Footer */ .footer { text-align: center; padding: 3rem 0 1.5rem 0; color: #9ca3af; border-top: 2px solid rgba(220, 38, 38, 0.3); margin-top: 4rem; background: linear-gradient(180deg, transparent 0%, rgba(26, 5, 5, 0.3) 100%); border-radius: 10px; } .footer strong { color: #ffffff !important; font-size: 1.1rem; } /* Prediction result boxes */ .stSuccess { background: linear-gradient(135deg, #1a1a1a 0%, #064e3b 100%) !important; border: 2px solid #10b981 !important; padding: 1.5rem; border-radius: 15px; font-weight: 600; box-shadow: 0 8px 24px rgba(16, 185, 129, 0.2); } .stError { background: linear-gradient(135deg, #1a1a1a 0%, #450a0a 100%) !important; border: 2px solid #dc2626 !important; padding: 1.5rem; border-radius: 15px; font-weight: 600; box-shadow: 0 8px 24px rgba(220, 38, 38, 0.2); } /* Button styling */ .stButton>button { background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%) !important; color: white !important; font-size: 1.3rem !important; font-weight: 700 !important; padding: 1rem 3rem !important; border-radius: 12px !important; border: 2px solid #ef4444 !important; width: 100%; margin-top: 2.5rem; text-transform: uppercase; letter-spacing: 2px; transition: all 0.3s ease; box-shadow: 0 6px 24px rgba(220, 38, 38, 0.4); } .stButton>button:hover { background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%) !important; transform: translateY(-3px); box-shadow: 0 12px 32px rgba(220, 38, 38, 0.6); border-color: #f87171 !important; } .stButton>button:active { transform: translateY(-1px); } /* Divider */ hr { border: none !important; height: 2px !important; background: linear-gradient(90deg, transparent 0%, #dc2626 50%, transparent 100%) !important; margin: 3rem 0 !important; } /* Results card */ .results-card { background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%); border: 2px solid rgba(220, 38, 38, 0.3); border-radius: 15px; padding: 2rem; margin-top: 1.5rem; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4); } .success-card { border-color: #10b981 !important; background: linear-gradient(135deg, #1a1a1a 0%, #064e3b 100%); box-shadow: 0 8px 24px rgba(16, 185, 129, 0.2); } .error-card { border-color: #dc2626 !important; background: linear-gradient(135deg, #1a1a1a 0%, #450a0a 100%); box-shadow: 0 8px 24px rgba(220, 38, 38, 0.2); } /* Probability text styling */ .prob-text { font-size: 1.2rem; font-weight: 600; margin: 1rem 0; padding: 1rem; background: rgba(0, 0, 0, 0.3); border-radius: 10px; border-left: 4px solid #dc2626; } /* Streamlit specific overrides */ .stApp { background: linear-gradient(180deg, #0a0a0a 0%, #1a0505 50%, #0a0a0a 100%); } /* Remove default padding */ .css-1d391kg, .css-1v0mbdj { padding-top: 2rem; } </style> """, unsafe_allow_html=True) # Define the filename for the pickle file filename = 'decision_tree_model.pkl' data_info_filename = 'data_info.pkl' # Load the model from the pickle file with open(filename, 'rb') as file: model = pickle.load(file) # Load data info (including expected columns and categorical values) with open(data_info_filename, 'rb') as file: data_info = pickle.load(file) expected_columns = data_info['expected_columns'] categorical_unique_values = data_info['categorical_unique_values'] # HEADER SECTION st.markdown("# Credit Default Prediction System") # Load and display images try: col1, col2, col3 = st.columns(3) with col1: st.markdown('<div class="image-container">', unsafe_allow_html=True) default_img = Image.open('default_image.jpeg') st.image(default_img, use_container_width=True) st.markdown('</div>', unsafe_allow_html=True) with col2: st.markdown('<div class="image-container">', unsafe_allow_html=True) loan_img = Image.open('loan_image.jpeg') st.image(loan_img, use_container_width=True) st.markdown('</div>', unsafe_allow_html=True) with col3: st.markdown('<div class="image-container">', unsafe_allow_html=True) euro_img = Image.open('euro_image.jpeg') st.image(euro_img, use_container_width=True) st.markdown('</div>', unsafe_allow_html=True) except: pass st.markdown("---") # MAIN SECTION - Description st.markdown(""" <div class="description-box"> <h2 style="color: #ffffff; margin-top: 0;">Predict Loan Default Risk with Confidence</h2> <p style="font-size: 1.1rem; line-height: 1.8; color: #e5e7eb;"> Our advanced machine learning model analyzes creditworthiness using the renowned German Credit Dataset. By evaluating key financial indicators—including loan duration, credit history, employment background, and personal financial status—this tool provides accurate predictions of loan default probability. Simply configure your parameters below and receive instant risk assessment to make informed lending decisions. Whether you're a financial institution, credit analyst, or researcher, this tool helps you understand credit risk with precision and clarity. </p> </div> """, unsafe_allow_html=True) # MAIN SECTION - Input Form st.markdown("## Enter Customer Details") # Numerical Features Section st.markdown("### Financial Information") months_loan_duration = st.slider('Months Loan Duration', min_value=6, max_value=72, value=12) amount = st.slider('Amount', min_value=250, max_value=18424, value=1000) percent_of_income = st.slider('Percent of Income', min_value=1, max_value=4, value=2) years_at_residence = st.slider('Years at Residence', min_value=1, max_value=4, value=2) age = st.slider('Age', min_value=18, max_value=75, value=30) st.markdown("---") # Categorical Features Section st.markdown("### Categorical Features") checking_balance = st.selectbox('Checking Balance', categorical_unique_values['checking_balance']) credit_history = st.selectbox('Credit History', categorical_unique_values['credit_history']) purpose = st.selectbox('Purpose', categorical_unique_values['purpose']) savings_balance = st.selectbox('Savings Balance', categorical_unique_values['savings_balance']) employment_duration = st.selectbox('Employment Duration', categorical_unique_values['employment_duration']) other_credit = st.selectbox('Other Credit', categorical_unique_values['other_credit']) housing = st.selectbox('Housing', categorical_unique_values['housing']) job = st.selectbox('Job', categorical_unique_values['job']) phone = st.selectbox('Phone', categorical_unique_values['phone']) # Collect user input into a dictionary user_input = { 'months_loan_duration': months_loan_duration, 'amount': amount, 'percent_of_income': percent_of_income, 'years_at_residence': years_at_residence, 'age': age, 'checking_balance': checking_balance, 'credit_history': credit_history, 'purpose': purpose, 'savings_balance': savings_balance, 'employment_duration': employment_duration, 'other_credit': other_credit, 'housing': housing, 'job': job, 'phone': phone, 'existing_loans_count': 1, 'dependents': 1 } # Convert user input to DataFrame input_df = pd.DataFrame([user_input]) # Apply one-hot encoding input_encoded = pd.get_dummies(input_df, drop_first=True, dtype=int) # Ensure all columns from training data are present and in the same order for col in expected_columns: if col not in input_encoded.columns: input_encoded[col] = 0 input_encoded = input_encoded[expected_columns] # Make prediction if st.button('Predict Default Risk'): prediction = model.predict(input_encoded) prediction_proba = model.predict_proba(input_encoded) st.markdown("---") st.markdown("## Prediction Results") if prediction[0] == 0: st.markdown('<div class="results-card success-card">', unsafe_allow_html=True) st.success('Prediction: No Default - Low Risk Customer') st.markdown(f""" <div class="prob-text" style="border-left-color: #10b981;"> <strong>Probability of No Default:</strong> <span style='color: #10b981; font-size: 1.5rem; font-weight: 700;'>{prediction_proba[0][0]:.1%}</span> </div> """, unsafe_allow_html=True) st.markdown(f""" <div class="prob-text" style="border-left-color: #6b7280;"> <strong>Probability of Default:</strong> <span style='color: #9ca3af; font-size: 1.2rem;'>{prediction_proba[0][1]:.1%}</span> </div> """, unsafe_allow_html=True) st.markdown('</div>', unsafe_allow_html=True) else: st.markdown('<div class="results-card error-card">', unsafe_allow_html=True) st.error('Prediction: Default - High Risk Customer') st.markdown(f""" <div class="prob-text" style="border-left-color: #dc2626;"> <strong>Probability of Default:</strong> <span style='color: #dc2626; font-size: 1.5rem; font-weight: 700;'>{prediction_proba[0][1]:.1%}</span> </div> """, unsafe_allow_html=True) st.markdown(f""" <div class="prob-text" style="border-left-color: #6b7280;"> <strong>Probability of No Default:</strong> <span style='color: #9ca3af; font-size: 1.2rem;'>{prediction_proba[0][0]:.1%}</span> </div> """, unsafe_allow_html=True) st.markdown('</div>', unsafe_allow_html=True) # FOOTER SECTION st.markdown(""" <div class="footer"> <p><strong>Credit Default Prediction System</strong></p> <p style="color: #9ca3af; margin: 0.5rem 0;">Powered by Machine Learning | German Credit Dataset</p> <p style="font-size: 1rem; color: #d1d5db; margin-top: 1.5rem; font-weight: 500;">Marcello Borromeo | CIS 300 Honors Contract</p> </div> """, unsafe_allow_html=True)
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
    pass
st.markdown("---")
# MAIN SECTION - Description
st.markdown("""
    <div class="description-box">
        <h2 style="color: #ffffff; margin-top: 0;">Predict Loan Default Risk with Confidence</h2>
        <p style="font-size: 1.1rem; line-height: 1.8; color: #e5e7eb;">
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
        st.markdown(f"""
            <div class="prob-text" style="border-left-color: #10b981;">
                <strong>Probability of No Default:</strong>
                <span style='color: #10b981; font-size: 1.5rem; font-weight: 700;'>{prediction_proba[0][0]:.1%}</span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
            <div class="prob-text" style="border-left-color: #6b7280;">
                <strong>Probability of Default:</strong>
                <span style='color: #9ca3af; font-size: 1.2rem;'>{prediction_proba[0][1]:.1%}</span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="results-card error-card">', unsafe_allow_html=True)
        st.error('Prediction: Default - High Risk Customer')
        st.markdown(f"""
            <div class="prob-text" style="border-left-color: #dc2626;">
                <strong>Probability of Default:</strong>
                <span style='color: #dc2626; font-size: 1.5rem; font-weight: 700;'>{prediction_proba[0][1]:.1%}</span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
            <div class="prob-text" style="border-left-color: #6b7280;">
                <strong>Probability of No Default:</strong>
                <span style='color: #9ca3af; font-size: 1.2rem;'>{prediction_proba[0][0]:.1%}</span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
# FOOTER SECTION
st.markdown("""
    <div class="footer">
        <p><strong>Credit Default Prediction System</strong></p>
        <p style="color: #9ca3af; margin: 0.5rem 0;">Powered by Machine Learning | German Credit Dataset</p>
        <p style="font-size: 1rem; color: #d1d5db; margin-top: 1.5rem; font-weight: 500;">Marcello Borromeo | CIS 300 Honors Contract</p>
    </div>
""", unsafe_allow_html=True)
