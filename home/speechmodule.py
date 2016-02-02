FIRST = ["","one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",             "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    if number / 100 > 0:
        hun = FIRST[number / 100] + ' ' + HUNDRED
    else:
        hun = ''
    if number % 100 < 20:
        tens = FIRST[number % 100]
    else:
        tens = FIRST[number % 10]
        number = number / 10
        tens = OTHER_TENS[number % 10 - 2] + ' ' + tens

    return " ".join([hun, tens]).strip()
      



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
