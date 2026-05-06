import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Civic AI System",
    page_icon="🚧",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fb;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #1f4e79;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #555;
        margin-bottom: 30px;
    }

    .result-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
        margin-top: 20px;
    }

    .footer {
        text-align: center;
        color: gray;
        margin-top: 40px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- LOAD MODEL ----------------
model = load_model("civic_model.h5")

class_names = ['clean', 'garbage', 'potholes']

# ---------------- PREDICTION FUNCTION ----------------
def predict_image(img):

    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    pred = model.predict(img_array)

    label = class_names[np.argmax(pred)]
    confidence = float(np.max(pred))

    return label, confidence

# ---------------- SEVERITY ----------------
def get_severity(label, conf):

    if label == "clean":
        return "None"

    elif label == "potholes":
        if conf > 0.9:
            return "High"
        else:
            return "Medium"

    elif label == "garbage":
        return "Medium"

    else:
        return "Unknown"

# ---------------- PRIORITY ----------------
def get_priority(label, severity):

    if label == "clean":
        return "None"

    elif label == "potholes":
        if severity == "High":
            return "Urgent 🚨"
        else:
            return "High"

    elif label == "garbage":
        return "Medium"

    return "Unknown"

# ---------------- TITLE ----------------
st.markdown('<div class="title">🚧 Civic AI Issue Detection System</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Upload a road image to detect civic issues using AI</div>',
    unsafe_allow_html=True
)

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "📤 Upload Image",
    type=["jpg", "jpeg", "png"]
)

# ---------------- PROCESS IMAGE ----------------
if uploaded_file is not None:

    img = Image.open(uploaded_file)

    st.image(img, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Analyzing image..."):
        label, conf = predict_image(img)

    severity = get_severity(label, conf)
    priority = get_priority(label, severity)

    # ISSUE COLORS
    if label == "clean":
        issue_emoji = "✅"
    elif label == "garbage":
        issue_emoji = "🗑️"
    else:
        issue_emoji = "⚠️"

    

    st.subheader("📊 Detection Results")

    st.write(f"### {issue_emoji} Issue Detected: **{label.upper()}**")
    st.write(f"### 🎯 Confidence: **{conf:.2f}**")
    st.write(f"### 📌 Severity: **{severity}**")
    st.write(f"### 🚦 Priority: **{priority}**")

    if conf < 0.6:
        st.warning("Low confidence prediction. Manual verification recommended.")

   

# ---------------- SIDEBAR ----------------
st.sidebar.title("📖 About Project")

st.sidebar.info(
    """
   This AI system analyzes road images to identify civic issues and road conditions.

Detected categories:
- Potholes
- Garbage accumulation
- Clean / no-issue roads

    Features:
    - AI-based issue detection
    - Confidence analysis
    - Severity estimation
    - Priority handling

    Future Scope:
    - GPS integration
    - YOLO object detection
    - Real-time complaint tracking
    """
)

# ---------------- FOOTER ----------------
st.markdown(
    '<div class="footer">Built using TensorFlow + Streamlit</div>',
    unsafe_allow_html=True
)
