from note import Note
from backup import Backup


class Measure(object):
    def __init__(self, bs_node):
        self.bs_node = bs_node

    def notes(self, show_hidden=False):
        for n in self.bs_node.select('note'):
            note = Note(bs_node=n)
            if show_hidden or not note.is_hidden():
                yield note

    def get_melody_stat(self):
        notes = self.get_melody_notes()
        diff_sum = 0
        for a, b in zip(notes, notes[1:]):
            diff_sum += abs(a - b)
        return diff_sum / float(len(notes) - 1)

    def get_melody_notes(self):
        note_layers = list(self._get_note_layers())
        return max(note_layers, key=lambda l: len(l))

    def _notes_with_backup(self):
        for child in self.bs_node.findChildren(recursive=False):
            if child.name == 'note':
                note = Note(bs_node=child)
                if not note.is_hidden():
                    yield note
            elif child.name == 'backup':
                yield Backup(child)

    def _get_note_layers(self):
        layer = []
        for n in self._notes_with_backup():
            if type(n) == Backup:
                if len(layer) > 0:
                    yield layer
                    layer = []
            else:
                layer.append(n)
        yield layer
