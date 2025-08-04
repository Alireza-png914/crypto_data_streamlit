
import pyodbc
import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://emalls.ir/%d9%84%db%8c%d8%b3%d8%aa-%d9%82%db%8c%d9%85%d8%aa_%d9%be%d9%85%d9%be-%da%a9%d9%88%d9%84%d8%b1~Category~385838'

response = requests.get(url)

data=BeautifulSoup(response.text,'html.parser')

pumps=data.find_all('div',class_='product-block-parent')
pumps_title=[]
pumps_price=[]
for pump in pumps:
    title=pump.find('div',class_='item-title').text
    pumps_title.append(title)
    price=pump.find('div',class_='prd-price').span.text
    pumps_price.append(price)

table=pd.DataFrame({'name':pumps_title,'price':pumps_price})


table.to_csv('info_pumps.csv')






df=pd.read_csv('D:/python/pycharm/info_pumps.csv')

server = 'localhost'
database ='pump_data'
username = 'alirza_malekshahi'
password = 'alireza_83'

cnxn =pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                    f"Server=localhost;"
                    f"Database=pump_data;"
                    f"username=alireza_malekshahi;"
                    f"password=alireza_83;"
                    f"Trusted_Connection=yes;")
cursor = cnxn.cursor()


for index, row in df.iterrows():
      cursor.execute("INSERT INTO data_pumps (name,price) values(?,?)",  str(row.name), str(row.price))


cnxn.commit()
cursor.close()





