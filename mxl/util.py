def pitch_to_string(pitch_tag):
    pitch_type = extract_text(pitch_tag, 'type')
    step = extract_text(pitch_tag, 'pitch step')
    return '%s (%s)' % (step, pitch_type)


def rest_to_string(rest_tag):
    t = rest_tag.select('type')
    rest_type = extract_text(rest_tag, 'type')
    return '%s rest' % (rest_type)


def note_to_string(note_tag):
    if note_tag('rest'):
        return rest_to_string(note_tag)
    elif note_tag('pitch'):
        return pitch_to_string(note_tag)
    else:
        return 'ERROR'


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
