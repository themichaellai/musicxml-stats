from bs4 import BeautifulSoup
from measure import Measure
from note import Note
from util import extract_measure_attributes


class MXLFile(object):
    def __init__(self, filename):
        with open(filename, 'r') as f:
            soup = BeautifulSoup(f.read())
        self.parts = [p for s in soup('score-partwise') for p in s('part')]
        self.measures = [[Measure(m) for m in p('measure')] for p in self.parts]

    def key_signature(self):
        fifths, major_minor, _, _ = extract_measure_attributes(
            self.measures[0][0].bs_node)
        return fifths, major_minor

    def time_signature(self):
        _, _, lower, upper = extract_measure_attributes(
            self.measures[0][0].bs_node)
        return lower, upper

    def part_measures(self, part_num=0):
        return self.measures[part_num]
