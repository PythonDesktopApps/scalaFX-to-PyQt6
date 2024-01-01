import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QCheckBox,
    QRadioButton,
    QButtonGroup,
    # QToggleButton, - create a class for this out of checkbox
    QVBoxLayout,
)


class QToggleButton(QPushButton):
    def __init__(self, label, parent=None):
        super().__init__(label, parent)
        self.setCheckable(True)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Label
        self.label = QLabel("Just used for feedback.", self)
        self.label.setGeometry(20, 20, 200, 20)

        # Button
        self.button = QPushButton("Button", self)
        self.button.setGeometry(20, 50, 80, 30)
        self.button.clicked.connect(self.onButtonClick)

        # CheckBoxes
        self.cb1 = QCheckBox("Check Box 1", self)
        self.cb1.setGeometry(20, 80, 120, 20)
        self.cb1.clicked.connect(self.onCheckBox1Click)

        self.cb2 = QCheckBox("Check Box 2", self)
        self.cb2.setGeometry(20, 110, 120, 20)
        self.cb2.clicked.connect(self.onCheckBox2Click)

        # RadioButtons
        self.rb1 = QRadioButton("Radio Button 1", self)
        self.rb1.setGeometry(20, 140, 120, 20)

        self.rb2 = QRadioButton("Radio Button 2", self)
        self.rb2.setGeometry(20, 170, 120, 20)

        self.rb3 = QRadioButton("Radio Button 3", self)
        self.rb3.setGeometry(20, 200, 120, 20)

        self.group1 = QButtonGroup(self)
        self.group1.addButton(self.rb1)
        self.group1.addButton(self.rb2)
        self.group1.addButton(self.rb3)
        self.group1.buttonClicked.connect(self.onRadioButtonClick)

        # Toggle Buttons
        self.tb1 = QToggleButton("Toggle Button 1", self)
        self.tb1.setGeometry(20, 230, 120, 20)
        self.tb1.clicked.connect(self.onToggleButton1Click)

        self.tb2 = QToggleButton("Toggle Button 2", self)
        self.tb2.setGeometry(20, 260, 120, 20)
        self.tb2.clicked.connect(self.onToggleButton2Click)

        self.tb3 = QToggleButton("Toggle Button 3", self)
        self.tb3.setGeometry(20, 290, 120, 20)
        self.tb3.clicked.connect(self.onToggleButton3Click)

        self.group2 = QButtonGroup(self)
        self.group2.addButton(self.tb1)
        self.group2.addButton(self.tb2)
        self.group2.addButton(self.tb3)
        self.group2.buttonClicked.connect(self.onToggleButtonClick)

        # Set up layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.cb1)
        self.layout.addWidget(self.cb2)
        self.layout.addWidget(self.rb1)
        self.layout.addWidget(self.rb2)
        self.layout.addWidget(self.rb3)
        self.layout.addWidget(self.tb1)
        self.layout.addWidget(self.tb2)
        self.layout.addWidget(self.tb3)

        self.setLayout(self.layout)
        self.setWindowTitle("Button Controls")
        self.setGeometry(100, 100, 300, 340)

    def onButtonClick(self):
        self.label.setText("Button clicked")

    def onCheckBox1Click(self):
        self.label.setText("Check Box 1 is " + str(self.cb1.isChecked()))

    def onCheckBox2Click(self):
        self.label.setText("Check Box 2 is " + str(self.cb2.isChecked()))

    def onRadioButtonClick(self, button):
        self.label.setText(
            "Radio Button {} is {}".format(button.text(), str(button.isChecked()))
        )

    def onToggleButton1Click(self):
        self.label.setText("Toggle Button 1 is " + str(self.tb1.isChecked()))

    def onToggleButton2Click(self):
        self.label.setText("Toggle Button 2 is " + str(self.tb2.isChecked()))

    def onToggleButton3Click(self):
        self.label.setText("Toggle Button 3 is " + str(self.tb3.isChecked()))

    def onToggleButtonClick(self, button):
        self.label.setText(
            "Toggle Button {} is {}".format(button.text(), str(button.isChecked()))
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())
