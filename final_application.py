# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open("final_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Simple Model to Predict Salary")


st.subheader("For how many years have you been writing code and/or programming?")
q11 = st.slider(label="Programming Experience", min_value=0, max_value=20, value=10)

# Bin Q11 input
if q11 <= 10:
    q11_bin = "5-10 years"
elif q11 <= 20:
    q11_bin = "10-20 years"
else:
    q11_bin = "20+ years"

# Q16
st.subheader("For how many years have you used machine learning methods?")
q16 = st.slider(label="ML Experience", min_value=0, max_value=20, value=10)

if q16 <= 5:
    q16_bin = "4-5 years"
elif q16 <= 10:
    q16_bin = "5-10 years"
elif q16 <= 20:
    q16_bin = "10-20 years"
else:
    q16_bin = "20+ years"

# Q18
st.subheader("What machine learning methods are you familiar with?")
q18 = st.multiselect(
    "Select all methods you are familiar with:",
    ["Evolutionary Approaches", "Convolutional Neural Networks", "Graph Neural Networks"]
)

# Q23
st.subheader("Select the title most similar to your current role (or most recent title if retired):")
q23 = st.selectbox(
    "Select your current or most recent title:",
    [
        "Data Analyst (Business, Marketing, Financial, Quantitative, etc.)",
        "Data Architect",
        "Data Scientist",
        "Developer Advocate",
        "Engineer (non-software)",
        "Manager (Program, Project, Operations, Executive-level, etc.)",
        "Other",
        "Research Scientist",
        "Software Engineer",
        "Teacher / Professor",
        "(None)"
    ]
)

# Q27
st.subheader("Does your current employer incorporate machine learning methods into their business?")
q27 = st.radio(
    "Select the most appropriate statement:",
    [
        "We are exploring ML methods (and may one day put a model into production)",
        "We have well-established ML methods (i.e., models in production for more than 2 years)",
        "We recently started using ML methods (i.e., models in production for less than 2 years)",
        "We use ML methods for generating insights (but do not put working models into production)",
        "(None)"
    ]
)

# Q28
st.subheader("Which of the following activities are an important part of your role at work?")
q28 = st.multiselect(
    "Select all activities relevant to your role:",
    [
        "Analyze and understand data to influence product or business decisions",
        "Build and/or run the data infrastructure that my business uses for storing, analyzing, and operationalizing data",
        "Build prototypes to explore applying machine learning to new areas",
        "Experimentation and iteration to improve existing ML models",
        "Do research that advances the state of the art of machine learning"
    ]
)

# Q30
st.subheader("Approximately how much money have you spent on machine learning and/or cloud computing services at home or at work in the past 5 years (approximate $USD)?")
q30 = st.slider(
    "Select your spending range (approximate $USD):",
    min_value=1, max_value=100000, value=10000, step=100
)

# Bin Q30 input
if q30 <= 100:
    q30_bin = "1-99"
elif q30 <= 9999:
    q30_bin = "1,000-9,999"
elif q30 <= 99999:
    q30_bin = "10,000-99,999"
else:
    q30_bin = "100,000 or more"

# Q31
st.subheader("Which cloud computing services are you familiar with?")
q31 = st.multiselect(
    "Select all services you are familiar with:",
    [
        "Amazon Web Services (AWS)",
        "Microsoft Azure",
        "IBM Cloud / Red Hat",
        "Huawei Cloud",
        "Other"
    ]
)

# Q33
st.subheader("Have you used Amazon Elastic Compute Cloud (EC2), Microsoft Azure Virtual Machines or Google Cloud Compute Engine for your work?")
q33 = st.radio(
    "Select one option:",
    ["Yes", "No", "I have used others"]
)

# Q34
st.subheader("Which storage services are you familiar with?")
q34 = st.multiselect(
    "Select all services you are familiar with:",
    ["Microsoft Azure Files", "Amazon Elastic File System (EFS)", "Google Cloud Filestore"]
)

