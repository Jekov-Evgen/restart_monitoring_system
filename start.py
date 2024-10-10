from draw_main_window import MainWindow
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    
    start = MainWindow()
    start.draw_UI()
    start.go_programm()
    
    app.exec()