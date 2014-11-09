from util import extract_text

class Note(object):
    def __init__(self, bs_node):
        self.bs_node = bs_node
        self.pitch_type = extract_text(bs_node, 'type')
        self.step = extract_text(bs_node, 'pitch step')
        self.staff = extract_text(bs_node, 'staff')
        if bs_node('rest'):
            self.is_note = False
        else:
            self.is_note = True


    def is_hidden(self):
        if ('print-object' in self.bs_node.attrs and
                self.bs_node['print-object'] == 'no'):
            return True
        return False


    def __str__(self):
        staff_string = 'staff %s' % self.staff if self.staff else ''
        if self.is_note:
            return '%s (%s) %s' % (self.step, self.pitch_type, staff_string)
        else:
            return 'rest (%s) %s' % (self.pitch_type, staff_string)


    def __repr__(self):
        if self.is_note:
            return '<Note: %s (%s) hidden: %s>' % (self.step, self.pitch_type, self.is_hidden())
        else:
            return '<Note: rest (%s) hidden: %s>' % (self.pitch_type, self.is_hidden())
