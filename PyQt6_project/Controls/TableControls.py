import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTableView, QVBoxLayout
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex


class Student:
    def __init__(self, name, test1, test2):
        self.name = name
        self.test1 = test1
        self.test2 = test2


class StudentTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.headers = ["Name", "Test 1", "Test 2", "Average"]

    def rowCount(self, parent=QModelIndex()):
        return len(self.data)

    def columnCount(self, parent=QModelIndex()):
        return len(self.headers)

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if (
            role == Qt.ItemDataRole.DisplayRole
            and orientation == Qt.Orientation.Horizontal
        ):
            return self.headers[section]

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            student = self.data[index.row()]
            if index.column() == 0:
                return student.name
            elif index.column() == 1:
                return str(student.test1)
            elif index.column() == 2:
                return str(student.test2)
            elif index.column() == 3:
                return "{:.2f}".format((student.test1 + student.test2) / 2.0)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        data = [
            Student("Mark Smith", 76, 89),
            Student("Lisa Doe", 97, 96),
            Student("Bob Builder", 20, 54),
        ]

        model = StudentTableModel(data)

        table = QTableView(self)
        table.setModel(model)

        layout = QVBoxLayout(self)
        layout.addWidget(table)

        self.setWindowTitle("Table Control")
        self.setGeometry(100, 100, 500, 300)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())
