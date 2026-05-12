# 🕵️ Deep Learning Implementation of Visual Information Concealment

A Deep Learning-based steganography detection system designed to identify hidden or concealed information inside digital images using **EfficientNet-B0** architecture. The system helps detect whether an uploaded image contains hidden content (**Stego**) or is a normal image (**Cover**) using image classification techniques.

---

## 📌 Project Overview

Steganography is a method of concealing secret information within digital media such as images, making communication invisible to unintended users. While it can be used for secure communication, it may also be exploited for malicious purposes such as hidden data transfer and unauthorized communication.

This project implements a **Deep Learning-based Steganography Detection System (Steganalysis)** capable of analyzing images and predicting whether hidden information is embedded within them.

The system uses **EfficientNet-B0**, a powerful convolutional neural network architecture, to classify uploaded images into:

- ✅ **Cover Image** → No hidden information detected  
- ⚠️ **Stego Image** → Hidden information detected

The application provides a user-friendly interface for uploading images, generating predictions, and visualizing classification confidence.

---

## 🎯 Problem Statement

Traditional methods for detecting hidden information in images often struggle with:

- Low detection accuracy
- Difficulty identifying concealed data patterns
- Inefficient manual analysis
- Limited scalability for large image datasets
- Lack of automated detection systems

This project addresses these challenges using **Deep Learning and Image Classification techniques**.

---

## ✨ Features

✅ Steganography detection using Deep Learning  
✅ EfficientNet-B0 based classification model  
✅ Binary image classification (**Cover vs Stego**)  
✅ Interactive image upload interface  
✅ Prediction confidence visualization  
✅ Real-time image analysis  
✅ Streamlit-based frontend application  
✅ FastAPI backend integration  
✅ User-friendly detection dashboard

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Deep Learning
- PyTorch
- EfficientNet-B0
- Torchvision

### Backend
- FastAPI

### Frontend
- Streamlit
- HTML
- CSS

### Image Processing
- PIL (Pillow)

### Data Visualization
- Altair
- Pandas
- NumPy

### Development Tools
- Visual Studio Code
- GitHub

---

## 📊 Model Used

The system uses an **EfficientNet-B0** deep learning model trained for steganography detection.

### Classification Categories

| Class | Meaning |
|--------|----------|
| Cover | No hidden information present |
| Stego | Hidden information detected |

The trained model file:

```text
alaska_optionA_efficientnet.pth
```

is used to classify uploaded images into **Cover** or **Stego** categories.

---

## ⚙️ System Architecture

The project follows the workflow below:

```text
Image Upload
      ↓
Image Preprocessing
      ↓
EfficientNet-B0 Model
      ↓
Prediction Generation
      ↓
Cover / Stego Classification
      ↓
Confidence Visualization
```

---

## 🔍 Workflow

1. Upload an image (`.jpg`, `.jpeg`, `.png`)
2. The image is preprocessed and resized
3. EfficientNet-B0 analyzes image features
4. The trained model predicts:
   - **Cover** → No hidden content
   - **Stego** → Hidden content detected
5. Results are displayed with confidence probability

---

## 📂 Project Structure

```text
Deep-Learning-Implementation-of-Visual-Information-Concealment/
│── app.py
│── main.py
│── UI.py
│── test_model.py
│── alaska_optionA_efficientnet.pth
│
│── templates/
│   └── index.html
│
│── static/
│
│── README.md
```

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/bharathm1307/Deep-Learning-Implementation-of-Visual-Information-Concealment.git
```

### Step 2: Navigate to Project Folder

```bash
cd Deep-Learning-Implementation-of-Visual-Information-Concealment
```

### Step 3: Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate virtual environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### Step 4: Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

### Run FastAPI Backend

```bash
uvicorn main:app --reload
```

### Run Streamlit Frontend

```bash
streamlit run app.py
```

The application will open in the browser automatically.

---

## 📸 Screenshots

### Application Interface

_Add your project screenshots here_

Example:

```md
![Dashboard](screenshots/dashboard.png)
```

---

## 🧪 Testing

The project was tested using:

- Functional Testing
- Model Prediction Testing
- Backend API Testing
- Frontend UI Testing
- Integration Testing

All core functionalities worked successfully.

---

## 📌 Results

The system successfully achieved:

✔️ Accurate hidden information detection  
✔️ Efficient image classification  
✔️ Real-time prediction generation  
✔️ Improved automated steganography detection  
✔️ User-friendly prediction interface

---

## 🔮 Future Improvements

- Higher accuracy deep learning models  
- Multi-class steganography detection  
- Cloud deployment support  
- Video steganography analysis  
- Advanced forensic analytics dashboard  
- Larger dataset integration

---

## 👥 Project Information

**Project Type:** Team Project

**Domain:**  
Deep Learning + Cybersecurity + Computer Vision

**Objective:**  
To develop an intelligent system capable of detecting hidden information concealed inside digital images using Deep Learning techniques.

---

## 📄 License

This project is developed for **academic purposes**.

---

## ⭐ Support

If you found this project useful, consider giving it a **star ⭐ on GitHub**.