from typing import Iterable


def chunking_by(items: list, size: int) -> Iterable:
    count = 0
    new_list = []
    chunks = []

    for item in items:
        if count == size:
            count = 0
            new_list.append(chunks)
            chunks = []
            chunks.append(item)
        else:
            chunks.append(item)
        count += 1
    if chunks:
        new_list.append(chunks)
    return new_list


if __name__ == '__main__':
    print("Example:")
    print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [
        [5, 4, 7], [3, 4, 5], [4]]
    assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
    assert list(chunking_by([5, 4], 7)) == [[5, 4]]
    assert list(chunking_by([], 3)) == []
    assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]
    print("Coding complete? Click 'Check' to earn cool rewards!")
