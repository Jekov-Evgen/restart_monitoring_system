from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QScrollArea
from PyQt6.QtGui import QIcon
from style import CONST_WINDOW_SYSTEM_MONITORING
from obtaining_data_from_running_processes import GetProcess


class RunProcess(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showMaximized()
        self.proc = GetProcess()
        
    def draw_window(self):
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        process_list = self.proc.get_process()
        label_list = []
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        
        for i in range(len(process_list)):
            label_list.append(QLabel())
        
        for i in range(len(process_list)):
            label_list[i].setText(process_list[i])
            
        for i in range(len(process_list)):
            control_UI.addWidget(label_list[i])
        
        central_widget.setLayout(control_UI)
        scroll.setWidget(central_widget)    
        
        self.setCentralWidget(scroll)    
        
    def data_installation(self):
        icon = "icon.png"
        app_ico = QIcon(icon)
        self.setWindowIcon(app_ico)
        self.setWindowTitle("Запущенные процессы")
        self.setStyleSheet(CONST_WINDOW_SYSTEM_MONITORING)