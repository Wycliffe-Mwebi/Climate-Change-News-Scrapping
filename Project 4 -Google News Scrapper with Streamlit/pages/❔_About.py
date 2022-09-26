import streamlit as st

# Page settings
st.set_page_config(
    page_title="About App",
    layout="wide",
    initial_sidebar_state="expanded"
 )

st.title("About this App")

st.write("This google news scrapper app allows you to scrape all the news that Google shows based on your input query. This web app is easy and intuitive to use.")

