class RomanNumeralGenerator(object):

    def generator(self, arabic):
        roman = self.to_roman(arabic)
        return roman

    def to_roman(self, number):
        roman_number = ""
        arabic_remainder = number

        values = [10, 9, 5, 4]
        symbols = ['X', 'IX', 'V', 'IV']

        for i in range(0, len(values)):
            while (arabic_remainder >= values[i]):
                roman_number += symbols[i]
                arabic_remainder -= values[i]

        while (arabic_remainder > 0):
            roman_number += "I"
            arabic_remainder -= 1

        return roman_number

