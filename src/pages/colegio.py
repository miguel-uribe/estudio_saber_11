import dash
from dash import html
import pickle
from dash import dcc, callback, Input, Output, ctx
import dash_bootstrap_components as dbc


dash.register_page(__name__,  name='Resultados por Colegio')

# loading the figures
with open("pickles/f7.pkl", "rb") as my_file:
    f7 = pickle.load(my_file)    
with open("pickles/f8.pkl", "rb") as my_file:
    f8 = pickle.load(my_file)
with open("pickles/f9.pkl", "rb") as my_file:
    f9 = pickle.load(my_file)
with open("pickles/f10.pkl", "rb") as my_file:
    f10 = pickle.load(my_file)
with open("pickles/f10a.pkl", "rb") as my_file:
    f10a = pickle.load(my_file)

layout = html.Div([
    html.H1('¿Cómo afecta el tipo de colegio?', className = 'H1MP', style = {'height':'8%'}),
    html.Hr( style = {'height': '2%'}),
    html.Div([
        html.Div([
            dbc.Button("Resultados por tipo de colegio", n_clicks =0, id='bt_cole', color="primary",class_name = 'BTXT', active = True, style ={'margin-top': '2%'}),
            html.P(["Veamos la distribución de los resultados por tipo de colegio."], className= 'BPG'),
            html.Hr(),
            dbc.Button("Resultados por género", n_clicks =0, id= 'bt_gen_cole', color="primary", class_name = "BTXT",active = False, style ={'margin-top': '2%'}),
            html.P(["¿Hay algún tipo de colegio para el que se reduzca la brecha entre hombres y mujeres?"], className= 'BPG'),
            html.Hr(),
            dbc.Button("Resultados por campo", n_clicks =0, id= 'bt_camp', color="primary", class_name = "BTXT",active = False, style ={'margin-top': '2%'}),
            html.P(["¿Cómo se comporta la brecha entre hombres y mujeres para cada campo del conocimiento?"], className= 'BPG'),
        ], style = {'margin': '0','width' : '25%', 'height': '100%', 'valign': 'top', 'display': 'inline-block'}
            ),
        html.Div(
            dcc.Graph(  id="fig3_1", 
                        style={'width': '100%', 'height': '100%'},
                        figure = f7),
            style={'width':'70%', 'height': '100%', 'display': 'inline-block', 'verticalAlign': 'top', 'margin-left': '5%'})
    ], style = {'width': '100%', 'height': '45%', 'display': 'inline-block'}
    ),
    html.Hr( style = {'height': '2%'}),
    html.Div([
        html.Div([
            html.H2('Distribución por tipo de colegio', className='PMT', style ={'text-align': 'center'}),
            html.P(["Veamos cómo se distribuye el número de pruebas por el tipo de colegio.",html.Br() ,"¿En qué tipo de instituciones estudian la gran mayoría de colombianos?"], className= 'BPG'),
            html.Div([
                dbc.Button("Escala lineal", n_clicks =0, id='bt_lin_2', color="primary",class_name = 'BTXT2', active = True, style ={'margin': '5%'}),
                dbc.Button("Escala logaritmica", n_clicks =0, id='bt_log_2', color="primary",class_name = 'BTXT2', active = True, style ={'margin': '5%'}),
            ], style = {'display': 'flex', 'justify-content': 'center'}
            )
            ], style = {'margin': '0','width' : '30%', 'height': '100%', 'valign': 'top', 'display': 'inline-block'}
            ),
        html.Div(
            dcc.Graph(  id="fig3_2", 
                        style={'width': '100%', 'height': '100%'},
                        figure = f10),
            style={'width':'65%', 'height': '90%', 'display': 'inline-block', 'verticalAlign': 'top', 'margin-left': '5%'})
    ], style = {'width': '100%', 'height': '40%', 'display': 'inline-block'}
    ),
    
], style ={'width':'75vw', 'height': '95vh','padding': '0', 'margins': '0'})


@callback(Output("fig3_1", "figure"),
          Output("bt_cole", "active"),
          Output("bt_gen_cole", "active"),
          Output("bt_camp", "active"),
            Input("bt_cole", "n_clicks"),
            Input("bt_gen_cole", "n_clicks"),
            Input("bt_camp", "n_clicks"))
def update_fig3(a, b, c):
    out = f7, True, False, False
    match ctx.triggered_id:
        case "bt_cole":
            out = f7, True, False, False
        case "bt_gen_cole":
            out = f8, False, True, False
        case "bt_camp":
            out = f9, False, False, True
    return out



@callback(Output("fig3_2", "figure"),
          Output("bt_lin_2", "active"),
          Output("bt_log_2", "active"),
            Input("bt_lin_2", "n_clicks"),
            Input("bt_log_2", "n_clicks"))
def update_fig2(red, diff):
    out = f10, True, False
    match ctx.triggered_id:
        case "bt_lin_2":
            out = f10, True, False
        case "bt_log_2":
            out = f10a, False, True
    return out
