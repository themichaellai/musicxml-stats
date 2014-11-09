import sys
from mxl import MXLFile

if __name__ == '__main__':
    mxlf = MXLFile(sys.argv[1])
    print len(mxlf.measures), 'measures'
    #for note in mxlf.measures[0].notes():
    #    print note
    mxlf._print_children_names(mxlf.measures[0])
    print mxlf.time_signature()
    print mxlf.key_signature()
    print len(mxlf.parts)
