import unittest
from roman_numeral_generator import RomanNumeralGenerator

class RomanNumeralTestCase(unittest.TestCase):
    """ Tests for `roman_numeral_generator.py`. """

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.testclass = RomanNumeralGenerator()

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_one(self):
        """ Does 1 return I? """
        result = self.testclass.generator(1)
        self.assertEqual(result, 'I')

    def test_two(self):
        """ Does 2 return II? """
        result = self.testclass.generator(2)
        self.assertEqual(result, 'II')

    def test_three(self):
        """ Does 3 return III? """
        result = self.testclass.generator(3)
        self.assertEqual(result, 'III')

    def test_four(self):
        """ Does 4 return IV? """
        result = self.testclass.generator(4)
        self.assertEqual(result, 'IV')

    def test_five(self):
        """ Does 5 return V? """
        result = self.testclass.generator(5)
        self.assertEqual(result, 'V')

if __name__ == '__main__':
    unittest.main()


