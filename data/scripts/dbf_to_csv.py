import sys
import getopt

import dbf

_inputFile = False
_outputFile = False

def export():
    table = dbf.Table(_inputFile)
    table.export(filename=_outputFile, header=True)

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
    export()

if __name__ == "__main__":
    main(sys.argv[1:])
