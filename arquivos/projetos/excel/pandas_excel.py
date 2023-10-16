import pandas as pd

data = pd.read_csv("arquivos\\projetos\\excel\\files\\flight_data.csv")
print(data.groupby("ORIGIN")["DEP_DELAY"].mean().max())
print(data.groupby("ORIGIN")["DEP_DELAY"].mean().idxmax())

def better_way():
    data['DEP_DELAY'] = pd.to_numeric(data['DEP_DELAY'], errors='coerce')

    if data['DEP_DELAY'].isna().any():
        print("Some values in the 'DEP_DELAY' column could not be converted to numerical values.")

    mean_delay_by_origin = data.groupby("ORIGIN")["DEP_DELAY"].mean()
    max_mean_delay = mean_delay_by_origin.max()
    origin_with_max_delay = mean_delay_by_origin.idxmax()

    print(f"Maximum Mean Departure Delay: {max_mean_delay}")
    print(f"Origin with Maximum Mean Departure Delay: {origin_with_max_delay}")