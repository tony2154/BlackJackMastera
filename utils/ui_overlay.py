from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextEdit
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

class OverlayWidget(QWidget):
    def __init__(self):
        super().__init__()
   
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        layout = QVBoxLayout()
        layout.setContentsMargins(12,12,12,12)

        self.count_label = QLabel("Conteo: 0")
        self.count_label.setFont(QFont("Arial", 28, QFont.Bold))
        self.count_label.setStyleSheet("color: lime;")
        layout.addWidget(self.count_label)

        self.advice_label = QLabel("Consejo: -")
        self.advice_label.setFont(QFont("Arial", 16))
        self.advice_label.setStyleSheet("color: white;")
        layout.addWidget(self.advice_label)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setFixedHeight(160)
        self.log.setStyleSheet("background: rgba(0,0,0,150); color: white;")
        layout.addWidget(self.log)

        self.setLayout(layout)
        self.resize(380, 240)

    def update(self, count, advice, detected):
        self.count_label.setText(f"Conteo: {count}")
        self.advice_label.setText(advice)
        if detected:
            self.log.append(f"Detectadas: {', '.join(detected)}")
