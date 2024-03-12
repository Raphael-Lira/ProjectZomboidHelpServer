import sys 
import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget 

# 
from qt_core import *

#
from gui.windows.main_window.ui_main_window import UI_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)


        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())