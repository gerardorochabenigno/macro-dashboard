import pandas as pd
"""
Módulo para la preparación de los datos para el dashbpard de dash
"""

class DataLoader:

    @staticmethod
    def carga_local(path:str) -> pd.DataFrame: # En este momento la carga solo es de datos mensuales, después se agregaran
        return pd.read_csv(path, encoding='utf-8', parse_dates=['date'])

class ChartDataPreprocessor:

    """
    Clase para cargar (local y de AWS), y preprocesar los datos que se mostrarán en las gráficas de dash.
    """

    def __init__(self, config): # Agregar más adelante las variables de entorno de AWS
        self.config = config

    @staticmethod
    def serie_igae_preprocessor():
        data_loader = DataLoader()
        igae_data = [pd.read_csv('https://macro-forecast.s3.amazonaws.com/data/inegi/csv/737121.csv'),
                     pd.read_csv('https://macro-forecast.s3.amazonaws.com/data/inegi/csv/737219.csv')]
        igae_df = pd.merge(igae_data[0], igae_data[1], how='inner', on='date')
        igae_df = igae_df.loc[igae_df['date']>='2000-01-01']
        igae_df.set_index('date', inplace=True)

        return igae_df
    
    @staticmethod
    def datos_corr_preprocessor():
        data_loader = DataLoader()
        corr_data = [pd.read_csv('https://macro-forecast.s3.amazonaws.com/data/inegi/csv/737121.csv'),
                     pd.read_csv('https://macro-forecast.s3.amazonaws.com/data/inegi/csv/737219.csv')]
        corr_data = pd.merge(corr_data[0], corr_data[1], how='inner', on='date')

        corr_data = corr_data.loc[corr_data['date']>='2000-01-01']
        corr_data.set_index('date', inplace=True)

        return corr_data
    

    
