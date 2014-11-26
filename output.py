from mxl import MXLFile
import fileinput

SEP = ','
COLUMNS = (
    'time.upper',
    'time.lower',
    'key.fifths',
    'maj.min',
    'melody.staff.1',
    'melody.staff.2',
    'num.dynamic.changes',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    '16th',
    'eighth',
    'half',
    'quarter',
    'whole'
)
if __name__ == '__main__':
    print SEP.join(COLUMNS)
    for line in fileinput.input():
        mxlf = MXLFile(line.rstrip('\n'))
        num_measures = len(mxlf.get_part(0).get_measures())

        note_type_counts = mxlf.get_part(0).get_note_type_counts(staff_num=1)
        note_pitch_counts = mxlf.get_part(0).get_note_pitch_counts(staff_num=1)

        num_staffs = mxlf.get_part(0).get_num_staffs()
        time_signature = mxlf.time_signature()
        key_signature = mxlf.key_signature()
        melody_staff_0 = mxlf.get_part(0).get_melody_stat(staff_num=1)
        if num_staffs > 1:
            melody_staff_1 = mxlf.get_part(0).get_melody_stat(staff_num=2)
        else:
            melody_staff_1 = -1
        columns = (
            time_signature[0],
            time_signature[1],
            key_signature[0],
            key_signature[1],
            melody_staff_0,
            melody_staff_1,
            len(list(mxlf.get_part(0).get_dynamic_changes())) / float(num_measures),
            note_pitch_counts['A'] / float(num_measures),
            note_pitch_counts['B'] / float(num_measures),
            note_pitch_counts['C'] / float(num_measures),
            note_pitch_counts['D'] / float(num_measures),
            note_pitch_counts['E'] / float(num_measures),
            note_pitch_counts['F'] / float(num_measures),
            note_pitch_counts['G'] / float(num_measures),
            note_type_counts['16th'] / float(num_measures),
            note_type_counts['eighth'] / float(num_measures),
            note_type_counts['half'] / float(num_measures),
            note_type_counts['quarter'] / float(num_measures),
            note_type_counts['whole'] / float(num_measures)
        )
        print SEP.join(map(str, columns))
