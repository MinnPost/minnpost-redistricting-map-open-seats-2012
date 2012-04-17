import sys
import getopt

import csv

_inputFile = False
_outputFile = False

def csvstrip():
    reader = csv.reader(open(_inputFile, "rb"))
    writer = csv.writer(open(_outputFile, "w"))
    for row in reader:
        writer.writerow([row[0].strip(), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]])

def usage():
    print """Usage: -f --file input file
    -o --out output file"""

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hf:o:", ["help", "file=", "out="])
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
    if (not _inputFile) or (not _outputFile):
        usage()
        sys.exit(2)
    csvstrip()

if __name__ == "__main__":
    main(sys.argv[1:])
