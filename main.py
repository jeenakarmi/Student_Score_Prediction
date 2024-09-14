import streamlit as st
import pandas as pd
import joblib
import numpy as np

#loading trained model
model = joblib.load('random_forest_model.pkl')

st.set_page_config(layout="wide")

#option dictionaries
gender_options = {
    'Male': 0, 'Female': 1
}
ethnicity_options = {
    'Caucasian': 0, 'African American': 1, 'Asian': 2, 'Other': 3
}
parental_education_options = {
    'None': 0, 'High School': 1, 'Some College': 2, 'Bachelors': 3, 'Higher': 4
}
parental_support_options = {
    'None': 0, 'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4
}
binary_options = {
    'No': 0, 'Yes': 1
}

def get_user_input():
    with st.form(key='my_form'):
        Age = st.slider('Age', 15, 22, 18)
        Gender = st.radio('Gender', list(gender_options.keys()), horizontal= True)
        Ethnicity = st.radio('Ethnicity', list(ethnicity_options.keys()), horizontal= True)
        ParentalEducation = st.radio('Parental Education', list(parental_education_options.keys()), horizontal= True)
        StudyTimeWeekly = st.slider('Study Time Weekly', min_value=0, max_value=20, value=10)
        Absences = st.slider('Absences', 0, 30, 10)
        Tutoring = st.radio('Tutoring', list(binary_options.keys()), horizontal= True)
        ParentalSupport = st.radio('Parental Support', list(parental_support_options.keys()), horizontal= True)
        Extracurricular = st.radio('Extracurricular Activities', list(binary_options.keys()), horizontal= True)
        Sports = st.radio('Sports', list(binary_options.keys()), horizontal= True)
        Music = st.radio('Music', list(binary_options.keys()), horizontal= True)
        Volunteering = st.radio('Volunteering', list(binary_options.keys()), horizontal= True)
        submit_button = st.form_submit_button(label='Submit')
    
    # Creating dictionary with the input
    user_data = {
        'Age': Age,
        'Gender': gender_options[Gender],
        'Ethnicity': ethnicity_options[Ethnicity],
        'ParentalEducation': parental_education_options[ParentalEducation],
        'StudyTimeWeekly': StudyTimeWeekly,
        'Absences': Absences,
        'Tutoring': binary_options[Tutoring],
        'ParentalSupport': parental_support_options[ParentalSupport],
        'Extracurricular': binary_options[Extracurricular],
        'Sports': binary_options[Sports],
        'Music': binary_options[Music],
        'Volunteering': binary_options[Volunteering]
    }
    
    # Convert user input into a dataframe
    features = pd.DataFrame(user_data, index=[0])
    return features

if __name__ == "__main__":
    col1, col2, col3 = st.columns([2, 3, 2])
    with col2: 
        st.title('Student Score Prediction')

        # Display the input fields and get user input
        user_input = get_user_input()
    
    st.write('User Input:')
    # st.dataframe(user_input, width=1500)  # Customize width and height as needed
    st.table(user_input)

    # Make prediction using the trained model
    prediction = model.predict(user_input)

    # Display the predicted score
    st.write(f'Predicted Score: {prediction[0]:.2f}')