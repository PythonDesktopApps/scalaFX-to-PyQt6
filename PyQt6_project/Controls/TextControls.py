import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QTextEdit,
    QVBoxLayout,
)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Label
        self.label = QLabel("Generally non-interactive text.", self)
        self.label.setGeometry(20, 20, 250, 20)

        # TextField
        self.textField = QLineEdit(self)
        self.textField.setGeometry(20, 50, 250, 20)
        self.textField.setPlaceholderText("Single-line field")
        self.textField.returnPressed.connect(self.onTextFieldEnter)
        self.textField.editingFinished.connect(self.onTextFieldFocusChange)

        # TextArea
        self.textArea = QTextEdit(self)
        self.textArea.setGeometry(20, 80, 460, 120)
        self.textArea.setPlaceholderText("Multi-line field")
        self.textArea.textChanged.connect(self.onTextAreaTextChange)
        self.textArea.focusOutEvent = self.onTextAreaFocusChange

        # Password Field
        self.passwordField = QLineEdit(self)
        self.passwordField.setGeometry(20, 205, 250, 20)
        self.passwordField.setPlaceholderText("Password field")
        self.passwordField.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordField.returnPressed.connect(self.onPasswordFieldEnter)
        self.passwordField.editingFinished.connect(self.onPasswordFieldFocusChange)

        # Set up layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textField)
        self.layout.addWidget(self.textArea)
        self.layout.addWidget(self.passwordField)

        self.setLayout(self.layout)
        self.setWindowTitle("Text Controls")
        self.setGeometry(100, 100, 500, 300)

    def onTextFieldEnter(self):
        self.label.setText("Field action : " + self.textField.text())

    def onTextFieldFocusChange(self):
        if not self.textField.hasFocus():
            self.label.setText("Field focus : " + self.textField.text())

    def onTextAreaTextChange(self):
        self.label.setText("Area focus : " + self.textArea.toPlainText())

    def onTextAreaFocusChange(self, event):
        if not self.textArea.hasFocus():
            self.label.setText("Area focus : " + self.textArea.toPlainText())

    def onPasswordFieldEnter(self):
        self.label.setText("Password action : " + self.passwordField.text())

    def onPasswordFieldFocusChange(self):
        if not self.passwordField.hasFocus():
            self.label.setText("Password focus : " + self.passwordField.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())
