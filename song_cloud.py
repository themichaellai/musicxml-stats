import sys
import os
from mxl import MXLFile
from mxl import util
from mxl.util import filename_escape
from itertools import izip

FRAME_SIZE = 3
SEP = ','
OUTPUT_EXT = 'csv'

def sum_attributes(fname, measures, *args, **kwargs):
    return sum(getattr(m, fname)(*args, **kwargs) for m in measures)

def measure_zip_params(measures, frame_size):
    return tuple(measures[i:] for i in range(frame_size))

def main(filename):
    mxlf = MXLFile(filename)
    measures = mxlf.get_part(0).get_measures()
    norm_constant = util.time_signature_normalizer(*reversed(mxlf.time_signature()))
    res_rows = []
    stats = (
        'melody',
        'rhythm1',
        'rhythm2'
    )
    res_rows.append(SEP.join(str(s) for s in stats))
    for measures in izip(*measure_zip_params(measures, FRAME_SIZE)):
        melody_staff_0 = sum_attributes('get_melody_stat', measures, staff_num=1)
        rhythm_1 = sum_attributes('get_rhythm_stat', measures, staff_num=1)
        rhythm_2 = sum_attributes('get_rhythm_stat2', measures, staff_num=1)
        stats = [
            melody_staff_0,
            rhythm_1,
            rhythm_2
        ]
        res_rows.append(SEP.join(str(s / norm_constant) for s in stats))
    return '\n'.join(res_rows), mxlf.song_name()

def write_result(text, output_dir, output_fname):
    with open(
            os.path.join(output_dir, '%s.%s' % (output_fname, OUTPUT_EXT)),
            'w') as f:
        f.write(text)

if __name__ == '__main__':
    if os.path.isfile(sys.argv[1]):
        print main(sys.argv[1])[0]
    elif os.path.isdir(sys.argv[1]):
        for _, _, files in os.walk(sys.argv[1]):
            for fname in files:
                print 'processing %s' % os.path.join(sys.argv[1], fname)
                res, song_name = main(os.path.join(sys.argv[1], fname))
                write_result(res, sys.argv[1], filename_escape(song_name))
    else:
        print 'not file or directory'
