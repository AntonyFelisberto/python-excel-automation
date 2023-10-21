import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


os.chdir("arquivos\\projetos\\excel\\files")

sales_data = pd.read_excel("sales_data.xlsx")

fig, (ax_one,ax_two) = plt.subplots(nrows=1,ncols=2)
plt.suptitle("sales breakdown by category and segment")
ax_one.set_title("Category Level Sales \n Breakdown")
data = sales_data.groupby("Category")["Sales"].sum().to_list()
labels = sales_data.groupby("Category")["Sales"].sum().index
ax_one.pie(data,labels=labels,autopct="%.2f%%")

ax_two.set_title("Segment Level Sales \n Breakdown")
data = sales_data.groupby("Segment")["Sales"].sum().to_list()
labels = sales_data.groupby("Segment")["Sales"].sum().index
ax_two.pie(data,autopct="%.2f%%",labels=labels)

print("%s %f"%("ola",45.0))