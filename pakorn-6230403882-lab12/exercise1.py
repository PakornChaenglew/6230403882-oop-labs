import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_value = 50
        self.init_value2 = 50
        self.slider = QSlider(Qt.Horizontal, self)
        self.label = QLabel(self)
        self.slider2 = QSlider(Qt.Horizontal, self)
        self.label2 = QLabel(self)
        self.oper = -1
        self.initUI()

    def initUI(self):

        fbox = QFormLayout(self)

        self.sliders(self.slider, self.label)
        self.sliders(self.slider2, self.label2)
        fbox.addRow(self.label, self.slider)
        fbox.addRow(self.label2, self.slider2)

        self.choose()

        fbox.addRow(self.hbox)

        self.edit = QLineEdit()
        self.edit.setStyleSheet("background-color: gray ; color: yellow")
        self.edit.setFont(QFont("Arial", 10))
        self.edit.setAlignment(Qt.AlignRight)

        result = QLabel("Result")
        rbox = QHBoxLayout(self)
        rbox.addWidget(self.edit)

        fbox.addRow(result, rbox)

        self.adjustSize()
        self.setWindowTitle('Simple Calculator')
        self.show()

    def choose(self):
        hbox = QHBoxLayout(self)
        self.hbox = hbox

        add = QPushButton("Add")
        add.clicked.connect(self.click)
        hbox.addWidget(add)
        self.add = add

        subtract = QPushButton("Subtract")
        subtract.clicked.connect(self.click)
        hbox.addWidget(subtract)
        self.subtract = subtract

        multiply = QPushButton("Multiply")
        multiply.clicked.connect(self.click)
        hbox.addWidget(multiply)
        self.multiply = multiply

        divide = QPushButton("Divide")
        divide.clicked.connect(self.click)
        hbox.addWidget(divide)
        self.divide = divide

    def sliders(self, slider, label):
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)
        slider.setTickPosition(self.slider.TicksBelow)
        slider.setTickInterval(5)
        slider.valueChanged[int].connect(self.change_value)

        label.setText(str(self.init_value))
        label.setFont(QFont("Arial", 20))
        label.setStyleSheet("color: blue")


    def change_value(self, value):
        updated_value = value
        sender = self.sender()
        if sender == self.slider:
            self.label.setText(str(updated_value))
            self.updated_value = updated_value
            self.init_value = updated_value
        elif sender == self.slider2:
            self.label2.setText(str(updated_value))
            self.updated_value2 = self.init_value2
            self.init_value2 = updated_value
        self.cal()


    def click(self):
        sender = self.sender()
        if sender.text() == "Add":
            x = "lightgreen"
            y, z, a  = "white", "white", "white"
            self.oper = 0
        elif sender.text() == "Subtract":
            y = "lightgreen"
            x, z, a = "white", "white", "white"
            self.oper = 1
        elif sender.text() == "Multiply":
            z = "lightgreen"
            x, y, a = "white", "white", "white"
            self.oper = 2
        elif sender.text() == "Divide":
            a = "lightgreen"
            x, y, z = "white", "white", "white"
            self.oper = 3
        self.add.setStyleSheet(f"background-color: {x} ")
        self.subtract.setStyleSheet(f"background-color: {y}")
        self.multiply.setStyleSheet(f"background-color: {z}")
        self.divide.setStyleSheet(f"background-color: {a}")
        self.cal()

    def cal(self):
        value = self.init_value
        value2 = self.init_value2
        if self.oper == 0:
            ans = value + value2
            self.edit.setText(str(ans))
        elif self.oper == 1:
            ans = value - value2
            self.edit.setText(str(ans))
        elif self.oper == 2:
            ans = value * value2
            self.edit.setText(str(ans))
        elif self.oper == 3:
            if value2 == 0:
                self.edit.setText("Can not divided by zero")
            else:
                ans = value / value2
                self.edit.setText(str(ans))
        else:
            pass

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()