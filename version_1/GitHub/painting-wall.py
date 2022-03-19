def checkio(required, operations):
    painted_range_set = set()
    for i, operation in enumerate(operations, 1):
        # TODO set(range(operation[0], operation[1]+1))が重すぎる
        painted_set = set(
            range(operation[0], operation[1]+1)) - painted_range_set
        painted_range_set = painted_range_set | painted_set
        if len(painted_range_set) >= required:
            return i
    return -1


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 1, "1st"
    assert checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 2, "2nd"
    assert checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 3, "3rd"
    assert checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 4, "4th"
    assert checkio(21, [[1, 5], [11, 15], [2, 14],
                        [21, 25]]) == -1, "not enough"
    assert checkio(1000000011, [[1, 1000000000], [
                   11, 1000000010]]) == -1, "large"


def checkio(required, operations):
    painted = []
    for k, i in enumerate(operations):
        painted.append(i[:])
        painted.sort(key=lambda i: i[0])
        j = 0
        for l in range(len(painted) - 1):
            if painted[j][1] >= painted[j + 1][0]:
                painted[j][1] = max(painted[j][1], painted[j + 1][1])
                painted.pop(j + 1)
            else:
                j += 1
        length = 0
        for l in painted:
            length += l[1] - l[0] + 1
        if length >= required:
            return k + 1
    return -1
