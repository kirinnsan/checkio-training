FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def make_first_place_speech(number):
    result = FIRST_TEN[number-1]
    return result


def make_first_ten_place_speech(number):
    index = int(str(number)[1])
    text_result = SECOND_TEN[index]
    return text_result


def make_second_ten_place_speech(number):
    index = int(str(number)[0])
    text_result = OTHER_TENS[index-2]
    return text_result


def make_hundred_speech(number):
    return FIRST_TEN[number-1] + ' ' + HUNDRED


def checkio(number):
    length = len(str(number))

    result_text = ''
    # 1桁
    if length == 1:
        result_text = make_first_place_speech(number)
    # 2桁
    elif length == 2:
        if 10 <= number < 20:
            result_text = make_first_ten_place_speech(number)
        elif str(number).endswith('0'):
            result_text = make_second_ten_place_speech(number)
        else:
            result_text = make_second_ten_place_speech(number)
            result_text += ' '
            first_num = int(str(number)[1])
            result_text += make_first_place_speech(first_num)
    # 3桁
    else:
        str_num = str(number)
        result_text = make_hundred_speech(int(str_num[0]))
        if str_num[1] == '0' and str_num[2] == '0':
            pass
        else:
            result_text += ' '
            result_text += checkio(int(str_num[1:]))

    return result_text

    # better
    # if number < 10:
    #     return FIRST_TEN[number - 1]
    # if number < 20:
    #     return SECOND_TEN[number - 10]
    # if number < 100:
    #     result = OTHER_TENS[(number // 10) - 2]
    #     if number % 10 != 0:
    #         result += " " + FIRST_TEN[(number % 10) - 1]
    #     return result
    # result = FIRST_TEN[(number // 100) - 1] + " " + HUNDRED
    # if number % 100 != 0:
    #     result += " " + checkio(number % 100)
    # return result

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(
        ' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
