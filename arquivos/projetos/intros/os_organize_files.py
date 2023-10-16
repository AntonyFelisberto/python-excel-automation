import os
import glob
import shutil

cwd = os.getcwd()

filenames = glob.glob("*.xlsx")#pegando arquivos local atual
for file in filenames:
    year = file.split(".")
    year = file.split(".")[-2][-4:]#1 posicao 4 caracteres
    try:
        int(year)
    except:
        print("year is not convertabel")
        continue
        
    if os.path.isdir(year) == False:
        os.mkdir(year)
    os.rename(file,os.path.join(cwd,year,file))