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

    def test_six(self):
        """ Does 6 return VI? """
        result = self.testclass.generator(6)
        self.assertEqual(result, 'VI')
        
    def test_seven(self):
        """ Does 7 return VII? """
        result = self.testclass.generator(7)
        self.assertEqual(result, 'VII')

    def test_eight(self):
        """ Does 8 return VIII? """
        result = self.testclass.generator(8)
        self.assertEqual(result, 'VIII')

    def test_nine(self):
        """ Does 9 return IX? """
        result = self.testclass.generator(9)
        self.assertEqual(result, 'IX')

    def test_ten(self):
        """ Does 10 return X? """
        result = self.testclass.generator(10)
        self.assertEqual(result, 'X')

    def test_twenty(self):
        """ Does 20 return X? """
        result = self.testclass.generator(20)
        self.assertEqual(result, 'XX')

if __name__ == '__main__':
    unittest.main()


