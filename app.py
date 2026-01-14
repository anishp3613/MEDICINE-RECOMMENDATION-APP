# app.py
import streamlit as st
from medicine_data import medicine_db  # import database

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Streamlit App
# -------------------------------
st.set_page_config(page_title="Symptom-to-Medicine App", layout="wide")

# Sidebar for user inputs
st.sidebar.header("Patient Details")
age = st.sidebar.number_input("Enter your age", min_value=0, max_value=120, value=25)
allergies = st.sidebar.multiselect("Do you have any known allergies?", 
                                   ["Paracetamol", "Aspirin", "Benadryl", "Ranitidine", "Cetirizine", "Ibuprofen"])

st.sidebar.header("Symptom Selection")
symptom = st.sidebar.selectbox("Select your symptom", list(medicine_db.keys()))

# Layout: Columns
col1, col2 = st.columns([2, 3])

with col1:
    st.image("https://img.icons8.com/color/96/000000/medicine-bottle.png", width=100)
    st.write("## Symptom Info")
    st.write(f"**Selected Symptom:** {symptom}")

with col2:
    med_data = medicine_db.get(symptom)
    if med_data:
        # Age-specific warning
        if age < 12 and med_data['not_for_children']:
            st.warning(f"⚠ Not suitable for children: {', '.join(med_data['not_for_children'])}")
        elif age >= 12:
            st.info("Suitable for adults")
        
        # Allergy alert
        allergy_conflicts = [a for a in allergies if a in med_data['allergy_risk']]
        if allergy_conflicts:
            st.error(f"⚠ Allergy Alert: You are allergic to {', '.join(allergy_conflicts)}")
        
        # Show medicines
        st.subheader("Recommended Medicines")
        st.write("**Primary Medicine:**", ", ".join(med_data['medicines']))
        st.write("**Alternative Medicines:**", ", ".join(med_data['alternatives']))
        st.write("**Precautions:**", med_data['precaution'])
        st.write("**Timing:**", med_data['timing'])

# -------------------------------
# Extra: Symptom statistics chart
# -------------------------------
st.markdown("---")
st.subheader("Symptom Distribution (Sample Data)")

sample_symptoms = ["Fever", "Headache", "Cold", "Cough", "Stomach Pain", "Fever", "Cold", "Headache", "Cough", "Fever"]
df = pd.DataFrame(sample_symptoms, columns=["Symptom"])
symptom_counts = df["Symptom"].value_counts()

fig, ax = plt.subplots()
symptom_counts.plot(kind="bar", color="skyblue", ax=ax)
ax.set_ylabel("Number of Cases")
ax.set_title("Sample Symptom Distribution")
st.pyplot(fig)

# -------------------------------
# Footer
# -------------------------------

st.warning("""
⚠️ **Disclaimer:** This app is for **educational purposes only**. 
Always **consult a qualified doctor** before taking any medication.
""")
st.markdown("""
---
Developed using **Python & Streamlit**  
Get instant visual output, fully data-centric. No HTML/CSS/JS needed.  
Create and share custom web apps in hours, not weeks!
""")
