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
    view.interface()
    fl = True
    while fl:
        num = view.interface_0()

        if num[0] == '1':
            choice_1()
        elif num[0] == '2' and num[1] != 0:
            choice_2()
        elif num[0] == '3' and num[1] != 0:
            choice_3()
        elif num[0] == '4' and num[1] != 0:
            choice_4()
        elif num[0] == '5' and num[1] != 0:
            choice_5()
        elif num[0] == '9':
            fl = end()
            print("\033[38;2;201;100;59mЗавершение программы 'Заметки'.\033[0;0m\n")
        else:
            print('Формат ввода неверный!')


def choice_1():
    view.interface_1()
    note.create_note()


def choice_2():
    view.interface_2()
    note.print_note()


def choice_3():
    view.interface_3()


def choice_4():
    view.interface_4()


def choice_5():
    view.interface_5()
