import unittest

from mxl.note import Note


class TestNote(unittest.TestCase):
    def test_subtraction_same(self):
        a = Note(pitch_type='half', step='C', octave=1, staff=1)
        b = Note(pitch_type='half', step='C', octave=1, staff=1)
        self.assertEqual(a - b, 0)

    def test_subtraction_same_octave(self):
        a = Note(pitch_type='half', step='C', octave=1, staff=1)
        b = Note(pitch_type='half', step='A', octave=1, staff=1)
        self.assertEqual(a - b, 2)

    def test_subtraction_same_octave_neg(self):
        a = Note(pitch_type='half', step='C', octave=1, staff=1)
        b = Note(pitch_type='half', step='A', octave=1, staff=1)
        self.assertEqual(b - a, -2)

    def test_subtraction_diff_octave(self):
        a = Note(pitch_type='half', step='A', octave=2, staff=1)
        b = Note(pitch_type='half', step='A', octave=1, staff=1)
        self.assertEqual(a - b, 7)

    def test_subtraction_diff_octave_diff_pitch(self):
        a = Note(pitch_type='half', step='C', octave=2, staff=1)
        b = Note(pitch_type='half', step='A', octave=1, staff=1)
        self.assertEqual(a - b, 9)

    def test_subtraction_diff_octave_neg(self):
        a = Note(pitch_type='half', step='A', octave=2, staff=1)
        b = Note(pitch_type='half', step='A', octave=1, staff=1)
        self.assertEqual(b - a, -7)

    def test_subtraction_diff_octave_diff_pitch_neg(self):
        a = Note(pitch_type='half', step='C', octave=2, staff=1)
        b = Note(pitch_type='half', step='A', octave=1, staff=1)
        self.assertEqual(b - a, -9)

if __name__ == '__main__':
    unittest.main()
