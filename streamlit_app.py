import streamlit as st
import pandas as pd
import pickle
import json
import requests 
from urllib.request import urlopen
from streamlit_lottie import st_lottie
from sklearn import sklearn

fail_logo_url = urlopen("https://raw.githubusercontent.com/RohanGJ/PMUMLAi/refs/heads/master/JSON%20Files/fail1.json")
pass_logo_url = urlopen("https://raw.githubusercontent.com/RohanGJ/PMUMLAi/refs/heads/master/JSON%20Files/pass.json")
pickle_url = "https://github.com/RohanGJ/PMUMLAi/raw/refs/heads/master/MODELS/MLPC.pkl"
url_fail = json.loads(fail_logo_url.read())
url_pass = json.loads(pass_logo_url.read())
  
def load_model_from_github(url):
  response = requests.get(url)
  response.raise_for_status()
  model = pickle.loads(response.content)
  return model

model = load_model_from_github(pickle_url)

st.title('MACHINE LEARNING')
st.info("Preventine Maintanance")

E1C,E2C,E3C,E4C,E5C = 0,0,0,0,0

Vmean,Rmean,Pmean,VBmean = 0.00,0.00,0.00,0.00

Vsd,Rsd,Psd,VBsd = 0.00,0.00,0.00,0.00

tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["Error_count","Voltage","Rotations","Pressure","Vibration","MISC"])

with tab1:
  st.write('Provide Error Counts for each attributes')
  E1C    = st.selectbox('Error1Count',[0,1,2,3,4])
  E2C    = st.selectbox('Error2Count',[0,1,2,3,4])
  E3C    = st.selectbox('Error3Count',[0,1,2,3,4])
  E4C    = st.selectbox('Error4Count',[0,1,2,3,4])
  E5C    = st.selectbox('Error5Count',[0,1,2,3,4])
  
with tab2:
  st.write('Provide Mean and SD of VTin')
  Vmean  = st.slider('Mean Voltage',110.00,280.00,170.00)
  Vsd    = st.slider('Standard Deviation (Voltage)',6.00,30.00,14.00)

with tab3:
  st.write('Provide Mean and SD of RTin')
  Rmean  = st.slider('Mean Rotation',0.00,720.00,360.00)
  Rsd    = st.slider('Standard Deviation (Rotation)',19.00,105.00,50.00)

with tab4:
  st.write('Provide Mean and SD of PRin')
  Pmean  = st.slider('Mean Pressure',0.00,200.00,100.00)
  Psd    = st.slider('Standard Deviation (Pressure)',4.00,30.00,9.00)

with tab5:
  st.write('Provide Mean and SD of VBin')
  VBmean  = st.slider('Mean Vibration',0.00,100.00,40.00)
  VBsd    = st.slider('Standard Deviation (Vibration)',2.00,14.00,5.00)
with tab6:
  MID    = st.slider('Machine ID',0,99,1)
  AGE    = st.slider('Age',0,20,1)
  modrang = list(range(0,100))
  MODEL  = st.selectbox('Model', modrang)

FinLis = {
      'machineID'    : [MID],
      'voltmean'     : [Vmean],
      'rotatemean'   : [Rmean],
      'pressuremean' : [Pmean],
      'vibrationmean': [VBmean], 
      'voltsd'       : [Vsd],
      'rotatesd'     : [Rsd], 
      'pressuresd'   : [Psd], 
      'vibrationsd'  : [VBsd],
      'error1count'  : [E1C],
      'error2count'  : [E2C], 
      'error3count'  : [E3C], 
      'error4count'  : [E4C], 
      'error5count'  : [E5C],
      'model'        : [MODEL], 
      'age'          : [AGE], 
  }

STDF = pd.DataFrame(FinLis)

def color_df(val):
  if val > 0 and val < 100:
    color = 'blue'
  elif val > 99:
    color = 'green'
  elif val == 0:
    color = 'red'
  else:
    color = 'orange'
  return f'background-color: {color}'

st.info("USER INPUTS :")
st.dataframe(STDF.iloc[:,[0,1,2,3,4,5,6,15]].style.applymap(color_df))
st.dataframe(STDF.iloc[:,7:-1].style.applymap(color_df))
#st.write(STDF[:][:8])

pred = []
STDF = STDF.values
pred = list(model.predict(STDF))

col1, col2 = st.columns(2, gap = "small")

col1.info("MODEL Eval")
col1.subheader("Prediction : ")
col1.write(model.predict(STDF))

col1.subheader("Prediction Probability :")
col1.write(model.predict_proba(STDF))

with col2:
  st.info("STATUS")
  if pred[0] == 0:
    st_lottie(url_pass, speed = 0.75, loop = False)
  elif pred[0] == 1:
   st_lottie(url_fail, speed = 0.75, loop = True, reverse = True) 
  else:
    st.info("Press Run model after selecting inputs")
