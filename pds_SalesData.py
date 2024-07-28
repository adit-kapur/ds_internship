import numpy as np
import pandas as pd
import datetime

sales = pd.read_excel("SalesData.xlsx", parse_dates=["OrderDate"])

item = sales.groupby("Item")["Sale_amt"].min()
print(item)

total = sales.groupby(by=["Region",sales.OrderDate.dt.year,"Item"])["Sale_amt"].sum()
print(total)

user_inp = input("enter date in format mm-dd-yyyy: ")
datetime_object = datetime.datetime.strptime(user_inp, '%m-%d-%Y')
#date = datetime.datetime.strptime(user_inp, "%m-%d-%Y").date()
sales["days_diff"] = (sales["OrderDate"] - datetime_object)
print(sales)

manager = pd.DataFrame(sales[['Manager', 'SalesMan']]).sort_values(by= 'Manager')
manager.reset_index(drop=True,inplace=True)
manager.drop_duplicates(subset="Manager")
manager.rename(columns = {'Manager':'Manager','SalesMan':'List_of_salesmen'}, inplace = True)
print(manager)


regional_sales = sales.groupby(["Region"]).agg({"SalesMan": "count", "Sale_amt" : "sum"})
regional_sales.rename(columns = {'SalesMan':'Salesmen_count','Sale_amt':"Total_sales"}, inplace = True)
print(regional_sales)

percent_sales = sales.groupby("Manager").agg({"Sale_amt":"sum"})#["Sale_amt"].apply(lambda x: 100*x/x.sum())
percent_sales["Sale_amt"] = 100*percent_sales["Sale_amt"]/percent_sales["Sale_amt"].sum()
percent_sales.rename(columns = {'Sale_amt':"Percent_sales"}, inplace = True)
print(percent_sales)