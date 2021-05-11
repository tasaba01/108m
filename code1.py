import pandas as pd
import csv
import plotly.figure_factory as fx

df=pd.read_csv("super.csv")
fig = fx.create_distplot([df["weight"].tolist()],["weight"],show_hist = False)
fig.show()