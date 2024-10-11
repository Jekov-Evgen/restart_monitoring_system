from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QTimer

class DataInstallation():
    def __init__(self) -> None:
        self.delay = None
    
    def start_update(self, data_cpu, data_memory,  lb_cpu : QLabel, lb_memory : QLabel):
        if self.delay is None:
            self.delay = QTimer()
            self.delay.timeout.connect(lambda: self.update(data_cpu, data_memory,  lb_cpu, lb_memory))
            self.delay.start(2000)
        
    def update(self, data_cpu, data_memory,  lb_cpu : QLabel, lb_memory : QLabel) -> None:
        cpu = data_cpu()
        memory = data_memory()
        lb_cpu.setText(f"{cpu} %")
        lb_memory.setText(f"{memory} %")
        