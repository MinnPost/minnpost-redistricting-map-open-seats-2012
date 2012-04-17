import csv

def concatFields(inFile, outFile, field1, field2, combineTitle, inFileArgs='rU', outFileArgs='wb'):
    """Combines two int fields into one string, separated by a colon"""
    inFile = open(inFile, inFileArgs)
    outFile = open(outFile, outFileArgs)
    r = csv.reader(inFile)
    o = csv.writer(outFile)

    # Write header row
    o.writerow(r.next() + [combineTitle])

    for line in r:
        try:
            concatenated = str(int(float(line[field1]))) + ':' + str(int(float(line[field2])))
        except ValueError:
            break

        o.writerow(line + [concatenated])

    inFile.close()
    outFile.close()
