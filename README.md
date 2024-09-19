# Predicting Student Final Grade

<p align="justify">
  This project aims to predict student academic performance based on multiple factors like study hours, parental support, extracurricular activities, and more. 
  By using a machine learning model (Random Forest), the project allows to predict student scores and identify key factors influencing student success.
  The project also includes an interactive interface built with Streamlit for easy data input and real-time predictions.
</p>

## Project Overview

<p align="justify">
This project focuses on predicting student academic performance by analyzing various factors such as study hours, parental education, parental support, and extracurricular activities.
The Random Forest model is trained on historical student data, providing accurate predictions on future student scores. 
The Streamlit-powered web interface allows users to input data and get real-time predictions, making the model accessible and easy to use for educators and administrators.
</p>

## Data Description

The dataset used in this project includes the following key features:

- **Age**: The age of the student.
- **Gender**: Male or Female, encoded for the model.
- **Ethnicity**: The ethnic background of the student.
- **Parental Education**: The highest level of education completed by the student's parents.
- **Study Time Weekly**: The number of hours a student spends studying each week.
- **Absences**: The number of classes a student has missed.
- **Tutoring**: Whether the student receives tutoring (Yes/No).
- **Parental Support**: Levels of parental support categorized as None, Low, Medium, High, and Very High.
- **Extracurricular Activities**: Participation in activities beyond the classroom.
- **Sports**: Whether the student participates in sports.
- **Music**: Participation in music-related activities.
- **Volunteering**: Involvement in volunteering.

The data is preprocessed and split into training and testing sets for building a regression model that predicts students' final scores.

## Installation

Follow these steps to set up the project:

1. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    ```

2. **Activate Virtual Environment**
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

Once the environment is set up, you're ready to run the project.

## Model Details

We utilize a **Random Forest Regressor** to predict student scores based on the above features. The model is trained and saved using **joblib**, and can be reused without retraining.

- **Model Used**: Random Forest Regressor
- **Evaluation Metrics**: Mean Squared Error, R-squared
- **Input Features**: Age, Gender, Study Time, Parental Support, etc.

## How to Run the Project

### Frontend (Streamlit Interface)

The frontend interface is powered by **Streamlit**, allowing users to input student data interactively and receive predictions in real time.

1. Open your terminal and navigate to the project folder.
2. Activate your virtual environment:
   ```bash
   venv\Scripts\activate  # for Windows
   source venv/bin/activate  # for macOS/Linux
   ```
3. Run the Streamlit app
   ```
   streamlit run app.py
   ```
## Features

- **Real-time Predictions**: Enter student details and get a predicted academic score instantly.
- **Interactive UI**: Simple and intuitive user interface for entering features like study time, absences, and parental support.
- **Model Accuracy**: Uses a robust Random Forest model with high prediction accuracy, evaluated using Mean Squared Error and R-squared.

## Contributors (Student Final Grade Prediction)
- Jeena Nakarmi
- Nimesh Shakya
- Subekshya Kadel
- Sujal Koju

