# Import necessary libraries
import streamlit as st
import pandas as pd
import streamlit as st 
import pickle

# Function to load the pre-trained model
@st.cache
def load_model():
    
    pickle_in =open('final_model.sav','rb')
    classifier = pickle.load(pickle_in)

# Function to make predictions
def predict(model, input_data):
    # Make predictions using the loaded model
    prediction = model.predict(input_data)
    return prediction

# Streamlit app
def main():
    # Load the pre-trained model
    model = load_model()

    # Set the title and description of the app
    st.title("Admission Chance Predictor")
    st.write(
        "This app predicts the chance of admission based on the provided input features."
    )

    # Create input form for user input
    st.sidebar.header("Input Features")
    serial_no = st.sidebar.number_input("Serial No.", min_value=0)
    gre_score = st.sidebar.number_input("GRE Score", min_value=0, max_value=340)
    toefl_score = st.sidebar.number_input("TOEFL Score", min_value=0, max_value=120)
    university_rating = st.sidebar.slider("University Rating", min_value=1, max_value=5)
    sop = st.sidebar.slider("SOP", min_value=1, max_value=5)
    lor = st.sidebar.slider("LOR", min_value=1, max_value=5)
    cgpa = st.sidebar.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
    research = st.sidebar.radio("Research", ["No", "Yes"])

    # Convert the research input to binary (0 or 1)
    research_binary = 0 if research == "No" else 1

    # Prepare input data for prediction
    input_data = [[serial_no, gre_score, toefl_score, university_rating, sop, lor, cgpa, research_binary]]

    # Make predictions
    if st.button("Predict"):
        prediction = predict(model, input_data)
        st.success(f"The predicted chance of admission is: {prediction[0]:.2%}")

if __name__ == "__main__":
    main()

    
    