

def calculate_pvi(row, rowNumberR, rowNumberD, rowNumberTotal, weight=1.0):
    """Returns pvi with given weight."""

    try:
        rNumber = float(row[rowNumberR])
    except ValueError:
        rNumber = 0
    try:
        dNumber = float(row[rowNumberD])
    except ValueError:
        dNumber = 0
    try:
        tNumber = float(row[rowNumberTotal])
    except ValueError:
        tNumber = 0

    try:
        percentR = 100.0 * rNumber / tNumber
        percentD = 100.0 * dNumber / tNumber
        pvi = percentR - percentD
        pvi *= weight
    except ZeroDivisionError:
        pvi = 1000
    return pvi

def add_to_pvi(pvi, ctupre, label, value):
    """Adds the pvi to the data dict"""
    if pvi != 1000:
        try:
            pvi[ctupre] = dict(pvi[ctupre].items() + {label: value}.items())
        except KeyError:
            pvi[ctupre] = {label: value}
    return pvi

def calculate_total(row, rowNumber):
    """Returns total votes for a given row."""
    try:
        number = int(float(row[rowNumber]))
    except ValueError:
        number = 0
    return number
