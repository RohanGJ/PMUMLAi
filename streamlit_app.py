import streamlit as st
import pandas as pd
import pickle
import requests 
from sklearn.preprocessing import LabelEncoder, StandardScaler

LE = LabelEncoder()
Scaler = StandardScaler()
xtr = pd.read_csv("https://github.com/RohanGJ/PMUMLAi/raw/refs/heads/master/xtr.csv",header = None, sep = ',')
Scaler.fit(xtr)

def load_model_from_github(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful
    model = pickle.loads(response.content)
    return model

pickle_url = "https://github.com/RohanGJ/PMUMLAi/raw/refs/heads/master/RFCV1.pkl"

model = load_model_from_github(pickle_url)

st.title('PREVENTIVE MAINTANANCE USING ML')

st.info('This MODEL predicts wheather an equipment is about to fail in the near future.')
 
with st.expander('**Error Inputs**'):
  st.write('Provide Error Counts for each attributes')
  E1C    = st.selectbox('Error1Count',[0,1,2])
  E2C    = st.selectbox('Error2Count',[0,1,2])
  E3C    = st.selectbox('Error3Count',[0,1,2])
  E4C    = st.selectbox('Error4Count',[0,1,2])
  E5C    = st.selectbox('Error5Count',[0,1,2])
  
with st.expander('**Voltage Inputs**'):
  st.write('Provide Mean and SD of VTin')
  Vmean  = st.slider('Mean Voltage',150.00,220.00,170.00)
  Vsd    = st.slider('Standard Deviation (Voltage)',6.50,27.50,14.50)

with st.expander('**Rotation Inputs**'):
  st.write('Provide Mean and SD of RTin')
  Rmean  = st.slider('Mean Rotation',260.00,500.00,450.00)
  Rsd    = st.slider('Standard Deviation (Rotation)',19.00,105.00,50.00)

with st.expander('**Pressure Inputs**'):
  st.write('Provide Mean and SD of PRin')
  Pmean  = st.slider('Mean Pressure',90.00,155.00,100.00)
  Psd    = st.slider('Standard Deviation (Pressure)',4.00,29.00,9.50)

with st.expander('**Vibration Inputs**'):
  st.write('Provide Mean and SD of VBin')
  VBmean  = st.slider('Mean Vibration',35.00,65.00,40.00)
  VBsd    = st.slider('Standard Deviation (Vibration)',2.00,14.00,5.00)

MID    = st.slider('Machine ID',0,99,1)
AGE    = st.slider('Age',0,20,1)
MODEL  = st.selectbox('Model', [range(0,100)])
FinLis = {
    'machineID'    : MID,
    'voltmean'     : Vmean,
    'rotatemean'   : Rmean,
    'pressuremean' : Pmean,
    'vibrationmean': VBmean, 
    'voltsd'       : Vsd,
    'rotatesd'     : Rsd, 
    'pressuresd'   : Psd, 
    'vibrationsd'  : VBsd,
    'error1count'  : E1C,
    'error2count'  : E2C, 
    'error3count'  : E3C, 
    'error4count'  : E4C, 
    'error5count'  : E5C,
    'model'        : MODEL, 
    'age'          : AGE, 
}
STDF = pd.DataFrame(FinLis)

STDF = Scaler.fit_transform(STDF)

st.subheader("USER INPUTS :")
st.write(STDF)

st.subheader("Prediction : ")
st.write(model.predict(STDF))

st.subheader("Prediction Probability :")
st.write(model.predict_proba(STDF))
