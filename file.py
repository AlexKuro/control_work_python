import json
import os.path

file_path = "note_json.txt"
fl = os.path.isfile(file_path)

if fl:
    data = json.load(open('note_json.txt'))
else:
    data = {
        "note_count": 0,
    }
    json.dump(data, fp=open('note_json.txt', 'w'), indent=4)
    data = json.load(open('note_json.txt'))
