import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QTreeView,
    QVBoxLayout,
)

from PyQt6.QtGui import QFileSystemModel


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.model = QFileSystemModel()
        self.model.setRootPath("")

        self.tree = QTreeView(self)
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(""))

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tree)

        self.setLayout(self.layout)
        self.setWindowTitle("Tree Control")
        self.setGeometry(100, 100, 500, 300)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())
