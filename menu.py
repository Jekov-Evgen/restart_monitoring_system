from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction
from style import CONST_MENU
from parameter_monitoring import SystemMonitoring

class Menu():
    def __init__(self, window) -> None:
        self.system_monitor_window = None
        
        menu_control = QMenuBar(window)
        window.setMenuBar(menu_control)
        menu_control.setStyleSheet(CONST_MENU)
        
        
        digital_transition = QAction("&Нагрузка системы", window)
        
        digital_transition.triggered.connect(self.system_load)
        
        menu_control.addAction(digital_transition)
        
    def system_load(self):
        if self.system_monitor_window is None:
            self.system_monitor_window = SystemMonitoring()
            self.system_monitor_window.data_installation()
            self.system_monitor_window.draw_system_monitoring()
            
        
        self.system_monitor_window.show()
        