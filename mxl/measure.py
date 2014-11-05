from util import note_to_string

class Measure(object):
    def __init__(self, bs_node):
        self.bs_node = bs_node

    def notes(self):
        return [note_to_string(n) for n in self.bs_node.select('note')]
