import sys
import json
import os
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QTextEdit, QFrame, QCheckBox, QSpacerItem, QSizePolicy, QHBoxLayout

# Imports script.py
import script

class OutputWindow(QTextEdit):
    def write(self, text):
        self.insertPlainText(text)

class OWOBOT(QWidget):
    def __init__(self):
        super().__init__()

        # Loads previous user input data
        self.default_data = {
            "User Token": "",
            "Botting URL": "",
            "Bot Token": "",
            "DM URL": "",
            "Send owo": "",
            "No break": "",
        }
        
        # Checks if there is data saved from previous user input
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        script_dir = os.path.join(parent_dir, "script")

        json_path = os.path.join(script_dir, "userData.json")

        try: 
            with open(json_path, 'r') as f:
                self.default_data = json.load(f)
        except FileNotFoundError:       
            pass

        self.initUI()

    def initUI(self):
        self.labels = [QLabel(label, self) for label in ["User Token", "Botting URL", "Bot Token", "DM URL"]]
        
        # Pre-fill the line edits based on the default_data dictionary
        self.line_edits = []
        for label in self.labels:
            line_edit = QLineEdit(self)
            if "Token" in label.text():
                line_edit.setText("*******")
            else:
                line_edit.setText(self.default_data.get(label.text(), ""))
            self.line_edits.append(line_edit)

        self.initUI()

    def initUI(self):
        self.labels = [QLabel(label, self) for label in ["User Token", "Botting URL", "Bot Token", "DM URL"]]
        self.line_edits = [QLineEdit(self) for _ in range(4)]
        self.save_button = QPushButton('Save', self)
        self.save_button.clicked.connect(self.save_to_json)
        self.terminal = OutputWindow(self)
        self.run_button = QPushButton('Run', self)
        self.run_button.clicked.connect(self.run_script)
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

        # Add save button
        vbox.addWidget(self.save_button)
        vbox.addWidget(self.run_button)

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
        
    def run_script(self):
        thread = threading.Thread(target=script.run_script)
        thread.start()

    def save_to_json(self):
        data = {}
        for label, line_edit in zip(self.labels, self.line_edits):
            data[label.text()] = line_edit.text()

        data["Send owo"] = "yes" if self.checkbox1.isChecked() else "no"
        data["No break"] = "yes" if self.checkbox2.isChecked() else "no"

        if not os.path.exists('script'):
            os.makedirs('script')

        with open('script/userData.json', 'w') as f:
            json.dump(data, f)

        print("Data saved!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OWOBOT()
    sys.stdout = ex.terminal

    print("Welcome to OWO BOT by Spaa!")
    print("Please refer to ReadMe.md files for further documentation and use case")

    # Checks if there is data saved from previous user input
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    script_dir = os.path.join(parent_dir, "script")

    json_path = os.path.join(script_dir, "userData.json")

    try: 
        with open(json_path, 'r') as f:
            default_data = json.load(f)
    except FileNotFoundError:       
        default_data = {
            "User Token": "",
            "Botting URL": "",
            "Bot Token": "",
            "DM URL": "",
            "Send owo": "",
            "No break": "",
        }

    if all(default_data.values()):
        print("Previous data input loaded")
    else:
        print("No previous data loaded, please fill the boxes with")
        print("correct values, click save and try again")

    sys.exit(app.exec_())

