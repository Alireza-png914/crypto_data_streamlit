import pyodbc
import pandas as pd


df=pd.read_csv('D:/python/pycharm/info_pumps.csv')

server = 'localhost'
database ='pumps_datas'
username = 'alirza_malekshahi'
password = 'alireza_83'

cnxn =pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                    f"Server=localhost;"
                    f"Database=pumps_datas;"
                    f"username=alireza_malekshahi;"
                    f"password=alireza_83;"
                    f"Trusted_Connection=yes;")
cursor = cnxn.cursor()


for index, row in df.iterrows():
      cursor.execute("INSERT INTO info_pumps (title,price) values(?,?)", str(row.title), str(row.price))


cnxn.commit()
cursor.close()

