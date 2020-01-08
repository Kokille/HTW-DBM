import json

def save(form_request):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = ()

    datei_inhalt.append()

    print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def coach_save(aktivitaet):
    datei_name = "co.txt"
    speichern(datei_name, zeitpunkt, aktivitaet)
    return zeitpunkt, aktivitaet