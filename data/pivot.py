import sys
import getopt
import csv
import dbf

_inputFile = False
_outputFile = False
_year = False

def calculatePvi(rval, dval, tval):
    return 100 * ((1.0 * rval/tval) - (1.0 * dval/tval))

def pivot():
    data = {}
    iFile = file(_inputFile, "rb")
    reader = csv.reader(iFile)
    head = reader.next()
    for row in reader:
# If data already contains this district, add each value to the running totals
        try:
            data[row[0]][head[1]] = float(row[1]) + data[row[0]][head[1]]
            data[row[0]][head[2]] = float(row[2]) + data[row[0]][head[2]]
            data[row[0]][head[3]] = float(row[3]) + data[row[0]][head[3]]
            data[row[0]][head[4]] = float(row[4]) + data[row[0]][head[4]]
            data[row[0]][head[5]] = float(row[5]) + data[row[0]][head[5]]
            data[row[0]][head[6]] = float(row[6]) + data[row[0]][head[6]]
            data[row[0]][head[7]] = float(row[7]) + data[row[0]][head[7]]
            data[row[0]][head[8]] = float(row[8]) + data[row[0]][head[8]]
            data[row[0]][head[9]] = float(row[9]) + data[row[0]][head[9]]
# Otherwise, create this district in data, with starting values
        except KeyError:
            data[row[0]] = { head[1]: int(float(row[1])), head[2]: int(float(row[2])), head[3]: int(float(row[3])), head[4]: int(float(row[4])), head[5]: int(float(row[5])), head[6]: int(float(row[6])), head[7]: int(float(row[7])), head[8]: int(float(row[8])), head[9]: int(float(row[9])) }
    iFile.close()

#TODO Double check this average math
# Create a .dbf file with proper attributes
    table = dbf.Table(_outputFile, 'District C(12); pvi06 N(15,10); pvi08 N(15,10); pvi10 N(15,10); pvi N(15,10); rpvi C(10)')
    oFile = file(_outputFile + ".csv", "w")
    writer = csv.writer(oFile)
    writer.writerow(["District", "pvi06", "pvi08", "pvi10", "pvi", "rpvi"])

    if _year == '2012':
# Order cannot change for .dbf files in shapefiles. This is the original order of
# the shapefile, so the resulting .dbf file will map correctly to the shapes.
        order = '39B 25A 21A 25B 21B 37A 37B 42A 31B 38B 38A 39A 32B 32A 11B 08A 04B 02B 01B 08B 09A 02A 01A 10A 05B 10B 05A 11A 06A 06B 28B 28A 07B 03B 07A 03A 04A 22B 23A 22A 16A 12A 16B 17A 17B 12B 18A 13A 23B 27A 27B 26A 26B 19A 19B 18B 20A 24A 20B 47A 47B 33A 34A 34B 40A 36B 36A 35A 35B 31A 15A 24B 58A 56B 50B 57A 51A 51B 57B 50A 61B 61A 62B 62A 63B 63A 55B 55A 56A 33B 48B 48A 44B 44A 49B 49A 46B 46A 45B 45A 14A 29A 29B 14B 13B 09B 15B 30B 30A 59B 59A 40B 60B 60A 41B 41A 64B 64A 52B 52A 65B 66A 65A 66B 42B 58B 54A 54B 67B 53A 67A 43A 43B 53B'.split()
        for k in order:
        #for k,v in data.iteritems():
            pvi06 = calculatePvi(data[k + '         ']["ltr06"], data[k + '         ']["ltd06"], data[k + '         ']["lot06"])
            pvi08 = calculatePvi(data[k + '         ']["ltr08"], data[k + '         ']["ltd08"], data[k + '         ']["lot08"])
            pvi10 = calculatePvi(data[k + '         ']["ltr10"], data[k + '         ']["ltd10"], data[k + '         ']["lot10"])

            pvi = (pvi06 + pvi08 + pvi10) / 3
            roundedPvi = int(round(pvi))
            if roundedPvi > 0:
                rpvi = "GOP + " + str(abs(roundedPvi))
            elif roundedPvi < 0:
                rpvi = "DFL + " + str(abs(roundedPvi))
            else:
                rpvi = "EVEN"
# Write to the .dbf file and to the .csv file
            table.append((k, pvi06, pvi08, pvi10, pvi, rpvi))
            writer.writerow([k, pvi06, pvi08, pvi10, pvi, rpvi])
        else:
            print '****' + k
            print data[k + '         ']
    elif _year == '2012_sen':
# Order cannot change for .dbf files in shapefiles. This is the original order of
# the shapefile, so the resulting .dbf file will map correctly to the shapes.
        order = '15 24 56 51 57 50 61 62 63 59 60 41 64 52 65 66 42 58 54 67 53 43 25 21 37 31 32 38 39 04 08 09 02 01 10 05 11 06 28 07 03 22 16 12 17 13 23 27 26 19 18 20 47 33 55 48 44 49 46 45 40 14 29 30 34 36 35'.split()
        for k in order:
            pvi06 = calculatePvi(data[k]["ltr06"], data[k]["ltd06"], data[k]["lot06"])
            pvi08 = calculatePvi(data[k]["ltr08"], data[k]["ltd08"], data[k]["lot08"])
            pvi10 = calculatePvi(data[k]["ltr10"], data[k]["ltd10"], data[k]["lot10"])

            pvi = (pvi06 + pvi08 + pvi10) / 3
            roundedPvi = int(round(pvi))
            if roundedPvi > 0:
                rpvi = "GOP + " + str(abs(roundedPvi))
            elif roundedPvi < 0:
                rpvi = "DFL + " + str(abs(roundedPvi))
            else:
                rpvi = "EVEN"
# Write to the .dbf file and to the .csv file
            table.append((k, pvi06, pvi08, pvi10, pvi, rpvi))
            writer.writerow([k, pvi06, pvi08, pvi10, pvi, rpvi])
        else:
            print '**** ' + k
            print data[k]

    oFile.close()

def usage():
    print """
Usage:
\t-f --file\tinput file with extension
\t-o --out\toutput file without extension
"""

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hf:o:y:", ["help", "file=", "out=", "year="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-f", "--file"):
            global _inputFile
            _inputFile = arg
        elif opt in ("-o", "--out"):
            global _outputFile
            _outputFile = arg
        elif opt in ("-y", "--year"):
            global _year
            _year = arg
    if (not _inputFile) or (not _outputFile) or (not _year):
        print """Error: must specifcy file and out"""
        usage()
        sys.exit(2)
    pivot()

if __name__ == "__main__":
    main(sys.argv[1:])
