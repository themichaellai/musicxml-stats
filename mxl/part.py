from collections import Counter


class Part(object):
    def __init__(self, measures):
        self.measures = measures

    def get_measures(self):
        return self.measures

    def get_note_type_counts(self, staff_num=None):
        """Gets the number of each type of note lengths in the part

        Returns a dictionary of counts of note lengths in the part.
        """
        acc = Counter()
        for measure in self.measures:
            acc.update(measure.get_note_type_counts(staff_num=staff_num))
        return acc

    def get_note_pitch_counts(self, staff_num=None):
        """Gets the number of each type of pitches in the part

        Returns a dictionary of counts of pitches in the part.
        """
        acc = Counter()
        for measure in self.measures:
            acc.update(measure.get_note_pitch_counts(staff_num=staff_num))
        return acc

    def get_note_octave_counts(self, staff_num=None):
        acc = Counter()
        for measure in self.measures:
            acc.update(measure.get_octave_counts(staff_num=staff_num))
        return acc

    def get_num_staffs(self):
        """Gets the number of staffs used in the part
        Determines this by looking at the first measure and counting the mumber
        of staffs it has.
        """
        return len(set(n.staff for n in self.measures[0].notes()))

    def get_melody_stat(self, staff_num=None):
        """Returns a number that attempts to describe the melody of the measure

        The number is the average of the difference between the pitches of the
        notes in measure of this part..
        """
        return (sum(m.get_melody_stat(staff_num=staff_num)
            for m in self.measures) / len(self.measures))

    def get_rhythm_stat(self, staff_num=None):
        """Returns a number that attempts to describe the rhythm difference of
        the part

        The number is the sum of the difference between the values of rhythms
        of the notes in the part, as assigned in RHYTHM_VALUES in note.py
        """
        return (sum(m.get_rhythm_stat(staff_num=staff_num)
            for m in self.measures) / len(self.measures))

    def get_dynamic_changes(self):
        """Returns a generator of pairs representing (dynamic, measure #)"""
        for i, measure in enumerate(self.get_measures()):
            dynamics = list(measure.get_dynamics())
            if len(dynamics) > 0:
                for dynamic in dynamics:
                    yield (i, dynamic)
