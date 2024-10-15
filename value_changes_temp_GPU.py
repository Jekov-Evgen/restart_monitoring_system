from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QTimer


class DataInstallationGPU():
    def __init__(self):
        self.delay = None
    
    def start_update(self, data_temperature_GPU, label_temperature_GPU : QLabel):
        if self.delay is None:
            self.delay = QTimer()
            self.delay.timeout.connect(lambda: self.update(data_temperature_GPU, label_temperature_GPU))
            self.delay.start(2000)
        
    def update(self, data_temperature_GPU, label_temperature_GPU : QLabel):
        data = data_temperature_GPU()
        label_temperature_GPU.setText(f"Температура вашего графического процессора: {data}")