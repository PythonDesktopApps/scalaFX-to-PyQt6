from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QSlider,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QGridLayout,
    QStackedLayout,
    QWidget,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor


class LayoutsApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layouts")
        self.setGeometry(100, 100, 750, 600)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QGridLayout(central_widget)

        # Top
        top_pane = self.add_controls_to_pane(QHBoxLayout(), QColor(63, 63, 63))
        layout.addWidget(top_pane, 0, 0)

        # Left
        left_pane = self.add_controls_to_pane(QVBoxLayout(), QColor(191, 191, 191))
        layout.addWidget(left_pane, 1, 0)

        # Bottom
        bottom_pane = self.add_controls_to_pane(QFormLayout(), QColor(127, 127, 127))
        layout.addWidget(bottom_pane, 2, 0)

        # Right
        right_pane = self.add_controls_to_pane(QStackedLayout(), QColor(255, 255, 255))
        layout.addWidget(right_pane, 0, 1, 3, 1)

        # Center (TilePane)
        tile_pane = self.add_controls_to_pane(QHBoxLayout(), QColor(0, 0, 0))
        layout.addWidget(tile_pane, 1, 1, 2, 1)

        self.setCentralWidget(central_widget)

    def add_controls_to_pane(self, pane_layout, fill_color):
        button = QPushButton("Click Me")
        label = QLabel("Plain label")
        field = QLineEdit()
        field.setText("Text Field")
        area = QTextEdit()
        area.setPlainText("Text Area\nMultiple\nLines")
        area.setFixedWidth(100)
        area.setFixedHeight(100)
        combo = QComboBox()
        combo.addItems(["Alpha", "Beta", "Gamma"])
        slider = QSlider(Qt.Orientation.Horizontal)

        pane_layout.addWidget(button)
        pane_layout.addWidget(label)
        pane_layout.addWidget(field)
        pane_layout.addWidget(area)
        pane_layout.addWidget(combo)
        pane_layout.addWidget(slider)

        # Set background color
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, fill_color)
        # pane_layout.setPalette(palette)

        return pane_layout


def main():
    app = QApplication([])
    window = LayoutsApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
