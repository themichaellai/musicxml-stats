from util import extract_text


NOTES = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
RHYTHM_VALUES = {
    'whole': 1,
    'half': 2,
    'quarter': 4,
    'eighth': 8,
    'sixteenth': 16,
    '16th': 16,
    '32nd': 32,
    '64th': 64,
    '128th': 128,
    '256th': 256
}

REST_RHYTHM_VALUES = {
    'whole': 4,
    'half': 2,
    'quarter': 1,
    'eighth': 1/2.0,
    'sixteenth': 1/4.0,
    '16th': 1/4.0,
    '32nd': 1/8.0,
    '64th': 1/16.0,
    '128th': 1/32.0,
    '256th': 1/64.0
}

def is_hidden(bs_node):
    if ('print-object' in bs_node.attrs and
            bs_node['print-object'] == 'no'):
        return True
    return False

class Note(object):
    def __init__(
            self, rhythm_type='', step='', octave='', staff='', is_note=True,
            bs_node=None):
        if bs_node:
            if bs_node('rest'):
                self.is_note = False
            else:
                self.is_note = True
            self.bs_node = bs_node
            if self.is_note:
                self.rhythm_type = extract_text(bs_node, 'type')
                self.step = extract_text(bs_node, 'pitch step')
                self.octave = int(extract_text(bs_node, 'pitch octave'))
                self.is_chord = bool(bs_node('chord'))
            else:
                self.rhythm_type = extract_text(bs_node, 'type')
                self.step = None
                self.octave = None
                self.is_chord = None
            self.staff = int(extract_text(bs_node, 'staff'))
            self.is_hidden = is_hidden(bs_node)
        else:
            self.rhythm_type = rhythm_type
            self.step = step
            self.octave = octave
            self.staff = staff
            self.is_note = is_note

    def should_show(self):
        return not (self.is_hidden or self.is_chord)

    def get_rhythm_value(self):
        return RHYTHM_VALUES[self.rhythm_type]

    def get_rest_rhythm_value(self):
        return REST_RHYTHM_VALUES[self.rhythm_type]

    def sub_rhythm(self, other):
        return RHYTHM_VALUES[self.rhythm_type] - RHYTHM_VALUES[other.rhythm_type]

    def __sub__(self, other):
        if other.octave == self.octave:
            return NOTES.index(self.step) - NOTES.index(other.step)
        elif other.octave < self.octave:
            return (NOTES.index(self.step) +
                    ((self.octave - other.octave - 1) * len(NOTES)) +
                    (len(NOTES) - NOTES.index(other.step)))
        else:
            return -(NOTES.index(other.step) +
                     ((other.octave - self.octave - 1) * len(NOTES)) +
                     (len(NOTES) - NOTES.index(self.step)))

    def __str__(self):
        staff_string = 'staff %s' % self.staff if self.staff else ''
        if self.is_note:
            return '%s (%s) %s chord: %s hidden: %s' % (
                self.step, self.rhythm_type, staff_string, self.is_chord, self.is_hidden)
        else:
            return 'rest (%s) %s' % (self.rhythm_type, staff_string)

    def __repr__(self):
        if self.is_note:
            return '<Note: %s (%s) hidden: %s>' % (
                self.step, self.rhythm_type, self.is_hidden)
        else:
            return '<Note: rest (%s) hidden: %s>' % (
                self.rhythm_type, self.is_hidden)

