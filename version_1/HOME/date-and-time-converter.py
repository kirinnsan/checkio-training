from datetime import datetime


def date_time(time: str) -> str:
    # replace this for solution
    date_time = datetime.strptime(time, '%d.%m.%Y %H:%M')
    # 注意点：0埋めなしの指定子はMacとWindowsで異なる
    # Windows：「#」をつける（例：「%#m」）
    # Mac：「-」をつける（例：「%-m」）
    date_time = date_time.strftime('%-d %B %Y year %-H hours %-M minutes')
    if '1 hours' in date_time:
        date_time = date_time.replace('1 hours', '1 hour')
    if '1 minutes' in date_time:
        date_time = date_time.replace('1 minutes', '1 minute')

    return date_time


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time(
        "11.04.1812 01:01") == "11 April 1812 year 1 hour 1 minute"
    assert date_time(
        "09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time(
        "20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
