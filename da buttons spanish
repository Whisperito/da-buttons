from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(" Los botones - Version Python 😎😎😎")
        self.setFixedSize(400, 200)



        self.count = 0
        self.label = QLabel(str(self.count), self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setGeometry(145, 75, 100, 45)


        self.button_plus = QPushButton('Botón +', self)
        self.button_plus.setGeometry(30, 125, 100, 45)
        self.button_plus.clicked.connect(self.increment)

        self.button_minus = QPushButton('Botón -', self)
        self.button_minus.setGeometry(270, 125, 100, 45)
        self.button_minus.clicked.connect(self.decrement)

    def increment(self):
        self.count += 1
        self.label.setText(str(self.count))

    def decrement(self):
        self.count -= 1
        self.label.setText(str(self.count))

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
