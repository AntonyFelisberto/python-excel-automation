import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr

os.chdir("arquivos\\projetos\\excel\\files")

sales_data = pd.read_excel("sales_data.xlsx")

def new_ticks(x,pos):
    return f"${round(x/1000)}"

fig = plt.figure()
fig.suptitle("City Level Performance",x=0,y=1)

ax_one = fig.add_axes([0,0,1,0.9])
ax_one.set_title("Top Cities")
ax_one.yaxis.label.set_visible(False)
ax_one.set_xlabel("Sales")
ax_one.axvline(x=100000,color="black",ls="--",linewidth=2)
ax_one.xaxis.set_major_formatter(tkr.FuncFormatter(new_ticks))

ax_two = fig.add_axes([0.65,0.55,0.25,0.25])
ax_two.set_title("Laggard Cities")
ax_two.xaxis.label.set_visible(False)
ax_two.set_ylabel("Sales")

sales_data.groupby("City")["Sales"].sum().sort_values(ascending=False).iloc[:15].plot(kind="barh",ax=ax_one)
sales_data.groupby("City")["Sales"].sum().sort_values(ascending=True).iloc[:5].plot(kind="bar",ax=ax_two)