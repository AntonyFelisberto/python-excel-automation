import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]),columns=["alpha","beta","cappa"])
print(df["alpha"])

df.columns = ["a","b","c"]
df.index = ["m","n","o"]

print(df["a"])
print(df[["a","b"]])
print(df[["a","c"]])
print(df.loc["m"])
print(df.loc["m","a"])

print(df.iloc[1])
print(df.loc["n","a"])

print(df.loc[["m","n"],["a","b"]])
print(df.iloc[[0,1],1:])
print(df.iloc[[0,2],[1,2]])
df_dict = pd.DataFrame({"a":[1,2,3],"b":[4,5,6],"c":[7,8,9]})

np_array = np.array([2,6,1,3])
pd_series = pd.Series(np_array)
pd_series = pd.Series(np_array,index=["a","b","c","d"])
pd_series_two = pd.Series({"a":2,"b":6,"c":1,"d":3})
print(pd_series["a"])
print(pd_series[["b","d"]])
pd_series[:]=10
print(pd_series[:])
print(pd_series_two[2:])
print(pd_series_two[1:3])

menu = pd.DataFrame({"item":["pizza","pasta","salad","burrito"],
                    "price":[14.99,12.99,7.99,10.99],
                    "popularity":["high","medium","low","high"]})

nutrition = pd.DataFrame({"item":["pizza","burrito","salad","pasta"],
                            "avg_calorie":[3200,940,240,740],
                            "protein":["12%","16%","6%","10%"]})

print(pd.concat([menu,nutrition]))
print(pd.concat([menu,nutrition],axis=1))
print(pd.concat([menu,nutrition],axis=0,ignore_index=True))

print(menu.merge(nutrition))
print(menu.merge(nutrition,how="inner"))
print(menu.merge(nutrition,how="outer"))
print(menu.merge(nutrition,how="left"))
print(menu.merge(nutrition,how="right"))
print(menu.merge(nutrition,how="inner",left_on="item",right_on="item"))

menu.set_index("items",inplace=True)
menu.reset_index(inplace=True)
menu.join(nutrition)
menu.set_index("item").join(nutrition.set_index("item"))

def handlings():
    data = pd.read_excel("arquivos\\projetos\\excel\\files\\data.xlsx",sheet_name="Orders",header=3,index_col="Row ID")
    data["Postal Code"] = data["Postal Code"].astype(str)
    data["Order Date"] = data["Order Date"].astype(str)
    data["Order Date"] = pd.to_datetime(data["Order Date"],errors="raise",format="%Y-%m-%d")
    data["month"] = data["Order Date"].dt.month
    data["year"] = data["Order Date"].dt.year
    data["processing time"] = data["Ship Date"] - data["Order Date"]
    data["string date"] = data["Order Date"].dt.strftime("%b-%Y")

def handlings_nan():
    data = pd.read_excel("arquivos\\projetos\\excel\\files\\data_2.xlsx",index_col="Row ID")
    print(data.isna().sum())
    print(data.isna().sum(axis=1))
    print(data.isna().sum(axis=1)>0)
    data.dropna()
    data.dropna(how="all")
    data.dropna(axis=1)
    data.dropna(axis=1,how="all",inplace=True)
    data.fillna()
    data.fillna(0)
    data.fillna(0,inplace=True)
    data.fillna(method="bfill",inplace=True)

def pandas_excel():
    data = pd.read_excel("arquivos\\projetos\\excel\\files\\sales_data.xlsx",index_col="Row ID")
    data["month_year"] = data["Order Date"].dt.strftime("%m-%Y")
    gb = data.groupby("month_year")
    ls = []

    for df in gb.groups:
        ls.append(gb.get_group(df))

    for df in ls:
        file_name = df["month_year"].iloc[0]
        df.to_excel(f"{file_name}.xlsx",index=False)

def np_and_pandas():
    commute = pd.read_excel("arquivos\\projetos\\excel\\files\\commute.xlsx",sheet_name="Sales",index_col="Date")
    commute.replace(["Yes","No"],[1,0],inplace=True)
    x = np.array(commute)
    y = np.array([8,3,0.5,12])
    daily_expenses = x.dot(y)
    print(commute.index[daily_expenses.argmax()].strftime("%Y-%m-%d"))