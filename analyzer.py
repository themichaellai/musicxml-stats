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
        print 'melody stat', mxlf.get_part(0).get_melody_stat(staff_num=staff_num)
        print 'part 0 note type counts:'
        for k, v in sorted(mxlf.get_part(0).get_note_type_counts(staff_num=staff_num).iteritems()):
            print '%s: %d' % (k, v)
        print 'part 0 note pitch counts:'
        for k, v in sorted(mxlf.get_part(0).get_note_pitch_counts(staff_num=staff_num).iteritems()):
            print '%s: %d' % (k, v)
        print 'part 0 note octave counts:'
        for k, v in sorted(mxlf.get_part(0).get_note_octave_counts(staff_num=staff_num).iteritems()):
            print '%s (%s): %d' % (k, type(k), v)
        print 'num dynamic changes: %d' % len(list(mxlf.get_part(0).get_dynamic_changes()))
        print 'rests:'
        for i, measure in enumerate(mxlf.get_part(0).get_measures()):
            rests = list(measure.rests(staff_num=staff_num))
            if len(rests) > 0:
                for rest in rests:
                    print 'measure %d - %s' % (i, str(rest))
