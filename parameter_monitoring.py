from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PyQt6.QtGui import QIcon
from style import CONST_WINDOW_SYSTEM_MONITORING
from value_changes import DataInstallation
from receiving_download_data import processor_integration, memory_integration, GPU_integration


class SystemMonitoring(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(800, 600)
        
    def draw_system_monitoring(self):
        control_system_V = QVBoxLayout()
        centr_w = QWidget()
        
        cpu = QLabel(text="Нагрузка процессора: ")
        self.cpu_info = QLabel(text="0")
        
        memory = QLabel(text="Нагрузка на память: ")
        self.memory_info = QLabel(text="0")
        
        gpu = QLabel(text="Нагрузка на видеокарту: ")
        self.gpu_info = QLabel(text="0")
        
        disk = QLabel(text="Нагрузка на диск: ")
        self.disk_info = QLabel(text="0")
        
        control_system_V.addWidget(cpu)
        control_system_V.addWidget(self.cpu_info)
        
        control_system_V.addWidget(memory)
        control_system_V.addWidget(self.memory_info)
        
        control_system_V.addWidget(gpu)
        control_system_V.addWidget(self.gpu_info)
        
        control_system_V.addWidget(disk)
        control_system_V.addWidget(self.disk_info)
        
        centr_w.setLayout(control_system_V)

        self.setCentralWidget(centr_w)
        
    def data_installation(self):
        icon = "icon.png"
        app_ico = QIcon(icon)
        self.setWindowIcon(app_ico)
        self.setStyleSheet(CONST_WINDOW_SYSTEM_MONITORING)
        self.setWindowTitle("Показания нагрузки системы")
        control = DataInstallation()
        control.start_update(processor_integration, memory_integration, GPU_integration,
                           self.cpu_info, self.memory_info, self.gpu_info)