import csv
import sys

from pvi import calculate_pvi, add_to_pvi, calculate_total

pvi = {}

# Calculate pvi for 2006 elections
file2006 = open('2006_results_ctu.csv', 'rU')
r2006 = csv.reader(file2006)

# Skip header row
#r2006.next()

for row in r2006:
    ctupre = row[61]
    mnleg_pvi_r_total_06 = calculate_total(row, 56)
    mnleg_pvi_d_total_06 = calculate_total(row, 57)
    mnleg_pvi_total_06 = calculate_total(row, 60)

    pvi = add_to_pvi(pvi, ctupre, 'mnleg_06_tr', mnleg_pvi_r_total_06)
    pvi = add_to_pvi(pvi, ctupre, 'mnleg_06_td', mnleg_pvi_d_total_06)
    pvi = add_to_pvi(pvi, ctupre, 'mnleg_06_ot', mnleg_pvi_total_06)

file2006.close()

# Calculate pvi for 2008 elections
file2008 = open('2008_results_ctu.csv', 'rU')
r2008 = csv.reader(file2008)

# Skip header row
r2008.next()

for row in r2008:
    ctupre = row[55]
    mnleg_pvi_r_total_08 = calculate_total(row, 49)
    mnleg_pvi_d_total_08 = calculate_total(row, 50)
    mnleg_pvi_total_08 = calculate_total(row, 52)

    pvi = add_to_pvi(pvi, ctupre, 'mnleg_08_tr', mnleg_pvi_r_total_08)
    pvi = add_to_pvi(pvi, ctupre, 'mnleg_08_td', mnleg_pvi_d_total_08)
    pvi = add_to_pvi(pvi, ctupre, 'mnleg_08_ot', mnleg_pvi_total_08)

file2008.close()

# Calculate pvi for 2010 elections
file2010 = open('2010_results_ctu.csv', 'rU')
r2010 = csv.reader(file2010)

# Skip header row
r2010.next()

for row in r2010:
    ctupre = row[61]
    mnleg_pvi_d_total_10 = calculate_total(row, 31)
    mnleg_pvi_r_total_10 = calculate_total(row, 32)
    mnleg_pvi_total_10 = calculate_total(row, 34)

    pvi = add_to_pvi(pvi, ctupre, 'mnleg_10_tr', mnleg_pvi_r_total_10)
    pvi = add_to_pvi(pvi, ctupre, 'mnleg_10_td', mnleg_pvi_d_total_10)
    pvi = add_to_pvi(pvi, ctupre, 'mnleg_10_ot', mnleg_pvi_total_10)

file2010.close()


# Prep an out file
fileOut = open('precincts_pvi.csv', 'wb')
out = csv.writer(fileOut)

out.writerow(['CTUPRE', 'ltr06', 'td06', 'lot06', 'ltr08', 'ltd08', 'lot08', 'ltr10', 'ltd10', 'lot10'])

for k,v in pvi.iteritems():
    try:
            out.writerow([k, v['mnleg_06_tr'], v['mnleg_06_td'], v['mnleg_06_ot'], v['mnleg_08_tr'], v['mnleg_08_td'], v['mnleg_08_ot'], v['mnleg_10_tr'], v['mnleg_10_td'], v['mnleg_10_ot']])
    except KeyError:
        # Don't write a row if precinct doesn't have valid data for all races
        pass

fileOut.close()

