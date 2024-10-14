from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon
import cpuinfo
import psutil
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
    
    def get_name_CPU(self):
        return self.contol_data.get('brand_raw')
    
    def get_arch_CPU(self):
        return self.contol_data.get('arch')
    
    def get_hz_actual_CPU(self):
        return self.contol_data.get('hz_actual_friendly')
    
    def get_hz_advertised_CPU(self):
        return self.contol_data.get('hz_advertised_friendly')
    
    def get_L2_cache_CPU(self):
        return str(int(self.contol_data.get('l2_cache_size')) / (1024 * 1024))
    
    def get_L3_cache_CPU(self):
        return str(int(self.contol_data.get('l3_cache_size')) / (1024 * 1024))
    
    def get_bool_ht_CPU(self):
        check = self.contol_data.get('flags')
        
        if "ht" in check:
            return "Поддержка многопоточности присутствует"
        else:
            return "Нет поддержки многопоточности"
    
    def get_bool_aes_CPU(self):
        check = self.contol_data.get('flags')
        
        if "aes" in check:
            return "Поддержка аппаратного шифрования присутствует"
        else:
            return "Нет поддержки аппаратного шифрования"
        
    def get_bool_vec_CPU(self):
        check = self.contol_data.get('flags')
        
        if (("avx" in check) and ("avx2" in check) and ("sse" in check)
            and ("sse2" in check) and ("sse4_1" in check) and ("sse4_2" in check)):
            
            return "Поддержка векторных инструкций присутствует"
        else:
            return "Нет поддержки векторных инструкций"
        
    def get_count_CPU(self):
        return self.contol_data.get('count')