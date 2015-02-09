import unittest
from roman_numeral_generator import generator

class RomanNumeralTestCase(unittest.TestCase):
    """ Tests for `roman_numeral_generator.py`. """

    def test_one(self):
        """ Does 1 return I? """
        self.assertEqual(generator(1), 'I')

if __name__ == '__main__':
    unittest.main()


