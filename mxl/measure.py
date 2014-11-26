from note import Note
from backup import Backup
from collections import Counter


class Measure(object):
    def __init__(self, bs_node):
        self.bs_node = bs_node
        self._notes_cache = None

    def _notes(self):
        if self._notes_cache == None:
            self._notes_cache = []
            for n in self.bs_node.select('note'):
                self._notes_cache.append(Note(bs_node=n))
        return self._notes_cache

    def notes(self, show_hidden=False, staff_num=None):
        for note in self._notes():
            if show_hidden or note.should_show():
                if staff_num == None or note.staff == staff_num:
                    yield note

    def get_melody_stat(self, staff_num=None, take_average=False):
        """Returns a number that attempts to describe the melody of the measure

        The number is the sum of the difference between the pitches of the notes
        in the measure.
        """
        notes_with_rests = self.get_interesting_notes(staff_num=staff_num)
        notes = [n for n in notes_with_rests if n.is_note]
        diff_sum = 0
        for a, b in zip(notes, notes[1:]):
            diff_sum += abs(a - b)
        if take_average:
            return diff_sum / float(len(notes) - 1)
        return diff_sum

    def get_rhythm_stat(self, staff_num=None, take_average=False):
        """Returns a number that attempts to describe the rhythm difference of
        the measure

        The number is the sum of the difference between the values of rhythms
        of the notes in the measure, as assigned in RHYTHM_VALUES in note.py
        """
        notes_with_rests = self.get_interesting_notes(staff_num=staff_num)
        notes = [n for n in notes_with_rests if n.is_note]
        diff_sum = 0
        for a, b in zip(notes, notes[1:]):
            diff_sum += abs(a.sub_rhythm(b))
        if take_average:
            return diff_sum / float(len(notes) - 1)
        return diff_sum

    def get_rhythm_stat2(self, staff_num=None, take_average=False):
        """Returns a number that attempts to describe the rhythm difference of
        the measure

        The number is the sum of the number of notes per frame weighted
        accordingly
        """
        notes_with_rests = self.get_interesting_notes(staff_num=staff_num)
        notes = [n for n in notes_with_rests if n.is_note]
        return sum(n.get_rhythm_value() for n in notes)

    def get_interesting_notes(self, staff_num=None):
        note_layers = list(self._get_note_layers(staff_num=staff_num))
        return max(note_layers, key=lambda l: len(l))

    def get_note_type_counts(self, staff_num=None):
        """Gets the number of each type of note lengths in a measure

        Returns a dictionary of counts of note lengths in the measure.
        """
        type_counter = Counter()
        for note in self.get_interesting_notes(staff_num=staff_num):
            if note.is_note:
                type_counter.update([note.rhythm_type])
        return type_counter

    def get_note_pitch_counts(self, staff_num=None):
        """Gets the number of each type of pitches in a measure

        Returns a dictionary of counts of pitches in the measure.
        """
        pitch_counter = Counter()
        for note in self.get_interesting_notes(staff_num=staff_num):
            if note.is_note:
                pitch_counter.update([note.step])
        return pitch_counter

    def get_num_staffs(self):
        """Gets the number of staffs used in the measure"""
        return len(set(n.staff for n in self.notes()))

    def get_dynamics(self):
        """Gets all dyanmic markings in the measure"""
        for dyn_node in self.bs_node.select('dynamics'):
            for dynamic in dyn_node.findChildren(recursive=False):
                yield dynamic.name

    def _notes_with_backup(self, staff_num=None):
        for child in self.bs_node.findChildren(recursive=False):
            if child.name == 'note':
                note = Note(bs_node=child)
                if (not note.is_hidden
                        and (staff_num == None or staff_num==note.staff)):
                    yield note
            elif child.name == 'backup':
                yield Backup(child)

    def _get_note_layers(self, staff_num=None):
        layer = []
        for n in self._notes_with_backup(staff_num=staff_num):
            if type(n) == Backup:
                if len(layer) > 0:
                    yield layer
                    layer = []
            else:
                layer.append(n)
        yield layer
