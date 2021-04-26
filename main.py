import random
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import csv

df = pd.read_csv("data.csv")

# HEIGHT-
height = df["Avg Rating"].tolist()
fig = ff.create_distplot([height], ["height"], show_hist= False )
fig.show()

# WEIGHT -
weight = df["Weight(Pounds)"].tolist()
fig1 = ff.create_distplot([weight], ["weight"], show_hist= False)
fig1.show()
# print(df)

