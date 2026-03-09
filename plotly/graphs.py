import plotly.express as px
import pandas as pd
import json

df = pd.read_csv('zk_char_db.csv')

fig = px.scatter(
    df,
    title='Zealkin Character DB',
    x='TOT',
    y='Role',
    symbol='GEN',
    color='GEN',
    hover_data=['FName','LName','Age'],
)

fig.update_xaxes(
    rangeslider_visible=True
)

fig.show() #show graph
# fig.write_html("zk_char_db.html") #convert to html
# fig_json = pio.to_json(fig) #convert to json
# with open("tot_violin.json", "w") as f:
#     json.dump(json.loads(fig_json), f, indent=4)


