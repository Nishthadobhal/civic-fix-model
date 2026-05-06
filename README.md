# Civic AI Issue Detection System 🚧

## Overview

This project is an AI-based civic issue detection system that analyzes road images and identifies common civic problems such as potholes and garbage accumulation.

The system uses a deep learning image classification model along with rule-based severity and priority estimation to assist in identifying and prioritizing civic complaints.

The project was built using TensorFlow/Keras for the AI model and Streamlit for the web application interface.

---

# Features ✨

* Detects:

  * Potholes
  * Garbage accumulation
  * Clean / no-issue roads

* AI-based image classification

* Confidence score prediction

* Severity estimation

* Priority handling

* Interactive Streamlit web interface

* Real-time image upload and prediction

---

# Technologies Used 🛠️

* Python
* TensorFlow / Keras
* Streamlit
* NumPy
* Pillow

---

# How It Works ⚙️

1. User uploads a road image.
2. The trained AI model analyzes the image.
3. The system predicts the issue category.
4. Confidence score is generated.
5. Rule-based logic estimates severity and priority.
6. Final results are displayed in the web application.

---

# Severity and Priority Logic 📌

The current version uses rule-based severity estimation.

### Example:

* Potholes are treated as higher-severity road safety issues.
* Garbage accumulation is treated as medium severity.
* Clean roads are marked as no issue.

Priority is estimated using:

* detected issue type
* severity level
* confidence score

---

# Model Information 🤖

The project currently uses an image classification approach with three classes:

* clean
* garbage
* potholes

Transfer learning was used for model training.

---

# Limitations ⚠️

* The model uses image classification, not object detection.
* Exact pothole size/depth estimation is not currently supported.
* Severity estimation is heuristic/rule-based.
* Multiple issue detection in a single image is limited.

---

# Future Improvements 🚀

Future versions may include:

* YOLO-based object detection
* GPS/location integration
* Duplicate complaint detection
* Real-time civic complaint tracking
* Advanced severity estimation
* Additional civic issue categories

---

# Live Demo 🌐

### Deploy Link:

https://civic-fix-model-hx5uexobjdatkuhainixbx.streamlit.app/

---

# Author 👩‍💻

Nishtha Dobhaal
