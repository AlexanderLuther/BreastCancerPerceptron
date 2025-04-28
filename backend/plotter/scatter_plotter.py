import tkinter as tk

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from backend.plotter.decision_boundary_plotter import DecisionBoundaryPlotter

class ScatterPlotter:
    def __init__(self):
        self.boundary_plotter = DecisionBoundaryPlotter()
        pass

    def plot(self, data, feature_x, feature_y, plot_frame, perceptron=None):
        for widget in plot_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots()
        classes = {'M': 'red', 'B': 'blue'}
        colors = data['diagnosis'].map(classes)
        ax.scatter(data[feature_x], data[feature_y], c=colors)
        ax.set_xlabel(feature_x)
        ax.set_ylabel(feature_y)
        ax.set_title('Grafico de Dispersion')

        if perceptron:
            accuracy = perceptron.calculate_accuracy(
                np.array(data[[feature_x, feature_y]]),
                np.array(data['diagnosis'].map({"M": 1, "B": 0}))
            )
            self.boundary_plotter.plot(ax, data, feature_x, feature_y, perceptron)
            ax.set_title(f'Gráfico de Dispersión y Frontera de Decisión\nExactitud: {accuracy * 100:.2f}%')

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)