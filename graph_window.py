from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QSizePolicy
from PyQt6.QtGui import QIcon
from style import CONST_WINDOW_SYSTEM_MONITORING
from draw_graph import DrawGraph

class GrapgIndicators(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(800, 600)

    def draw_window(self):
        contol_UI = QVBoxLayout()
        centr_w = QWidget()

        graph = DrawGraph()
        
        graph.draw_graph_cpu([1, 2, 3, 4])
        graph.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)  # Политика размера
        contol_UI.addWidget(graph)

        graph = DrawGraph()
        graph.draw_graph_gpu([1, 2, 3, 4])
        graph.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        contol_UI.addWidget(graph)

        graph = DrawGraph()
        graph.draw_graph_gpu_temp([1, 2, 3, 4])
        graph.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        contol_UI.addWidget(graph)

        centr_w.setLayout(contol_UI)
        self.setCentralWidget(centr_w)

    def data_inst(self):
        icon = "icon.png"
        app_ico = QIcon(icon)
        self.setWindowIcon(app_ico)
        self.setStyleSheet(CONST_WINDOW_SYSTEM_MONITORING)
        self.setWindowTitle("Графики нагрузок")