# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 23:13:26 2025

@author: Aries
"""

import streamlit as st
import pandas as pd
import joblib

pipeline = joblib.load("spam_pipeline.pkl")

expected_columns = joblib.load("expected_columns.pkl")

st.title("Spam Email Classifier")

with open("sample_input.xlsx", "rb") as file:
    st.download_button(
        label = "Download Sample Input(Excel)",
        data = file,
        file_name = "sample_input.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

uploaded_file = st.file_uploader("Upload an Excel file", type = ['xlsx'])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    df.columns = [str(col) for col in df.columns]
    
    if list(df.columns) != expected_columns:
        st.warning("Uploaded file's columns do not match the training data")
        st.write(f"Expected {len(expected_columns)} columns.")
        st.write(f"Uploaded file has {df.shape[1]} columns.")

        if set(df.columns) == set(expected_columns):
            df = df[expected_columns]
        else:
            st.error("File doesnt contain the correct feature set")
            st.stop()
    
    st.write("Uploaded data preview")
    st.dataframe(df.head())
    
    try:
        predictions = pipeline.predict(df)
        df["Prediction"] = ["Spam" if p == 1 else "Not Spam" for p in predictions]
        st.success("Prediction completed!")
        st.dataframe(df)
        
        st.download_button("Download Predictions", df.to_csv(index = False), file_name="Predictions.csv")
    except Exception as e:
        st.error(f"Prediction failed: {e}")