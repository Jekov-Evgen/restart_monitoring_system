CONST_MENU = """
    QMenuBar {
        background-color: #333333 !important; /* Принудительное задание фона */
        border: 1px solid #555555;
        padding: 5px;
    }

    QMenuBar::item {
        padding: 5px 15px;
        background: transparent !important; /* Принудительное задание прозрачного фона */
        color: #ffffff !important; /* Принудительно белый текст */
        min-width: 100%;
        text-align: center;
    }

    QMenuBar::item:selected {
        background-color: #444444 !important; 
        border-radius: 3px;
    }

    QMenuBar::item:pressed {
        background-color: #222222 !important;
    }
"""

CONST_WINDOW = """
    QLabel {
        font-size: 18px;
        color: #f0f0f0;
        padding: 5px;
        border: 1px solid #555555; 
        border-radius: 4px;
        background-color: #444444;
    }
    
    QWidget {
        background-color: #222222;
        padding: 10px;
    }
    
    QMainWindow {
        background-color: #333333;
    }
"""

CONST_WINDOW_SYSTEM_MONITORING = """
    QLabel {
        font-size: 18px;
        color: #f0f0f0;
        padding: 5px;
        border: 1px solid #555555;
        border-radius: 4px;
        background-color: #444444;
    }

    QWidget {
        background-color: #222222;
        padding: 10px;
    }

    QMainWindow {
        background-color: #333333;
    }
"""
