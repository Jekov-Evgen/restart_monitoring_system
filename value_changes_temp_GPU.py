from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QTimer


class DataInstallationGPU():
    def __init__(self) -> None:
        self.delay = None
    
    def start_update(self, data_temp, lb_temp : QLabel):
        if self.delay is None:
            self.delay = QTimer()
            self.delay.timeout.connect(lambda: self.update(data_temp, lb_temp))
            self.delay.start(2000)
        
    def update(self, data_temp, lb_temp : QLabel) -> None:
        data = data_temp()
        lb_temp.setText(f"Температура вашего графического процессора: {data}")