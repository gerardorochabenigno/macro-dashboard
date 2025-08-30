from dash import Input, Output
import plotly.graph_objects as go
import pandas as pd

def register_igae_timeseries_callback(app, igae_data:pd.DataFrame):
    """Método para registrar el callback de la gráfica de series de tiempo del IGAE -original y desestacionalziado-"""
    @app.callback(
        Output('igae-timeseries', 'figure'),
        [Input('date-range-slider', 'value')]
    )
    def update_timeseries(date_range):
        fig = go.Figure()

        # Agregamos la serie original
        fig.add_trace(go.Scatter(
            x=igae_data.index,
            y = igae_data['737121'],
            mode='lines',
            name='IGAE (original)',
            line=dict(color='#3498db', width=2),
            opacity=0.7
        ))

        # Agregamos la serie desestacionalizada
        fig.add_trace(go.Scatter(
            x=igae_data.index,
            y = igae_data['737219'],
            mode='lines',
            name='IGAE (desestacionalizada)',
            line=dict(color='#d4631e', width=2),
            opacity=1
        ))

        fig.update_layout(
            title="IGAE: serie original y desestacionalizada",
            xaxis_title="Fecha",
            yaxis_title="IGAE (índice)",
            hovermode="x unified",
            plot_bgcolor="white",
            paper_bgcolor="white",
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.2,
                xanchor="center",
                x=0.5),
            autosize=False,
            height=500
        )
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')

        return fig
    
def register_correlations_callback(app, corr_data: pd.DataFrame):
    @app.callback(
        Output('correlation-scatter', 'figure'),
        [Input('correlation-variables', 'value')]
    )
    def update_correlations(selected_vars):  # Solo el parámetro del Input
        fig = go.Figure()
        
        if not selected_vars or len(selected_vars) == 0:
            # Gráfica vacía si no hay selección
            fig.update_layout(title="Selecciona variables para ver correlaciones",
                              #xaxis_title=var_name,
                              #yaxis_title="IGAE",
                              height=200,
                              autosize=False)
            return fig
        
        # Tomar la primera variable seleccionada
        var_name = selected_vars[0]
        
        if var_name in corr_data.columns:
            fig.add_trace(go.Scatter(
                x=corr_data[var_name],
                y=corr_data[corr_data.columns[0]],  # o la columna que tengas
                mode='markers',
                name=f'IGAE vs {var_name}',
                marker=dict(color='#3498db', size=6, opacity=0.6)
            ))
            
            fig.update_layout(
                title=f"Correlación: IGAE vs {var_name}",
                xaxis_title=var_name,
                yaxis_title="IGAE",
                height=200,
                autosize=False
            )
        
        return fig