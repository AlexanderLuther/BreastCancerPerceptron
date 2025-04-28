import numpy as np

class DecisionBoundaryPlotter:
    def __init__(self):
        pass

    def plot(self, ax, data, feature_x, feature_y, perceptron):
        """
        Dibuja solo la frontera de decisión sobre un eje (ax).

        Parámetros:
        - ax: el eje de matplotlib donde dibujar.
        - data: DataFrame con los datos (para tomar el rango de valores).
        - feature_x: nombre del feature para X.
        - feature_y: nombre del feature para Y.
        - perceptron: objeto Perceptron entrenado.
        """
        # Definir rango para los features
        x_min, x_max = data[feature_x].min() - 1, data[feature_x].max() + 1
        y_min, y_max = data[feature_y].min() - 1, data[feature_y].max() + 1

        # Crear una malla de puntos
        xx, yy = np.meshgrid(
            np.linspace(x_min, x_max, 200),
            np.linspace(y_min, y_max, 200)
        )

        # Predecir la clase de cada punto
        grid = np.c_[xx.ravel(), yy.ravel()]
        Z = np.array([perceptron.predict(point) for point in grid])
        Z = Z.reshape(xx.shape)

        # Dibujar la frontera (colorear regiones)
        ax.contourf(xx, yy, Z, alpha=0.3, cmap="coolwarm")
