import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.colors as colors
from src.layout import create_layout
from src.callbacks import register_igae_timeseries_callback, register_correlations_callback
from src.dash_prep import DataLoader, ChartDataPreprocessor

app = dash.Dash(__name__)

app.layout = create_layout()

chart_prep = ChartDataPreprocessor('config')
igae_data = chart_prep.serie_igae_preprocessor()

chart_prep = ChartDataPreprocessor('config')
igae_data = chart_prep.serie_igae_preprocessor()
corr_data = chart_prep.datos_corr_preprocessor()

register_igae_timeseries_callback(app, igae_data=igae_data)
register_correlations_callback(app, igae_data, )


if __name__=='__main__':
    app.run(debug=False, host='0.0.0.0', port = 8050)
