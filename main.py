import streamlit as st

st.title("Financial Literacy: Explained")

st.sidebar.title("Navigation")
st.sidebar.markdown("Navigate to the page you want to visit")

page = st.sidebar.selectbox("Select a page", ["Home", "Private Sector", "Public Sector", "Government Sector"])



# this would be much faster rather than caching the entire page.
def main():
    if page == "Home":
        st.write("Welcome to the home page")
    elif page == "Private Sector":
        st.title("Private Sector")
        st.write("This is the about page")
    elif page == "Government Sector":
        st.title("Government Sector")
        st.write("This is the contact page")
    elif page == "Public Sector":
        st.title("Public Sector")
        st.write("This is the about page")
        
if __name__ == "__main__":
    main()