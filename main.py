from re import S
import streamlit as st
import pandas as pd
import pandas as pd 
import plotly_express as px
import matplotlib.pyplot as plt
from sklearn import preprocessing
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.title("Financial Literacy: Explained")

st.sidebar.title("Navigation")
st.sidebar.markdown("Navigate to the page you want to visit")

page = st.sidebar.selectbox("Select a page", ["Home", "Private Sector", "Public/Government Sector"])


# this would be much faster rather than caching the entire page.
def main():
    if page == "Home":
        st.write("Welcome to the Volatility Explained! This is a website that aims to explain the basics of financial literacy to the average person. We hope you enjoy your stay!")
        
        
    elif page == "Private Sector":
        st.title("Private Sector")
        st.write("Private sector is generally the businesses and the companies. They  play the moving joint of an economy, like investors and people like you!")
        st.write("While Private sector can affect the volatility of the market by themselves, it's oftentimes affected bt how the public acts as well. For example, if the public is buying a lot of a certain stock, the price of that stock will go up. This is because the public is buying the stock, and the more people buy the stock, the more the price will go up. This is called the law of supply and demand. Without going too much into technical details, we can see that the public sector can affect the private sector, and vice versa.")
        st.write("A very common graph that's used to figure out the volatility of the market is the VIX. Also called the fear index by people with fancy suits, it shows the stock market's expectation of volatility. The higher it is, the more expectation of a volatility is expected.")
    
        df_vix = pd.read_csv("VIX/VIXCLS.csv")
        df_vix['DATE'] = pd.to_datetime(df_vix['DATE'])
        df_vix['VIXCLS'] = df_vix['VIXCLS'].replace('.', None)
        df_vix['VIXCLS'] = df_vix['VIXCLS'].dropna()
        # replace . wit None
        df_vix['VIXCLS'] = df_vix['VIXCLS'].astype(float)
        fig = px.line(df_vix, x="DATE", y="VIXCLS")
        st.plotly_chart(fig)
        
        
    elif page == "Public/Government Sector":
        st.title("Public/Government Sector")
        st.write("Although public sector is used synonymously, with this one we are referring to the PEOPLE. This is us, the people who are affected by the market volatility with having the least capability to change it unless they act as the government.")
        st.write("There is multiple ways that the government can influence the economy when the market volatility is high. One very common is the FED interest rates, the interest rates set up the tendency of banks lending money to others. The higher it is, the more difficult it gets for a buyer to borrow money. ")
        st.write("There's a significant correlation between how high the interest rates are, and how private companies move.")
        
        df_federal = pd.read_csv("interest_rate+sp/DFF.csv")
        df_sp = pd.read_csv("interest_rate+sp/SP500.csv")
        # remove the datapoints that have a . instead of a number
        df_federal['DATE'] = pd.to_datetime(df_federal['DATE'])
        df_sp['SP500'] = df_sp['SP500'].replace('.', None)
        df_sp = df_sp.dropna()
        df_sp['SP500'] = df_sp['SP500'].astype(float)
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace( go.Scatter(x=df_federal['DATE'], y=df_federal['DFF'], name="Federal Funds Rate"), secondary_y=True,)
        fig.add_trace( go.Scatter(x=df_sp['DATE'], y=df_sp['SP500'], name="S&P 500"), secondary_y=False,)
        fig.update_yaxes(title_text="<b>S&P 500</b> ", secondary_y=False)
        fig.update_yaxes(title_text="<b>Federal Funds Rate</b>", secondary_y=True)
        # add source 
        fig.update_layout( title="Federal Funds Rate vs S&P 500 <br>Source: FRED",  xaxis_title="Date", yaxis_title="Value", font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),)    
        st.plotly_chart(fig)
        
    
        
if __name__ == "__main__":
    main()