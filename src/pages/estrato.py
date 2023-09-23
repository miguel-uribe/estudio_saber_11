import dash
from dash import html
import pickle
from dash import dcc, callback, Input, Output, ctx
import dash_bootstrap_components as dbc


dash.register_page(__name__,  name='Resultados por Estrato')
# loading the figures
with open("pickles/f4.pkl", "rb") as my_file:
    f4 = pickle.load(my_file)    
with open("pickles/f5.pkl", "rb") as my_file:
    f5 = pickle.load(my_file)
with open("pickles/f6.pkl", "rb") as my_file:
    f6 = pickle.load(my_file)
with open("pickles/f6a.pkl", "rb") as my_file:
    f6a = pickle.load(my_file)

layout = html.Div([
    html.H1('¿Cómo afecta el estrato el resultado?', className = 'H1MP', style = {'height':'8%'}),
    html.Hr( style = {'height': '2%'}),
    html.Div([
        html.Div([
            dbc.Button("Resultados por Estrato", n_clicks =0, id='bt_est', color="primary",class_name = 'BTXT', active = True, style ={'margin-top': '5%'}),
            html.P(["Veamos los resultados compilados de los últimos años, discriminados por estrato.",
                    html.Br(),
                    "¿Hay diferencias significativas entre estratos?",
                    "¿Existe algún comportamiento inesperado en las distribuciones?"], className= 'BPG'),
            html.Hr(),
            dbc.Button("Resultados por género", n_clicks =0, id= 'bt_gen_est', color="primary", class_name = "BTXT",active = False, style ={'margin-top': '5%'}),
            html.P(["¿Cómo cambian los resultados por estrato de un género al otro?", html.Br(),"¿En qué estrato se maximiza la diferencia entre hombres y mujeres?"], className= 'BPG'),
        ], style = {'margin': '0','width' : '25%', 'height': '100%', 'valign': 'top', 'display': 'inline-block'}
            ),
        html.Div(
            dcc.Graph(  id="fig2_1", 
                        style={'width': '100%', 'height': '100%'},
                        figure = f4),
            style={'width':'70%', 'height': '100%', 'display': 'inline-block', 'verticalAlign': 'top', 'margin-left': '5%'})
    ], style = {'width': '100%', 'height': '45%', 'display': 'inline-block'}
    ),
    html.Hr( style = {'height': '2%'}),
    html.Div([
        html.Div([
            html.H2('Distribución por estratos', className='PMT', style ={'text-align': 'center'}),
            html.P(["La gráfica muestra el número de pruebas por estrato.",html.Br() ,"¿Cuáles son los estratos predominantes en el país?"], className= 'BPG'),
            html.Div([
                dbc.Button("Escala lineal", n_clicks =0, id='bt_lin', color="primary",class_name = 'BTXT2', active = True, style ={'margin': '5%'}),
                dbc.Button("Escala logaritmica", n_clicks =0, id='bt_log', color="primary",class_name = 'BTXT2', active = True, style ={'margin': '5%'}),
            ], style = {'display': 'flex', 'justify-content': 'center'}
            )
            ], style = {'margin': '0','width' : '30%', 'height': '100%', 'valign': 'top', 'display': 'inline-block'}
            ),
        html.Div(
            dcc.Graph(  id="fig2_2", 
                        style={'width': '100%', 'height': '100%'},
                        figure = f6),
            style={'width':'65%', 'height': '90%', 'display': 'inline-block', 'verticalAlign': 'top', 'margin-left': '5%'})
    ], style = {'width': '100%', 'height': '40%', 'display': 'inline-block'}
    ),
    
], style ={'width':'75vw', 'height': '95vh','padding': '0', 'margins': '0'})


@callback(Output("fig2_2", "figure"),
          Output("bt_lin", "active"),
          Output("bt_log", "active"),
            Input("bt_lin", "n_clicks"),
            Input("bt_log", "n_clicks"))
def update_fig2(red, diff):
    out = f6, True, False
    match ctx.triggered_id:
        case "bt_lin":
            out = f6, True, False
        case "bt_log":
            out = f6a, False, True
    return out


@callback(Output("fig2_1", "figure"),
          Output("bt_est", "active"),
          Output("bt_gen_est", "active"),
            Input("bt_est", "n_clicks"),
            Input("bt_gen_est", "n_clicks"))
def update_fig2a(red, diff):
    out = f4, True, False
    match ctx.triggered_id:
        case "bt_est":
            out = f4, True, False
        case "bt_gen_est":
            out = f5, False, True
    return out