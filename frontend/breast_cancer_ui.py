import tkinter as tk

import numpy as np
from backend.exception.HellException import HellException
from backend.file_reader import FileReader
from backend.perceptron import Perceptron
from backend.scatter_plotter import ScatterPlotter
from frontend.configuration_frame import ConfigurationFrame
from frontend.plot_frame import PlotFrame
from tkinter import filedialog
from tkinter import messagebox

FEATURE_NAMES = [
    'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
    'compactness_mean', 'concavity_mean', 'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean',
    'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
    'compactness_se', 'concavity_se', 'concave_points_se', 'symmetry_se', 'fractal_dimension_se',
    'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
    'compactness_worst', 'concavity_worst', 'concave_points_worst', 'symmetry_worst', 'fractal_dimension_worst'
]

class BreastCancerUI:

    def __init__(self):
        self.data = None
        self.file_reader = FileReader(headers=FEATURE_NAMES)
        self.scatter_plotter = ScatterPlotter()

        self.root = tk.Tk()
        self.root.title("Clasificador de Cancer de Mama")
        self.root.geometry("800x600")
        self.init()
        self.root.mainloop()

    def init(self):
        # Menú
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Cargar Datos", command=self.select_file)
        menubar.add_cascade(label="Archivo", menu=file_menu)

        # Principal frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Configuration frame
        self.config_frame = ConfigurationFrame(
            main_frame,
            plot_method=self.plot_data,
            train_method=self.train_perceptron
        )
        self.config_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Plot frame
        self.plot_frame = PlotFrame(main_frame)
        self.plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo de datos",
            filetypes=[("Archivos DATA", "*.data")]
        )
        if file_path:
            self.load_data(file_path)

    def load_data(self, file_path):
        try:
            self.data = self.file_reader.read_data(file_path)
            messagebox.showinfo(
                title="Éxito",
                message="¡Los datos se cargaron exitosamente!",
                parent=self.root
            )
        except HellException as e:
            messagebox.showerror("Error", f"No se pudieron cargar los datos:\n{e}")

    def plot_data(self):
        feature_x = self.config_frame.get_selected_feature1()
        feature_y = self.config_frame.get_selected_feature2()
        if self.general_required_data_is_complete(feature_x, feature_y):
            self.scatter_plotter.plot(
                data=self.data,
                feature_x=feature_x,
                feature_y=feature_y,
                plot_frame=self.plot_frame
            )

    def train_perceptron(self):
        feature_x = self.config_frame.get_selected_feature1()
        feature_y = self.config_frame.get_selected_feature2()
        if self.general_required_data_is_complete(feature_x, feature_y):
            learning_rate = self.config_frame.get_learning_rate()
            epochs = self.config_frame.get_epochs()
            if not learning_rate:
                messagebox.showerror("Error", "Tasa de aprendizaje no especificada", parent=self.root)
                return
            if not epochs:
                messagebox.showerror("Error", "Numero de epocas no especificado", parent=self.root)
                return
            converted_expected_outputs = self.data['diagnosis'].map({"M": 1, "B": 0})
            perceptron = Perceptron(num_inputs=2)
            perceptron.train(
                training_inputs=np.array(self.data[[feature_x, feature_y]]),
                expected_outputs=np.array(converted_expected_outputs),
                epochs=int(epochs),
                learning_rate=float(learning_rate)
            )
            self.scatter_plotter.plot(
                data=self.data,
                feature_x=feature_x,
                feature_y=feature_y,
                plot_frame=self.plot_frame,
                perceptron=perceptron
            )



    def general_required_data_is_complete(self, feature_x, feature_y):
        if self.data is None:
            messagebox.showerror("Error", "No hay datos cargados")
            return False
        if not feature_x:
            messagebox.showerror("Error", "Caracteristica 1 no seleccionada", parent=self.root)
            return False
        if not feature_y:
            messagebox.showerror("Error", "Caracteristica 2 no seleccionada", parent=self.root)
            return False
        return True
