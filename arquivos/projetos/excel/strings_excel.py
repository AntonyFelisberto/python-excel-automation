import os
import pandas as pd
import numpy as np

os.chdir("arquivos\\projetos\\excel\\files")

sales_data = pd.read_excel("sales_data.xlsx")

sales_data["Order ID"].str[3:7]
sales_data["Order ID"].str[:2]
sales_data["Order ID"].str[-2:]
sales_data["Order ID"].str.split("-").str[1]

sales_data["Order ID"].str.strip()

sales_data["location"]=sales_data["State"]+"_"+sales_data["City"]
sales_data["State"].str.upper()
sales_data["State"].str.lower()

sales_data["City"].str.find("Fort")