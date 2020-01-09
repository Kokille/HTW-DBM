import json




"""
def co_schreiben(daten):
    with open('co.txt', "w", encoding="utf-8") as open_file:
        json.dump(daten, open_file)


#Coachdaten - Name/Vorname/Jahrgang - erfassen
def c_data(form_request):
    print(form_request)
    name = form_request.get('name')
    vorname = form_request.get('vorname')
    jahrgang = form_request.get('jahrgang')
    c_data_2 = name + vorname + str(jahrgang)

    co = dict{


    }
    neu hinzufügen

    co_schreiben(c_data_2)
"""

"""

#Coachdaten - Name/Vorname/Jahrgang - erfassen
def safe_entry_form(form_request):
    print(form_request)
    name = form_request.get('name')
    vorname = form_request.get('vorname')
    jahrgang = form_request.get('jahrgang')
    safe_entry(name, vorname, jahrgang)

#Coachdaten - Funktion, um Einträge des Benutzers auf "Dateneingabe" zu schreiben ("w")
def safe_entry(name, vorname, jahrgang):
    coaches = co_lesen()
    coaches[coach] = {"name": name, "vorname": vorname, "jahrgang": jahrgang}   
    print(coaches)
    co_schreiben(coaches)
"""

"""
#Entgegennehmen der Daten
def eintrag_speichern_von_formular(form_request):
    print(form_request)
    schluessel = form_request.get('schluessel')
    wert = form_request.get('wert')
    menge = form_request.get('menge')
    eintrag_speichern(schluessel, wert, menge)

#Funktion, um Einträge des Benutzers auf "Dateneingabe" zu schreiben ("w")
def eintrag_speichern(schluessel, wert, menge):
    avocado = datenbank_lesen()
    avocado[schluessel] = {"schluessel": schluessel, "wert": wert, "menge": menge}   
    print(avocado)
    datenbank_schreiben(avocado)


def datenbank_schreiben(daten):
    with open('datenbank.txt', "w", encoding="utf-8") as open_file:
        json.dump(daten, open_file)
"""

