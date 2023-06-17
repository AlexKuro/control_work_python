import json
import os.path


def file_save(dat):
    json.dump(dat, fp=open('note_json.txt', 'w'), indent=4)
    print('\033[38;2;30;144;205mФайл сохранен.\033[0;0m')


file_path = "note_json.txt"
fl = os.path.isfile(file_path)

if fl:
    data = json.load(open('note_json.txt'))
else:
    data = {
        "note_count": 0,
    }
    file_save(data)
    data = json.load(open('note_json.txt'))
