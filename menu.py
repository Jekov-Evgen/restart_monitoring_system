from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction
from style import CONST_MENU
from parameter_monitoring import SystemMonitoring
from CPU_expansion_window import ProcessorAdvansed
from GPU_expansion_window import GPUAdvansed
from running_processes import RunProcess

class Menu():
    def __init__(self, window):
        self.system_monitor_window = None
        self.extended_CPU_window = None
        self.extended_GPU_window = None
        self.running_applications_window = None
        
        menu_control = QMenuBar(window)
        window.setMenuBar(menu_control)
        menu_control.setStyleSheet(CONST_MENU)
        
        
        total_system_load = QAction("&Нагрузка системы", window)
        CPU_data = QAction("&Расширенные данные процессора", window)
        GPU_data = QAction("&Расширенные данные видеокарты", window)
        running_processors = QAction("&Запущенные процессы", window)
        
        total_system_load.triggered.connect(self.system_load)
        CPU_data.triggered.connect(self.CPU)
        GPU_data.triggered.connect(self.GPU)
        running_processors.triggered.connect(self.run_process)
        
        menu_control.addAction(total_system_load)
        menu_control.addAction(CPU_data)
        menu_control.addAction(GPU_data)
        menu_control.addAction(running_processors)
        
    def system_load(self):
        if self.system_monitor_window is None:
            self.system_monitor_window = SystemMonitoring()
            self.system_monitor_window.draw_system_monitoring()
            self.system_monitor_window.data_installation()
        
        self.system_monitor_window.show()
        
    def CPU(self):
        if self.extended_CPU_window is None:
            self.extended_CPU_window = ProcessorAdvansed()
            self.extended_CPU_window.data_installation()
            self.extended_CPU_window.draw_processor_advansed()
            
        self.extended_CPU_window.show()
        
    def GPU(self):
        if self.extended_GPU_window is None:
            self.extended_GPU_window = GPUAdvansed()
            self.extended_GPU_window.draw_GPU_advansed()
            self.extended_GPU_window.data_installation()
        
        self.extended_GPU_window.show()
        
    def run_process(self):
        if self.running_applications_window is None:
            self.running_applications_window = RunProcess()
            self.running_applications_window.data_installation()
            self.running_applications_window.draw_window()
        
        self.running_applications_window.show()
        