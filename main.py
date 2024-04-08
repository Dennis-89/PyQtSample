#!/usr/bin/env python3
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QWidget)


class MainWindow(QWidget):
    COMPRESSORS = [
        "TRZ 400",
        "TZW 70",
        "TVD 900",
    ]

    USER_REQUESTS = [
        ("Saugdruck", "bar"),
        ("Enddruck", "bar"),
        ("Gas", "-"),
    ]

    def __init__(self, parent=None):
        super().__init__(parent, windowTitle="Beispiel")

        main_layout = QVBoxLayout()
        layout = QGridLayout()
        for row, (request, unit) in enumerate(self.USER_REQUESTS):
            layout.addWidget(QLabel(request), row, 0, Qt.AlignRight)
            layout.addWidget(QLineEdit(), row, 1)
            layout.addWidget(QLabel(unit), row, 2, Qt.AlignRight)

        group_box = QGroupBox("Kundendaten eintragen")
        group_box.setLayout(layout)
        main_layout.addWidget(group_box)

        groupbox = QGroupBox()
        layout = QVBoxLayout()

        column_layout = QVBoxLayout()
        column_layout.addWidget(QLabel("Kompressor auswählen:"))
        self.combo_box = QComboBox()
        self.combo_box.addItems(self.COMPRESSORS)
        column_layout.addWidget(self.combo_box)

        row_layout = QHBoxLayout()
        result_description = QLabel("Bester Kompressor:")
        self.result_label = QLabel()
        row_layout.addWidget(result_description)
        row_layout.addWidget(self.result_label)
        layout.addLayout(column_layout)
        layout.addLayout(row_layout)

        groupbox.setLayout(layout)
        main_layout.addWidget(groupbox)

        layout = QHBoxLayout()

        quit_button = QPushButton("Schließen")
        layout.addWidget(quit_button)

        calculate_button = QPushButton("Berechnen")
        layout.addWidget(calculate_button)

        main_layout.addLayout(layout)

        self.setLayout(main_layout)

        quit_button.clicked.connect(self.close)
        calculate_button.clicked.connect(self.process_user_input)

    def process_user_input(self):
        self.result_label.setText(self.combo_box.currentText())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
