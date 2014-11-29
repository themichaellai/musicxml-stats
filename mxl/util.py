import string
import re


def key_to_string(key_tag):
    fifths, major_minor = extract_adjacent_nodes(key_tag, 'fifths', 'mode')
    return fifths, major_minor


def time_to_string(time_tag):
    lower, upper = extract_adjacent_nodes(time_tag, 'beat-type', 'beats')
    return lower, upper


def extract_measure_attributes(measure_tag):
    attributes = measure_tag('attributes')
    if attributes:
        attributes = attributes[0]
        key = attributes('key')
        fifths, major_minor = key_to_string(key[0]) if key else (None, None)
        time = attributes('time')
        lower_time, upper_time = time_to_string(time[0]) if time else (None, None)
        return fifths, major_minor, lower_time, upper_time

# Gets text inside xml node
def extract_text(tag, child_name, css_selector=True):
    if css_selector:
        child = tag.select(child_name)
    else:
        child = tag(child_name)
    return ''.join(t.get_text() for t in child)


# Extracts text from adjacent nodes given the adjacent node names
def extract_adjacent_nodes(parent_node, *node_names):
    return [extract_text(parent_node, k, False) for k in node_names]


def time_signature_normalizer(up, low):
    RHYTHM_NORM_VALUES = {
        '1': 4,
        '2': 2,
        '4': 1,
        '8': 2,
        '16': 4,
        '32': 8
    }
    return int(up) * (1 / float(RHYTHM_NORM_VALUES[str(low)]))

def filename_escape(fname):
    valid_chars = '-_.()%s%s' % (string.ascii_letters, string.digits)
    unwhitespaced = re.sub('\s', '-', fname)
    return ''.join(c for c in unwhitespaced if c in valid_chars)

def cache(f):
    cached = {}
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cached:
            cached[key] = f(*args, **kwargs)
        return cached[key]
    return wrapper
