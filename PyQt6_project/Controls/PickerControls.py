import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QDateEdit,
    QVBoxLayout,
    QColorDialog,
    QPushButton,
)

from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import QDate


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Label
        self.label = QLabel("Shows date once selected.", self)
        self.label.setGeometry(20, 20, 200, 20)

        # ColorPicker
        self.colorPicker = QPushButton("Select color", self)
        self.colorPicker.clicked.connect(self.getColor)

        # DatePicker
        self.datePicker = QDateEdit(self, calendarPopup=True)
        self.datePicker.setDate(QDate.currentDate())
        self.datePicker.dateChanged.connect(self.onDatePickerChange)

        # Set up layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.colorPicker)
        self.layout.addWidget(self.datePicker)

        self.setLayout(self.layout)
        self.setWindowTitle("Picker Controls")
        self.setGeometry(100, 100, 250, 130)

    # First, we need to separate out Palette and Style. Style will overwrite the Palette color and settings.
    # Palette is done using QPalette object. Style can be applied to the main window or
    # individual widgets using a string that is similar to CSS.
    def getColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.label.setStyleSheet(f"background-color: {color.name()}")

    def onDatePickerChange(self, date):
        self.label.setText("Date is: " + date.toString("yyyy-MM-dd"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())
