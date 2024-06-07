import requests
import pandas as pd
import xml.etree.ElementTree as ET
from sqlalchemy import create_engine

# API data
response = requests.get('https://api.restful-api.dev/objects')
api_data = response.json()
df_api = pd.json_normalize(api_data)

# CSV data
csv_data_1 = pd.read_csv('./industry.csv')
csv_data_2 = pd.read_csv('./output.csv')

# JSON data
json_data = pd.read_json('./sample4.json')

# Excel data
excel_data = pd.read_excel('./movies.xlsx')

# XML data
data = []
tree = ET.parse('./book.xml')
root = tree.getroot()

for item in root:
    author = item.find('author').text
    title = item.find('title').text
    genre = item.find('genre').text
    price = float(item.find('price').text)
    publish_date = item.find('publish_date').text
    description = item.find('description').text

    data.append({
        'author': author,
        'title': title,
        'genre': genre,
        'price': price,
        'publish_date': publish_date,
        'description': description
    })

df_xml = pd.DataFrame(data)

# SQL data
username = 'root'
password = 'root'
host = 'localhost'
database = 'sample'

engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}/{database}')
query = 'SELECT * FROM products'
sql_data = pd.read_sql(query, con=engine)


combined_df = pd.concat([df_api, csv_data_1, csv_data_2, json_data, excel_data, df_xml, sql_data], ignore_index=True)

combined_df.to_excel('combined_data.xlsx', index=False)

print("Data has been successfully combined ")
