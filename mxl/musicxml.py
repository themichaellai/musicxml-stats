from bs4 import BeautifulSoup
from measure import Measure
from note import Note
from part import Part
from util import extract_measure_attributes


class MXLFile(object):
    def __init__(self, filename):
        with open(filename, 'r') as f:
            soup = BeautifulSoup(f.read())
        self.parts = [p for s in soup('score-partwise') for p in s('part')]
        measures = [[Measure(m) for m in p('measure')] for p in self.parts]
        self.parts = [Part(ms) for ms in measures]

    def key_signature(self):
        fifths, major_minor, _, _ = extract_measure_attributes(
            self.parts[0].get_measures()[0].bs_node)
        return fifths, major_minor

    def time_signature(self):
        _, _, lower, upper = extract_measure_attributes(
            self.parts[0].get_measures()[0].bs_node)
        return lower, upper

    def get_part(self, part_num=0):
        return self.parts[part_num]
