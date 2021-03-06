# Imports from 3rd party libraries
import dash
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
epsilon = ['genres', 'spoken_languages', 'production_countries', 'original_language', 'production_company']
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Movies - getting a bang for your buck

            Movie_monies provides potential revenue of bigger budget films, estimate the effects of any particular 
            
            feature on revenues. Adjust some features of an upcoming film production to see potential impacts on revenue.

            """
        ),
        dcc.Link(dbc.Button('Your Call To Action', color='primary'), href='/predictions')
    ],
    md=4,
)


ao = pd.read_csv('https://raw.githubusercontent.com/peterger8y/Movie_money/main/ao')



column2 = html.Div([
 

        html.Div([
            dcc.Dropdown(
                id ='xaxis-column',
                options=[{'label': i, 'value': i} for i in epsilon],
                value='popularity'
            ),
        ],
        style={'width': '48%', 'display': 'inline-block'}),

    ])
dcc.Graph(id='indicator-graphic'),

layout = dbc.Row([column1, column2])

@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'))

def update_graph(xaxis_column_name):
    dff = df[df['indicator'] == xaxis_column_name]

    fig = px.scatter(x=dff['x_domain'],
                     y=dff['x_domain'])
    fig.add_trace(go.scatter(x=dff['x_domain'],
                             y=dff['xgboost_pred'], ))

     return fig


if __name__ == '__main__':
    app.run_server(debug=True
