import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

medicine = pd.read_csv("../../excercises/week2/Medical_Tracker.csv")
my_medicine = pd.read_csv("../../excercises/week2/My_Medications.csv")

st.image("../../images/reminder1.png", width=300 )
st.title("Medical Tracker")

#select box to select medical name easily, as it fills fields such as ingredient, dosage, frequency.
client = st.selectbox(
    "Select your medicine",
    medicine["name"]
)

selected = medicine[medicine["name"] == client].iloc[0]

name = selected["name"]
ingredient = selected["ingredient"]
dosage = selected["dosage"]
frequency = selected["frequency_hours"]

#user inputs manually fields such as expiry date and libs such as datetime helps to indentify the next dosage
exp = st.text_input("What's the expiry date?")

if st.button("Taken medicine"):

    now = datetime.now()
    next = now + timedelta(hours=int(frequency))

    df = pd.DataFrame([{
        "name": selected["name"],
        "ingredient": selected["ingredient"],
        "dosage": selected["dosage"],
        "frequency": selected["frequency_hours"],
        "expiry": exp,
        "next_dosage": next
    }])

    my_medicine = pd.concat([my_medicine, df], ignore_index=True)
    my_medicine.to_csv("../../excercises/week2/My_Medications.csv", index=False)

    st.success("Medicine taken!")

st.write("Your medications")
st.dataframe(my_medicine)

#celebration complete button
if st.button("Complete", type="primary"):
    st.balloons()
    st.snow()