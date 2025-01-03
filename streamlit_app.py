import streamlit as st
import pandas as pd

st.title('PREVENTIVE MAINTANANCE USING ML')

st.info('This MODEL predicts wheather an equipment is about to fail in the near future.')

with st.expander('**Data Frame**'):
  st.write('Feature Dataset')
  DF = pd.read_csv("https://drive.google.com/file/d/1KdbROD9dBgTfBvP1roISbnZ_JyAR9OQ5/view?usp=drive_link")
  DF
