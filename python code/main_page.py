import streamlit as st
import pandas as pd

st.sidebar.markdown("# Medication tracker")

st.image("../../images/add1.png", width=300 )

st.title("Add New Medication")

medicine = pd.read_csv("../../excercises/week2/Medical_Tracker.csv")

#user adds input fields of their new medicine

name = st.text_input("Enter medicine's name")
ing = st.text_input("What's the ingredient")
cata = st.text_input("What's the category")
sym = st.text_input("What's the symptoms")
inst = st.text_input("What's the instructions")
dos = st.text_input("What's the dosage")
frq = st.text_input("What's the frequency hours")
saf = st.text_input("What's the safety precautions")
urg = st.text_input("What's the urgency")

#fields are saved and stored and ID is always different as it adds the last one by 1.

if st.button("Add Medication"):

    id = len(medicine) + 1

    updated_data = [{
        "id": id,
        "name": name,
        "ingredient": ing,
        "category": cata,
        "symptoms": sym,
        "instructions": inst,
        "dosage": dos,
        "frequency_hours": frq,
        "safety": saf,
        "urgency": urg
    }]

    df = pd.DataFrame(updated_data)

    #prints new data altogether by concatenation
    medicine = pd.concat([medicine, df])

    medicine.to_csv("../../excercises/week2/Medical_Tracker.csv", index=False)

    st.success("Medication added successfully!")

st.dataframe(medicine)
