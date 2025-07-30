import streamlit as st
# import pandas as pd

page = st.sidebar.radio("Select one:", ["Model","Performance Curves", "Documentation"])

if page=="Model":
    st.title("HEART DISEASE PREDICTOR")
    st.write("This model is for :red[EDUCATIONAL PURPOSE ONLY] and It is :red[NOT] a replacement for doctors/Professionals :(")
    
    st.markdown("#### **Enter your age**")
    age = st.number_input("Age", 0, 120)
    
    st.markdown("#### **Enter your sex**")
    sex = st.radio("Sex", ["Male", "Female"])
    
    st.markdown("#### **Enter your Chest Pain type**")
    chest_PT = st.radio("Pain Type", ['ATA :blue[(Atypical Angina)]','NAP :blue[(Non-Atypical Angina)]','ASY :blue[(Asymptomatic pain)]','TA :blue[(Typical Angina)]'])
    
    st.markdown("#### **Enter your Resting Blood Pressure (mm Hg)**")
    resting_BP = st.number_input("Resting BP", 10,500)
    
    st.markdown("#### **Enter your Cholesterol Level (mg/dl)**")
    cholesterol = st.number_input("Cholesterol",10,500)
    
    st.markdown("#### **Enter your Fasting Blood Sugar**")
    fasting_BS = st.radio("Fasting Blood Sugar", ["1 :blue[(if FastingBS > 120 mg/dl)]", "0 :blue[(otherwise)]"])
    
    st.markdown("#### **Enter your Resting ECG**")
    resting_ECG = st.radio("Resting ECG", ["Normal","ST :blue[(having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV))]","LVH :blue[(showing probable or definite left ventricular hypertrophy by Estes' criteria)]"])
    
    st.markdown("#### **Enter your Max Heart Rate (BPM)**")
    max_HR = st.number_input("Max Heart Rate",60,202)
    
    st.markdown("#### **Do you experience Exercise Induced Angina?**")
    exercise_angina = st.radio("Excercise Angina", ["YES", "NO"])
    
    st.markdown("#### **Old Peak (ST depression caused by activity)**")
    old_peak = st.slider("Old peak", float(0),float(10),step=0.1)
    
    st.markdown("#### **ST_Slope (the slope of the peak exercise ST segment)**")
    st_slope = st.radio("ST_Slope",["Up :blue[(Upsloping)]", "Flat :blue[(Flat)]", "Down :blue[(downsloping)]"])
    
    st.button("Submit")
    
elif page=="Performance Curves":
    st.title("Performance Curves")
    curves = st.select_slider("Slide to see the Performance Curves\n" ,options=["Confusion Matrix","Data Split","ROC Curve"],)
    if curves == "Confusion Matrix":
        st.header("Confusion Matrix")
        #TODO st.image()
    elif curves == "Data Split":
        st.header("Data Split (Bar graph)")
        #TODO st.image()
    else:
        st.header("ROC Curve")
        #TODO st.image()
