import pandas as pd
import os

os.chdir("arquivos\\projetos\\excel\\files")

data = pd.read_excel("data.xlsx",sheet_name="Orders",header=3,index_col="Row ID")
print(data.head())
print(data.head(10))
print(data.tail())
print(data.dtypes)
print(data.describe())
print(data.columns)

data["Per Unit Sale"] = data["Sales"]/data["Quantity"]
data.to_excel("data_2.xlsx")
data.to_excel("data_sem_indices.xlsx",index=False)

print(data.drop("Product Name",axis=1,inplace=True))
print(data.drop(["Product Name","Ship Date"],axis=1))