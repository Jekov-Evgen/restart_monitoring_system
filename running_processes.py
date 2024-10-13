from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon
from style import CONST_WINDOW_SYSTEM_MONITORING


class RunProcess(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(800, 600)
        
    def draw_window(self):
        pass
    
    def data_inst(self):
        icon = "icon.png"
        app_ico = QIcon(icon)
        self.setWindowIcon(app_ico)
        self.setWindowTitle("Информация о запущенных процессах")
        self.setStyleSheet(CONST_WINDOW_SYSTEM_MONITORING)