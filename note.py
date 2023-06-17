import datetime
import time
import file
import json


def timeUnixJson(seconds):
    unixJs = time.ctime(seconds)
    weekA = weekEnRu(unixJs[:3])
    dateA = unixJs[8:10]
    monthA = monthEnRu(unixJs[4:7])
    yearA = unixJs[20:]
    timeA = unixJs[11:19]
    st = weekA + " " + dateA + " " + monthA + " " + yearA + " " + timeA
    return st


def weekEnRu(week):
    if week == "Sun":
        return "ВС"
    elif week == "Mon":
        return "ПН"
    elif week == "Tue":
        return "ВТ"
    elif week == "Wed":
        return "СР"
    elif week == "Thu":
        return "ЧТ"
    elif week == "Fri":
        return "ПТ"
    elif week == "Sat":
        return "СБ"


def monthEnRu(month):
    if month == "Jan":
        return "Января"
    elif month == "Feb":
        return "Февраля"
    elif month == "Mar":
        return "Марта"
    elif month == "Apr":
        return "Апреля"
    elif month == "May":
        return "Мая"
    elif month == "Jun":
        return "Июня"
    elif month == "Jul":
        return "Июля"
    elif month == "Aug":
        return "Августа"
    elif month == "Sep":
        return "Сентября"
    elif month == "Oct":
        return "Октября"
    elif month == "Nov":
        return "Ноября"
    elif month == "Dec":
        return "Декабря"


def monthEnInt(month):
    if month == "Jan":
        return 1
    elif month == "Feb":
        return 2
    elif month == "Mar":
        return 3
    elif month == "Apr":
        return 4
    elif month == "May":
        return 5
    elif month == "Jun":
        return 6
    elif month == "Jul":
        return 7
    elif month == "Aug":
        return 8
    elif month == "Sep":
        return 9
    elif month == "Oct":
        return 10
    elif month == "Nov":
        return 11
    elif month == "Dec":
        return 12


def create_note():
    fl = True
    while fl:
        date = datetime.datetime.now()
        time_unix = int(str(datetime.datetime.timestamp(date))[:10])
        unix_time = timeUnixJson(time_unix)
        id = str(time_unix)[5:10]
        name_note = 'note_' + id
        nameN = 'note_' + id
        print('Имя заметки: ' + name_note)
        print("Изменить имя заметки.\tДа --> нажмите 'Y'\n\t\t\t\t\t\tНет -> нажмите 'N'")
        st = input('Изменить имя заметки? -> ')
        fl = True
        while fl:
            if st.lower() == 'y':
                nameN = input('Введите имя заметки: -> ')
                fl = False
            elif st.lower() == 'n':
                print('Имя заметки: ' + name_note + ' ' + unix_time)
                fl = False
            else:
                print('Формат ввода неверный!')

        text = input('Введите текст заметки: -> ')
        print("Заметка '" + nameN + "' сохранена.")
        print('\n\tИнформация о заметке')
        print('\033[38;2;201;100;59m  Имя заметки: \033[0;0m' + name_note)
        print('\033[38;2;201;100;59m     id номер: \033[0;0m' + id)
        print('\033[38;2;201;100;59m         Дата: \033[0;0m' + unix_time)
        print('\033[38;2;201;100;59mТекст заметки: \033[0;0m' + text)

        file.data[name_note] = {'id': id, 'date': time_unix, 'name': nameN, 'text': text}
        file.data['note_count'] += 1
        json.dump(file.data, fp=open('note_json.txt', 'w'), indent=4)

        print("Создать новую заметку.\tДа --> нажмите 'Y'.\n\t\t\t\t\t\tНет -> нажмите 'N'")
        st = input('Создать новую заметку? -> ')
        if st.lower() == 'y':
            fl = True
        elif st.lower() == 'n':
            fl = False
        else:
            print('Формат ввода неверный!')


def note_js(key, num):
    if num != 0:
        ds = file.data[key]
        print('\033[38;2;153;50;204m------------- ' + str(num) + ' -------------\033[0;0m')
        print('\033[38;2;201;100;59m  Имя заметки\033[0;0m: ' + ds['name'])
        print('\033[38;2;201;100;59m     id номер\033[0;0m: ' + ds['id'])
        print('\033[38;2;201;100;59m         Дата\033[0;0m: ' + timeUnixJson(ds['date']))
        print('\033[38;2;201;100;59mТекст заметки\033[0;0m: ' + ds['text'])
    else:
        print('Заметок нет')


def note_keys(data):
    d = []
    for key in data:
        d.append(key)
    return d


def print_note():
    dataK = note_keys(file.data)
    length = len(dataK)
    for i in range(1, length):
        note_js(dataK[i], i)


def print_note_find(dataK):
    length = len(dataK)
    for i in range(0, length):
        note_js(dataK[i], i + 1)


def find_elements(key, find):
    ds = file.data[key]
    length = len(find)
    name = ds['name']
    id = str(ds['id'])
    if name[:length] == find or id[:length] == find:
        return key
    else:
        return '0'


def note_find(find):
    ds = note_keys(file.data)
    arr = []
    for i in range(1, len(ds)):
        elem = find_elements(ds[i], find)
        if elem != '0':
            arr.append(elem)
    if len(arr) != 0:
        print(f"\nПо введенным данным '{find}' найдено заметок: --> {len(arr)}")
        print_note_find(arr)
    else:
        print(f"\nПо введенным данным '{find}' заметок нет:")


def note_check(num):
    dataK = note_keys(file.data)
    length = len(dataK)
    if num < length:
        return True
    else:
        return False


def editing_note(numst, comand):
    dataK = note_keys(file.data)
    num = int(numst)
    dataEdit = dataK[num]
    note_js(dataEdit, num)
    print(comand)
    fl = True
    while fl:
        num = input("Введите число -> ")
        if num == '1':
            nameN = file.data[dataEdit]['name']
            print('Имя заметки: ' + nameN)
            nameN = input('Введите новое имя заметки: -> ')
            file.data[dataEdit]['name'] = nameN
            file.file_save(file.data)
            fl = False
        elif num == '2':
            nameN = file.data[dataEdit]['text']
            print('Текст заметки: ' + nameN)
            nameN = input('Введите новый текст заметки: -> ')
            file.data[dataEdit]['text'] = nameN
            file.file_save(file.data)
            fl = False
        else:
            print('Введен не корректный порядковый номер.')


def del_note(numst):
    dataK = note_keys(file.data)
    num = int(numst)
    dataEdit = dataK[num]
    note_js(dataEdit, num)
    del file.data[dataEdit]
    file.data['note_count'] -= 1
    print('Заметка удалена')
    file.file_save(file.data)
