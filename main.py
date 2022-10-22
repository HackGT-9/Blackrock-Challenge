import streamlit as st

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
    elif page == "Public/Government Sector":
        st.write("Although public sector is used synonymously, with this one we are referring to the PEOPLE. This is us, the people who are affected by the market volatility with having the least capability to change it unless they act as the government.")
        st.write("There is multiple ways that the government can influence the economy when the market volatility is high.")
        # TODO: get a graph here https://seekingalpha.com/article/4470812-rising-interest-rates-matter-stock-market
        # TODO: READ this to get some insight https://www.investopedia.com/articles/economics/11/how-governments-influence-markets.asp
if __name__ == "__main__":
    main()