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

    def get_num_staffs(self):
        """Gets the number of staffs used in the part
        Determines this by looking at the first measure and counting the mumber
        of staffs it has.
        """
        return len(set(n.staff for n in self.measures[0].notes()))
