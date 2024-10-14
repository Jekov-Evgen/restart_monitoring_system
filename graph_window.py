from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon
from style import CONST_WINDOW_SYSTEM_MONITORING

class GrapgIndicators(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(800, 600)
        
    def draw_window(self):
        contol_UI = QVBoxLayout()
        centr_w = QWidget()
        
        graph_cpu = QLabel(text="График процессора(Нагрузка): ")
        graph_gpu = QLabel(text="График графического процессора(Нагрузка): ")
        graph_temp_gpu = QLabel(text="График графического процессора(температура): ")
        
        contol_UI.addWidget(graph_cpu)
        contol_UI.addWidget(graph_gpu)
        contol_UI.addWidget(graph_temp_gpu)
        
        centr_w.setLayout(contol_UI)
        
        self.setCentralWidget(centr_w)
    
    def data_inst(self):
        icon = "icon.png"
        app_ico = QIcon(icon)
        self.setWindowIcon(app_ico)
        self.setStyleSheet(CONST_WINDOW_SYSTEM_MONITORING)
        self.setWindowTitle("Графики нагрузок")