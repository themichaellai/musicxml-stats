import sys
from mxl import MXLFile

if __name__ == '__main__':
    mxlf = MXLFile(sys.argv[1])
    print len(mxlf.get_part(0).get_measures()), 'measures'
    print 'melody stat', mxlf.get_part(0).get_measures()[0].get_melody_stat()
    print mxlf.time_signature()
    print mxlf.key_signature()
    print len(mxlf.parts)
    print 'part 0 note type counts:'
    for k, v in mxlf.get_part(0).get_note_type_counts().iteritems():
        print '%s: %d' % (k, v)
    print 'part 0 note pitch counts:'
    for k, v in mxlf.get_part(0).get_note_pitch_counts().iteritems():
        print '%s: %d' % (k, v)
