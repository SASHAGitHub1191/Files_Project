from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QListWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout, QInputDialog

from PyQt6.QtCore import Qt
from random import randint
from  random import shuffle
app = QApplication([])
window = QWidget()
window.show()
teds_list = QListWidget()
h_line = QHBoxLayout()
v_line = QVBoxLayout()
h_line3 = QHBoxLayout()
h_line2 = QHBoxLayout()
text = QTextEdit()
redacktor_text = QLineEdit()
button_notes1 = QPushButton('Создать заметку')
button_notes2 = QPushButton('Удалить заметку')
button_notes3 = QPushButton('Сохранить заметку')
button_tegs1 = QPushButton('Создать заметку')
button_tegs2 = QPushButton('Удалить заметку')
button_tegs3 = QPushButton('Сохранить заметку')
notes_label = QLabel('Список заметок')
tegs = QLabel('Список тегов')
notes_list = QListWidget()
window.setLayout(h_line)
h_line.addWidget(text)
h_line.addLayout(v_line)
v_line.addWidget(notes_label)
v_line.addWidget(notes_list)
v_line.addLayout(h_line2)
h_line2.addWidget(button_notes1)
h_line2.addWidget(button_notes2)
v_line.addWidget(button_notes3)
v_line.addWidget(tegs)
v_line.addWidget(teds_list)
v_line.addWidget(redacktor_text)
v_line.addLayout(h_line3)
h_line3.addWidget(button_tegs1)
h_line3.addWidget(button_tegs2)
v_line.addWidget(button_tegs3)
redacktor_text.setPlaceholderText('Введите текст...')
notes = {}

def append_note():
    note_name,ok = QInputDialog.getText(window,'добавить заметку','Название заметки:')
    if note_name and ok:
        notes_list.addItem(note_name)
        notes[note_name] = {'Теги': [], 'Текст': ''}
    print(notes)
def save_note():
    if notes_list.selectedItems():
        note_name = notes_list.selectedItems()[0].text()
        note_text = text.toPlainText()#вытаскиываем текст
        notes[note_name]['Текст'] = note_text
def show_note():
    note_name = notes_list.selectedItems()[0].text()
    note_text = notes[note_name]['Текст']
    text.setText(note_text)

button_notes3.clicked.connect(save_note)
notes_list.itemClicked.connect(show_note)
def del_note():
    if notes_list.selectedItems():
        note_name = notes_list.selectedItems()[0].text()
        del notes[note_name]
        notes_list.clear()
        notes_list.addItems(notes)
        print('1234567890')
button_notes2.clicked.connect(del_note)

# TODO: ПОСЛЕ ДОБАВЛЕНИЯ ЗАМЕТКИ ТЕКСТ СТИРАЕТСЯ И ДОБАВЛЯЕТСЯ

button_notes1.clicked.connect(append_note)
app.exec()
# notes = {'Название заметки':{
#     'Теги':['Тег1,Тег2,Тег3...'],
#     'Текст':'САМ текст'
# }
# }
