# Importing streamlit 
import streamlit as st
import streamlit.components as stc

# Importing other necessary dependencies
import numpy as np
import pandas as pd
import base64
import time
from time import sleep
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
    
# Imporitng and setting up Selenium
# import selenium
from selenium import webdriver 
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

#Function to download the file as csv
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
    menu = ["Home","S&P 500","NASDAQ 100","Crypto","About"]
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
        st.markdown("### Stock Bot lets you view and download top US indexes:money_with_wings: ###")
        
    elif choice == "S&P 500":
        st.subheader("S&P 500")
        driver.get("https://www.slickcharts.com/sp500")
        df = pd.read_html(driver.page_source)[0]
        df = df.head(500)
        st.dataframe(df)
        csv_downloader(df,"S&P 500")
        driver.quit()

    elif choice == "NASDAQ 100":
        st.subheader("NASDAQ 100")
        driver.get("https://www.slickcharts.com/nasdaq100")
        df = pd.read_html(driver.page_source)[0]
        df = df.head(100)
        st.dataframe(df)
        csv_downloader(df,"NASDAQ 100")
        driver.quit()

    elif choice == "Crypto":
        st.subheader("Cryptocurrenices")
        driver.get("https://www.slickcharts.com/currency")
        df = pd.read_html(driver.page_source)[0]
        df = df.head(100)
        st.dataframe(df)
        csv_downloader(df,"Crypto")
        driver.quit()

    else:
        st.markdown("## About ##")
        st.write("Thanks for visiting stockbot")
        #st.write("Code available on [Github](https://github.com/kkarthi6/Streamlit/blob/51e014589d2f0b95ee8c4de94209dfd53d38b2a0/Streamlit_stock_app.py)")
        
if __name__ == '__main__':
    main()
