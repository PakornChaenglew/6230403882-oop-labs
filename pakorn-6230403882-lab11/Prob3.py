import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        label_name = QLabel("Name")
        self.edit_name = QLineEdit(self)

        fbox = QFormLayout(self)
        fbox.addRow(label_name, self.edit_name)
        vbox = QVBoxLayout(self)

        library = QLabel("Library")

        layout = QHBoxLayout()
        PyQt = QCheckBox('PyQt', self)
        layout.addWidget(PyQt)
        PyQt.stateChanged.connect(lambda :self.chk(PyQt))
        PyQt.setChecked(True)
        PyGame = QCheckBox('PyGame', self)
        layout.addWidget(PyGame)
        PyGame.stateChanged.connect(lambda: self.chk(PyGame))
        PyTorch = QCheckBox('PyTorch', self)
        layout.addWidget(PyTorch)
        PyTorch.stateChanged.connect(lambda: self.chk(PyTorch))
        fbox.addRow(library, layout)


        hbox = QHBoxLayout(self)
        hbox.addStretch(1)
        submit = QPushButton("Submit")
        submit.clicked.connect(self.namef)
        hbox.addWidget(submit)

        cancel = QPushButton("Cancel")
        hbox.addWidget(cancel)
        fbox.addRow(hbox)

        self.sizeHint()
        self.setWindowTitle('Problem3')

        self.show()

    def chk(self, ck):
        if ck.isChecked() == True:
            print(ck.text() + "is selected")
        else:
            print(ck.text() + "is deselected")

    def namef(self):
        a = self.edit_name.text()
        if a == '':
            pass
        else:
            print("Name is", a)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()