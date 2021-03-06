# Imports from 3rd party libraries
import dash
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
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
html.Div([

        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in epsilon],
                value='genres'
            )
        ]

ao = pd.read_csv('

fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])
