# Práctico Experimental N°005

## 📊 Simulación de Datos Históricos y Predicción con Random Forest

Este proyecto corresponde al **Práctico-Experimental N°005** de la asignatura **Data Mining** y tiene como objetivo simular un conjunto de datos históricos y aplicar un modelo de **Machine Learning (Random Forest)** para estimar la probabilidad de éxito de combinaciones numéricas generadas aleatoriamente.

El enfoque del desarrollo se basa en **Programación Orientada a Objetos (POO)**, asegurando una arquitectura modular, clara y escalable.

---
## 🧠 Descripción General del Código 

El código implementa un flujo completo de minería de datos, dividido en clases con responsabilidades bien definidas:

1. **Generación de datos**
   Se crean combinaciones numéricas aleatorias que simulan sorteos históricos, incluyendo una etiqueta de éxito o fracaso.

2. **Preparación del dataset**
   Los datos generados se organizan en un `DataFrame`, separando características y variable objetivo.

3. **Entrenamiento del modelo**
   Se entrena un modelo de **Random Forest** utilizando datos previamente escalados para mejorar su desempeño.

4. **Predicción probabilística**
   El modelo estima la probabilidad de éxito de nuevas combinaciones generadas.

5. **Visualización de resultados**
   Se presenta un gráfico con las combinaciones más prometedoras según la probabilidad estimada.

---

## 🧱 Arquitectura del Proyecto

El sistema está organizado en las siguientes clases:

* **GeneradorSeries**: genera combinaciones numéricas aleatorias.
* **DatosLoteria**: construye el dataset histórico de entrenamiento.
* **ModeloLoteria**: entrena el modelo Random Forest y realiza predicciones.
* **VisualizadorResultados**: muestra gráficamente las combinaciones con mayor probabilidad.
* **EjecutarSimulacion**: coordina todo el flujo de ejecución del proyecto.

---

## ⚙️ Requisitos del Sistema

* Python **3.10 o superior**
* Entorno virtual (recomendado)

### 📦 Librerías necesarias

```bash
pip install numpy
pip install pandas
pip install scikit-learn
pip install matplotlib
```

---

## ▶️ Ejecución del Proyecto

1. Crear y activar un entorno virtual.
2. Instalar las dependencias indicadas.
3. Ejecutar el archivo principal del proyecto.
4. Visualizar en consola la combinación con mayor probabilidad estimada.
5. Analizar el gráfico generado con el **Top 10** de combinaciones más prometedoras.

---

## ✍️ Autores

Práctica desarrollada por: **Byron Gonzalez-Brian Aguinsaca-Abel Mora**.
