import dash
from dash import html

dash.register_page(__name__, path='/',  name='Introducción')

layout = html.Div([
    html.H1('Pruebas SABER 11', className = 'H1MP'),
    html.Hr(),
    html.Div([
        html.H2('¿Qué son?', style = {'width': '25%','height': '100%',"display": "inline-block", "verticalAlign": 'top'}, className='PMT'),
        html.P('Las pruebas SABER 11 son pruebas estandarizadas que se aplican a todos los estudiantes de Grado 11 en el país. Son un insumo importante para estudiar las desigualdades existentes en el sistema educativo básico y medio en el país.', className= "PMP", style = {"width": "70%","display": "inline-block", "padding-left": "2vmax"})
    ], style = {"width": "100%", 'verticalAlign': 'top', "margin-top": "3vmax"}
    ),
    html.Div([
        html.H2('¿De dónde sacamos los datos?', style = {'width': '25%','height': '100%',"display": "inline-block", "verticalAlign": 'top'}, className='PMT'),
        html.P('Los datos han sido recuperados directamente de la página del ICFES, corresponden a los resultados animizados de las pruebas SABER 11 desde el año 2017 hasta 2022. Estas bases son públicas y cualquier colombiano las puede usar para hacer análisis o investigación.', className= "PMP", style = {"width": "70%","display": "inline-block", "padding-left": "2vmax"})
    ], style = {"width": "100%",  'verticalAlign': 'top', "margin-top": "2vmax"}
    ),
    html.Div([
        html.H2('¿Cuántos y qué datos tenemos?', style = {'width': '25%','height': '100%',"display": "inline-block", "verticalAlign": 'top'}, className='PMT'),
        html.P('La base de datos completa contiene los resultados de la prueba SABER 11 de 3.303.475 personas, para cada persona tenemos información personal como el género y la edad, del tipo de colegio del que se graduó, y también información socioeconómica de relevancia.', className= "PMP", style = {"width": "70%","display": "inline-block", "padding-left": "2vmax"})
    ], style = {"width": "100%", 'verticalAlign': 'top', "margin-top": "2vmax"}
    ),
    html.Div([
        html.H2('¿Quién elaboró el DashBoard?', style = {'width': '25%','height': '100%',"display": "inline-block", "verticalAlign": 'top'}, className='PMT'),
        html.P('Miguel Ángel Uribe es físico y magister en física de la Universidad Nacional de Colombia, y Doctor en Física de la Universidad de Friburgo, Suiza. Es profesor asociado de la Facultad de Ingeniería de la Universidad de la Sabana. La analítica de datos es su principal campo de interés y actualmente tiene proyectos donde aplica estos conocimientos en campos tan variados como la educación, el transporte, la psiquiatría y la terapia física.', className= "PMP", style = {"width": "60%","display": "inline-block", "padding-left": "2vmax"}),
        html.Img(src="assets/FOTO.png", style = {'width' : '15%', 'object-fit': 'contain', 'verticalAlign': 'top', 'padding-left':"0.8vmax"}),
    ], style = {"width": "100%",  'verticalAlign': 'top', "margin-top": "2vmax"}
    ),
], style ={'width':'75vw', 'height': '95vh','padding': '0', 'margins': '0'})