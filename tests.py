import unittest

from mxl.note import Note
from mxl import util


class TestNote(unittest.TestCase):
    def test_subtraction_same(self):
        a = Note(rhythm_type='half', step='C', octave=1, staff=1)
        b = Note(rhythm_type='half', step='C', octave=1, staff=1)
        self.assertEqual(a - b, 0)

    def test_subtraction_same_octave(self):
        a = Note(rhythm_type='half', step='C', octave=1, staff=1)
        b = Note(rhythm_type='half', step='A', octave=1, staff=1)
        self.assertEqual(a - b, 2)

    def test_subtraction_same_octave_neg(self):
        a = Note(rhythm_type='half', step='C', octave=1, staff=1)
        b = Note(rhythm_type='half', step='A', octave=1, staff=1)
        self.assertEqual(b - a, -2)

    def test_subtraction_diff_octave(self):
        a = Note(rhythm_type='half', step='A', octave=2, staff=1)
        b = Note(rhythm_type='half', step='A', octave=1, staff=1)
        self.assertEqual(a - b, 7)

    def test_subtraction_diff_octave_diff_pitch(self):
        a = Note(rhythm_type='half', step='C', octave=2, staff=1)
        b = Note(rhythm_type='half', step='A', octave=1, staff=1)
        self.assertEqual(a - b, 9)

    def test_subtraction_diff_octave_neg(self):
        a = Note(rhythm_type='half', step='A', octave=2, staff=1)
        b = Note(rhythm_type='half', step='A', octave=1, staff=1)
        self.assertEqual(b - a, -7)

    def test_subtraction_diff_octave_diff_pitch_neg(self):
        a = Note(rhythm_type='half', step='C', octave=2, staff=1)
        b = Note(rhythm_type='half', step='A', octave=1, staff=1)
        self.assertEqual(b - a, -9)

    def test_rhythm_subtraction_pos(self):
        a = Note(rhythm_type='half')
        b = Note(rhythm_type='quarter')
        self.assertEqual(a.sub_rhythm(b), -2)

    def test_rhythm_subtraction_neg(self):
        a = Note(rhythm_type='half')
        b = Note(rhythm_type='quarter')
        self.assertEqual(b.sub_rhythm(a), 2)

    def test_time_sig_normalize(self):
        self.assertEqual(util.time_signature_normalizer(3, 8), 1.5)
        self.assertEqual(util.time_signature_normalizer(4, 4), 4)
        self.assertEqual(util.time_signature_normalizer(3, 4), 3)

    def test_time_sig_normalize_unicode_input(self):
        self.assertEqual(util.time_signature_normalizer(u'3', u'8'), 1.5)
        self.assertEqual(util.time_signature_normalizer(u'4', u'4'), 4)
        self.assertEqual(util.time_signature_normalizer(u'3', u'4'), 3)

if __name__ == '__main__':
    unittest.main()
