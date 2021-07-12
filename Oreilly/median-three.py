from typing import Iterable
import statistics


def median_three(els: Iterable[int]) -> Iterable[int]:
    if len(els) <= 2:
        return els
    result = [els[0], els[1]]
    for i in range(2, len(els)):
        median_of_three = statistics.median([els[i-2], els[i-1], els[i]])
        result.append(median_of_three)
    return result


if __name__ == '__main__':
    print("Example:")
    print(list(median_three([1, 2, 3, 4, 5, 6, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
