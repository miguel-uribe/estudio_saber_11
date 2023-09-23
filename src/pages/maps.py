import dash
from dash import html
import pickle
from dash import dcc, callback, Input, Output, ctx
import dash_bootstrap_components as dbc


dash.register_page(__name__,  name='Resultados por Municipio')

# loading the figures
with open("pickles/f11.pkl", "rb") as my_file:
    f11 = pickle.load(my_file)    
with open("pickles/f12.pkl", "rb") as my_file:
    f12 = pickle.load(my_file)
with open("pickles/f13.pkl", "rb") as my_file:
    f13 = pickle.load(my_file)
with open("pickles/f14.pkl", "rb") as my_file:
    f14 = pickle.load(my_file)    
with open("pickles/f15.pkl", "rb") as my_file:
    f15 = pickle.load(my_file)
with open("pickles/f16.pkl", "rb") as my_file:
    f16 = pickle.load(my_file)
    
    
layout = html.Div([
    html.H1('¿Cómo se Distribuyen Geográficamente los Resultados?', className = 'H1MP', style = {'height':'8%'}),
    html.Hr( style = {'height': '2%'}),
    html.Div([
        html.Div([
            html.P(["Analicemos ahora cómo es la variación geográfica de los resultados de la prueba Saber 11, por tipo de colegio."], className= 'BPG', style = {'margin-top': '1%'}),
            dbc.Button("Todos", n_clicks =0, id='bt_all', color="primary",class_name = 'BTXT', active = True, style ={'margin-top': '2%'}),
            dbc.Button("Publicos", n_clicks =0, id= 'bt_pub', color="primary", class_name = "BTXT",active = False, style ={'margin-top': '2%'}),
            dbc.Button("Privados", n_clicks =0, id= 'bt_priv', color="primary", class_name = "BTXT",active = False, style ={'margin-top': '2%'}),
            html.Hr(),
            html.P(["Juguemos con la escala, a continuación podemos modificar la visualización para ver los resultados por Departamento o por Municipio."], className= 'BPG', style = {'margin-top': '1%'}),
            dbc.Button("Por Departamento", n_clicks =0, id='bt_dept', color="primary",class_name = 'BTXT', active = True, style ={'margin-top': '2%'}),
            dbc.Button("Por Municipio", n_clicks =0, id= 'bt_mun', color="primary", class_name = "BTXT",active = False, style ={'margin-top': '2%'}),
        ], style = {'margin': '0','width' : '25%', 'height': '100%', 'valign': 'top', 'display': 'inline-block'}
            ),
        html.Div(
            dcc.Graph(  id="fig4_1", 
                        style={'width': '100%', 'height': '100%'},
                        figure = f14),
            style={'width':'70%', 'height': '100%', 'display': 'inline-block', 'verticalAlign': 'top', 'margin-left': '5%'})
    ], style = {'width': '100%', 'height': '85%', 'display': 'inline-block'}
    )    
], style ={'width':'75vw', 'height': '95vh','padding': '0', 'margins': '0'})


@callback(Output("fig4_1", "figure"),
          Output("bt_all", "active"),
          Output("bt_pub", "active"),
          Output("bt_priv", "active"),
          Output("bt_dept", "active"),
          Output("bt_mun", "active"),
          Input("bt_all", "n_clicks"),
          Input("bt_pub", "n_clicks"),
          Input("bt_priv", "n_clicks"),
          Input("bt_dept", "n_clicks"),
          Input("bt_mun", "n_clicks"),
          Input("bt_all", "active"),
          Input("bt_pub", "active"),
          Input("bt_priv", "active"),
          Input("bt_dept", "active"),
          Input("bt_mun", "active"),
          )
def update_fig4(bt_all_n, bt_pub_n, bt_priv_n, bt_dept_n, bt_mun_n, bt_all_a, bt_pub_a, bt_priv_a, bt_dept_a, bt_mun_a):
    out = f14, True, False, False, True, False
    match ctx.triggered_id:
        case "bt_all":
            if bt_dept_a:
                out = f14, True, False, False, True, False
            elif bt_mun_a:
                out = f11, True, False, False, False, True
        case "bt_pub":
            if bt_dept_a:
                out = f15, False, True, False, True, False
            elif bt_mun_a:
                out = f12, False, True, False, False, True
        case "bt_priv":
            if bt_dept_a:
                out = f16, False, False, True, True, False
            elif bt_mun_a:
                out = f13, False, False, True, False, True
        case "bt_dept":
            if bt_all_a:
                out = f14, True, False, False, True, False
            elif bt_pub_a:
                out = f15, False, True, False, True, False
            elif bt_priv_a:
                out = f16, False, False, True, True, False
        case "bt_mun":
            if bt_all_a:
                out = f11, True, False, False, False, True
            elif bt_pub_a:
                out = f12, False, True, False, False, True
            elif bt_priv_a:
                out = f13, False, False, True, False, True
    return out

"""

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
"""