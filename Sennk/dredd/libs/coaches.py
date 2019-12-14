import json

#Coachdaten - Name/Vorname/Jahrgang - erfassen
def eintrag_speichern_von_formular(form_request):
    print(form_request)
    schluessel = form_request.get('schluessel')
    wert = form_request.get('wert')
    menge = form_request.get('menge')
    eintrag_speichern(schluessel, wert, menge)

#Funktion, um Einträge des Benutzers auf "Dateneingabe" zu schreiben ("w")
def eintrag_speichern(schluessel, wert, menge):
    coaches = datenbank_lesen()
    coaches[schluessel] = {"schluessel": schluessel, "wert": wert, "menge": menge}   
    print(coaches)
    datenbank_schreiben(coaches)


def datenbank_schreiben(daten):
    with open('datenbank.txt', "w", encoding="utf-8") as open_file:
        json.dump(daten, open_file)

#Datei laden und anzeigen
def datenbank_lesen():
    data = {}
    try:
        with open('datenbank.txt', "r") as open_file:
            data = json.load(open_file)
    except:
        print("Error with file!")
    finally:
        return data

#Zu Suchanfrage schlüssel inkl wert ausgeben
def daten_suchen(form_request):
    coaches = datenbank_lesen()
    schluessel = form_request.get('schluessel')

    if schluessel in coaches:
        return {schluessel: coaches[schluessel]}



        
