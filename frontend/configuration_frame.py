import tkinter as tk
from tkinter import ttk
import re

FEATURE_NAMES = [
    'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
    'compactness_mean', 'concavity_mean', 'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean',
    'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
    'compactness_se', 'concavity_se', 'concave_points_se', 'symmetry_se', 'fractal_dimension_se',
    'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
    'compactness_worst', 'concavity_worst', 'concave_points_worst', 'symmetry_worst', 'fractal_dimension_worst'
]

class ConfigurationFrame(tk.Frame):
    def __init__(self, master, plot_method, train_method):
        super().__init__(master, bd=2, relief=tk.RIDGE, padx=10, pady=10)
        self.plot_method = plot_method
        self.train_method = train_method
        self.setup_widgets()

    def setup_widgets(self):
        tk.Label(self, text="Características para Grafico de Dispersion", font=("Arial", 14)).pack(pady=5)

        self.feature1_combo = ttk.Combobox(self, values=FEATURE_NAMES, state="readonly")
        self.feature1_combo.pack(pady=5)

        self.feature2_combo = ttk.Combobox(self, values=FEATURE_NAMES, state="readonly")
        self.feature2_combo.pack(pady=5)

        tk.Button(self, text="Visualizar Datos", command=self.plot_method).pack(pady=10)

        tk.Label(self, text="Parámetros de Entrenamiento", font=("Arial", 14)).pack(pady=10)

        learning_rate_validator = (self.register(self.__validate_learning_rate), "%P")
        tk.Label(self, text="Tasa de Aprendizaje").pack()
        self.learning_rate_entry = tk.Entry(self, validate="key", validatecommand=learning_rate_validator)
        self.learning_rate_entry.pack(pady=5)

        epoch_validator = (self.register(self.__validate_epochs), "%P")
        tk.Label(self, text="Número de Épocas").pack()
        self.epochs_entry = tk.Entry(self, validate="key", validatecommand=epoch_validator)
        self.epochs_entry.pack(pady=5)

        percentage_validator = (self.register(self.__validate_percentage), "%P")
        tk.Label(self, text="Porcentaje de datos para entrenar (%)").pack()
        self.train_percentage_entry = tk.Entry(self, validate="key", validatecommand=percentage_validator)
        self.train_percentage_entry.pack(pady=5)

        tk.Button(self, text="Entrenar Perceptrón", command=self.train_method).pack(pady=15)

    def __validate_epochs(self, value):
        if value == "":
            return True
        if value.isdigit():
            if int(value) > 0:
                return True
        return False

    def __validate_learning_rate(self, value):
        if value == "":
            return True
        if value == "0" or value == "0.":
            return True
        pattern = r"^0\.\d*$"
        if re.match(pattern, value):
            return True
        return False

    def __validate_percentage(self, value_if_allowed):
        if value_if_allowed == "":
            return True
        if value_if_allowed.isdigit():
            value = int(value_if_allowed)
            return 1 <= value <= 100
        return False

    def get_selected_feature1(self):
        return self.feature1_combo.get()

    def get_selected_feature2(self):
        return self.feature2_combo.get()

    def get_learning_rate(self):
        return self.learning_rate_entry.get()

    def get_train_percentage(self):
        return self.train_percentage_entry.get()

    def get_epochs(self):
        return self.epochs_entry.get()

