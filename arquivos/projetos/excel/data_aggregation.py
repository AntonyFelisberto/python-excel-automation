import pandas as pd
import os

os.chdir("arquivos\\projetos\\excel\\files")

data = pd.read_excel("data.xlsx",sheet_name="Orders",header=3,index_col="Row ID")
print(data.columns)
print(data.groupby("Region"))
print(data.groupby("Region").count())
print(data.groupby(["Region","Category"]).sum())
print(data.groupby(["Region","Category"]).sum()["Profit"])
print(data.groupby(["Region","Category"]).sum().unstack())

gb = data.groupby("Region")
print(gb.groups)
print(gb.get_group("South"))