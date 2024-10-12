from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon
from menu import Menu
from style import CONST_WINDOW
from data_on_the_main_window import PC


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(800, 600)
        self.pc = PC()
        
    def draw_UI(self):
        self.menu = Menu(self)
        interface_creation_V = QVBoxLayout()
        centr_w = QWidget()
        
        pc_name = QLabel(text="Имя пк: ")
        pc_name_info = QLabel(text=f"Имя вашего пк: {self.pc.machine_name()}")
        
        cpu = QLabel(text="Процессор: ")
        cpu_info = QLabel(text=f"Модель процессора: {self.pc.cpu_name()}")
        
        memory = QLabel(text="Память: ")
        memory_info = QLabel(text=f"Общее количество оперативной памяти: {self.pc.memory_total()} GB")
        
        gpu = QLabel(text="Графический процессор: ")
        gpu_info = QLabel(text=f"Модель графического процессора: {self.pc.gpu_name()}")
        
        disk = QLabel(text="Диск: ")
        disk_data = self.pc.memory_disk()
        disk_list = []
        
        for i in range(len(disk_data)):
            disk_list.append(QLabel())
            
        for i in range(0, len(disk_list)):
            temp = disk_list[i]
            temp.setText(f"Количество памяти на диске {i + 1}: {str(disk_data[i])} GB")
        
        interface_creation_V.addWidget(pc_name)
        interface_creation_V.addWidget(pc_name_info)
        
        interface_creation_V.addWidget(cpu)
        interface_creation_V.addWidget(cpu_info)
        
        interface_creation_V.addWidget(memory)
        interface_creation_V.addWidget(memory_info)
        
        interface_creation_V.addWidget(gpu)
        interface_creation_V.addWidget(gpu_info)
        
        interface_creation_V.addWidget(disk)
        
        for i in range(0, len(disk_list)):
            interface_creation_V.addWidget(disk_list[i])
        
        centr_w.setLayout(interface_creation_V)
        
        self.setCentralWidget(centr_w)
        
        
    def go_programm(self):
        self.setStyleSheet(CONST_WINDOW)
        icon = "icon.png"
        app_ico = QIcon(icon)
        self.setWindowIcon(app_ico)
        self.setWindowTitle("Система мониторинга")
        
        self.show()