# Q35
st.subheader("Which database services are you familiar with?")
q35 = st.multiselect(
    "Select all services you are familiar with:",
    [
        "MySQL",
        "Oracle Database",
        "MongoDB",
        "Snowflake",
        "Microsoft SQL Server",
        "Microsoft Azure SQL Database",
        "Amazon Redshift",
        "Amazon RDS",
        "Google Cloud SQL",
        "(None)"
    ]
)

def preprocess_inputs():
    model_inputs = {}

    # Q11
    model_inputs["Q11~For how many years have you been writing code and/or programming?_5-10 years"] = 1 if q11_bin == "5-10 years" else 0
    model_inputs["Q11~For how many years have you been writing code and/or programming?_10-20 years"] = 1 if q11_bin == "10-20 years" else 0
    model_inputs["Q11~For how many years have you been writing code and/or programming?_20+ years"] = 1 if q11_bin == "20+ years" else 0

    # Q16
    model_inputs["Q16~For how many years have you used machine learning methods?_4-5 years"] = 1 if q16_bin == "4-5 years" else 0
    model_inputs["Q16~For how many years have you used machine learning methods?_5-10 years"] = 1 if q16_bin == "5-10 years" else 0
    model_inputs["Q16~For how many years have you used machine learning methods?_10-20 years"] = 1 if q16_bin == "10-20 years" else 0

    # Q18
    model_inputs["Q18_5~Evolutionary Approaches"] = 1 if "Evolutionary Approaches" in q18 else 0
    model_inputs["Q18_7~Convolutional Neural Networks"] = 1 if "Convolutional Neural Networks" in q18 else 0
    model_inputs["Q18_12~Graph Neural Networks"] = 1 if "Graph Neural Networks" in q18 else 0
    model_inputs["Q18_4~(None)"] = 1 if "(None)" in q18 else 0

    # Q23
    roles = {
        "Data Analyst (Business, Marketing, Financial, Quantitative, etc.)": "Data Analyst",
        "Data Architect": "Data Architect",
        "Data Scientist": "Data Scientist",
        "Developer Advocate": "Developer Advocate",
        "Engineer (non-software)": "Engineer (non-software)",
        "Manager (Program, Project, Operations, Executive-level, etc.)": "Manager",
        "Other": "Other",
        "Research Scientist": "Research Scientist",
        "Software Engineer": "Software Engineer",
        "Teacher / Professor": "Teacher / professor",
        "(None)": "(None)"
    }
    for role in roles.values():
        model_inputs[f"Q23~Select the title most similar to your current role (or most recent title if retired): - Selected Choice_{role}"] = 1 if roles[q23] == role else 0

    # Q30
    spending_bins = {
        "1-99": "Q30~Approximately how much money have you spent on machine learning and/or cloud computing services at home or at work in the past 5 years (approximate $USD)?_$1-$99",
        "1,000-9,999": "Q30~Approximately how much money have you spent on machine learning and/or cloud computing services at home or at work in the past 5 years (approximate $USD)?_$1,000-9,999",
        "10,000-99,999": "Q30~Approximately how much money have you spent on machine learning and/or cloud computing services at home or at work in the past 5 years (approximate $USD)?_$10,000-99,999",
        "100,000 or more": "Q30~Approximately how much money have you spent on machine learning and/or cloud computing services at home or at work in the past 5 years (approximate $USD)?_$100,000 or more"
    }
    for spending_bin, feature_name in spending_bins.items():
        model_inputs[feature_name] = 1 if q30_bin == spending_bin else 0

    # Add additional feature preprocessing logic as necessary...

    input_df = pd.DataFrame([model_inputs])
    return input_df


# Predict Button
if st.button("Submit"):
    try:
        input_df = preprocess_inputs()

        # Align with model's expected features
        expected_features = set(model.model.exog_names)
        missing_features = expected_features - set(input_df.columns)
        extra_features = set(input_df.columns) - expected_features
        # Add missing features
        for feature in missing_features:
            input_df[feature] = 0

        # Remove extra features
        input_df = input_df.drop(columns=extra_features)

        # Align column order
        input_df = input_df[list(expected_features)]
        # Prediction
        prediction = model.predict(input_df)
        #Set prediction into dollar format
        formatted = "${:,.2f}".format(prediction[0])
        st.success(f"The model predicts: {formatted}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
