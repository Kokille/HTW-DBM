from datetime import datetime
import math

laufendes_jahr = datetime.today().year

# Define age categorie - take year of birth from /athletes page and subtract it from year it is
# devide year in olympic categories
def parse_jahrgang(jahrgang):
    alter = laufendes_jahr - int(jahrgang)

    if alter < 14:
        return 'U14'
    elif alter < 16:
        return 'U16'
    elif alter < 18:
        return 'U18'
    elif alter < 21:
        return 'U21'
    else:
        return 'Elite'

"""------------------------------------------------------------------------------------------------------------"""

# Help from a Coworker to create weight classes
# Input data from screen /athletes get pulled out of json and filtered in "classes"
def parse_gewicht(gewicht):
    endnummer = int(gewicht[-1])
    gewicht = int(gewicht)

    # Round the number down
    gewicht = math.floor(gewicht / 10) * 10

    if endnummer < 5:
        return f'-{gewicht}'
    else:
        return f'+{gewicht}'

"""------------------------------------------------------------------------------------------------------------"""

def parse_athlete(json):
    # Combine Jahrgang und Gewicht (pull out of json) to one object to display in one colum -> kategorie
    parsed_items = []
    for obj in json:
        obj['kategorie'] = ', '.join([
            parse_jahrgang(obj['jahrgang']),
            parse_gewicht(obj['gewicht']),
        ])
        parsed_items.append(obj)

    return parsed_items