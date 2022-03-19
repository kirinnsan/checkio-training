from typing import List


def checkio(a: int, b: int, c: int) -> List[int]:

    angle = 180

    if sum([a, b, c]) != 12:
        return [0, 0, 0]

    sorted_list = sorted(
        [round(angle * (a/12)), round(angle * (b/12)), round(angle * (c/12))])
    return sorted_list


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(4, 4, 4))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")
