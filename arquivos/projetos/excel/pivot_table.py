import os
import glob
import pandas as pd
import numpy as np

os.chdir("arquivos\\projetos\\excel\\files")

cwd = os.getcwd()

filenames = glob.glob(cwd + "\\*xlsx") # "\\*\\*xlsx" dependendo do numero de pastas que tem pros excels voce tem que colocar mais \\*

consolidated = pd.DataFrame(columns=pd.read_excel(filenames[0]).columns)
for file in filenames:
    temp = pd.read_excel(file)
    consolidated = consolidated._append(temp,ignore_index=True)

pd.pivot_table(consolidated,values="Profit",index = ["Segment","Category","Sub-Category"],columns=["Region","State"],aggfunc=np.sum)

colums = ["Region"]
rows = ["Segment","Category","Sub-Category"]
values = ["Profit"]

relevant_df = consolidated.loc[:,colums+rows+values]
print(relevant_df.groupby(rows+colums).sum())
print(relevant_df.groupby(rows+colums).sum().unstack([-1,-2]))

pivot_df = relevant_df.groupby(rows+colums).sum().unstack()
pivot_df.to_excel("pivot.xlsx")
pivot_df.to_html("pivot.html")

