import sys
from mxl import MXLFile

if __name__ == '__main__':
    mxlf = MXLFile(sys.argv[1])
    print len(mxlf.measures), 'measures'
    print mxlf.measures[0].notes()
    print mxlf.time_signature()
    print mxlf.key_signature()
