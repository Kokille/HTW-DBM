import json


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