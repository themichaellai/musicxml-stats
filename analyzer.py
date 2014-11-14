import sys
from mxl import MXLFile

if __name__ == '__main__':
    mxlf = MXLFile(sys.argv[1])
    print len(mxlf.measures), 'measures'
    print 'melody stat', mxlf.measures[0].get_melody_stat()
    print mxlf.time_signature()
    print mxlf.key_signature()
    print len(mxlf.parts)
