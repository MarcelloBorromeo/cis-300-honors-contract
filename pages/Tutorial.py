import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Tutorial", layout="centered")

# --- TITLE ---
st.markdown(
    """
    <h1 style='text-align:center;'>How to Use the Credit Default Prediction App</h1>
    """,
    unsafe_allow_html=True
)

st.image("loan.jpeg", use_column_width=True)

st.markdown(
    """
    <div style='background-color:#2c2c2c; color:white; padding:18px; border-radius:10px; border:1px solid #444; text-align:justify; font-size:16px;'>
    This tutorial will guide you through using the <b>Credit Default Prediction Tool</b>. 
    Our machine learning model analyzes financial and personal information to predict the likelihood 
    that a customer may default on a loan. It is based on the <b>German Credit Dataset</b>, a well-known dataset 
    used in credit risk modeling.
    </div>
    """,
    unsafe_allow_html=True
)

# --- SECTION 1: NUMERIC INPUTS ---
st.header("1. Enter Customer Details")
st.markdown(
    """
    These fields represent key financial and demographic indicators. Adjust them using the sliders:
    - **Months Loan Duration** → How long the loan will last.
    - **Amount** → Total loan amount requested.
    - **Percent of Income** → The portion of monthly income the loan payment represents.
    - **Years at Residence** → How long the customer has lived at their current address.
    - **Age** → Customer’s age in years.
    """
)

# --- SECTION 2: CATEGORICAL FEATURES ---
st.header("2. Categorical Features")
st.markdown("Each dropdown represents a coded financial category from the German Credit Dataset. Expand each section to see what the codes mean:")

# --- CHECKING BALANCE ---
with st.expander("💳 Checking Balance"):
    st.markdown(
        """
        | Code | Meaning |
        |------|----------|
        | **A11** | Balance < 0 DM (overdrawn) |
        | **A12** | 0 ≤ Balance < 200 DM |
        | **A13** | Balance ≥ 200 DM |
        | **A14** | No checking account |
        """
    )

# --- CREDIT HISTORY ---
with st.expander("📜 Credit History"):
    st.markdown(
        """
        | Code | Meaning |
        |------|----------|
        | **A30** | No credits taken / all paid back duly |
        | **A31** | All credits at this bank paid back duly |
        | **A32** | Existing credits paid back till now |
        | **A33** | Delay in paying off in the past |
        | **A34** | Critical account / other credits existing |
        """
    )

# --- PURPOSE ---
with st.expander("🎯 Purpose of the Loan"):
    st.markdown(
        """
        | Code | Meaning |
        |------|----------|
        | **A40** | Car (new) |
        | **A41** | Car (used) |
        | **A42** | Furniture or equipment |
        | **A43** | Radio/TV |
        | **A44** | Domestic appliances |
        | **A45** | Repairs |
        | **A46** | Education |
        | **A47** | Vacation |
        | **A48** | Retraining |
        | **A49** | Business |
        | **A410** | Other purpose |
        """
    )

# --- SAVINGS BALANCE ---
with st.expander("💰 Savings Balance"):
    st.markdown(
        """
        | Code | Meaning |
        |------|----------|
        | **A61** | < 100 DM |
        | **A62** | 100 ≤ Savings < 500 DM |
        | **A63** | 500 ≤ Savings < 1000 DM |
        | **A64** | ≥ 1000 DM |
        | **A65** | Unknown / No savings account |
        """
    )

# --- EMPLOYMENT DURATION ---
with st.expander("👷 Employment Duration"):
    st.markdown(
        """
        | Code | Meaning |
        |------|----------|
        | **A71** | Unemployed |
        | **A72** | < 1 year |
        | **A73** | 1 ≤ Years < 4 |
        | **A74** | 4 ≤ Years < 7 |
        | **A75** | ≥ 7 years |
        """
    )

# --- OTHER CREDIT ---
with st.expander("🏦 Other Credit"):
    st.markdown(
        """
        | Code | Meaning |
        |------|----------|
        | **A101** | None |
        | **A102** | Store credit |
        | **A103** | Bank credit |
        """
    )

# --- HOUSING ---
with st.expander("🏠 Housing Type"):
    st.markdown(
        """
        | Code | Meaning |
        |------|----------|
        | **A151** | Rent |
        | **A152** | Own |
        | **A153** | For free (no rent) |
        """
    )

# --- JOB ---
with st.expander("💼 Job Type"):
    st.markdown(
        """
        | Code | Meaning |
        |------|----------|
        | **A171** | Unemployed / unskilled (non-resident) |
        | **A172** | Unskilled (resident) |
        | **A173** | Skilled employee / official |
        | **A174** | Management / highly qualified / self-employed |
        """
    )

# --- PHONE ---
with st.expander("📞 Phone Availability"):
    st.markdown(
        """
        | Code | Meaning |
        |------|----------|
        | **A191** | No phone |
        | **A192** | Has phone (registered under customer’s name) |
        """
    )

# --- FOOTER / RETURN LINK ---
st.markdown("<hr>", unsafe_allow_html=True)
if st.button("⬅️ Back to Credit Default App"):
    st.markdown("<meta http-equiv='refresh' content='0; url=../' />", unsafe_allow_html=True)

st.markdown(
    """
    <p style="text-align:center; color:gray; font-size:14px;">
    © Marcello Borromeo | CIS 300 Honors Contract
    </p>
    """,
    unsafe_allow_html=True
)
