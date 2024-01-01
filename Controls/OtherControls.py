from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QProgressBar,
    QScrollBar,
    QLabel,
    QSlider,
    QToolBar,
    QVBoxLayout,
    QSplitter,
    QWidget,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QAction


class OtherControlsApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Other Controls")
        self.setGeometry(100, 100, 500, 190)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        tool_bar = QToolBar()
        tool_bar.setFixedWidth(500)

        adv_action = QAction("Advance", self)
        dec_action = QAction("Decrement", self)

        tool_bar.addActions([adv_action, dec_action])
        tool_bar.addSeparator()
        tool_bar.addActions([QAction("Tool 1", self), QAction("Tool 2", self)])

        layout.addWidget(QProgressBar(), alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(QScrollBar(), alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(
            QLabel("Scroll bar value"), alignment=Qt.AlignmentFlag.AlignTop
        )
        layout.addWidget(QSplitter(Qt.Orientation.Vertical))
        layout.addWidget(QSlider(Qt.Orientation.Horizontal))
        layout.addWidget(QLabel("Slider value"))

        layout.addWidget(tool_bar)
        # self.setLayout(layout)

        adv_action.triggered.connect(self.advance_progress)
        dec_action.triggered.connect(self.decrement_progress)

    def advance_progress(self):
        progress = self.findChild(QProgressBar)
        if progress:
            progress.setValue(progress.value() + 5)
            progress.setValue(min(100, max(0, progress.value())))

    def decrement_progress(self):
        progress = self.findChild(QProgressBar)
        if progress:
            progress.setValue(progress.value() - 5)
            progress.setValue(min(100, max(0, progress.value())))


def main():
    app = QApplication([])
    window = OtherControlsApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
