from datetime import datetime, timedelta


def vacation(date, days):
    _date = datetime.strptime(date, '%Y-%m-%d').date()
    target_day = _date + timedelta(days=days)
    # Saturday
    if target_day.weekday() == 5:
        target_day = target_day + timedelta(days=2)
    # Sunday
    elif target_day.weekday() == 6:
        target_day = target_day + timedelta(days=1)
    result = target_day.strftime('%Y-%m-%d')
    return result


if __name__ == '__main__':
    print("Example:")
    print(vacation('2018-07-01', 14))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert vacation('2018-07-01', 14) == '2018-07-16'
    assert vacation('2018-02-19', 10) == '2018-03-01'
    assert vacation('2000-02-28', 5) == '2000-03-06'
    assert vacation('1999-12-20', 14) == '2000-01-03'
    print("Coding complete? Click 'Check' to earn cool rewards!")
