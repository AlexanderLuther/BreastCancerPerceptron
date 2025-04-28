import tkinter as tk

class PlotFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master, bd=2, relief=tk.RIDGE, padx=10, pady=10)
        self.setup_widgets()

    def setup_widgets(self):
        self.plot_area = tk.Label(self, text="Area de gráficos", bg="white")
        self.plot_area.pack(fill=tk.BOTH, expand=True)

    def update_plot_text(self, text):
        self.plot_area.config(text=text)