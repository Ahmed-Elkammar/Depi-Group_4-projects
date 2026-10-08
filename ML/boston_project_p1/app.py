import streamlit as st
import pandas as pd
import joblib
import json
import os

# Set page config
st.set_page_config(page_title="Boston Housing Predictor", page_icon="🏠", layout="centered")

# Load model and metrics
@st.cache_resource
def load_model_and_metrics():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model = joblib.load(os.path.join(base_dir, "model.joblib"))
    with open(os.path.join(base_dir, "metrics.json")) as f:
        metrics = json.load(f)
    return model, metrics

model, metrics = load_model_and_metrics()
RANGES = metrics["feature_ranges"]

# UI Design
st.title("🏠 Boston Housing Price Predictor")
st.write("Estimate Boston real estate market prices based on neighborhood and property metrics.")
st.markdown("---")

# Input fields
st.subheader("Property Features")
rm = st.number_input(
    f"RM (Average Rooms per Dwelling) [{RANGES['RM'][0]} - {RANGES['RM'][1]}]", 
    value=6.0, step=0.1
)
lstat = st.number_input(
    f"LSTAT (% Lower Status of the Population) [{RANGES['LSTAT'][0]}% - {RANGES['LSTAT'][1]}%]", 
    value=12.0, step=0.1
)
ptratio = st.number_input(
    f"PTRATIO (Pupil-Teacher Ratio by Town) [{RANGES['PTRATIO'][0]} - {RANGES['PTRATIO'][1]}]", 
    value=18.0, step=0.1
)

st.markdown("<br>", unsafe_allow_html=True)

# Prediction Logic
if st.button("Predict Estimated Value", type="primary", use_container_width=True):
    # Warnings for out-of-range inputs
    warnings = []
    if not (RANGES['RM'][0] <= rm <= RANGES['RM'][1]): warnings.append("RM")
    if not (RANGES['LSTAT'][0] <= lstat <= RANGES['LSTAT'][1]): warnings.append("LSTAT")
    if not (RANGES['PTRATIO'][0] <= ptratio <= RANGES['PTRATIO'][1]): warnings.append("PTRATIO")
    
    if warnings:
        st.warning(f"⚠️ Note: Input values for **{', '.join(warnings)}** are outside the training range. The prediction might be less reliable.")
    
    # Make Prediction
    X_input = pd.DataFrame([{"RM": rm, "LSTAT": lstat, "PTRATIO": ptratio}])
    prediction = model.predict(X_input)[0]
    
    st.success(f"### Estimated Market Value: ${prediction:,.0f}")

st.markdown("---")

# Display Model Metrics
st.subheader("Model Performance")
col1, col2, col3 = st.columns(3)
col1.metric("Model Type", metrics['model'].split('(')[0].strip())
col2.metric("Test R² Score", metrics['test_r2'])
col3.metric("Test MAE", f"${metrics['test_mae']:,.0f}")
