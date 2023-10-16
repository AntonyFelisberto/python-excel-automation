import os
import pandas as pd

os.chdir("arquivos\\projetos\\excel\\files")

sales_data = pd.read_excel("sales_data.xlsx")

sales_data.groupby("Region")[["Sales","Profit"]].sum().plot(kind="bar",
                                                            title="Regression Sales & Profits",
                                                            subplots=True,
                                                            layout=(1,2),
                                                            sharey=True)

sales_data.groupby("Region")[["Sales","Profit"]].sum().plot(kind="bar",
                                                            title="Regression Sales & Profits",
                                                            stacked=True)

