import sys
from mxl import MXLFile

if __name__ == '__main__':
    mxlf = MXLFile(sys.argv[1])
    num_measures = len(mxlf.get_part(0).get_measures())
    print mxlf.time_signature()
    print mxlf.key_signature()
    print len(mxlf.parts)
    num_staffs = mxlf.get_part(0).get_num_staffs()
    print 'num staffs: %d' % num_staffs
    for staff_i in xrange(num_staffs):
        staff_num = staff_i + 1
        print 'staff number %d' % staff_num
        print 'melody stat', mxlf.get_part(0).get_melody_stat()
        print 'part 0 note type counts:'
        for k, v in sorted(mxlf.get_part(0).get_note_type_counts(staff_num=staff_num).iteritems()):
            print '%s: %d' % (k, v)
        print 'part 0 note pitch counts:'
        for k, v in sorted(mxlf.get_part(0).get_note_pitch_counts(staff_num=staff_num).iteritems()):
            print '%s: %d' % (k, v)
