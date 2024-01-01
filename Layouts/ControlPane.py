from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QSplitter,
    QPlainTextEdit,
    QScrollArea,
    QTextEdit,
    QAccordion,
    QAccordionItem,
    QPushButton,
)


class ControlPanesApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Control Panes")
        self.setGeometry(100, 100, 500, 250)

        self.init_ui()

    def init_ui(self):
        central_widget = QTabWidget(self)
        self.setCentralWidget(central_widget)

        tab_panes = QSplitter(central_widget)

        panes_tab = QSplitter()
        tab_area = QPlainTextEdit()
        panes_tab.addWidget(panes_tab)
        panes_tab.addWidget(tab_area)

        area_tab = QTextEdit()
        area_tab.setPlainText("Text Area")

        central_widget.addTab(panes_tab, "Control Panes")
        central_widget.addTab(area_tab, "Text Area")

        scroll_area = QScrollArea()
        right_area = QTextEdit()

        accordion = QAccordion()
        for i in range(1, 11):
            accordion_item = QAccordionItem()
            accordion_item.setText("Title Pane " + str(i))
            accordion_item.setContent(QPushButton("Button " + str(i)))
            accordion.addItem(accordion_item)

        scroll_area.setWidget(accordion)

        panes_tab.addWidget(scroll_area)
        panes_tab.addWidget(right_area)


def main():
    app = QApplication([])
    window = ControlPanesApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
