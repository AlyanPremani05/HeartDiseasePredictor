import streamlit as st
import pandas as pd
import joblib

page = st.sidebar.radio("Select one:", ["Model","Performance Graphs", "About"])
# st.sidebar.image("icon.png")
st.logo(image ="icon.png",size="large")

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
    resting_BP = st.number_input("Resting BP", 50,250)
    
    st.markdown("#### **Enter your Cholesterol Level (mg/dl)**")
    cholesterol = st.number_input("Cholesterol",50,400)
    
    st.markdown("#### **Enter your Fasting Blood Sugar**")
    fasting_BS = st.radio("Fasting Blood Sugar", ["1 :blue[(if FastingBS > 120 mg/dl)]", "0 :blue[(otherwise)]"])
    
    st.markdown("#### **Enter your Resting ECG**")
    resting_ECG = st.radio("Resting ECG", ["LVH :blue[(showing probable or definite left ventricular hypertrophy by Estes' criteria)]","Normal","ST :blue[(having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV))]"])
    
    st.markdown("#### **Enter your Max Heart Rate (BPM)**")
    max_HR = st.number_input("Max Heart Rate",60,202)
    
    st.markdown("#### **Do you experience Exercise Induced Angina?**")
    exercise_angina = st.radio("Excercise Angina", ["YES", "NO"])
    
    st.markdown("#### **Old Peak (ST depression caused by activity)**")
    old_peak = st.slider("Old peak", float(0),float(10),step=0.1)
    
    st.markdown("#### **ST Slope (the slope of the peak exercise ST segment)**")
    st_slope = st.radio("ST Slope",["Down :blue[(downsloping)]","Flat :blue[(Flat)]","Up :blue[(Upsloping)]"])
    
    user_input = {}
    user_input["Age"] = age
    
    if sex == "Male":
        user_input["Sex"] = 1
    else:
        user_input["Sex"] = 0

    user_input["RestingBP"] = resting_BP

    user_input["Cholesterol"] = cholesterol

    if fasting_BS == "1 :blue[(if FastingBS > 120 mg/dl)]":
        user_input["FastingBS"] = 1
    else:
        user_input["FastingBS"] = 0

    user_input["MaxHR"] = max_HR

    if exercise_angina == "YES":
        user_input["ExerciseAngina"] = 1
    else:
        user_input["ExerciseAngina"] = 0

    user_input["Oldpeak"] = old_peak

    if chest_PT == "ASY :blue[(Asymptomatic pain)]":
        user_input["ChestPainType_ASY"] = 1
    else:
        user_input["ChestPainType_ASY"] = 0

    if chest_PT == "ATA :blue[(Atypical Angina)]":
        user_input["ChestPainType_ATA"] = 1
    else:
        user_input["ChestPainType_ATA"] = 0

    if chest_PT == "NAP :blue[(Non-Atypical Angina)]":
        user_input["ChestPainType_NAP"] = 1
    else:
        user_input["ChestPainType_NAP"] = 0

    if chest_PT == "TA :blue[(Typical Angina)]":
        user_input["ChestPainType_TA"] = 1
    else:
        user_input["ChestPainType_TA"] = 0

    if resting_ECG == "LVH :blue[(showing probable or definite left ventricular hypertrophy by Estes' criteria)]":
        user_input["RestingECG_LVH"] = 1
    else:
        user_input["RestingECG_LVH"] = 0


    if resting_ECG == "Normal":
        user_input["RestingECG_Normal"] = 1
    else:
        user_input["RestingECG_Normal"] = 0
        
    if resting_ECG == "ST :blue[(having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV))]":
        user_input["RestingECG_ST"] = 1
    else:
        user_input["RestingECG_ST"] = 0
        
    if st_slope == "Down :blue[(downsloping)]":
        user_input["ST_Slope_Down"] = 1
    else:
        user_input["ST_Slope_Down"] = 0

    if st_slope == "Flat :blue[(Flat)]":
        user_input["ST_Slope_Flat"] = 1
    else:
        user_input["ST_Slope_Flat"] = 0
    
    if st_slope == "Up :blue[(Upsloping)]":
        user_input["ST_Slope_Up"] = 1
    else:
        user_input["ST_Slope_Up"] = 0

    df = pd.DataFrame([user_input])
    if st.button("Submit"):
        rand_forest = joblib.load("../HeartDisease.pkl")
        prediction = rand_forest.predict(df)
        if prediction[0] == 1:
            st.error("YOU HAVE A HIGH RISK OF HEART DISEASE")
        else:
            st.success("YOU DO NOT HAVE A HEART DISEASE")
            st.balloons()
    
elif page=="Performance Graphs":
    st.title("Performance Graphs")
    curves = st.select_slider("Slide to see the Performance Graphs\n" ,options=["Confusion Matrix","Feature Importance","ROC Curve"],)
    if curves == "Confusion Matrix":
        st.header("Confusion Matrix")
        st.image("../PERFORMANCE_GRAPHS/Confusion Matrix.png")
        
    elif curves == "Feature Importance":
        st.header("Feature Importance")
        st.image("../PERFORMANCE_GRAPHS/feature_importance.png")
    else:
        st.header("ROC Curve")
        st.image("../PERFORMANCE_GRAPHS/ROC Curve.png")
elif page =="About":
    st.title("👨‍💻 About the Developer")
    st.snow()
    st.markdown("""
    ## **Hi, I'm Alyan Premani!**  
    This app was built as part of a data science and machine learning project to predict heart disease based on patient inputs.
    I have trained only a single model(Random Forest) for now But I will train more models in the future to compare performance.

    - Tools used: Streamlit,scikit-learn, pandas, matplotlib, Seaborn
    - Model: Random Forest trained on a public dataset
    - GitHub Repo: [Click here](https://github.com/AlyanPremani05/HeartDiseasePredictor/)

    I DO NOT own the dataset. The dataset was taken from [Kaggle](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)

    I built this app for :red[educational purposes] only. It's not intended for clinical use.  
    Feel free to explore the repo and suggest improvements!
    """)
        