CONST_MENU = """
    QMenuBar {
        background-color: #333333; /* Темный серый фон */
        border: 1px solid #555555; /* Тонкая рамка */
        padding: 5px;
    }

    QMenuBar::item {
        padding: 5px 15px;
        background: transparent;
        color: #dddddd; /* Светло-серый цвет текста */
        min-width: 100%;
        text-align: center;
    }

    QMenuBar::item:selected {
        background-color: #444444; /* Темный оттенок при наведении */
        border-radius: 3px; /* Округлённые углы при наведении */
    }

    QMenuBar::item:pressed {
        background-color: #222222; /* Ещё более темный оттенок при нажатии */
    }
"""

CONST_WINDOW = """
    QLabel {
        font-size: 18px;
        color: #f0f0f0; /* Светлый цвет текста на тёмном фоне */
        padding: 5px;
        border: 1px solid #555555; /* Тонкая рамка вокруг текста */
        border-radius: 4px; /* Легкое округление углов */
        background-color: #444444; /* Тёмный фон для меток */
    }
    
    QWidget {
        background-color: #222222; /* Тёмный фон для виджетов */
        padding: 10px;
    }
    
    QMainWindow {
        background-color: #333333; /* Темный фон для основного окна */
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
