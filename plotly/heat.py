import plotly.express as px
import pandas as pd
import json

df = pd.read_csv('generated_data.csv')

fig = px.scatter(
    df, 
    x="volumes_uploaded", 
    y="images_master",
)
fig.show()