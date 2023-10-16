import os
import glob
import pandas as pd

os.chdir("arquivos\\projetos\\excel\\files")

cwd = os.getcwd()

filenames = glob.glob(cwd + "\\*xlsx") # "\\*\\*xlsx" dependendo do numero de pastas que tem pros excels voce tem que colocar mais \\*

consolidated = pd.DataFrame(columns=pd.read_excel(filenames[0]).columns)
for file in filenames:
    temp = pd.read_excel(file)
    consolidated = consolidated._append(temp,ignore_index=True)

consolidated.to_excel("consolidated.xlsx", index = False)