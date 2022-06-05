def time_converter(time):
    hour, minute = time.split(":")
    new_hour = int(hour)
    meridiem = "a.m."
    if new_hour > 12:
        new_hour = new_hour - 12
        meridiem = "p.m."
    elif new_hour == 12:
        meridiem = "p.m."
    elif new_hour == 00:
        meridiem = "a.m."
        new_hour = 12

    return f"{new_hour}:{minute} {meridiem}"


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
