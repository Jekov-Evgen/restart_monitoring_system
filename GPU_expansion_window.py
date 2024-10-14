from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon
from style import CONST_WINDOW_SYSTEM_MONITORING
from GetGpu import GetGPU
from value_changes_temp_GPU import DataInstallationGPU



class GPUAdvansed(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(800, 600)
        self.get_gpu = GetGPU()
        
    def draw_GPU_advansed(self):
        control_UI = QVBoxLayout()
        center_w = QWidget()
        
        name_gpu = QLabel()
        name_gpu.setText(f"Имя вашего графического процессора: {self.get_gpu.get_name_GPU()}")
        
        self.temp_gpu = QLabel()
        self.temp_gpu.setText(f"Температура вашего графического процессора: {self.get_gpu.get_temp_GPU()}")
        
        memory_used_gpu = QLabel()
        memory_used_gpu.setText(f"Количество используемой памяти: {self.get_gpu.get_memory_used_GPU()}")
        
        total_memory_gpu = QLabel()
        total_memory_gpu.setText(f"Общее количество памяти: {self.get_gpu.get_memory_total_GPU()}")
        
        control_UI.addWidget(name_gpu)
        control_UI.addWidget(self.temp_gpu)
        control_UI.addWidget(memory_used_gpu)
        control_UI.addWidget(total_memory_gpu)
        
        center_w.setLayout(control_UI)
        
        self.setCentralWidget(center_w)
    
    def data_inst(self):
        icon = "icon.png"
        app_ico = QIcon(icon)
        self.setWindowIcon(app_ico)
        self.setStyleSheet(CONST_WINDOW_SYSTEM_MONITORING)
        self.setWindowTitle("Расширинная информация видеокарты")
        set_data = DataInstallationGPU()
        set_data.start_update(self.get_gpu.get_temp_GPU, self.temp_gpu)