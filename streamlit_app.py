import streamlit as st
import pandas as pd

st.title('PREVENTIVE MAINTANANCE USING ML')

st.info('This MODEL predicts wheather an equipment is about to fail in the near future.')

with st.expander('**Data Frame**'):
  st.write('Feature Dataset')
  DF = pd.read_csv("https://raw.githubusercontent.com/RohanGJ/PMUMLAi/refs/heads/master/features1.csv")
  DF
  
with st.expander('**INPUT**'):
  st.write('Inputs to Model')
  ageopt = list(range(0,20))
  age    = st.selectbox('age',ageopt)
