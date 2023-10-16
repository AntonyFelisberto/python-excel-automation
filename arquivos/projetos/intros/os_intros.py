import os
import glob
import shutil

print(os.getcwd())
cwd = os.getcwd()

os.chdir("F:\\")

os.rename(os.path.join(cwd,"01-2024.xlsx"),os.path.join(cwd,"2014","01-2024.xlsx")) #movendo o arquivo para outra pasta
os.rename(os.path.join(cwd,"01-2024.xlsx"),os.path.join(cwd,"2014","01-2025.xlsx")) #movendo o arquivo para outra pasta e renomeando
os.renames("2014","2015") #renomeando arquivos

os.mkdir("test")
os.rmdir("test")
os.system("clear")
os.path.join(cwd,"assigment","test")

shutil.copy("01-2024.xlsx",os.path.join(cwd,"2014","01-2024.xlsx"))
shutil.copytree("2014","2014 copy") #copiar pasta
shutil.move()

filenames = glob.glob("*")#pegando arquivos local atual
filenames = glob.glob("*.xlsx")#pegando arquivos local atual
filenames = glob.glob("*2016*")#pegando arquivos local atual
filenames = glob.glob("2016.xlsx")#pegando arquivos local atual

glob.glob(cwd+"\\*\\*\\*.xlsx") #pegando os items dentro de pastas