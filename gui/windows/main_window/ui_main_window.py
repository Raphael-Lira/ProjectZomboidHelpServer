from qt_core import *

class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")


        parent.resize(1200,720)
        parent.setMinimumSize(960, 540)


        self.central_frame = QFrame()
        self.main_layout = QHBoxLayout(self.central_frame)
        #left menu
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        #
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")
        # add wigets
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        parent.setCentralWidget(self.central_frame)