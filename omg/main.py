from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import random


class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_generate.clicked.connect(self.example)

    def example(self):
        sings = ""
        if self.ui.cb_leter.isChecked():
            sings = "вввв"
        if self.ui.cb_num.isChecked():
            sings += "фівфівфі"

        result = ""

        number = random.randint(5, 10)
        for i in range(number):
            result_text += random.choice(sings)

        self.ui.result.setText(result_text)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()