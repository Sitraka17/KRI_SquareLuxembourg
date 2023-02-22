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
st.set_page_config(page_title='Retail Credit Risk Management', page_icon=':bar_chart:', layout='wide')

# Title
st.title('🛍️ Retail Credit Risk Management')

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
    st.warning('Please select at least one blockchain to see the metrics.')


# Cross Chain Comparison
else:
    subtab_overview, subtab_prices, subtab_heatmap = st.tabs(['Overview', 'Prices', 'Heatmap'])
    with subtab_overview:
        st.subheader('Overview')
        df = nfts_overview.query('Blockchain == @options')

        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(df, x='Blockchain', y='Volume', color='Blockchain', title='Total Sales Volume', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Volume [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = px.bar(df, x='Blockchain', y='Sales', color='Blockchain', title='Total Sales', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Sales', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.bar(df, x='Blockchain', y='Buyers', color='Blockchain', title='Total Buyers', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Buyers', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = px.bar(df, x='Blockchain', y='NFTs', color='Blockchain', title='Total Traded NFTs', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='NFTs', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c3:
            fig = px.bar(df, x='Blockchain', y='Collections', color='Blockchain', title='Total Traded Collections', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Collections', xaxis={'categoryorder':'total ascending'})
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

        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.pie(df, values='Buyers', names='Blockchain', title='Share of Total Buyers')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = px.pie(df, values='NFTs', names='Blockchain', title='Share of Traded NFTs')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c3:
            fig = px.pie(df, values='Collections', names='Blockchain', title='Share of Total Traded Collections')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        st.subheader('Activity Over Time')
        df = nfts_daily.query('Blockchain == @options')
        c1, c2 = st.columns(2)
        with c1:
            fig = px.line(df, x='Date', y='Volume', color='Blockchain', title='Daily Sales Volume', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume [USD]')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df, x='Date', y='Sales', color='Blockchain', title='Daily Sales', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Sales')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = px.line(df, x='Date', y='Buyers', color='Blockchain', title='Daily Buyers', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Buyers')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = px.line(df, x='Date', y='NFTs', color='Blockchain', title='Daily Traded NFTs', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='NFTs')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = px.line(df, x='Date', y='Collections', color='Blockchain', title='Daily Traded Collections', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Collections')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Blockchain == @i")['Date'],
                    y=df.query("Blockchain == @i")['Volume'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Sales Volume')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Blockchain == @i")['Date'],
                    y=df.query("Blockchain == @i")['Sales'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Sales')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Blockchain == @i")['Date'],
                    y=df.query("Blockchain == @i")['Buyers'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Buyers')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Blockchain == @i")['Date'],
                    y=df.query("Blockchain == @i")['NFTs'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Traded NFTs')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Blockchain == @i")['Date'],
                    y=df.query("Blockchain == @i")['Collections'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Traded Collections')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    with subtab_prices:
        st.subheader('Overview')
        df = nfts_overview.query('Blockchain == @options')
        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.bar(df, x='Blockchain', y='PriceAverage', color='Blockchain', title='Average NFT Prices', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Average [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = px.bar(df, x='Blockchain', y='PriceMedian', color='Blockchain', title='Median NFT Prices', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Median [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c3:
            fig = px.bar(df, x='Blockchain', y='PriceMax', color='Blockchain', title='Maximum NFT Prices', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Maximum [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        st.subheader('Activity Over Time')
        df = nfts_daily.query('Blockchain == @options')

        fig = px.line(df, x='Date', y='PriceAverage', color='Blockchain', title='Daily Average NFT Prices', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Average [USD]')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.line(df, x='Date', y='PriceMedian', color='Blockchain', title='Daily Median NFT Prices', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Median [USD]')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.line(df, x='Date', y='PriceMax', color='Blockchain', title='Daily Maximum NFT Prices', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Maximum [USD]')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    with subtab_heatmap:
        st.subheader('Sales')
        df = nfts_heatmap.query('Blockchain == @options')
        c1, c2 = st.columns(2)
        with c1:
            df = nfts_heatmap.query("Blockchain == @options")
            df['Volume'] = df.groupby('Blockchain')['Volume'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Day', z='Volume', histfunc='avg', title='Daily Heatmap of Normalized Sales Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = nfts_heatmap.query("Blockchain == @options")
            df['Sales'] = df.groupby('Blockchain')['Sales'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Day', z='Sales', histfunc='avg', title='Daily Heatmap of Normalized Sales')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = nfts_heatmap.query("Blockchain == @options")
            df['Buyers'] = df.groupby('Blockchain')['Buyers'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Day', z='Buyers', histfunc='avg', title='Daily Heatmap of Normalized Buyers')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = nfts_heatmap.query("Blockchain == @options")
            df['NFTs'] = df.groupby('Blockchain')['NFTs'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Day', z='NFTs', histfunc='avg', title='Daily Heatmap of Normalized Traded NFTs')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = nfts_heatmap.query("Blockchain == @options")
            df['Collections'] = df.groupby('Blockchain')['Collections'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Day', z='Collections', histfunc='avg', title='Daily Heatmap of Normalized Traded Collections')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        with c2:
            df = nfts_heatmap.query("Blockchain == @options")
            df['Volume'] = df.groupby('Blockchain')['Volume'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Hour', z='Volume', histfunc='avg', title='Hourly Heatmap of Normalized Sales Volume', nbinsy=24)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days, dtick=2)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = nfts_heatmap.query("Blockchain == @options")
            df['Sales'] = df.groupby('Blockchain')['Sales'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Hour', z='Sales', histfunc='avg', title='Hourly Heatmap of Normalized Sales', nbinsy=24)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days, dtick=2)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = nfts_heatmap.query("Blockchain == @options")
            df['Buyers'] = df.groupby('Blockchain')['Buyers'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Hour', z='Buyers', histfunc='avg', title='Hourly Heatmap of Normalized Buyers', nbinsy=24)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days, dtick=2)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = nfts_heatmap.query("Blockchain == @options")
            df['NFTs'] = df.groupby('Blockchain')['NFTs'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Hour', z='NFTs', histfunc='avg', title='Hourly Heatmap of Normalized Traded NFTs', nbinsy=24)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days, dtick=2)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = nfts_heatmap.query("Blockchain == @options")
            df['Collections'] = df.groupby('Blockchain')['Collections'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Hour', z='Collections', histfunc='avg', title='Hourly Heatmap of Normalized Traded Collections', nbinsy=24)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days, dtick=2)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        st.subheader('Prices')
        c1, c2 = st.columns(2)
        with c1:
            df = nfts_heatmap.query("Blockchain == @options")
            df['PriceAverage'] = df.groupby('Blockchain')['PriceAverage'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Day', z='PriceAverage', histfunc='avg', title='Daily Heatmap of Normalized Average NFT Prices')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = nfts_heatmap.query("Blockchain == @options")
            df['PriceMedian'] = df.groupby('Blockchain')['PriceMedian'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Day', z='PriceMedian', histfunc='avg', title='Daily Heatmap of Normalized Median NFT Prices')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = nfts_heatmap.query("Blockchain == @options")
            df['PriceMax'] = df.groupby('Blockchain')['PriceMax'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Day', z='PriceMax', histfunc='avg', title='Daily Heatmap of Normalized Maximum NFT Prices')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        with c2:
            df = nfts_heatmap.query("Blockchain == @options")
            df['PriceMax'] = df.groupby('Blockchain')['PriceMax'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Hour', z='PriceMax', histfunc='avg', title='Hourly Heatmap of Normalized Maximum NFT Prices', nbinsy=24)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days, dtick=2)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
