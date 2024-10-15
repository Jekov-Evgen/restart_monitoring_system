from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon
from style import CONST_WINDOW_SYSTEM_MONITORING
from GetCpu import GetCPU


class ProcessorAdvansed(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 600)
        self.get_data_CPU = GetCPU()
        
    def draw_processor_advansed(self):
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        cpu_name = QLabel()
        cpu_name.setText(f"Модель вашего процессора: {self.get_data_CPU.get_name_CPU()}")
        
        cpu_arch = QLabel()
        cpu_arch.setText(f"Архитектура на которой работает ваш процессор: {self.get_data_CPU.get_arch_CPU()}")
        
        cpu_hz = QLabel()
        cpu_hz.setText(f"Актуальные гигагерцы: {self.get_data_CPU.get_hz_actual_CPU()}")
        
        cpu_hz_advertised = QLabel()
        cpu_hz_advertised.setText(f"Рекламные гигагерцы: {self.get_data_CPU.get_hz_advertised_CPU()}")
        
        cpu_cache2 = QLabel()
        cpu_cache2.setText(f"Количество памяти в кэше 2 уровня: {self.get_data_CPU.get_L2_cache_CPU()} Мb")
        
        cpu_cache3 = QLabel()
        cpu_cache3.setText(f"Количество памяти в кэше 3 уровня: {self.get_data_CPU.get_L3_cache_CPU()} Mb")
        
        cpu_count = QLabel()
        cpu_count.setText(f"Количество ядер вашего процессора: {self.get_data_CPU.get_count_CPU()}")
        
        multithreading_support = QLabel()
        multithreading_support.setText(self.get_data_CPU.get_bool_ht_CPU())
        
        hardware_encryption_support = QLabel()
        hardware_encryption_support.setText(self.get_data_CPU.get_bool_aes_CPU())
        
        vector_instructions = QLabel()
        vector_instructions.setText(self.get_data_CPU.get_bool_vec_CPU())
        
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
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
    
    def data_installation(self):
        icon = "icon.png"
        app_ico = QIcon(icon)
        self.setWindowIcon(app_ico)
        self.setStyleSheet(CONST_WINDOW_SYSTEM_MONITORING)
        self.setWindowTitle("Расширинная информация процессора")