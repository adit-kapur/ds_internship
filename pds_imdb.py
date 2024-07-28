import numpy as np
import pandas as pd 


imdb = pd.read_csv("imdb.csv",header=0, escapechar="\\")  
rating_5 = imdb["imdbRating"].iloc[4]
print("imdb rating of 5th movie of dataframe is:", rating_5)

title_min = (imdb[imdb["duration"] == imdb["duration"].min()]["title"]).index
print(title_min)

title_max = imdb[imdb["duration"] == imdb["duration"].max()]["title"]
print(title_max)

sorted_imdb = imdb.sort_values(["year","imdbRating"],ascending=[True, False])
print(sorted_imdb[["year","imdbRating"]].head(50))

low = 60*30
high = 180*60
mask = imdb["duration"].between(low,high)
subset_imdb = imdb[mask]
print(imdb.duration.head(10))





