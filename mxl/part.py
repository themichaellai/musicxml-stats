from collections import Counter


class Part(object):
    def __init__(self, measures):
        self.measures = measures

    def get_measures(self):
        return self.measures

    def get_note_type_counts(self):
        """Gets the number of each type of note lengths in the part

        Returns a dictionary of counts of note lengths in the part.
        """
        acc = Counter()
        for measure in self.measures:
            acc.update(measure.get_note_type_counts())
        return acc

    def get_note_pitch_counts(self):
        """Gets the number of each type of pitches in the part

        Returns a dictionary of counts of pitches in the part.
        """
        acc = Counter()
        for measure in self.measures:
            acc.update(measure.get_note_pitch_counts())
        return acc
