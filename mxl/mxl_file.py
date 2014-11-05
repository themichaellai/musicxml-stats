from bs4 import BeautifulSoup


class MXLFile(object):
    def __init__(self, filename):
        with open(filename, 'r') as f:
            soup = BeautifulSoup(f.read())
        self.parts = [p for s in soup('score-partwise') for p in s('part')]
        self.measures = [m for p in parts for m in p('measure')]
