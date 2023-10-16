import os
import pandas as pd
import numpy as np

os.chdir("arquivos\\projetos\\excel\\files")

sales_data = pd.read_excel("sales_data.xlsx")


print(len((sales_data[sales_data["Quantity"] > 5])))
print(sales_data[sales_data["Quantity"] > 5].shape)

print(len(sales_data[(sales_data["State"]=="Kentucky") & (sales_data["Quantity"]==5)]))

print(sales_data[sales_data["City"].str.contains("Fort")])
print(sales_data[sales_data["City"].str[:4]=="Fort"])
print(sales_data[sales_data["City"].str[:4]=="Fort"]["Profit"])
print(sales_data[sales_data["City"].str[:4]=="Fort"]["Profit"].sum())
print(sales_data.loc[sales_data["City"].str[:4]=="Fort","Profit"].sum())

print(sales_data[(sales_data["City"].str[:4]=="Fort") & (sales_data["Quantity"]>5)]["Profit"].sum())