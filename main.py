from PyQt6.QtWidgets import QApplication,QWidget, QTextEdit,QListWidget, QLabel,QVBoxLayout,QPushButton,QHBoxLayout, QRadioButton,QSlider,QDial,QLineEdit,QGroupBox, QHBoxLayout

from PyQt6.QtCore import Qt
from random import randint
from  random import shuffle
app = QApplication([])
window = QWidget()
window.show()
h_line = QHBoxLayout()
v_line = QVBoxLayout()
text = QTextEdit()
qlist = QListWidget()
window.setLayout(h_line)
h_line.addWidget(text)
h_line.addLayout(v_line)
v_line.addWidget(qlist)

app.exec()