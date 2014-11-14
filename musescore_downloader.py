import requests
import fileinput
import re
import time
import sys


def rate_limit_list(arr, chunk_size, sleep_time):
    num_in_chunk = 0
    for el in arr:
        if (num_in_chunk == chunk_size):
            time.sleep(sleep_time)
            num_in_chunk = 0
        yield el
        num_in_chunk += 1

if __name__ == '__main__':
    for line in rate_limit_list(fileinput.input(), 2, 1):
        line = line.rstrip('\n')
        html = requests.get(line).text
        mxl_url = re.search('/score/\d+/download/mxl', html).group(0)
        print 'http://musescore.com%s' % mxl_url
        sys.stdout.flush()
