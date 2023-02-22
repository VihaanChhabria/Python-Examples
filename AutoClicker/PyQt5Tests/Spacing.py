from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication([])

app.setStyle('Fusion')
app.setStyleSheet("QPushButton { margin: 10ex; }")
window = QWidget()
layout = QVBoxLayout()

app.setFixed

layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)

window.show()
app.exec()