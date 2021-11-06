

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st
import joblib 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

#pickle_in = open("iris1.ml","rb")
#classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def insurance_prediction(Age,Driving_License,Region_Code,Previously_Insured,Annual_Premium,Policy_Sales_Channel,Vintage, a,b,c,Female,Male):
    
   
    classifier=joblib.load('insurance.ml')
    prediction=classifier.predict([[Age,Driving_License,Region_Code,Previously_Insured,Annual_Premium,Policy_Sales_Channel,Vintage,a,b,c,Female,Male]])
    print(prediction)
    return prediction



def main():
    st.title("insurance ml")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">insurance_predicting_ML_App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.text_input("Age ","Type Here")
    Driving_License= st.text_input("Driving_License","Type Here")
    Region_Code= st.text_input("Region_Code","Type Here")
    Previously_Insured= st.text_input("Previously_insured","Type Here")
    Annual_Premium=st.text_input("Annual_Premium","Type Here")
    Policy_Sales_Channel=  st.text_input("Policy_Sales_Channel","Type Here")                            
    Vintage=st.text_input("Vintage","Type Here")
    a=st.text_input("1-2 Year","Type Here")
    b=st.text_input("< 1 Year ","Type Here")
    c=st.text_input("> 2 Years ","Type Here")
    Female=st.text_input("Female ","Type Here")
    Male=st.text_input("Male","Type Here")
    result=""
    if st.button("Predict"):
        result=insurance_prediction(Age,Driving_License,Region_Code,Previously_Insured,Annual_Premium,
        Policy_Sales_Channel,Vintage,a,b,c,Female,Male)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()