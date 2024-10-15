from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon
from menu import Menu
from style import CONST_WINDOW
from data_on_the_main_window import PC


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 600)
        self.pc = PC()
        
    def draw_UI(self):
        self.menu = Menu(self)
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        pc_name = QLabel(text="Имя пк: ")
        pc_name_info = QLabel(text=f"{self.pc.machine_name()}")
        
        cpu = QLabel(text="Процессор: ")
        cpu_info = QLabel(text=f"Модель процессора: {self.pc.cpu_name()}")
        
        memory = QLabel(text="Память: ")
        memory_info = QLabel(text=f"Общее количество оперативной памяти: {self.pc.memory_total()} Gb")
        
        gpu = QLabel(text="Графический процессор: ")
        gpu_info = QLabel(text=f"Модель графического процессора: {self.pc.gpu_name()}")
        
        disk = QLabel(text="Диск(Диски): ")
        disk_data = self.pc.memory_disk()
        disk_list = []
        
        for i in range(len(disk_data)):
            disk_list.append(QLabel())
            
        for i in range(0, len(disk_list)):
            temp = disk_list[i]
            temp.setText(f"Количество памяти на диске {i + 1}: {str(disk_data[i])} Gb")
        
        control_UI.addWidget(pc_name)
        control_UI.addWidget(pc_name_info)
        
        control_UI.addWidget(cpu)
        control_UI.addWidget(cpu_info)
        
        control_UI.addWidget(memory)
        control_UI.addWidget(memory_info)
        
        control_UI.addWidget(gpu)
        control_UI.addWidget(gpu_info)
        
        control_UI.addWidget(disk)
        
        for i in range(0, len(disk_list)):
            control_UI.addWidget(disk_list[i])
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        
    def start(self):
        self.setStyleSheet(CONST_WINDOW)
        icon = "icon.png"
        app_ico = QIcon(icon)
        self.setWindowIcon(app_ico)
        self.setWindowTitle("Система мониторинга")
        
        self.show()