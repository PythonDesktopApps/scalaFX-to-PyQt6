from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QSlider,
    QVBoxLayout,
    QSizePolicy,
    QWidget,
)
from PyQt6.QtCore import Qt, QRect, pyqtSlot, pyqtProperty
from PyQt6.QtGui import QColor


class ConditionalBindingsApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Conditional Bindings")
        self.setGeometry(100, 100, 500, 250)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Label
        self.label = QLabel("Hover to change background.")
        self.label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignTop)

        # Slider
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(0)
        layout.addWidget(slider, alignment=Qt.AlignmentFlag.AlignTop)

        # Connections
        slider.valueChanged.connect(self.on_slider_value_changed)
        self.label.setMouseTracking(True)
        self.label.enterEvent = self.on_label_enter
        self.label.leaveEvent = self.on_label_leave

        self.setCentralWidget(central_widget)

    @pyqtSlot(int)
    def on_slider_value_changed(self, value):
        x = 0 if value < 50 else self.width() - self.label.width()
        self.label.setGeometry(
            int(x),
            int((self.height() - self.label.height()) / 2),
            int(self.label.width()),
            int(self.label.height()),
        )

    def on_label_enter(self, event):
        self.label.setStyleSheet("background-color: red;")

    def on_label_leave(self, event):
        self.label.setStyleSheet("background-color: white;")


def main():
    app = QApplication([])
    window = ConditionalBindingsApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
