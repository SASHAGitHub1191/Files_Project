from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QListWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout, QInputDialog
import json
from PyQt6.QtCore import Qt
from random import randint
from  random import shuffle


def append_note():

    note_name, ok = QInputDialog.getText(window, 'добавить заметку', 'Название заметки:')
    if note_name and ok:
        notes[note_name] = {'Теги': [], 'Текст': ''}
        save_file()
        update_notes(notes)

def save_note():
    if notes_list.selectedItems():
        note_name = notes_list.selectedItems()[0].text()
        note_text = text.toPlainText()  # вытаскиываем текст
        notes[note_name]['Текст'] = note_text
        save_file()
        update_notes(notes)


def show_note_info():
    note_name = notes_list.selectedItems()[0].text()
    note_text = notes[note_name]['Текст']
    text.setText(note_text)
    tegs_list.clear()
    tegs_list.addItems(notes[note_name]['Теги'])

def del_note():
    if notes_list.selectedItems():
        note_name = notes_list.selectedItems()[0].text()
        del notes[note_name]
        save_file()
        update_notes(notes)

def load_info():
    try:
        with open('note.json','r', encoding='UTF-8') as file:
            return json.load(file)

    except FileNotFoundError :
        return {}


def save_file():
    with open('note.json','w', encoding='UTF-8') as file:

        json.dump(notes, file)



def update_notes(notes):
    text.clear()
    notes_list.clear()
    notes_list.addItems(notes)
    tegs_list.clear()
    tags = set()
    for name_note in notes:
        name_tags = notes[name_note]['Теги']
        for tag in name_tags:
            tags.add(tag)


    tegs_list.addItems(tags)

def append_tag():

    if notes_list.selectedItems():
        teg_name, ok = QInputDialog.getText(window, 'добавить тег', 'Название тега:')
        if teg_name and ok:
            note_name = notes_list.selectedItems()[0].text()
            notes[note_name]['Теги'].append(teg_name)
            update_notes(notes)
        save_file()


def del_tag():

    if notes_list.selectedItems() and tegs_list.selectedItems():
        note_name = notes_list.selectedItems()[0].text()
        tag_name = tegs_list.selectedItems()[0].text()

        notes[note_name]['Теги'].remove(tag_name)

        update_notes(notes)
        save_file()
def filter_notes():
    name_tag = redacktor_text.text()
    filtered_notes = {}
    if name_tag:

        for note in notes:
            for tag in notes[note]['Теги']:
                if name_tag in tag:
                    filtered_notes[note] = notes[note]
        update_notes(filtered_notes)

    else:
        update_notes(notes)

app = QApplication([])
window = QWidget()
window.show()
tegs_list = QListWidget()
h_line = QHBoxLayout()
v_line = QVBoxLayout()
h_line3 = QHBoxLayout()
h_line2 = QHBoxLayout()
text = QTextEdit()
redacktor_text = QLineEdit()
button_notes1 = QPushButton('Создать заметку')
button_notes2 = QPushButton('Удалить заметку')
button_notes3 = QPushButton('Сохранить заметку')
button_tegs1 = QPushButton('Прикрепить тег')
button_tegs2 = QPushButton('Удалить тег')

notes_label = QLabel('Список заметок')
label_tags = QLabel('Список тегов')  #Просто надпись
notes_list = QListWidget()  # под 'Список звметок'(отображение заметок)

window.setLayout(h_line)
h_line.addWidget(text)
h_line.addLayout(v_line)
v_line.addWidget(notes_label)
v_line.addWidget(notes_list)
v_line.addLayout(h_line2)
h_line2.addWidget(button_notes1)
h_line2.addWidget(button_notes2)
v_line.addWidget(button_notes3)
v_line.addWidget(label_tags)
v_line.addWidget(tegs_list)
v_line.addWidget(redacktor_text)
v_line.addLayout(h_line3)
h_line3.addWidget(button_tegs1)
h_line3.addWidget(button_tegs2)

redacktor_text.setPlaceholderText('Введите текст...')


button_notes3.clicked.connect(save_note)
notes_list.itemClicked.connect(show_note_info)
button_notes2.clicked.connect(del_note)
button_notes1.clicked.connect(append_note)
button_tegs1.clicked.connect(append_tag)
button_tegs2.clicked.connect(del_tag)
redacktor_text.textChanged.connect(filter_notes)
# TODO: g
notes = load_info()
update_notes(notes)

app.exec()
# notes = {'Название заметки':{
#     'Теги':['Тег1,Тег2,Тег3...'],
#     'Текст':'САМ текст'
# }
# }
