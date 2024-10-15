from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon
from style import CONST_WINDOW_SYSTEM_MONITORING
from value_changes import DataInstallation
from receiving_download_data import data_CPU_C, data_memory_C, data_GPU


class SystemMonitoring(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 600)
        
    def draw_system_monitoring(self):
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        cpu = QLabel(text="Нагрузка процессора: ")
        self.cpu_info = QLabel(text="0")
        
        memory = QLabel(text="Нагрузка на память: ")
        self.memory_info = QLabel(text="0")
        
        gpu = QLabel(text="Нагрузка на видеокарту: ")
        self.gpu_info = QLabel(text="0")
        
        control_UI.addWidget(cpu)
        control_UI.addWidget(self.cpu_info)
        
        control_UI.addWidget(memory)
        control_UI.addWidget(self.memory_info)
        
        control_UI.addWidget(gpu)
        control_UI.addWidget(self.gpu_info)
        
        central_widget.setLayout(control_UI)

        self.setCentralWidget(central_widget)
        
    def data_installation(self):
        icon = "icon.png"
        app_ico = QIcon(icon)
        self.setWindowIcon(app_ico)
        self.setStyleSheet(CONST_WINDOW_SYSTEM_MONITORING)
        self.setWindowTitle("Показания нагрузки системы")
        control = DataInstallation()
        control.start_update(data_CPU_C, data_memory_C, data_GPU,
                           self.cpu_info, self.memory_info, self.gpu_info)