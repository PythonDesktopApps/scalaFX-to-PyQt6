import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QComboBox,
    QListWidget,
    QVBoxLayout,
)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Label
        self.label = QLabel("For display purposes.", self)
        self.label.setGeometry(20, 20, 200, 20)

        # ChoiceBox
        self.choiceBox = QComboBox(self)
        self.choiceBox.setGeometry(20, 50, 100, 20)
        self.choiceBox.addItems(["Choice 1", "Choice 2", "Choice 3"])
        self.choiceBox.currentIndexChanged.connect(self.onChoiceBoxChange)

        # ComboBox
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(20, 80, 100, 20)
        self.comboBox.addItems(["Combo 1", "Combo 2", "Combo 3"])
        self.comboBox.currentIndexChanged.connect(self.onComboBoxChange)

        # ListView
        self.listView = QListWidget(self)
        self.listView.setGeometry(353, 20, 100, 160)
        self.listView.addItems(["List 1", "List 2", "List 3"])
        self.listView.clicked.connect(self.onListViewClick)

        # Set up layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.choiceBox)
        self.layout.addWidget(self.comboBox)
        self.layout.addWidget(self.listView)

        self.setLayout(self.layout)
        self.setWindowTitle("Selection Controls")
        self.setGeometry(100, 100, 667, 200)

    def onChoiceBoxChange(self, index):
        self.label.setText("Choice selected: " + self.choiceBox.itemText(index))

    def onComboBoxChange(self, index):
        self.label.setText("Combo box selected: " + self.comboBox.itemText(index))

    def onListViewClick(self, index):
        self.label.setText("List view selected: " + self.listView.model().data(index))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())
