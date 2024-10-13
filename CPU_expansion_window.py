from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon
import cpuinfo
from style import CONST_WINDOW_SYSTEM_MONITORING


class ProcessorAdvansed(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(800, 600)
        
    def draw_processor_advansed(self):
        control_UI = QVBoxLayout()
        center_w = QWidget()
        
        cpu_name = QLabel(text="Название процессора")
        cpu_arch = QLabel(text="Архитектура процессора")
        cpu_hz = QLabel(text="тактовая чистота процессора, настоящая")
        cpu_hz_advertised = QLabel(text="Рекламируемая частота")
        cpu_cache2 = QLabel(text="Сколько кеша на 2 уровне")
        cpu_cache3 = QLabel(text="Размер кэша на 3 уровне")
        cpu_count = QLabel(text="Количество ядер процессора")
        multithreading_support = QLabel(text="Поддержка многопточности")
        hardware_encryption_support = QLabel(text="Поддержка аппаратного шифрования")
        vector_instructions = QLabel(text="Проверка поддержки векторных инструкций")
        temp_cpu = QLabel(text="Температура процессора")
        
        control_UI.addWidget(cpu_name)
        control_UI.addWidget(cpu_arch)
        control_UI.addWidget(cpu_hz)
        control_UI.addWidget(cpu_hz_advertised)
        control_UI.addWidget(cpu_cache2)
        control_UI.addWidget(cpu_cache3)
        control_UI.addWidget(cpu_count)
        control_UI.addWidget(multithreading_support)
        control_UI.addWidget(hardware_encryption_support)
        control_UI.addWidget(vector_instructions)
        control_UI.addWidget(temp_cpu)
        
        center_w.setLayout(control_UI)
        
        self.setCentralWidget(center_w)
    
    def data_inst(self):
        icon = "icon.png"
        app_ico = QIcon(icon)
        self.setWindowIcon(app_ico)
        self.setStyleSheet(CONST_WINDOW_SYSTEM_MONITORING)
        self.setWindowTitle("Расширинная информация процессора")
        
        

class GetCPU:
    def __init__(self) -> None:
        self.contol_data = cpuinfo.get_cpu_info()
        
    def all_result(self):
        return self.contol_data