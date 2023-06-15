import file
import app
import note

comd = '\n\t\t- - - - - Заметки - - - - -'
comd_0 = ("\tГлавное меню:\n"
          "\tСоздание заметки - - - - нажмите '1'\n"
          "\tСписок заметок - - - - - нажмите '2'\n"
          "\tПоиск заметки  - - - - - нажмите '3'\n"
          "\tРедактирование заметки - нажмите '4'\n"
          "\tУдаление заметки - - - - нажмите '5'\n"
          "\tВыход из программы - - - нажмите '9'\n")
comd_1 = '\tСоздание заметки:'
comd_2 = '\tСписок заметок:'
comd_3 = '\tПоиск заметки:'


def interface_0():
    print(comd)
    print(app.noteCount((file.data['note_count'])))
    print(comd_0)
    num = input("Введите число -> ")
    return num


def interface_1():
    print(comd_1)


def interface_2():
    print(comd_2)
    print(app.noteCount((file.data['note_count'])))


def interface_3():
    fl = True
    while fl:
        print(comd_3)
        find = input("Введите данные для поиска -> ")
        note.note_find(find)
        print('----------------')
        print("Продолжить поиск?.\tДа --> нажмите 'Y'\n\t\t\t\t\tНет -> нажмите 'N'")
        st = input("Продолжить поиск? ")
        if st.lower() == 'y':
            fl = True
        elif st.lower() == 'n':
            fl = False
        else:
            print('Формат ввода неверный!')
