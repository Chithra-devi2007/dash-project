import dash
from dash import html
import pandas as pd

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Hello Dash with Pandas!")
])

if __name__ == '__main__':
    app.run_server(debug=True)
