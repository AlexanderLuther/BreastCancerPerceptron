import numpy as np

class DecisionBoundaryPlotter:
    def __init__(self):
        pass

    def plot(self, ax, data, feature_x, feature_y, perceptron):
        # Set range for x and y
        x_min, x_max = data[feature_x].min() - 1, data[feature_x].max() + 1
        y_min, y_max = data[feature_y].min() - 1, data[feature_y].max() + 1

        # Create a point mesh
        xx, yy = np.meshgrid(
            np.linspace(x_min, x_max, 200),
            np.linspace(y_min, y_max, 200)
        )

        # Predict class of each point in mesh
        grid = np.c_[xx.ravel(), yy.ravel()]
        Z = np.array([perceptron.predict(point) for point in grid])
        Z = Z.reshape(xx.shape)

        # Write decision boundary
        ax.contourf(xx, yy, Z, alpha=0.3, cmap="coolwarm")
