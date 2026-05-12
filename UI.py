import streamlit as st
import requests
from PIL import Image

# --------------------------
# PAGE CONFIG
# --------------------------
st.set_page_config(
    page_title="Steganography Detector",
    page_icon="🔍",
    layout="centered",
)

# --------------------------
# CUSTOM HEADER
# --------------------------
st.markdown(
    """
    <h1 style="text-align:center; color:#1a365d; font-weight:900;">
        🔍 Steganography Detection System
    </h1>
    <p style="text-align:center; color:#4a5568; font-size:18px;">
        ALASKA2 - EfficientNet Model
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("---")

# --------------------------
# FILE UPLOAD
# --------------------------
uploaded_file = st.file_uploader(
    "Upload an image to analyze",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    st.write("")

    if st.button("Run Analysis"):
        with st.spinner("Processing…"):
            try:
                # Send to FastAPI backend
                response = requests.post(
                    "http://127.0.0.1:8000/predict",
                    files={"file": uploaded_file.getvalue()}
                )

                result = response.json().get("prediction", "Error: No prediction received")

                st.success(f"✅ Prediction: **{result}**")

            except Exception as e:
                st.error("❌ Unable to connect to backend.")
                st.info("Make sure FastAPI is running on port 8000.")
                st.code(str(e))

else:
    st.info("⬆️ Upload an image to get started.")
