from datetime import datetime
import math

laufendes_jahr = datetime.today().year


def jahrgang():
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


def gewicht():
    endnummer = int(gewicht[-1])
    gewicht = int(gewicht)

    # Round the number down
    gewicht = math.floor(gewicht / 10) * 10

    if endnummer < 5:
        return f'-{gewicht}'
    else:
        return f'+{gewicht}'