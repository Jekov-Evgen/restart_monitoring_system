from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QSizePolicy, QLabel
from PyQt6.QtGui import QIcon
from style import CONST_WINDOW_SYSTEM_MONITORING
from draw_graph import DrawGraph
from value_changes import DataInstallation

class GrapgIndicators(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(800, 600)

    def draw_window(self):
        contol_UI = QVBoxLayout()
        centr_w = QWidget()

        graph_cpu = DrawGraph()
        graph_gpu = DrawGraph()
        graph_temp_gpu = DrawGraph()
        control_data = DataInstallation()

        control_data.start_update(self.generate_fake_cpu_data, self.generate_fake_memory_data, self.generate_fake_gpu_data, QLabel, QLabel, QLabel)
        
        graph_cpu.draw_graph_cpu(control_data.get_cpu())
        graph_cpu.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        contol_UI.addWidget(graph_cpu)

        graph_gpu.draw_graph_gpu(control_data.get_gpu())
        graph_gpu.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        contol_UI.addWidget(graph_gpu)

        graph_temp_gpu.draw_graph_gpu_temp([50, 55, 60, 65])
        graph_temp_gpu.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        contol_UI.addWidget(graph_temp_gpu)

        centr_w.setLayout(contol_UI)
        self.setCentralWidget(centr_w)

    def data_inst(self):
        icon = "icon.png"
        app_ico = QIcon(icon)
        self.setWindowIcon(app_ico)
        self.setStyleSheet(CONST_WINDOW_SYSTEM_MONITORING)
        self.setWindowTitle("Графики нагрузок")

    def generate_fake_cpu_data(self):
        return 30

    def generate_fake_memory_data(self):
        return 40

    def generate_fake_gpu_data(self):
        return 20 
