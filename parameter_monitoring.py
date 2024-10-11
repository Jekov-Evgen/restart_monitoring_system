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
        cpu_H_L = QHBoxLayout()
        memory_H_L = QHBoxLayout()
        gpu_H_L = QHBoxLayout()
        centr_w = QWidget()
        
        cpu = QLabel(text="Нагрузка процессора: ")
        self.cpu_info = QLabel(text="0")
        
        memory = QLabel(text="Нагрузка на память: ")
        self.memory_info = QLabel(text="0")
        
        gpu = QLabel(text="Нагрузка на видеокарту: ")
        self.gpu_info = QLabel(text="0")
        
        cpu_H_L.addWidget(cpu)
        cpu_H_L.addWidget(self.cpu_info)
        
        memory_H_L.addWidget(memory)
        memory_H_L.addWidget(self.memory_info)
        
        gpu_H_L.addWidget(gpu)
        gpu_H_L.addWidget(self.gpu_info)
        
        control_system_V.addLayout(cpu_H_L)
        control_system_V.addLayout(memory_H_L)
        control_system_V.addLayout(gpu_H_L)
        
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