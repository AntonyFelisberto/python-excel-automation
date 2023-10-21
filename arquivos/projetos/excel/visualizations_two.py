import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


os.chdir("arquivos\\projetos\\excel\\files")

sales_data = pd.read_excel("sales_data.xlsx")

def fmt_wdgs(data):
    def fmt_values(pct):
        total = sum(data)
        abs_value = round(pct*total/100000,1)
        return f"${abs_value}K"
    return fmt_values

fig, (ax_one,ax_two) = plt.subplots(nrows=1,ncols=2)
plt.suptitle("sales breakdown by category and segment")
ax_one.set_title("Category Level Sales \n Breakdown")
data = sales_data.groupby("Category")["Sales"].sum().to_list()
labels = sales_data.groupby("Category")["Sales"].sum().index
explode = [0 if x!= max(data) else 0.1 for x in data]
ax_one.pie(data,labels=labels,explode=explode,autopct=fmt_wdgs(data))

ax_two.set_title("Segment Level Sales \n Breakdown")
data = sales_data.groupby("Segment")["Sales"].sum().to_list()
labels = sales_data.groupby("Segment")["Sales"].sum().index
explode = [0 if x!= max(data) else 0.1 for x in data]
ax_two.pie(data,autopct="%.2f%%")
ax_two.legend(labels,explode=explode,bbox_to_anchor=(1,0,0.5,0.5))

print("%s %f"%("ola",45.0))