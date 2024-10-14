from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QScrollArea
from PyQt6.QtGui import QIcon
from style import CONST_WINDOW_SYSTEM_MONITORING
from obtaining_data_from_running_processes import GetProcess


class RunProcess(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.showMaximized()
        self.proc = GetProcess()
        
    def draw_window(self):
        control_UI = QVBoxLayout()
        center_w = QWidget()
        proc_list = self.proc.get_process()
        label_list = []
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        
        for i in range(len(proc_list)):
            label_list.append(QLabel())
        
        for i in range(len(proc_list)):
            label_list[i].setText(proc_list[i])
            
        for i in range(len(proc_list)):
            control_UI.addWidget(label_list[i])
        
        center_w.setLayout(control_UI)
        scroll.setWidget(center_w)    
        
        self.setCentralWidget(scroll)    
        
    def data_inst(self):
        icon = "icon.png"
        app_ico = QIcon(icon)
        self.setWindowIcon(app_ico)
        self.setWindowTitle("Запущенные процессы")
        self.setStyleSheet(CONST_WINDOW_SYSTEM_MONITORING)