# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список
# заметок, редактировать заметку, удалять заметку.
import datetime

def input_new_name():
    return input('Введите имя новой заметки: ')

def input_body_note():
    return input('Введите тело заметки: ')

def create_note():
    name = input_new_name()
    body = input_body_note()
    date_time = datetime.datetime.now()
    return f'{name}\n{body}\n{date_time}\n\n'

def add_note():
    note = create_note()
    with open('notes.csv','a', encoding='UTF-8') as file:
        file.write(note)
    print('Заметка сохранена')
    print()    

def show_info():
    print() 
    with open('notes.csv','r', encoding='UTF-8') as file:
        notes_list = file.read().rstrip().split('\n\n')
        note_name_list = []
        for note in notes_list:
            note_name = note.rstrip().split('\n')
            note_name_list.append(note_name[0])
        for note in enumerate(note_name_list,1): 
            print(*note)    
    number_note = int(input('\nПоказать заметку целиком? Если ДА - введите номер заметки. Если НЕТ - введите 0\n'))
    if (number_note == 0): print()
    else: print('\n' + notes_list[number_note-1] + '\n') 
    

def edit_note():
    show_info()
    with open('notes.csv','r', encoding='UTF-8') as file:
        notes_list = file.read().rstrip().split('\n\n')
    number_note = int(input('Введите номер заметки, которую необходимо редактировать: \n'))    
    print(
        'Что будем редактировать?\n'
        '1. Название заметки\n'
        '2. Тело заметки\n'
    )
    var_edit = input('Выберите вариант редактирования: ')                 
    
    while var_edit not in ('1', '2'):
            print('Некорректный ввод данных')
            var_edit = input('Выберите вариант редактирования: ')
            
    note_edit = notes_list[number_note-1].rstrip().split('\n')

    print('\nСейчас заметка выглядит так: \n' + note_edit[int(var_edit)-1])
    new_note = input('\nВведите отредактированную заметку для перезаписи: \n')
    if (var_edit == '1'):
        notes_list[number_note-1] = new_note + '\n' + note_edit[1] + '\n' + str(datetime.datetime.now())
    if (var_edit == '2'):
        notes_list[number_note-1] =  note_edit[0] + '\n' + new_note + '\n' + str(datetime.datetime.now())

    with open('notes.csv','w', encoding='UTF-8') as file:
        file.close()

    with open('notes.csv','a', encoding='UTF-8') as file:
        for note in notes_list:    
            file.write(note + '\n\n')
            
    print('\nИзменения сохранены! \n')

def sort_notes():
    with open('notes.csv','r', encoding='UTF-8') as file:
        notes_list = file.read().rstrip().split('\n\n')
    note_date_list = []
    for note in notes_list:
        note_date = note.rstrip().split('\n')
        note_date_list.append(note_date[2])
    print('\n')    
    note_date_list.sort()
    note_name_list = []
    for note in note_date_list:
        for i in range(len(notes_list)):
            if (note in notes_list[i]):
                note_name = notes_list[i].rstrip().split('\n')
                note_name_list.append(note_name[0])
    for note in enumerate(note_name_list,1): 
        print(*note)
    print('\n\n')
    var = input('Отсортировать заметки в файле? (да/нет) \n')
    if (var == 'да'):
        with open('notes.csv','w', encoding='UTF-8') as file:
            file.close()
        for note in note_date_list:
            for i in range(len(notes_list)):
                if (note in notes_list[i]):
                    with open('notes.csv','a', encoding='UTF-8') as file:
                        file.write(notes_list[i] + '\n\n')
    else: print()                    

def delete_note():
    show_info()
    with open('notes.csv','r', encoding='UTF-8') as file:
        notes_list = file.read().rstrip().split('\n\n')
    number_note = int(input('Введите номер заметки, которую необходимо удалить: \n'))

    with open('notes.csv','w', encoding='UTF-8') as file:
        file.close()

    with open('notes.csv','a', encoding='UTF-8') as file:
        for i in range(number_note-1):
            file.write(notes_list[i] + '\n\n')
        for i in range(number_note, len(notes_list)):
            file.write(notes_list[i] + '\n\n') 
    print('\nЗаметка удалена!\n')        

def interface():
    with open('notes.csv','a', encoding='UTF-8'):
        pass
    command = '-1'
    while command != '6':
        print('Варианты меню: \n'
            '1. Создать заметку\n'
            '2. Вывести список заметок\n'
            '3. Редактировать заметку\n'
            '4. Удалить заметку\n'
            '5. Сортировать заметки по дате создания/изменения\n'
            '6. Выход из программы')
        command = input('Выберите пункт меню: ')
    
        while command not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод данных')
            command = input('Выберите пункт меню: ')

        match command:
            case '1':
                add_note()
            case '2':
                show_info()
            case '3':
                edit_note() 
            case '4':
                delete_note()
            case '5':
                sort_notes()       
            case '6':
                print("\nВсего хорошего!\n")  

interface()