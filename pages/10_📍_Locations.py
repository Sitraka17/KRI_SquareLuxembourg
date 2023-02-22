# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import data

# Global Variables
theme_plotly = None # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Config
st.set_page_config(page_title='Risk Management by regions 📍', page_icon=':bar_chart:', layout='wide')

# Title
st.title('📍 Risk Management by regions')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Data Sources
nfts_overview = data.get_data('NFTs Overview')
nfts_daily = data.get_data('NFTs Daily')
nfts_heatmap = data.get_data('NFTs Heatmap')

# Filter
options = st.multiselect(
    '**Select your desired Retail Credit Risk:**',
    options=nfts_overview['Blockchain'].unique(),
    default=nfts_overview['Blockchain'].unique(),
    key='nfts_options'
)

# Selected Blockchain
if len(options) == 0:
    st.warning('Please select at least one to see the metrics.')


# Cross Chain Comparison
else:
    subtab_overview, subtab_prices, subtab_heatmap = st.tabs(['Overview', 'Prices', 'Heatmap'])
    with subtab_overview:
        st.subheader('Overview')
        df = nfts_overview.query('Blockchain == BSC')

        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(df, x='Blockchain', y='Volume', color='Blockchain', title='Total Sales Volume', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Volume [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = px.bar(df, x='Blockchain', y='Sales', color='Blockchain', title='Total Sales', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Sales', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

       

        st.subheader('Market Shares')
        c1, c2 = st.columns(2)
        with c1:
            fig = px.pie(df, values='Volume', names='Blockchain', title='Share of Total Sales Volume')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = px.pie(df, values='Sales', names='Blockchain', title='Share of Total Sales')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

