import requests
import streamlit as st

st.title('Crypto Data')
coin=st.text_input('Enter the coin:(اولشو با حرف بزرگ وارد کنید) ')
if coin:
    url=f'https://api.diadata.org/v1/assetQuotation/{coin}/0x0000000000000000000000000000000000000000'
    res=requests.get(url).json()
    name=res['Name']
    price=res['Price']
    Blockchain=res['Blockchain']
    PriceYesterday=res['PriceYesterday']
    Time=res['Time']
    try:
        st.write('crypto name=',name)
        st.write('The price now=',price)
        st.write('Blockchain_address=',Blockchain)
        st.write('yesterday_price=',PriceYesterday)
        st.write('Time=',Time)

    except requests.RequestException as e:
        st.error(f"error: {e}")

