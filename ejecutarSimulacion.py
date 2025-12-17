from generadorSeries import GeneradorSeries
from datosLoteria import DatosLoteria
from modeloLoteria import ModeloLoteria
from visualizadorResultados import VisualizadorResultados
import pandas as pd

def main():
    
    generador = GeneradorSeries()
    # Generar 10 combinaciones de ejemplo
    series = generador.generar_series(10)
    print("Series generadas:")
    for i, serie in enumerate(series, 1):
        print(f"Combinación {i}: {serie}")

    print("\n" + "="*50 + "\n")
    datos_loteria = DatosLoteria()

    # Generamos los datos de entrenamiento
    df_entrenamiento = datos_loteria.generar_datos_entrenamiento(1000)

    print("Datos de entrenamiento generados:")
    print(f"Shape del DataFrame: {df_entrenamiento.shape}")
    print("Primeras 10 filas:")
    print(df_entrenamiento.head(10))
    print("\nDistribución de la columna 'Exito':")
    print(df_entrenamiento['Exito'].value_counts())

    print("\n" + "="*50 + "\n")
    modelo_loteria = ModeloLoteria()

    # Preparar datos para entrenamiento
    X = df_entrenamiento.drop('Exito', axis=1)
    y = df_entrenamiento['Exito']

    # Entrenamiento del modelo
    modelo_loteria.entrenar(X, y)

    print("Modelo entrenado exitosamente.")

    print("\n" + "="*50 + "\n")

    # Se genera nuevas combinaciones para predicción
    nuevas_series = generador.generar_series(100)
    df_nuevas = pd.DataFrame(nuevas_series, columns=[f'num{i+1}' for i in range(6)])

    # Predecir probabilidades
    probabilidades = modelo_loteria.predecir_probabilidades(df_nuevas)

    print("Predicciones realizadas para 100 nuevas combinaciones.")
    print("Primeras 10 probabilidades:")
    for i in range(10):
        print(f"Combinación {i+1}: {probabilidades[i]:.4f}")

    # Encontrar la mejor combinación
    idx_max = probabilidades.argmax()
    mejor_combinacion = nuevas_series[idx_max]
    mejor_prob = probabilidades[idx_max]
    print(f"\nMejor combinación encontrada: {mejor_combinacion} con probabilidad {mejor_prob:.4f}")

    print("\n" + "="*50 + "\n")

    # Crear instancia de VisualizadorResultados
    visualizador = VisualizadorResultados()

    # Graficar top 10 combinaciones en un modelo de barras
    print("Generando gráfico de top 10 combinaciones más prometedoras...")
    visualizador.graficar_top_combinaciones(df_nuevas, probabilidades, top_n=10)


if __name__ == "__main__":
    main()

