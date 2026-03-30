from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('dt-data.csv')

app = Dash()

# layout
app.layout = [
    html.H1(children="Test App", style={'textAlign':'center'}),
    dcc.Dropdown(df.operator_name.unique(), 'Javonn', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content','figure'),
    Input('dropdown-selection','value')
)
def update_graph(value):
    dff = df[df.operator_name==value]
    fig = px.scatter(
        dff, 
        x='date', 
        y='score',
        color='station',
    )

    fig.add_hline(
        y=96.5,                        # your threshold value
        line_dash="dash",
        line_color="red",
        annotation_text="Threshold",
        annotation_position="top right"
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)