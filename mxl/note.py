from util import extract_text


NOTES = ('A', 'B', 'C', 'D', 'E', 'F', 'G')


class Note(object):
    def __init__(
            self, pitch_type='', step='', octave='', staff='', is_note=True,
            bs_node=None):
        if bs_node:
            self.bs_node = bs_node
            self.pitch_type = extract_text(bs_node, 'type')
            self.step = extract_text(bs_node, 'pitch step')
            self.octave = extract_text(bs_node, 'pitch octave')
            self.staff = extract_text(bs_node, 'staff')
            if bs_node('rest'):
                self.is_note = False
            else:
                self.is_note = True
        else:
            self.pitch_type = pitch_type
            self.step = step
            self.octave = octave
            self.staff = staff
            self.is_note = is_note

    def is_hidden(self):
        if ('print-object' in self.bs_node.attrs and
                self.bs_node['print-object'] == 'no'):
            return True
        return False

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
            return '%s (%s) %s' % (self.step, self.pitch_type, staff_string)
        else:
            return 'rest (%s) %s' % (self.pitch_type, staff_string)

    def __repr__(self):
        if self.is_note:
            return '<Note: %s (%s) hidden: %s>' % (
                self.step, self.pitch_type, self.is_hidden())
        else:
            return '<Note: rest (%s) hidden: %s>' % (
                self.pitch_type, self.is_hidden())
