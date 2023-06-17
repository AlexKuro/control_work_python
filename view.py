import file
import app
import note
import choice

comd = '\n\t\t\033[38;2;201;100;59m - - - - - Заметки - - - - -\033[0;0m'
comd_0 = ("\t\033[38;2;46;139;87mГлавное меню:\n"
          "\tСоздание заметки - - - - нажмите '1'\n"
          "\tСписок заметок - - - - - нажмите '2'\n"
          "\tПоиск заметки  - - - - - нажмите '3'\n"
          "\tРедактирование заметки - нажмите '4'\n"
          "\tУдаление заметки - - - - нажмите '5'\n"
          "\tВыход из программы - - - нажмите '9'\033[0;0m\n")
comd_0_1 = ("\t\033[38;2;46;139;87mГлавное меню:\n"
            "\tСоздание заметки - - - - нажмите '1'\n"
            "\tВыход из программы - - - нажмите '9'\033[0;0m\n")
comd_1 = '\t\033[38;2;46;139;87mСоздание заметки:\033[0;0m'
comd_2 = '\t\033[38;2;46;139;87mСписок заметок:\033[0;0m'
comd_3 = '\t\033[38;2;46;139;87mПоиск заметки:\033[0;0m'
comd_4 = '\t\033[38;2;46;139;87mРедактирование заметки:\n\033[0;0m'
comd_4_1 = 'Для изменения заметки введите порядковый номер из списка -> '
comd_4_2 = ("\t\033[38;2;46;139;87mИзменить имя - - - - - - нажмите '1'\n"
            "\tИзменить текст - - - - - нажмите '2'\033[0;0m\n")
comd_5 = '\t\033[38;2;46;139;87mУдаление заметки:\033[0;0m\n'
comd_5_1 = 'Для удалении заметки введите порядковый номер из списка -> '


def interface():
    print(comd)


def interface_0():
    cou = file.data['note_count']
    print(app.noteCount(cou))
    if cou != 0:
        print(comd_0)
    else:
        print(comd_0_1)
    num = input("Введите число -> ")
    return num, cou


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
        print('\033[38;2;153;50;204m-----------------------------\033[0;0m')
        print("Продолжить поиск ->\tДа --> нажмите 'Y'\n\t\t\t\t\tНет -> нажмите 'N'")
        st = input("Продолжить поиск? ")
        if st.lower() == 'y':
            fl = True
        elif st.lower() == 'n':
            fl = False
        else:
            print('Формат ввода неверный!')


def interface_4():
    print(comd_4)
    choice.choice_2()
    fl = True
    while fl:
        num = input(comd_4_1)
        if note.note_check(int(num)):
            note.editing_note(num, comd_4_2)
            fl = False
        else:
            print('Формат ввода неверный!')


def interface_5():
    print(comd_5)
    choice.choice_2()
    fl = True
    while fl:
        num = input(comd_5_1)
        if note.note_check(int(num)):
            note.del_note(num)
            fl = False
        else:
            print('Формат ввода неверный!')
