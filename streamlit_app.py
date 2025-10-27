# Custom CSS for styling with larger text
st.markdown("""
    <style>
    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
   
    /* Main background with gradient */
    .main {
        background: linear-gradient(180deg, #0a0a0a 0%, #1a0505 50%, #0a0a0a 100%);
        padding: 2rem;
        font-family: 'Inter', sans-serif;
    }
   
    /* Content container */
    .block-container {
        background: linear-gradient(135deg, #1a1a1a 0%, #2a1a1a 100%);
        border-radius: 20px;
        padding: 3rem;
        box-shadow: 0 8px 32px rgba(220, 38, 38, 0.3), 0 0 80px rgba(220, 38, 38, 0.1);
        border: 1px solid rgba(220, 38, 38, 0.3);
        backdrop-filter: blur(10px);
    }
   
    /* All text white by default */
    .main * {
        color: white !important;
    }
   
    /* Header styling - ALL WHITE */
    h1 {
        color: #ffffff !important;
        font-size: 4.2rem !important; /* Increased from 3.5rem to 4.2rem */
        font-weight: 700 !important;
        text-align: center;
        margin-bottom: 1rem !important;
        text-transform: uppercase;
        letter-spacing: 3px;
        text-shadow: 0 0 30px rgba(220, 38, 38, 0.5);
    }
   
    h2 {
        color: #ffffff !important;
        font-size: 2.5rem !important; /* Increased from 2rem to 2.5rem */
        margin-top: 2.5rem !important;
        border-bottom: 3px solid #dc2626;
        padding-bottom: 0.8rem;
        font-weight: 600 !important;
        text-shadow: 0 0 20px rgba(220, 38, 38, 0.3);
    }
   
    h3 {
        color: #ffffff !important;
        font-size: 1.8rem !important; /* Increased from 1.5rem to 1.8rem */
        margin-top: 2rem !important;
        font-weight: 600 !important;
        position: relative;
        padding-left: 20px;
    }
   
    h3:before {
        content: '';
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 4px;
        height: 24px;
        background: linear-gradient(180deg, #dc2626 0%, #ef4444 100%);
        border-radius: 2px;
    }
   
    /* Description box */
    .description-box {
        background: linear-gradient(135deg, #2a1a1a 0%, #1a1a1a 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4), inset 0 0 0 2px rgba(220, 38, 38, 0.3);
        border: 2px solid transparent;
        background-clip: padding-box;
        position: relative;
        overflow: hidden;
    }
   
    .description-box p {
        font-size: 1.4rem !important; /* Increased from 1.1rem to 1.4rem */
        line-height: 1.8;
        color: #e5e7eb !important;
    }
   
    .description-box:before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #dc2626 0%, #ef4444 50%, #dc2626 100%);
    }
   
    /* Input labels */
    label {
        color: #e5e7eb !important;
        font-weight: 500 !important;
        font-size: 1.3rem !important; /* Increased from 1rem to 1.3rem */
        margin-bottom: 0.5rem !important;
    }
   
    /* Footer */
    .footer {
        text-align: center;
        padding: 3rem 0 1.5rem 0;
        color: #9ca3af;
        border-top: 2px solid rgba(220, 38, 38, 0.3);
        margin-top: 4rem;
        background: linear-gradient(180deg, transparent 0%, rgba(26, 5, 5, 0.3) 100%);
        border-radius: 10px;
    }
   
    .footer strong {
        color: #ffffff !important;
        font-size: 1.4rem !important; /* Increased from 1.1rem to 1.4rem */
    }
   
    .footer p {
        font-size: 1.2rem !important; /* Increased from implied default to 1.2rem */
        color: #9ca3af !important;
    }
   
    /* Probability text styling */
    .prob-text {
        font-size: 1.5rem !important; /* Increased from 1.2rem to 1.5rem */
        font-weight: 600;
        margin: 1rem 0;
        padding: 1rem;
        background: rgba(0, 0, 0, 0.3);
        border-radius: 10px;
        border-left: 4px solid #dc2626;
    }
   
    .prob-text span {
        font-size: 1.8rem !important; /* Increased from 1.5rem to 1.8rem for main probability */
    }
   
    .prob-text span[style*="font-size: 1.2rem"] {
        font-size: 1.5rem !important; /* Increased secondary probability text from 1.2rem to 1.5rem */
    }
   
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%) !important;
        color: white !important;
        font-size: 1.6rem !important; /* Increased from 1.3rem to 1.6rem */
        font-weight: 700 !important;
        padding: 1rem 3rem !important;
        border-radius: 12px !important;
        border: 2px solid #ef4444 !important;
        width: 100%;
        margin-top: 2.5rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.3s ease;
        box-shadow: 0 6px 24px rgba(220, 38, 38, 0.4);
    }
   
    /* Streamlit specific overrides */
    .stApp {
        background: linear-gradient(180deg, #0a0a0a 0%, #1a0505 50%, #0a0a0a 100%);
    }
   
    /* Remove default padding */
    .css-1d391kg, .css-1v0mbdj {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)
