import streamlit as st
import time
import pandas as pd
import numpy as np

# Main page content
st.markdown("# Welcome to my digital medical tracker app")
st.sidebar.markdown("# Main page")

#main points of the application
header = st.container()
header.write("Aim - Create a digital medication tracker and personal health record application that allows users to store, retrieve, and "
             "manage their daily medications and health logs through a Python application that stores data in a .csv file.")

st.write("Features - ")

#features of the application

st.write(" 1. Add a new medication to the tracker")
st.write(" 2. Search for medications by active ingredient/symptom ")
st.write(" 3. Receive a beneficial tip")
st.write(" 4. View all users logged medications")
st.write(" 5. Gain insights through a Chatbot")

#with st.expander("Show details"):
    #st.write("Here are the details...")
st.image("images/meds1.png", width=300)
#st.image("../../images/meds1.png", width=300 )

data = pd.read_csv("../../excercises/week2/Medical_Tracker.csv")

#added animation to process the data smoothly

tab1= st.tabs(["Data"])[0]

with st.spinner("Loading Tab 1..."):
    time.sleep(2)
with tab1:
    st.dataframe(data)



