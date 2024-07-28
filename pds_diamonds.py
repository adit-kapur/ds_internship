import numpy as np
import pandas as pd


diamonds = pd.read_csv("diamonds.csv")
print(diamonds.shape)
duplicate_count = diamonds.duplicated().sum()
print("The number of duplicated rows is:", duplicate_count)

diamonds_2 = diamonds.dropna(subset=["carat","cut"])
print(diamonds_2.shape)

diamonds_3 = diamonds.select_dtypes(include=np.number)
print(diamonds_3.head(6))

depth_cond = diamonds["depth"] > 60
vol = diamonds.x*diamonds.y*diamonds.z
diamonds['volume'] = np.where(depth_cond, vol , 8)


diamonds["price"]= diamonds["price"].fillna(diamonds["price"].mean())
print(diamonds.head(6))
