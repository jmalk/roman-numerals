class RomanNumeralGenerator(object):

    def generator(self, arabic):
        roman = self.to_roman(arabic)
        return roman

    def to_roman(self, number):
        roman_number = ""
        arabic_remainder = number

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        for i in range(0, len(values)):
            while (arabic_remainder >= values[i]):
                roman_number += symbols[i]
                arabic_remainder -= values[i]

        return roman_number

