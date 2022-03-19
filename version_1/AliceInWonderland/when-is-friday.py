from datetime import date

FRIDAY_NUM = 4


def friday(day):

    day, month, year = day.split('.')
    _date = date.fromisoformat(year + '-' + month + '-' + day)
    weekday_num = _date.weekday()
    if weekday_num <= FRIDAY_NUM:
        result = FRIDAY_NUM - weekday_num
    else:
        result = FRIDAY_NUM + (7 - weekday_num)
    return result


if __name__ == '__main__':
    print("Example:")
    print(friday('23.04.2018'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert friday('23.04.2018') == 4
    assert friday('01.01.1999') == 0
    assert friday('11.11.1111') == 6
    print("Coding complete? Click 'Check' to earn cool rewards!")
