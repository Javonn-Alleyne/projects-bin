import plotly.express as px
import pandas as pd
import json

df = pd.read_csv('zk_char_db.csv')

fig = px.density_heatmap(
    df, 
    x="BTOT", 
    y="HTOT",
    nbinsx=10, 
    nbinsy=10,
    text_auto=True,
)
fig.show()