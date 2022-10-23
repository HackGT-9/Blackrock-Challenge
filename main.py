from re import S
import streamlit as st
import pandas as pd
import pandas as pd 
import plotly_express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit.components.v1 as components
st.set_page_config(layout="wide")
st.title("Financial Literacy: ✨ Explained✨ " )

st.sidebar.title("Navigation")
st.sidebar.markdown("Navigate to the page you want to visit")

page = st.sidebar.selectbox("Select a page", ["Home", "Private Sector", "Public/Government Sector"])


# this would be much faster rather than caching the entire page.
def main():
    if page == "Home":
        st.write("Welcome to the Volatility Explained! This is a website that aims to explain the basics of financial literacy and market volatility to the average person. We hope you enjoy your stay!")
        
        
        #TODO: #5 get some financial API to show SP500 and NASDAQ and DOW Jones here. Just simple this week's data, does not have to update real-time. 
        st.header("What is market volatility?")
        st.write("Market volatility essentially means the change. Things change, prices change. The frequency these prices change matter so we can predict the growth. When the market rises and falls at random situations, market is said to be _volatile_.")
        st.header("Wait, so it's a normal thing?")
        st.write("Certainly. If prices stayed the same thing, we'd always be in the same situation, there would be no _decline_, but there'd also be no _growth_.")
        
        st.header("What causes market volatility?")
        st.write("Well, the financial market isn't really a one way road where we know where things start and where things end. It's more like this:")
        st.image('./files/48100391372_213a56dcba_c.jpg')
        st.write("Every invidiual is a part of what makes the _economy_ and could be a part of what we call the _financial market_. Within this guide, we've studied the effects of market volatility and relation based on several things called sectors.")
        
        st.header("How do we know whether the market is volatile or not?")
        
        st.write("Several ways of measurement are used to determine the volatility of the market.Generally speaking, we can use certain charts that are presented below to determine the volatility of the market. A very common index that's used is VIX, which is further defined in 'Private Sector' page.Beware that it's quite common in the finance field to represent things with charts and graphs, and charts could be used to deceive you. Here's an example chart from the Federal Bank of St.Louis Dataset:")
        st.image('https://fred.stlouisfed.org/graph/fredgraph.png?g=Vau5', width=800)
        
        st.write("The black line does not provide proper information, does it? It is almost as if the interest rates that are presented by the Federal Reserve has _no effect_ on S&P 500 performance.However, take a look at this chart, which presents the same data with different scaling:")
        
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
        
        
        st.write("From the graph on the top, we can see that there seems to be a reverse correlation between the graphs. As one increases, the other decreases. This is an important matter to consider when looking at charts. The Federal Reserve has a lot of power in the economy, and it's important to know how it affects the market and how visualization is chosen to be is quite important to the narrative.")
        
        
        st.header("What are sectors?")
        st.write("Sectors are small sets of groups that are a part of the economy that affect the movements of financial markets. We mainly talk about two sectors: the _private sector_ and the _public sector_. You can use the navigation bar to the left to navigate to the page you want to visit and learn more about each sector and their interactions with the financial market and with each other.")
        
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
        st.plotly_chart(fig, use_container_width=True)
        
        
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