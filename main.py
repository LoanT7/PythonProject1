#showing the main app window
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from gui import Ui_MainWindow
from logic import VotLogic


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.logic = VotLogic(self.ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())



