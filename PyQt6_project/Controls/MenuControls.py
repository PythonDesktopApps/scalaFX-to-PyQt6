from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QMenuBar,
    QMenu,
    QCheckBox,
    QRadioButton,
    QMenu,
    QMenuBar,
    QMenu,
    QMenu,
    QPushButton,
    QSplitter,
    QFileDialog,
    QWidget,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QActionGroup


class MenuControlsApp(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.main_window = MainWindow()
        self.main_window.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu Controls")
        self.setGeometry(100, 100, 500, 200)

        self.layout = QVBoxLayout()

        self.menu_bar = QMenuBar()
        self.menu_bar.setNativeMenuBar(True)

        file_menu = QMenu("File")
        new_action = QAction("New", self)
        new_action.setShortcut("Ctrl+N")
        open_action = QAction("Open", self)
        open_action.setShortcut("Ctrl+O")
        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+X")

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        self.menu_bar.addMenu(file_menu)

        check_menu = QMenu("Checks")
        check1 = QAction("Check 1", self, checkable=True)
        check2 = QAction("Check 2", self, checkable=True)

        check_menu.addAction(check1)
        check_menu.addAction(check2)

        self.menu_bar.addMenu(check_menu)

        radio_menu = QMenu("Radios")

        # action group is exclusive by default
        radio_group = QActionGroup(radio_menu)
        radio1 = QAction("Radio 1", self, checkable=True)
        radio2 = QAction("Radio 2", self, checkable=True)
        radio3 = QAction("Radio 3", self, checkable=True)

        radio_menu.addAction(radio_group.addAction(radio1))
        radio_menu.addAction(radio_group.addAction(radio2))
        radio_menu.addAction(radio_group.addAction(radio3))
        self.menu_bar.addMenu(radio_menu)

        types_menu = QMenu("Types")
        types_menu.addMenu(check_menu)
        types_menu.addMenu(radio_menu)

        self.menu_bar.addMenu(types_menu)

        menu_button = QPushButton("Menu Button", self)

        split_menu_button = QSplitter(Qt.Orientation.Horizontal)
        split_menu_button.addAction(QAction("Split Button 1", self))
        split_menu_button.addAction(QAction("Split Button 2", self))

        context_menu = QMenu(self)
        context_menu.addAction(QAction("Context 1", self))
        context_menu.addAction(QAction("Context 2", self))

        label = QLabel("Right-click this to get a context menu.")
        label.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.layout.addWidget(self.menu_bar)
        self.layout.addWidget(menu_button)
        self.layout.addWidget(split_menu_button)
        self.layout.addWidget(label)

        self.setLayout(self.layout)

        exit_action.triggered.connect(self.close)
        save_action.triggered.connect(self.show_save_dialog)
        open_action.triggered.connect(self.show_open_dialog)

        label.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        label.customContextMenuRequested.connect(self.show_context_menu)

    def show_save_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "All Files (*);;Text Files (*.txt)", options=options
        )
        if file_name:
            self.centralWidget().findChild(QLabel).setText("Save to: " + file_name)

    def show_open_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "All Files (*);;Text Files (*.txt)", options=options
        )
        if file_name:
            self.centralWidget().findChild(QLabel).setText("Open: " + file_name)

    def show_context_menu(self, event):
        context_menu = self.centralWidget().findChild(QMenu)
        context_menu.exec_(event.globalPos())


if __name__ == "__main__":
    import sys

    app = MenuControlsApp(sys.argv)
    sys.exit(app.exec())
