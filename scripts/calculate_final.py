import csv

r2008 = csv.reader(open('../data/2008_general_results_calculated.csv', 'rU'));
out = csv.writer(open('../data/spvi.csv', 'wb'));

# Skip header row
r2008.next()

# Write header row
out.writerow(['CTUPRE', 'SPVI']);

count = 0
matches = 0

print 'This is very inefficient, and may take a minute ..'

for line_2008 in r2008:
    found = False
    r2010 = csv.reader(open('../data/2010_general_results_calculated.csv', 'rU'));
    r2010.next() # skip the header row
    for line_2010 in r2010:
        if line_2008[29] == line_2010[32]:
            spvi = int(round((int(line_2008[30]) + int(line_2010[33])) / 2.0))
            out.writerow([line_2008[29], spvi])
            matches += 1
            found = True
            break
    if not found:
        print line_2008[29]
    count += 1

print 'Found ' + str(matches) + ' out of' + str(count) + ' records.'
