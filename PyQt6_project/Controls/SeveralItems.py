import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QCheckBox,
    QComboBox,
    QListWidget,
    QVBoxLayout,
)
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create and place elements
        self.button = QPushButton("Click me!", self)
        self.button.setGeometry(75, 45, 80, 30)
        self.button.clicked.connect(self.onButtonClick)

        self.rectangle = QLabel(self)
        self.rectangle.setGeometry(10, 140, 200, 150)
        self.rectangle.setStyleSheet("background-color: coral;")

        self.label = QLabel("A label", self)
        self.label.setGeometry(250, 10, 80, 30)

        self.checkBox = QCheckBox("Would you like to play a game?", self)
        self.checkBox.setGeometry(250, 40, 250, 30)
        self.checkBox.stateChanged.connect(self.onCheckBoxStateChanged)

        self.comboBox = QComboBox(self)
        self.comboBox.addItems(["Scala", "Java", "C++"])
        self.comboBox.setGeometry(250, 70, 100, 30)

        # not QListView, QListView requires QActions instead of str
        self.listView = QListWidget(self)
        self.listView.setGeometry(250, 100, 120, 190)
        self.listView.setModelColumn(0)
        self.listView.addItems(["AWT", "Swing", "JavaFX", "ScalaFX"])

        # Set up layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.rectangle)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.checkBox)
        self.layout.addWidget(self.comboBox)
        self.layout.addWidget(self.listView)

        self.setLayout(self.layout)
        self.setWindowTitle("First GUI")
        self.setGeometry(100, 100, 500, 300)

    def onButtonClick(self):
        print("Button clicked")

    def onCheckBoxStateChanged(self, state):
        print("Checkbox state changed to", state == Qt.CheckState.Checked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())
