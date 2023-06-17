import view
import note


def check(num):
    if num == '1' \
            or num == '2' \
            or num == '3' \
            or num == '4' \
            or num == '5':
        return True
    else:
        return False


def end():
    return False


def choice_0():
    fl = True
    while fl:
        num = view.interface_0()
        if num == '1':
            choice_1()
        elif num == '2':
            choice_2()
        elif num == '3':
            choice_3()
        elif num == '4':
            choice_4()
        elif num == '5':
            choice_1()
        elif num == '9':
            fl = end()
            print("Завершение программы 'Заметки'.\n")
        else:
            print('Формат ввода неверный!')


def choice_1():
    view.interface_1()
    note.creat_note()


def choice_2():
    view.interface_2()
    note.print_note()


def choice_3():
    view.interface_3()


def choice_4():
    view.interface_4()
