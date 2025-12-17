import matplotlib.pyplot as plt
import pandas as pd

class VisualizadorResultados:
    def __init__(self):
        pass

    def graficar_top_combinaciones(self, df_series, probabilidades, top_n=10):
        """
        Muestra un gráfico de barras horizontal con las top_n combinaciones más prometedoras.
        """
        # Crear etiquetas para las combinaciones
        etiquetas = []
        for _, row in df_series.iterrows():
            combinacion = '-'.join(map(str, row.values))
            etiquetas.append(combinacion)

        # Crear DataFrame temporal con etiquetas y probabilidades
        df_temp = pd.DataFrame({
            'Combinacion': etiquetas,
            'Probabilidad': probabilidades
        })
        df_top = df_temp.sort_values('Probabilidad', ascending=False).head(top_n)
        plt.figure(figsize=(10, 6))
        plt.barh(df_top['Combinacion'], df_top['Probabilidad'], color='skyblue')
        plt.xlabel('Probabilidad de Éxito')
        plt.ylabel('Combinación')
        plt.title(f'Top {top_n} Combinaciones Más Prometedoras')
        plt.gca().invert_yaxis() 
        plt.tight_layout()
        plt.show()