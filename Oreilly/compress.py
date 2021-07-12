from typing import Iterable


def compress(items: list) -> Iterable:
    if not items:
        return []
    compressed_list = [items[0]]
    current = items[0]
    for item in items:
        if item == current:
            continue
        else:
            compressed_list.append(item)
            current = item
    return compressed_list


if __name__ == '__main__':
    print("Example:")
    print(list(compress([
        5, 5, 5,
        4, 5, 6,
        6, 5, 5,
        7, 8, 0,
        0])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(compress([
        5, 5, 5,
        4, 5, 6,
        6, 5, 5,
        7, 8, 0,
        0])) == [5, 4, 5, 6, 5, 7, 8, 0]
    assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
    assert list(compress([7, 7])) == [7]
    assert list(compress([])) == []
    assert list(compress([1, 2, 3, 4])) == [1, 2, 3, 4]
    assert list(compress([9, 9, 9, 9, 9, 9, 9])) == [9]
    print("Coding complete? Click 'Check' to earn cool rewards!")
