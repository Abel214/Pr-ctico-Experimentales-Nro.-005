from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np

class ModeloLoteria:
    def __init__(self):
        self.scaler = StandardScaler()
        self.modelo = RandomForestClassifier(random_state=42)

    def entrenar(self, X, y):
        """
        Entrena el modelo RandomForestClassifier con los datos escalados.
        """
        # Escalar las características
        X_scaled = self.scaler.fit_transform(X)

        # Entrenar el modelo
        self.modelo.fit(X_scaled, y)

    def predecir_probabilidades(self, X):
        """
        Predice las probabilidades de éxito para nuevas combinaciones.
        """
        # Escalar las características
        X_scaled = self.scaler.transform(X)

        # Predecir probabilidades
        probabilidades = self.modelo.predict_proba(X_scaled)[:, 1]
        return probabilidades