from datetime import datetime


def checkio(year: int) -> int:
    return sum(datetime(year, month, 13).weekday() == 4 for month in range(1, 13))


if __name__ == '__main__':
    print("Example:")
    print(checkio(2015))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
    print("Coding complete? Click 'Check' to earn cool rewards!")
