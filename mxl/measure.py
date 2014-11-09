from note import Note


class Measure(object):
    def __init__(self, bs_node):
        self.bs_node = bs_node

    def notes(self, show_hidden=False):
        for n in self.bs_node.select('note'):
            note = Note(n)
            if show_hidden or not note.is_hidden():
                yield note
