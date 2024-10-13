from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction
from style import CONST_MENU
from parameter_monitoring import SystemMonitoring
from CPU_expansion_window import ProcessorAdvansed
from GPU_expansion_window import GPUAdvansed
from running_processes import RunProcess
from graph_window import GrapgIndicators

class Menu():
    def __init__(self, window) -> None:
        self.system_monitor_window = None
        self.advanced_processor = None
        self.advanced_GPU = None
        self.process = None
        self.graph = None
        
        menu_control = QMenuBar(window)
        window.setMenuBar(menu_control)
        menu_control.setStyleSheet(CONST_MENU)
        
        
        digital_transition = QAction("&Нагрузка системы", window)
        processor_data = QAction("&Расширенные данные процессора", window)
        GPU_data = QAction("&Расширенные данные видеокарты", window)
        run_process_data = QAction("&Запущенные процессы", window)
        graph = QAction("&Графики для процессоров", window)
        
        digital_transition.triggered.connect(self.system_load)
        processor_data.triggered.connect(self.processor)
        GPU_data.triggered.connect(self.GPU)
        run_process_data.triggered.connect(self.run_process)
        graph.triggered.connect(self.graph_indicators)
        
        menu_control.addAction(digital_transition)
        menu_control.addAction(processor_data)
        menu_control.addAction(GPU_data)
        menu_control.addAction(run_process_data)
        menu_control.addAction(graph)
        
    def system_load(self):
        if self.system_monitor_window is None:
            self.system_monitor_window = SystemMonitoring()
            self.system_monitor_window.draw_system_monitoring()
            self.system_monitor_window.data_installation()
        
        self.system_monitor_window.show()
        
    def processor(self):
        if self.advanced_processor is None:
            self.advanced_processor = ProcessorAdvansed()
            self.advanced_processor.data_inst()
            self.advanced_processor.draw_processor_advansed()
            
        self.advanced_processor.show()
        
    def GPU(self):
        if self.advanced_GPU is None:
            self.advanced_GPU = GPUAdvansed()
            self.advanced_GPU.data_inst()
            self.advanced_GPU.draw_GPU_advansed()
        
        self.advanced_GPU.show()
        
    def run_process(self):
        if self.process is None:
            self.process = RunProcess()
            self.process.data_inst()
            self.process.draw_window()
        
        self.process.show()
        
    def graph_indicators(self):
        if self.graph is None:
            self.graph = GrapgIndicators()
            self.graph.data_inst()
            self.graph.draw_window()
        
        self.graph.show()
        