from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QTimer

class DataInstallation():
    def __init__(self):
        self.delay = None
    
    def start_update(self, data_cpu, data_memory, data_gpu, label_cpu : QLabel, label_memory : QLabel, label_gpu : QLabel):
        if self.delay is None:
            self.delay = QTimer()
            self.delay.timeout.connect(lambda: self.update(data_cpu, data_memory, data_gpu, label_cpu, label_memory, label_gpu))
            
            self.delay.start(2000)
        
    def update(self, data_cpu, data_memory, data_gpu, label_cpu : QLabel, label_memory : QLabel, label_gpu : QLabel):
        cpu = data_cpu()
        memory = data_memory()
        gpu = data_gpu()
        label_cpu.setText(f"{cpu} %")
        label_memory.setText(f"{memory} %")
        label_gpu.setText(f"{gpu} %")
        