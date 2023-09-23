import dash
from dash import html
import pickle
from dash import dcc, callback, Input, Output, ctx
import dash_bootstrap_components as dbc


dash.register_page(__name__,  name='Resultados Históricos')
# loading the figures
with open("pickles/f1.pkl", "rb") as my_file:
    f1 = pickle.load(my_file)
with open("pickles/f2.pkl", "rb") as my_file:
    f2 = pickle.load(my_file)
    
with open("pickles/f3.pkl", "rb") as my_file:
    f3 = pickle.load(my_file)
    
layout = html.Div([
    html.H1('Evolución temporal de las pruebas', className = 'H1MP', style = {'height':'8%'}),
    html.Hr( style = {'height': '2%'}),
    html.Div([
        html.Div([
            dbc.Button("Resultados históricos", n_clicks =0, id='gen_res', color="primary",class_name = 'BTXT', active = True, style ={'margin-top': '5%'}),
            html.P(["Exploremos los resultados históricos en el puntaje global.",html.Br(),"¿Hay cambios en la tendencia a lo largo de los años?" ], className= 'BPG'),
            html.Hr(),
            dbc.Button("Resultados por género", n_clicks =0, id= 'gen_diff', color="primary", class_name = "BTXT",active = False, style ={'margin-top': '5%'}),
            html.P(["Exploremos los resultados históricos, discriminados por género, para los  resultados globales de la prueba.", html.Br(), "¿Qué nos sugieren los datos?"], className= 'BPG'),
        ], style = {'margin': '0','width' : '20%', 'height': '100%', 'valign': 'middle', 'display': 'inline-block'}
            ),
        html.Div(
            dcc.Graph(  id="fig1", 
                        style={'width': '100%', 'height': '100%'},
                        figure = f1),
            style={'width':'75%', 'height': '100%', 'display': 'inline-block', 'verticalAlign': 'top', 'margin-left': '5%'})
    ], style = {'width': '100%', 'height': '45%', 'display': 'inline-block'}
    ),
    html.Hr( style = {'height': '2%'}),
    html.Div([
        html.Div([
            html.H2('¿Cómo evoluciona la población estudiantil?', className='PMT', style ={'text-align': 'center'}),
            html.P(["La gráfica muestra cómo ha evolucionado el número de pruebas realizadas año tras año, tanto para hombres como para mujeres.", html.Br(), "¿Qué podemos concluir a partir de esta observación?"], className= 'BPG'),
            ], style = {'margin': '0','width' : '30%', 'height': '100%', 'valign': 'middle', 'display': 'inline-block'}
            ),
        html.Div(
            dcc.Graph(  id="fig2", 
                        style={'width': '100%', 'height': '100%'},
                        figure = f3),
            style={'width':'65%', 'height': '90%', 'display': 'inline-block', 'verticalAlign': 'top', 'margin-left': '5%'})
    ], style = {'width': '100%', 'height': '40%', 'display': 'inline-block'}
    ),
    
], style ={'width':'75vw', 'height': '95vh','padding': '0', 'margins': '0'})




@callback(Output("fig1", "figure"),
          Output("gen_res", "active"),
          Output("gen_diff", "active"),
            Input("gen_diff", "n_clicks"),
            Input("gen_res", "n_clicks"))
def update_fig1(red, diff):
    out = f1, True, False
    match ctx.triggered_id:
        case "gen_res":
            out = f1, True, False
        case "gen_diff":
            out = f2, False, True
    
    return out