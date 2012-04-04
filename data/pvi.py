

def calculate_pvi(row, rowNumberR, rowNumberD, rowNumberTotal, weight=1.0):
    """Returns pvi with given weight."""

    rNumber = int(row[rowNumberR])
    dNumber = int(row[rowNumberD])
    tNumber = int(row[rowNumberTotal])
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

