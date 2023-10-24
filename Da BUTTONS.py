from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QSpinBox, QComboBox
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Da BUTTONS - Python Edition 😎😎😎")
        self.setFixedSize(400, 200)



        self.count = 0
        self.label = QLabel(str(self.count), self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setGeometry(145, 75, 100, 45)


        self.button_plus = QPushButton('Da Button +', self)
        self.button_plus.setGeometry(30, 125, 100, 45)
        self.button_plus.clicked.connect(self.increment)

        self.button_minus = QPushButton('Da Button -', self)
        self.button_minus.setGeometry(270, 125, 100, 45)
        self.button_minus.clicked.connect(self.decrement)

        self.language_button = QPushButton('Change', self)
        self.language_button.setGeometry(220, 30, 50, 25)
        self.language_button.clicked.connect(self.change_language)


        self.box = QComboBox(self)
        self.box.setGeometry(120, 30, 100, 25)
        self.box.addItems(["English", "Français", "Español", "Português", "Russian"])

    def change_language(self):
        if self.box.currentIndex() == 1:
            self.setWindowTitle("Les BOUTONS - Version Python 😎😎😎")
            self.button_plus.setText("Bouton +")
            self.button_minus.setText("Bouton -")
        elif self.box.currentIndex() == 0:
            self.setWindowTitle("Da BUTTONS - Python Edition 😎😎😎")
            self.button_plus.setText("Da Button +")
            self.button_minus.setText("Da Button -")
        elif self.box.currentIndex() == 2:
            self.setWindowTitle("Los BOTONES - Version Python 😎😎😎")
            self.button_plus.setText("Botón +")
            self.button_minus.setText("Botón -")
        elif self.box.currentIndex() == 3:
            self.setWindowTitle("BOTÕES - Versão Python😎😎😎")
            self.button_plus.setText("Botão +")
            self.button_minus.setText("Botão -")
        elif self.box.currentIndex() == 5:
            self.setWindowTitle("КНОПКИ - версия Python 😎😎😎")
            self.button_plus.setText("+ кнопка")
            self.button_minus.setText("- + кнопка")    


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
