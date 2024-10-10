from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon
from menu import Menu
from style import CONST_WINDOW


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(800, 600)
        
    def draw_UI(self):
        self.menu = Menu(self)
        interface_creation_V = QVBoxLayout()
        centr_w = QWidget()
        
        cpu = QLabel(text="Процессор: ")
        cpu_info = QLabel(text="Название")
        
        memory = QLabel(text="Память: ")
        memory_info = QLabel(text="Название")
        
        gpu = QLabel(text="Графический процессор: ")
        gpu_info = QLabel(text="Название")
        
        interface_creation_V.addWidget(cpu)
        interface_creation_V.addWidget(cpu_info)
        
        interface_creation_V.addWidget(memory)
        interface_creation_V.addWidget(memory_info)
        
        interface_creation_V.addWidget(gpu)
        interface_creation_V.addWidget(gpu_info)
        
        centr_w.setLayout(interface_creation_V)
        
        self.setCentralWidget(centr_w)
        
        
    def go_programm(self):
        self.setStyleSheet(CONST_WINDOW)
        icon = "icon.png"
        app_ico = QIcon(icon)
        self.setWindowIcon(app_ico)
        self.setWindowTitle("Система мониторинга")
        
        self.show()