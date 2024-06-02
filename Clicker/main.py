import sys
import pyautogui
import time
import keyboard
from PySide6.QtWidgets import QApplication, QMainWindow
from Clicker import Ui_MainWindow

class Clicker(QMainWindow):
    def __init__(self):
        super(Clicker, self).__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Start.clicked.connect(lambda: self.b_start("Press start"))

    def b_start(self, Main_info: str) -> None:
        if self.ui.Main_info.text() == "Press start":
            self.ui.Main_info.setText("Change speed and press start")
        elif self.ui.Main_info.text() == "Change speed and press start":
            self.ui.Main_info.setText("Press 1 to stop")
            while self.ui.Main_info.text() == "Press 1 to stop":
                pyautogui.click()
                time.sleep(self.ui.Speed_box.value())
                if keyboard.is_pressed("1"):
                    self.ui.Main_info.setText("Press start")
                    break
        else:
            self.ui.Main_info.setText("Press start")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Clicker()
    window.show()

    sys.exit(app.exec())