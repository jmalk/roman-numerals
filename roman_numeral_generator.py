class RomanNumeralGenerator(object):

    def generator(self, arabic):
        roman = self.to_roman(arabic)
        return roman

    def to_roman(self, number):
        roman_number = ""
        arabic_remainder = number

        if (arabic_remainder >= 10):
            roman_number += 'X'
            arabic_remainder -= 10

        if (arabic_remainder >= 9):
            roman_number = 'IX'
            arabic_remainder -= 9

        if (arabic_remainder >= 5):
            roman_number += 'V'
            arabic_remainder -= 5

        if (arabic_remainder >= 4):
            roman_number = 'IV'
            arabic_remainder -= 4

        while (arabic_remainder > 0):
            roman_number += "I"
            arabic_remainder -= 1

        return roman_number
