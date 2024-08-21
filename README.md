# Titanic Survival Prediction App

## Overview

This Streamlit app predicts the survival status of Titanic passengers based on various features such as passenger class, age, fare, sex, and embarkation point. It leverages a logistic regression model trained on the Titanic dataset to provide predictions.

## Features

- Predict whether a passenger survived or not based on user inputs.
- Inputs include:
  - Passenger class (Pclass)
  - Age
  - Fare
  - Sex (male or female)
  - Embarked location (C, Q, S)
- Displays prediction results directly in the app.

## Installation

To run this app locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

python -m venv env
source env/bin/activate

python -m venv env
source env/bin/activate

pip install -r requirements.txt

streamlit run app.py
   
