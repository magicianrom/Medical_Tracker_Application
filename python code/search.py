import streamlit as st
import pandas as pd

st.markdown("# My Medicine")
st.sidebar.markdown("# Browser an ingredient/symptoms and receive a tip")

search = st.text_input("enter an ingredient or symptoms")


st.image("../../images/pills1.png", width=300 )
medicine = pd.read_csv("../../excercises/week2/Medical_Tracker.csv")

#search finds values from either symptoms or ingredient in medical data
if st.button("Search"):
    if search:
        results = medicine[
        medicine['symptoms'].str.contains(search) |
        medicine['ingredient'].str.contains(search)
    ]
    st.success("Medication searched successfully!")
    st.dataframe(results)

else:
    st.warning("Please enter an ingredient or symptom.")

#randomizes a value from the safety column in medical data
tip = st.button("Random tip")

if tip:
    random = medicine['safety'].sample()
    st.success('Tip')
    st.dataframe(random)



