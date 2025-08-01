# Heart Disease Predictor
### Alyan Premani

A machine learning web application that predicts the likelihood of heart disease based on patient medical data. Built with Python and deployed using Streamlit.

## StreamLit App

**[Streamlit App](https://heartdisease--predictor.streamlit.app/)**

## Overview

This application uses a Random Forest machine learning model to predict heart disease risk based on various medical parameters including age, chest pain type, blood pressure, cholesterol levels, and other clinical indicators. 

## Features

- Interactive web interface for inputting patient data
- Real-time heart disease risk prediction
- Model performance visualization with confusion matrix and other metrics
- Clean, user-friendly design
- Fast prediction results

## Dataset

The model is trained on a comprehensive heart disease dataset containing the following features:
- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate Achieved
- Exercise Induced Angina
- ST Slope
- Old peak


## Technology Stack

- **Python**: Core programming language
- **Scikit-learn**: Machine learning model development
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib/Seaborn**: Data visualization
- **Joblib**: Model serialization

## Installation and Local Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Steps

1. Clone the repository:
```bash
git clone https://github.com/AlyanPremani05/HeartDiseasePredictor.git
cd HeartDiseasePredictor
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run Streamlit/streamlit_gui.py
```


## Usage

1. Access the web application through the provided link or local setup
2. Enter patient medical information in the input fields
3. Click the prediction button to get heart disease risk assessment
4. View the prediction result
5. Explore model performance metrics in the performance section


## Model Development

The machine learning model was developed using:
- Data preprocessing
- Exploratory data analysis
- Dataset Splitting
- Random Forest algorithm implementation
- Model evaluation using cross-validation

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## Disclaimer

This application is for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical decisions.