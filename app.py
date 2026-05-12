import streamlit as st
from PIL import Image
import torch
import torch.nn.functional as F
import torchvision.transforms as T
import timm
import numpy as np
import io
import altair as alt
import pandas as pd
from datetime import datetime

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Stego Detector",
    layout="wide",
    page_icon="🕵️‍♂️"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>
body {background-color: #121212; color: #e0e0e0; font-family: 'Helvetica', sans-serif;}
h1 {color: #00bcd4; font-size: 48px; text-align: center;}
h2 {color: #ff9800; font-size: 28px; text-align: center;}
.stButton>button {
    background-color: transparent;
    color: #001f7f;
    border: 2px solid #001f7f;
    height: 3em;
    width: 100%;
    font-size: 20px;
    border-radius: 12px;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: #001f7f33;
    color: #ffffff;
}
.stImage>img {border-radius: 12px; box-shadow: 0 0 20px #00bcd4aa;}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Load Model
# -------------------------------
@st.cache_resource
def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = timm.create_model("efficientnet_b0", pretrained=False, num_classes=2)
    model.load_state_dict(torch.load("alaska_optionA_efficientnet.pth", map_location=device))
    model.to(device)
    model.eval()
    return model, device

model, device = load_model()

# -------------------------------
# Preprocessing
# -------------------------------
preprocess = T.Compose([
    T.Resize((224, 224)),
    T.ToTensor(),
    T.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# -------------------------------
# Session state for previous predictions
# -------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------------
# Sidebar Info
# -------------------------------
st.sidebar.header("Model Details")
st.sidebar.text("Architecture: EfficientNet-B0")
st.sidebar.text("Classes: Cover, Stego")
st.sidebar.text(f"Device: {device}")

st.sidebar.header("Previous Predictions")
if st.session_state.history:
    for item in reversed(st.session_state.history):
        img = Image.open(io.BytesIO(item["image_bytes"]))
        st.sidebar.image(img, width=60)
        st.sidebar.markdown(f"{item['label']} ({item['confidence']:.2f}) - {item['timestamp']}")

# -------------------------------
# Main Area
# -------------------------------
st.title("Stego Image Detection System")
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(io.BytesIO(uploaded_file.read())).convert("RGB")
    st.image(image, caption="Uploaded Image", width=250)

    if st.button("🔎 Predict"):
        with st.spinner("Analyzing..."):

            # Preprocess
            img_tensor = preprocess(image).unsqueeze(0).to(device)

            # Predict
            with torch.no_grad():
                logits = model(img_tensor)
                probs = F.softmax(logits, dim=1).cpu().numpy()[0]

            pred_class = int(np.argmax(probs))
            label = "Stego" if pred_class == 1 else "Cover"

            # Prediction badge
            color = "#4caf50" if label == "Cover" else "#f44336"
            st.markdown(f"<h2 style='color:{color};'>Prediction: {label}</h2>", unsafe_allow_html=True)

            # -------------------------------
            # NEW MESSAGE FOR STEGO
            # -------------------------------
            if label == "Stego":
                st.write("⚠️ Hidden content detected in this image.")
            else:
                st.write("✔️ No hidden content detected.")

            # Confidence bar
            st.progress(float(probs[pred_class]))

            # Probability chart
            probs_df = pd.DataFrame({
                'Class': ['Cover', 'Stego'],
                'Probability': probs
            })
            chart = alt.Chart(probs_df).mark_bar(cornerRadiusTopLeft=5, cornerRadiusTopRight=5).encode(
                x='Probability',
                y=alt.Y('Class', sort='-x'),
                color=alt.Color('Class', scale=alt.Scale(domain=['Cover','Stego'], range=['#4caf50','#f44336']))
            )
            st.altair_chart(chart, use_container_width=True)

            # Save to history
            img_bytes = io.BytesIO()
            image.save(img_bytes, format="PNG")
            st.session_state.history.append({
                "image_bytes": img_bytes.getvalue(),
                "label": label,
                "confidence": float(probs[pred_class]),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
