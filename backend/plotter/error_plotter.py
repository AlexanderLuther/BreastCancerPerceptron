import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ErrorPlotter:
    def __init__(self, parent_window):
        self.__parent_window = parent_window
        pass

    def plot(self, errors):
        # Create a new window
        error_window = tk.Toplevel(self.__parent_window)
        error_window.title("Error vs Épocas")
        error_window.geometry("600x400")

        # Create a matplotlib figure
        fig, ax = plt.subplots()
        ax.plot(range(1, len(errors) + 1), errors, marker='o')
        ax.set_xlabel('Épocas')
        ax.set_ylabel('Error Total')
        ax.set_title('Error vs Épocas')

        # Integrate graphic in tkinter
        canvas = FigureCanvasTkAgg(fig, master=error_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
