import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
# the style arguments for the sidebar. We use position:fixed and a fixed width

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "padding": "2vw",
    "width": "80%",
    "height": "100%",
    "display": 'inline-block',
    "top": '0',
    "left": '20%',
    'bottom': '0',
    'position': 'fixed',
}
    
sidebar = html.Div(
    [
        html.Img(src="assets/logo_ingenieria.png", style = {'width' : '100%', 'object-fit': 'contain'}),
        html.H1("SABER 11", className="H1SB"),
        html.Hr(),
        html.P(
            "Exploremos los resultados de la prueba Saber 11 de los últimos años. ¿Qué desigualdades podemos identificar?", className="PSB"
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Introducción", href="/", active="exact"),
                dbc.NavLink("Históricos", href="/evtemp", active="exact"),
                dbc.NavLink("Por Estrato", href="/estrato", active="exact"),
                dbc.NavLink("Por Tipo Colegio", href="/colegio", active="exact"),
                dbc.NavLink("Por Municipio", href="/maps", active="exact"),
            ],
            vertical=True,
            pills=True,
            class_name = 'nbar'
        ),
    ],
    id='SIDEBAR',
)

content = html.Div(children = dash.page_container, id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([sidebar, content], style ={'display': 'inline-block'})


if __name__ == "__main__":
    app.run_server(debug=True)