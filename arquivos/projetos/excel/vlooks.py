import os
import pandas as pd

os.chdir("arquivos\\projetos\\excel\\files")

sales = pd.read_excel("sales_data.xlsx",index_col="Row ID")#index_col remove os itens duplicados

zip_income = pd.read_csv("zipcode_income.csv",engine="python", encoding="ISO-8859-1")

print(sales.merge(zip_income,how="left",left_on="Postal Code",right_on="Zip_Code"))
print(sales.merge(zip_income.loc[:,["Zip_Code","Mean"]],how="left",left_on="Postal Code",right_on="Zip_Code"))


sales = pd.read_excel("sales_data.xlsx")
temp = sales.merge(zip_income.loc[:,["Zip_Code","Mean"]].rename(columns={"Zip_Code":"Postal Code","Mean":"Mean Code"}),how="left",on="Postal Code")
temp.drop_duplicates(subset=["Row ID"],keep="first",inplace=True)
temp.isna().sum()

def vlookup(left_df,right_df,left_key,right_key,right_val):
    left = pd.read_excel(left_df)
    left.reset_index(inplace=True)
    right = pd.read_csv(right_df,engine="python", encoding="ISO-8859-1")
    right = right.loc[:,[right_key,right_val]].rename(columns={right_key:left_key})
    temp = left.merge(right,how="left",on=left_key)
    temp.drop_duplicates(subset=["index"],keep="first",inplace=True)
    return temp.set_index("index")

print(vlookup("sales_data.xlsx","sales_income.csv","Postal Code","Zip_Code","Mean"))