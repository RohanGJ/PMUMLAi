import streamlit as st
import pandas as pd

st.title('PREVENTIVE MAINTANANCE USING ML')

st.info('This MODEL predicts wheather an equipment is about to fail in the near future.')

with st.expander('**Data Frame**'):
  st.write('Feature Dataset')
  DF = pd.read_csv("https://raw.githubusercontent.com/RohanGJ/PMUMLAi/refs/heads/master/features1.csv")
  DF
  
with st.expander('**Error Inputs**'):
  st.write('Provide Error Counts for each attributes')
  age    = st.selectbox('AGE of machine',list(range(0,19)))
  E1C    = st.selectbox('Error1Count',[0,1,2])
  E2C    = st.selectbox('Error2Count',[0,1,2])
  E3C    = st.selectbox('Error3Count',[0,1,2])
  E4C    = st.selectbox('Error4Count',[0,1,2])
  E5C    = st.selectbox('Error5Count',[0,1,2])
