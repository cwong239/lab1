import unittest
from main import *

class Lab1TestCase(unittest.TestCase):
    def test_f2m_1(self):
        result = f2m(1)
        self.assertEqual(result, 0.3048)
    def test_f2m_2(self):
        result = f2m("not a number")
        self.assertEqual(result, "Enter a number please")
    def test_f2m_3(self):
        result = f2m(0.92137875)
        self.assertEqual(result, 0.28083624300000004)
    def test_up_one_octave_1(self):
        n1 = Note(10, 2)
        result = up_one_octave(n1)
        self.assertEqual(result, 20)
    def test_up_one_octave_2(self):
        n3 = Note("Not a number", 2)
        result = up_one_octave(n3)
        self.assertEqual(result, "Please enter a valid number")
    def test_up_one_octave_3(self):
        n5 = Note(1203, 2)
        result = up_one_octave(n5)
        self.assertEqual(result, 2406)

