import csv

from pvi import calculate_pvi, add_to_pvi

pvi = {}

# Calculate pvi for 2008 elections
file2008 = open('2008_results_ctu.csv', 'rU')
r2008 = csv.reader(file2008)

# Skip header row
r2008.next()

for row in r2008:
    ctupre = row[55]
    pres_pvi = calculate_pvi(row, 23, 24, 31)
    mn_leg_pvi = calculate_pvi(row, 49, 50, 52)
    mn_sen_pvi = calculate_pvi(row, 33, 34, 38)
    pvi = add_to_pvi(pvi, ctupre, 'pres_2008', pres_pvi)
    pvi = add_to_pvi(pvi, ctupre, 'mn_leg_2008', mn_leg_pvi)
    pvi = add_to_pvi(pvi, ctupre, 'mn_sen_2008', mn_sen_pvi)

file2008.close()

# Calculate pvi for 2010 elections
file2010 = open('2010_results_ctu.csv', 'rU')
r2010 = csv.reader(file2010)

# Skip header row
r2010.next()

for row in r2010:
    ctupre = row[61]
    gov_pvi = calculate_pvi(row, 36, 37, 43)
    mn_leg_pvi = calculate_pvi(row, 31, 32, 34)
    pvi = add_to_pvi(pvi, ctupre, 'gov_2010', gov_pvi)
    pvi = add_to_pvi(pvi, ctupre, 'mn_leg_2010', mn_leg_pvi)

file2010.close()


# Prep an out file
fileOut = open('precincts_pvi.csv', 'wb')
out = csv.writer(fileOut)

out.writerow(['CTUPRE', 'p08', 'leg08', 'sen08', 'g10', 'leg10', 'pvi', 'rpvi'])

for k,v in pvi.iteritems():
    try:
        # Calculate an overall pvi value
        pres_2008 = float(v['pres_2008'])
        mn_leg_2008 = float(v['mn_leg_2008'])
        mn_sen_2008 = float(v['mn_sen_2008'])
        gov_2010 = float(v['gov_2010'])
        mn_leg_2010 = float(v['mn_leg_2010'])

        if pres_2008 < 1000 or mn_leg_2008 < 1000 or mn_sen_2008 < 1000 or gov_2010 < 1000 or mn_leg_2010 < 1000:
            overall_pvi = (pres_2008 + mn_leg_2008 + mn_sen_2008 + gov_2010 + mn_leg_2010) / 5

            # Create a readable pvi field
            rounded_pvi = round(overall_pvi)
            if rounded_pvi > 0:
                readable_pvi = 'GOP +%d' % abs(rounded_pvi)
            elif rounded_pvi < 0:
                readable_pvi = 'DFL +%d' % abs(rounded_pvi)
            else:
                readable_pvi = 'EVEN'

            out.writerow([k, v['pres_2008'], v['mn_leg_2008'], v['mn_sen_2008'], v['gov_2010'], v['mn_leg_2010'], overall_pvi, readable_pvi])
    except KeyError:
        # Don't write a row if precinct doesn't have valid data for all races
        pass

fileOut.close()

