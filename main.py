import random
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import csv

df = pd.read_csv("data.csv")

# Average Rating-
averageRating = df["Avg Rating"].tolist()
fig = ff.create_distplot([averageRating], ["Average-Rating"], show_hist= True )
fig.show()




