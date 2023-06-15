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


def creat_note():
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
        if st.lower() == 'y':
            nameN = input('Введите имя заметки: -> ')
        elif st.lower() == 'n':
            print('Имя заметки: ' + name_note + ' ' + unix_time)
        else:
            print('Формат ввода неверный!')

        text = input('Введите текст заметки: -> ')
        print('Заметка ' + name_note + ' сохранена.')
        print('\n\tИнформация о заметке')
        print('  Имя заметки: ' + name_note)
        print('     id номер: ' + id)
        print('         Дата: ' + unix_time)
        print('Текст заметки: ' + text)

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
        print('------------- ' + str(num) + ' -------------')
        print('  Имя заметки: ' + ds['name'])
        print('     id номер: ' + ds['id'])
        print('         Дата: ' + timeUnixJson(ds['date']))
        print('Текст заметки: ' + ds['text'])
    else:
        print('Заметок нет')


def note_keys(data):
    d = []
    for key in data:
        d.append(key)
    return d


def note_search(search):
    pass


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


def editing_note():
    pass


def del_note():
    pass
