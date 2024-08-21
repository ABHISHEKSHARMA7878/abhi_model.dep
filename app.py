import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the trained model
import joblib
model = joblib.load('logistic_regression_model.pkl')

def main():
    st.title("Titanic Survival Prediction")

    # User inputs
    pclass = st.selectbox("Pclass", [1, 2, 3])
    age = st.slider("Age", 0, 100, 30)
    fare = st.slider("Fare", 0, 500, 50)
    sex = st.radio("Sex", ["male", "female"])
    embarked = st.selectbox("Embarked", ["C", "Q", "S"])

    # Preprocess inputs
    data = pd.DataFrame({
        'Pclass': [pclass],
        'Age': [age],
        'Fare': [fare],
        'Sex_female': [1 if sex == "female" else 0],
        'Sex_male': [1 if sex == "male" else 0],
        'Embarked_C': [1 if embarked == "C" else 0],
        'Embarked_Q': [1 if embarked == "Q" else 0],
        'Embarked_S': [1 if embarked == "S" else 0]
    })

    # Prediction
    prediction = model.predict(data)[0]
    st.write(f"Prediction: {'Survived' if prediction == 1 else 'Not Survived'}")

if __name__ == "__main__":
    main()