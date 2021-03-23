# Importing  necessary dependencies
import numpy as np
import pandas as pd
import base64
import time

# Imporitng and setting up Streamlit - For creating the web app
import streamlit as st
import streamlit.components as stc

# Function to download the file as csv
def csv_downloader(data,name):
    csvfile = data.to_csv()
    b64 = base64.b64encode(csvfile.encode()).decode()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    timestr = name+timestr
    new_filename = "StockBot_{}_.csv".format(timestr)
    st.markdown("### Download as CSV ###")
    href = f'<a href = "data:file/csv;base64,{b64}" download = "{new_filename}">Click here to download your file!</a>'
    st.markdown(href,unsafe_allow_html=True)

# Streamlit app
def main():
    
    st.markdown("---")
    menu = ["Home","S&P 500","NASDAQ 100","Dow 30","About"]
    choice = st.selectbox("App navigator",menu)
    st.sidebar.markdown("---")
    st.sidebar.markdown("App developed by")
    st.sidebar.markdown("Kavin Karthikeyan")  
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Connect with me! ###")
    st.sidebar.write("[Linkedin](https://www.linkedin.com/in/kavin-karthikeyan/)")
    st.sidebar.write("[Github](https://github.com/kkarthi6)")
    st.sidebar.write("[Twitter](https://twitter.com/kkarthi96)")

    
    if choice == "Home":
        st.markdown("---")
        st.markdown("# Stock Bot #")
        st.image("https://images.unsplash.com/photo-1468254095679-bbcba94a7066?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1498&q=80",
        width=500)
        st.markdown("### Stock Bot lets you view and download data for top US indexes :money_with_wings: ###")
        
    elif choice == "S&P 500":
        st.subheader("S&P 500")
        df = pd.read_html('https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC')[0]
        st.dataframe(df)
        csv_downloader(df,"S&P500")

    elif choice == "NASDAQ 100":
        st.subheader("NASDAQ 100")
        df = pd.read_html('https://finance.yahoo.com/quote/%5EIXIC/history?p=%5EIXIC')[0]
        st.dataframe(df)
        csv_downloader(df,"NASDAQ100")

    elif choice == "Dow 30":
        st.subheader("Dow 30")
        df = pd.read_html('https://finance.yahoo.com/quote/%5EDJI/history?p=%5EDJI')[0]
        st.dataframe(df)
        csv_downloader(df,"Dow30")

    else:
        st.markdown("## About ##")
        st.write("Thanks for visiting stockbot")
        
if __name__ == '__main__':
    main()