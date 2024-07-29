#%%
import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns

abc_data = pd.read_excel("DS Internship - EDA - Data.xlsx", dtype={"Sales":"int64","SGM":"int64"}, parse_dates=["Store Open"])

abc_data["Sales"] = abc_data["Sales"].astype("int64")
total_sales = abc_data.groupby("Year")["Sales"].sum()
print(total_sales)

mask_1 = abc_data["Store Open"].dt.year == 1991
print(abc_data[mask_1].head())

mask_2 = abc_data["Store Modification"] != "no change"
remodel = abc_data[mask_1][mask_2]
print(remodel.head())

sns.relplot(data = abc_data, x = "Sales", y="Total Sq Ft" )
print("There is no relation between Sales and total sq. ft")


profit = abc_data.groupby("Super Division").agg({"SGM":"sum"})
mask_3 = profit["SGM"] == profit.SGM.max()
val = profit[mask_3]
print("The most prfitable super division is: ")
print(val)

mask_4 = abc_data["Store Close"] == "No Close date"
active = abc_data[mask_4]
val_2 = active.shape[0]
print("The number of stores active today is: ", val_2)

sqft_av = abc_data.groupby("Super Division").agg({"Total Sq Ft":"mean"})
mask_5 = sqft_av["Total Sq Ft"] == sqft_av["Total Sq Ft"].max()
val_3 = sqft_av[mask_5]
print("The super div with the largest av area is: ")
print(val_3)
sns.catplot(data=sqft_av, x = "Super Division", y ="Total Sq Ft", kind='bar')


new_store = abc_data.groupby("State").agg({"Sales":"sum"}).sort_values("Sales",ascending=False)
sns.catplot(data=new_store, x = "State", y ="Sales", kind='bar')
print("The 3 stores are as follows")
print(new_store.iloc[-3:])

dates = abc_data.groupby(abc_data["Store Open"].dt.month_name()).agg({"Sales":"sum"}).sort_values("Sales", ascending=False)
mask_6 = dates["Sales"] == dates["Sales"].max()
val_4 = dates[mask_6]
sns.catplot(data=dates, x = "Store Open", y ="Sales", kind='bar')
print("The month is: ")
print(val_4)

mask_7 = abc_data["Store Close"] != "No Close date"
outlet = abc_data[mask_7]
fin = outlet.groupby("Outlet Type").agg({"Outlet Type":"count"})
print(fin)
print("It appears outlets in the strip close down the most")
