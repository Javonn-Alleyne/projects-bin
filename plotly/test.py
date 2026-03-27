from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('disk_space_data_set.csv')

app = Dash()

# layout
app.layout = [
    html.H1(children="Test App", style={'textAlign':'center'}),
    dcc.Dropdown(df.quarter.unique(), 'first', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content','figure'),
    Input('dropdown-selection','value')
)
def update_graph(value):
    dff = df[df.quarter==value]
    # return px.line(
    fig = px.line(
        dff, 
        x='date', 
        y='estimated_storage_on_viwer',
    )

    # fig.add_hline(
    #     y=64,                        # your threshold value
    #     line_dash="dash",
    #     line_color="red",
    #     annotation_text="Threshold",
    #     annotation_position="top right"
    # )

    return fig

if __name__ == '__main__':
    app.run(debug=True)