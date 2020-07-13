import plotly.express as px
import pandas as pd

df = {
"our_data": [123, 132, 654, 345, 125, 498],
"more_data": [345, 67, 176, 245, 197, 391],
"columns": ["a", "b", "c", "d", "e", "f"]
}
fig = px.line(df, y="our_data", x="columns")
fig.show()
fig = px.line(df, y=["our_data", "more_data"], x="columns")
fig.show()