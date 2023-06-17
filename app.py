import choice


def noteCount(count):
    if count == 0:
        return '\t--> Заметок нет.'
    else:
        s = '\n\t--> Найдено заметок: \033[38;2;153;50;204m' + str(count) + '\033[0;0m'
        return s


def start():
    choice.choice_0()



