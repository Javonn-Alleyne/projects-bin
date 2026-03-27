import pandas as pd
import plotly.express as px

df = pd.read_csv('Liked_Songs.csv')
sort = df.sort_values(by='Release Date')
final = sort [ ['Track Name','Artist Name(s)','Release Date','Genres','Duration (ms)']]
# print(final)
final.to_csv('output.csv', index=False)

data = pd.read_csv('output.csv')

fig = px.scatter(
    df,
    title='test',
    x='Release Date',
    y='Artist Name(s)',
    color='Genres',
)

fig.show()