# Libraries Block 
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import data
import numpy as np

# Global Variables
theme_plotly = None # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Config
st.set_page_config(page_title='ERB', page_icon=':bar_chart:', layout='wide')

# Title
st.title('ERB')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Data Sources



#Chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A-Agriculture', 'C-Manufacturing', 'F-Construction'])

st.line_chart(chart_data)

