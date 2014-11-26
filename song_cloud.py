import sys
from mxl import MXLFile
from mxl import util
from itertools import izip

FRAME_SIZE = 3
SEP = ','

def sum_attributes(fname, measures, *args, **kwargs):
    return sum(getattr(m, fname)(*args, **kwargs) for m in measures)

def measure_zip_params(measures, frame_size):
    return tuple(measures[i:] for i in range(frame_size))

if __name__ == '__main__':
    mxlf = MXLFile(sys.argv[1])
    measures = mxlf.get_part(0).get_measures()
    norm_constant = util.time_signature_normalizer(*reversed(mxlf.time_signature()))
    stats = (
        'melody',
        'rhythm1',
        'rhythm2'
    )
    print SEP.join(str(s) for s in stats)
    for measures in izip(*measure_zip_params(measures, FRAME_SIZE)):
        melody_staff_0 = sum_attributes('get_melody_stat', measures, staff_num=1)
        rhythm_1 = sum_attributes('get_rhythm_stat', measures, staff_num=1)
        rhythm_2 = sum_attributes('get_rhythm_stat2', measures, staff_num=1)
        stats = [
            melody_staff_0,
            rhythm_1,
            rhythm_2
        ]
        print SEP.join(str(s / norm_constant) for s in stats)
