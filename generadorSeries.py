import numpy as np

class GeneradorSeries:
    def __init__(self):
        pass

    def generar_series(self, cantidad):
        """
        Genera cantidad combinaciones de 6 números únicos aleatorios entre 1 y 49.
        Cada combinación está ordenada.

        """
        series = []
        for _ in range(cantidad):
            # Generar 6 números únicos entre 1 y 49
            combinacion = np.random.choice(range(1, 50), size=6, replace=False)
            # Ordenar la combinación
            combinacion.sort()
            series.append(combinacion.tolist())
        return series
