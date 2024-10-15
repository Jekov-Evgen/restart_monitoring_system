from PyQt6.QtWidgets import QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class DrawGraph(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
    
    def draw_graph_cpu(self, data_cpu):
        fig = Figure(figsize=(5, 4), dpi=100)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        
        ax.plot(data_cpu, label='Нагрузка процессора', color='blue', linestyle='-', marker='o')
        ax.legend(loc='upper left', frameon=True)
        ax.grid(True)
        ax.set_facecolor('#444444')
        
        self.layout.addWidget(canvas)
    
    def draw_graph_gpu(self, data_gpu):
        fig = Figure(figsize=(5, 4), dpi=100)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        
        ax.plot(data_gpu, label='Нагрузка GPU', color='blue', linestyle='-', marker='o')
        ax.legend(loc='upper left', frameon=True)
        ax.grid(True)
        ax.set_facecolor('#444444')
        
        self.layout.addWidget(canvas)
    
    def draw_graph_gpu_temp(self, data_gpu_temp):
        fig = Figure(figsize=(5, 4), dpi=100)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        
        ax.plot(data_gpu_temp, label='Температура GPU', color='red', linestyle='-', marker='o')
        ax.legend(loc='upper left', frameon=True)
        ax.grid(True)
        ax.set_facecolor('#444444')
        
        self.layout.addWidget(canvas)