import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Loading trained model
model = joblib.load('random_forest_model.pkl')

def get_user_input():
    Age = st.slider('Age', 15, 22, 18)
    Gender = st.selectbox('Gender', [0, 1])
    Ethnicity = st.selectbox('Ethnicity', [0, 1, 2, 3, 4])
    ParentalEducation = st.selectbox('Parental Education', [0, 1, 2, 3, 4])
    StudyTimeWeekly = st.number_input('Study Time Weekly', min_value=0.0, max_value=40.0, value=10.0)
    Absences = st.slider('Absences', 0, 50, 10)
    Tutoring = st.selectbox('Tutoring', [0, 1])
    ParentalSupport = st.selectbox('Parental Support', [0, 1, 2, 3])
    Extracurricular = st.selectbox('Extracurricular Activities', [0, 1])
    Sports = st.selectbox('Sports', [0, 1])
    Music = st.selectbox('Music', [0, 1])
    Volunteering = st.selectbox('Volunteering', [0, 1])
    
    # Creating dictionary with the input
    user_data = {
        'Age': Age,
        'Gender': Gender,
        'Ethnicity': Ethnicity,
        'ParentalEducation': ParentalEducation,
        'StudyTimeWeekly': StudyTimeWeekly,
        'Absences': Absences,
        'Tutoring': Tutoring,
        'ParentalSupport': ParentalSupport,
        'Extracurricular': Extracurricular,
        'Sports': Sports,
        'Music': Music,
        'Volunteering': Volunteering
    }
    
    # Convert user input into a dataframe
    features = pd.DataFrame(user_data, index=[0])
    return features

if __name__ == "__main__":
    st.title('Student Score Prediction')

    # Display the input fields and get user input
    user_input = get_user_input()

    # Show the user input for confirmation
    st.write('User Input:')
    st.write(user_input)

    # Make prediction using the trained model
    prediction = model.predict(user_input)

    # Display the predicted score
    st.write(f'Predicted Score: {prediction[0]:.2f}')