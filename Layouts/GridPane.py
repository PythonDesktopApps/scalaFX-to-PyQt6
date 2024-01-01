from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QGridLayout,
    QSizePolicy,
    QWidget,
)


class GridPaneApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GridPane")
        self.setGeometry(100, 100, 300, 300)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QGridLayout(central_widget)

        buttons = [QPushButton(str(i)) for i in range(1, 10)]
        for i, button in enumerate(buttons):
            layout.addWidget(button, i // 3 + 1, i % 3)
            button.setSizePolicy(
                QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
            )

        text_field = QLineEdit()
        layout.addWidget(text_field, 0, 0, 1, 4)

        zero_button = QPushButton("0")
        layout.addWidget(zero_button, 4, 0, 1, 2)
        zero_button.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )

        period_button = QPushButton(".")
        layout.addWidget(period_button, 4, 2, 1, 1)
        period_button.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )

        operators = ["+", "-", "*", "/"]
        for i, op in enumerate(operators):
            button = QPushButton(op)
            layout.addWidget(button, i + 1, 3)
            button.setSizePolicy(
                QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
            )

        self.setCentralWidget(central_widget)


def main():
    app = QApplication([])
    window = GridPaneApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
