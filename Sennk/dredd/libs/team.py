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



"""

dict_coach = [
        {
            "name": "Senn",
            "vorname": "Kilian",
            "jahrgang": "1998"
        },
         {
            "name": "Sprenger",
            "vorname": "Aileen",
            "jahrgang": "1995"
        }
    ]
    dict_athlete = [
        {
            "name": "Senn",
            "vorname": "Kilian",
            "disziplin": "Kumite Male",
            "kategorie": "U16, +58kg"
        }
    ]

"""



"""
#Datei laden und anzeigen
def datenbank_lesen(file_name):
    data = {}
    try:
        with open(file_name, "r") as open_file:
            data = json.load(open_file)
    except:
        print("Error with file!")
    finally:
        return data
"""