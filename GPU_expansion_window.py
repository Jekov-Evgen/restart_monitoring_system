from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon
import GPUtil
from style import CONST_WINDOW_SYSTEM_MONITORING


class GPUAdvansed(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(800, 600)
        
    def draw_GPU_advansed(self):
        control_UI = QVBoxLayout()
        center_w = QWidget()
        
        name_gpu = QLabel(text="Название карты")
        temp_gpu = QLabel(text="Температура")
        memory_used_gpu = QLabel(text="Количестов использованной памяти")
        total_memory_gpu = QLabel(text="Общее количество памяти")
        
        control_UI.addWidget(name_gpu)
        control_UI.addWidget(temp_gpu)
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
        
        
class GetGPU:
    def __init__(self) -> None:
        self.control_data = GPUtil.getGPUs()
    
    def all_GPU(self):    
        result = []
    
        for i in range(len(self.control_data)):
            gpu_data = self.control_data[i]
        
            result.append({
            'GPU_name': getattr(gpu_data, 'name', 'Unknown'), 
            'temperature': getattr(gpu_data, 'temperature', 'Unknown'), 
            'memory_used': getattr(gpu_data, 'memory_used', 'Unknown'),  
            'memory_total': getattr(gpu_data, 'memory_total', 'Unknown')  
            })
    
        return result