from datetime import datetime


def time_converter(time):
    # dt = datetime.strptime(time, '%H:%M').strftime('%I:%M')
    # result = None
    # if dt < datetime.strptime('12:00', '%H:%M'):
    #     result = dt.strftime('%I:%M') + ' a.m.'
    # else:
    #     result = dt.strftime('%I:%M') + ' p.m.'
    # if result.startswith('0'):
    #     result = result[1:]
    # return result

    # 別解
    dt = datetime.strptime(time, '%H:%M').strftime('%I:%M %p').lstrip('0')
    result = dt.replace('AM', 'a.m.').replace('PM', 'p.m.')
    return result


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
