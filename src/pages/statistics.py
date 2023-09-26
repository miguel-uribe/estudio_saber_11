import dash
from dash import html
import pickle
from dash import dcc, callback, Input, Output, ctx
import dash_bootstrap_components as dbc


dash.register_page(__name__,  name='Resultados de Regresión')

# loading the figures
with open("pickles/f17.pkl", "rb") as my_file:
    f17 = pickle.load(my_file)    

    
    
layout = html.Div([
    html.H1('¿Cuáles son los factores más importantes en el resultado?', className = 'H1MP', style = {'height':'8%'}),
    html.Hr( style = {'height': '2%'}),
    html.P(["Analicemos ahora los resultados de una regresión lineal para modelar los exámenes Saber 11. ¿Cuáles son los principales determinantes del resultado?"], className= 'BPG'),
    html.Div([
        dcc.Graph(  id="fig5_1", 
                        style={'width': '100%', 'height': '100%'},
                        figure = f17)
    ], style ={'width': '100%', 'height': '70vh'})
    ],
            style={'width':'100%', 'height': '100%', 'display': 'inline-block', 'verticalAlign': 'top', 'margin-left': '5%'}
    )    

