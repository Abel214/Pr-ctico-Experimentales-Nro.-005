import pandas as pd
import numpy as np
from generadorSeries import GeneradorSeries

class DatosLoteria:
    def __init__(self):
        self.generador = GeneradorSeries()

    def generar_datos_entrenamiento(self, cantidad=1000):
        """
        Generar un DataFrame con 1000 combinaciones y una columna adicional
          llamada "Exito" con valores 1 (éxito) o 0 (fracaso), simulando que el 10% de las combinaciones fueron ganadoras.
        """
        # Generar las series
        series = self.generador.generar_series(cantidad)

        # Crear DataFrame
        df = pd.DataFrame(series, columns=[f'num{i+1}' for i in range(6)])

        # Simular éxito: 10% de las combinaciones son exitosas
        num_exitos = int(cantidad * 0.1)
        exitos = [1] * num_exitos + [0] * (cantidad - num_exitos)
        np.random.shuffle(exitos)  # Mezclar aleatoriamente
        df['Exito'] = exitos

        return df