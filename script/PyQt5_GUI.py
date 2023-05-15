import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QTextEdit, QFrame, QCheckBox, QSpacerItem, QSizePolicy, QHBoxLayout
import json
import os

class OutputWindow(QTextEdit):
    def write(self, text):
        self.insertPlainText(text)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.labels = [QLabel(label, self) for label in ["User Token", "Botting URL", "Bot Token", "DM URL"]]
        self.line_edits = [QLineEdit(self) for _ in range(4)]
        self.save_button = QPushButton('Save', self)
        self.save_button.clicked.connect(self.save_to_json)
        self.terminal = OutputWindow(self)
        self.checkbox1 = QCheckBox("Send owo", self)
        self.checkbox2 = QCheckBox("No break", self)

        vbox = QVBoxLayout()
        for label, line_edit in zip(self.labels, self.line_edits):
            vbox.addWidget(label)
            vbox.addWidget(line_edit)

        # Add checkbox in QHBoxLayout with expanding space
        hbox = QHBoxLayout()
        hbox.addWidget(self.checkbox1)
        hbox.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        vbox.addLayout(hbox)
        hbox.addWidget(self.checkbox2)
        hbox.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        vbox.addLayout(hbox)


        vbox.addWidget(self.save_button)

        # Add a separator between the inputs and the output
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        vbox.addWidget(separator)

        vbox.addWidget(QLabel('Output:'))
        vbox.addWidget(self.terminal)

        self.setLayout(vbox)

        self.setWindowTitle('OWO BOT by Spaa')
        self.setGeometry(500, 500, 500, 600)
        self.show()

    def save_to_json(self):
        data = {}
        for label, line_edit in zip(self.labels, self.line_edits):
            data[label.text()] = line_edit.text()

        data["send_owo"] = "yes" if self.checkbox1.isChecked() else "no"
        data["no break"] = "yes" if self.checkbox2.isChecked() else "no"

        if not os.path.exists('script'):
            os.makedirs('script')

        with open('script/userData.json', 'w') as f:
            json.dump(data, f)

        print("Data saved!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()

    sys.stdout = ex.terminal
    print("Welcome to OWO BOT by Spaa!")
    print("Please refer to ReadMe.md files for further documentation and use case")

    sys.exit(app.exec_())
