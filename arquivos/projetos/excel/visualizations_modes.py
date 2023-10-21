import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr

os.chdir("arquivos\\projetos\\excel\\files")

sales_data = pd.read_excel("sales_data.xlsx")

def new_ticks(x,pos):
    return f"${round(x/1000)}"

sales_data["year"] = sales_data["Order Date"].dt.year
timeseries_data = sales_data.groupby("Order Date")[["year","Sales"]].agg({"year":"first","Sales":"sum"})
timeseries_data .sort_index(inplace=True)
data_year = timeseries_data[timeseries_data["year"] == 2017]
data_year["cum_sales"] = data_year["Sales"].cumsum()

plt.style.use("ggplot")
fig = plt.figure()
fig.suptitle("Cumulative Sales",x=0.5,y=1)
ax_one = fig.add_axes([0,0,1,0.9])
ax_one.set_title("2017 Cumulative Sales")
ax_one.plot(data_year["cum_sales"])
ax_one.set_ylabel("Sales")
ax_one.yaxis.set_major_formatter(tkr.FuncFormatter(new_ticks))

ax_two = fig.add_axes([0.2,0.55,0.25,0.25])
ax_two.set_title("Yearly Sales")
x = timeseries_data.groupby("year").sum().index
height = timeseries_data.groupby("year").sum()["Sales"].to_list()
ax_two.bar(x,height)
ax_two.set_ylabel("Sales")
ax_two.set_xticks(x)
ax_two.set_yticks([0,200000,20000,200000])
ax_two.yaxis.set_major_formatter(tkr.FuncFormatter(new_ticks))