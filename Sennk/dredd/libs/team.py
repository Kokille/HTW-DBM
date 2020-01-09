import json

def load_json(file):
    with open(file) as f:
        obj = json.load(f)
    return obj


def save_json(file, form_request):
    try:
        with open(file) as f:
            datei_inhalt = json.load(f)
    except FileNotFoundError:
        datei_inhalt = ()

    # Append new object to json list
    datei_inhalt.append(
        form_request
    )

    # Rewrite and dump object to json
    with open(file, 'w') as f:
        json.dump(datei_inhalt, f)