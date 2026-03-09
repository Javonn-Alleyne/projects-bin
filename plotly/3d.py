import plotly.express as px
import pandas as pd
import json

df = pd.read_csv('zk_char_db.csv')

fig = px.scatter_3d(
    df, 
    x='Role', 
    y='Class', 
    z='TOT',
    color='GEN'
)

fig.show()