from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QSlider,
    QScrollBar,
    QVBoxLayout,
    QSizePolicy,
    QWidget,
)
from PyQt6.QtCore import Qt, QRect


class NumericBindingsApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Numeric Bindings")
        self.setGeometry(100, 100, 600, 250)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Label
        label = QLabel("This stays centered.")
        label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignTop)

        # Sliders
        x_slider = QSlider(Qt.Orientation.Horizontal)
        x_slider.setMinimum(0)
        x_slider.setMaximum(100)
        x_slider.setValue(0)
        layout.addWidget(x_slider, alignment=Qt.AlignmentFlag.AlignTop)

        y_slider = QSlider(Qt.Orientation.Horizontal)
        y_slider.setMinimum(0)
        y_slider.setMaximum(100)
        y_slider.setValue(0)
        layout.addWidget(y_slider, alignment=Qt.AlignmentFlag.AlignTop)

        size_slider = QSlider(Qt.Orientation.Horizontal)
        size_slider.setMinimum(0)
        size_slider.setMaximum(100)
        size_slider.setValue(0)
        layout.addWidget(size_slider, alignment=Qt.AlignmentFlag.AlignTop)

        # ScrollBar
        scroll = QScrollBar(Qt.Orientation.Horizontal)
        scroll.setMinimum(0)
        scroll.setMaximum(100)
        layout.addWidget(scroll, alignment=Qt.AlignmentFlag.AlignTop)

        # Rectangle
        rectangle = QWidget()
        rectangle.setGeometry(QRect(0, 40, 10, 10))
        layout.addWidget(rectangle, alignment=Qt.AlignmentFlag.AlignTop)

        self.setCentralWidget(central_widget)

        label.setGeometry(
            int((self.width() - label.width()) / 2),
            int((self.height() - label.height()) / 2),
            int(label.width()),
            int(label.height()),
        )

        x_slider.valueChanged.connect(
            lambda value: rectangle.setGeometry(
                value * 6,
                y_slider.value() + 40,
                size_slider.value() * 2 + 10,
                size_slider.value() * 2 + 10,
            )
        )
        y_slider.valueChanged.connect(lambda value: scroll.setValue(value))
        size_slider.valueChanged.connect(
            lambda value: rectangle.setGeometry(
                x_slider.value() * 6,
                y_slider.value() + 40,
                value * 2 + 10,
                value * 2 + 10,
            )
        )
        scroll.valueChanged.connect(lambda value: y_slider.setValue(value))


def main():
    app = QApplication([])
    window = NumericBindingsApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
