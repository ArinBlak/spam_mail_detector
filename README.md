# spam_mail_detector
# 📧 Spam Mail Detector

This project is a **machine learning-based web app** built with **Streamlit** that classifies emails as **Spam** or **Not Spam** based on structured features. Users can upload an Excel file containing preprocessed email data and receive instant predictions.

---

## 🚀 Features

- Upload `.xlsx` files with structured email data
- Detect whether each entry is **Spam** or **Not Spam**
- Preview predictions directly on the app
- Download results as a `.csv` file
- Sample input file available for download
- Fully deployed using **Streamlit Cloud**

---

## 🔗 Live App

👉 [Launch the Web App](https://spammaildetector-cd6ejgyuukzvazbb8trawd.streamlit.app/)  

---

## 🧠 How It Works

- The model was trained on a dataset with over 5,000 records and 3,000+ features
- The pipeline includes:
  - Feature scaling with **StandardScaler**
  - Dimensionality reduction with **PCA**
  - Classification using **Random Forest classifier**
- The trained pipeline and expected feature columns are saved using `joblib`

---

## 📁 File Structure

📦 spam_mail_detector
├── app.py # Streamlit app
├── spam_pipeline.pkl # Trained ML pipeline (scaler + PCA + model)
├── screenshots # Contains screenshots of the home page, how to upload and an example prediction
├── expected_columns.pkl # List of expected column names for validation
├── sample_input.xlsx # Example input file for testing
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 🧪 Sample Input Format

- Download the sample input file from the app
- Ensure your Excel file has the **exact same columns and structure** as the one used during training
- The model will raise an error if column mismatch occurs

---

## ⚙️ Setup (For Local Use)

1. Clone this repository:

   ```bash
   git clone https://github.com/ArinBlak/spam_mail_detector.git
   cd spam_mail_detector

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   

3. Run the app locally

   ```bash
   streamlit run app.py

## 📌 Tech Stack
-  Python
-  Streamlit
-  Scikit-learn
-  Pandas, NumPy
-  Joblib
-  OpenPyXL

## ✍️ Author
Arindam Ray
This project is part of my hands-on machine learning journey. Future improvements may include:
-  Email text parsing using NLP
-  Automatic feature extraction
