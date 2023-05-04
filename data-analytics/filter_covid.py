import pandas as pd


## set the number of rows to return
pd.set_option("display.min_rows", 12)


# print(data.covid_19_data_us)
data_filter = pd.read_csv("data/covid_19_data_us/us.csv", index_col="date")

print(data_filter)