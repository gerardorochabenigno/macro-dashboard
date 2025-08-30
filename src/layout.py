import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.colors as colors

def create_layout():

    """Método para crear layout de la página de Dash"""    

    # Configuración del layout
    return html.Div([
        # Título principal
        html.H1("Dashboard Macro",
                style={
                    'textAlign': 'center',
                    'marginBottom': 30,
                    'color': '#2c3e50',
                    'fontFamily': 'Times New Roman, serif'
                }),
        # Contenedor de dos columnas para las gráficas
        html.Div([
            # Columna izquierda - Serie de tiempo del IGAE
            html.Div([
                html.H3("Indicador Global de la Actividad Económica",
                    style={'textAlign': 'center', 'color': '#34495e'}),

                # Controles de la gráfica
                html.Div([
                    dcc.RangeSlider(
                        id='date-range-slider',
                        marks = {},
                        value=[],
                        tooltip={'placement':'bottom', 'always_visible':True}
                    )
                ], style={'margin': '20px 0'}),
                # Gráfica de serie de tiempo
                dcc.Graph(id='igae-timeseries')
            ], style={
                'flex': '1',
                'verticalAlign': 'top',
                'padding': '20px',
                'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
                'borderRadius': '8px',
                'backgroundColor': '#ffffff',
                'marginBottom': '20px',
                'height': '600px',
                #'overflowY': 'auto'
            }),
            # Columna derecha - Correlaciones entre el IGAE y las otras variables
            html.Div([
                html.H3("Correlaciones con el IGAE",
                        style={'textAlign': 'center', 'color': '#34495e'}),
                
                # Selector de variables
                html.Div([
                    html.Label("Seleccionar variables"),
                    dcc.Dropdown(
                        id='correlation-variables',
                        multi=True,
                        placeholder="Selecciona una variable para correlación"
                    )
                ], style={'margin':'20px 0'}),

                # Gráfica de correlaciones
                dcc.Graph(id='correlation-scatter'),

                # Tabla de correlaciones
                html.Div(id='correlation-table')
            ], style={
                'flex': '1',
                'verticalAlign': 'top',
                'padding': '20px',
                'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
                'borderRadius': '8px',
                'backgroundColor': '#ffffff',
                'marginBottom': '20px',
                'height': '600px',
                'overflowY': 'auto'
            }),
        ], style={
            'display':'flex',
            'justifyContent': 'space-between',
            'gap': '20px'
        }),

        # Información adicional
        html.Div([
            html.Hr(),
            html.P("IGAE: Indicador Global de la Actividad Económica", 
                style={'textAlign': 'center', 'color': '#7f8c8d', 'fontStyle': 'italic'})
        ])
    ])