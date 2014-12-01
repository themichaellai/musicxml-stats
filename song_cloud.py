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

def calc_col_maxes(matrix):
    return [max(col) for col in izip(*matrix)]

def norm_row(top, bottom):
    res = []
    for a, b in zip(top, bottom):
        if b > 0:
            res.append(a / float(b))
        else:
            res.append(a)
    return res

stats = (
    'melody',
    'rhythm1',
    'rhythm2',
    'octave1',
    'octave2',
    'octave3',
    'octave4',
    'octave5',
    'octave6',
    'octave7',
    'restrhythm'
)
def main(filename):
    mxlf = MXLFile(filename)
    measures = mxlf.get_part(0).get_measures()
    norm_constant = util.time_signature_normalizer(*reversed(mxlf.time_signature()))
    res_rows = []
    #res_rows.append(SEP.join(str(s) for s in stats))
    for measures in izip(*measure_zip_params(measures, FRAME_SIZE)):
        melody_staff_0 = sum_attributes('get_melody_stat', measures, staff_num=1)
        rhythm_1 = sum_attributes('get_rhythm_stat', measures, staff_num=1)
        rhythm_2 = sum_attributes('get_rhythm_stat2', measures, staff_num=1)
        octaves_tup = [[m.get_octave_count(i) for i in range(1, 8)] for m in measures]
        octaves_sum = [sum(col) for col in izip(*octaves_tup)]
        rest_rhythm = sum_attributes('get_rest_rhythm_stat', measures, staff_num=1)
        stats = [
            melody_staff_0,
            rhythm_1,
            rhythm_2,
            octaves_sum[0],
            octaves_sum[1],
            octaves_sum[2],
            octaves_sum[3],
            octaves_sum[4],
            octaves_sum[5],
            octaves_sum[6],
            rest_rhythm
        ]
        res_rows.append([s / norm_constant for s in stats])
        #res_rows.append(SEP.join(str(s / norm_constant) for s in stats))
    col_maxes = calc_col_maxes(res_rows)
    res_rows = [norm_row(row, col_maxes) for row in res_rows]
    return '\n'.join(SEP.join(str(c) for c in row) for row in res_rows), mxlf.song_name()

def write_result(text, output_dir, output_fname):
    with open(
            os.path.join(output_dir, '%s.%s' % (output_fname, OUTPUT_EXT)),
            'w') as f:
        f.write(text)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print SEP.join(str(s) for s in stats)
    elif os.path.isfile(sys.argv[1]):
        print main(sys.argv[1])[0]
    elif os.path.isdir(sys.argv[1]):
        for _, _, files in os.walk(sys.argv[1]):
            for fname in files:
                print 'processing %s' % os.path.join(sys.argv[1], fname)
                res, song_name = main(os.path.join(sys.argv[1], fname))
                write_result(res, sys.argv[1], filename_escape(song_name))
    else:
        print 'not file or directory'
