from typing import List
from itertools import groupby

def sum_consecutives(num_list: List):
    if not num_list:
        return []

    # result = []
    # tmp_val = num_list[0]
    # sum_val = 0
    # for num in num_list:
    #     if num == tmp_val:
    #         sum_val += num
    #     else:
    #         result.append(sum_val)
    #         sum_val = num
    #         tmp_val = num
    # if sum_val:
    #     result.append(sum_val)
    # return result

    # good
    return [sum(g) for _, g in groupby(num_list)]


if __name__ == '__main__':
    print("Example:")
    print(list(sum_consecutives([1, 1, 1, 1])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(sum_consecutives([1, 1, 1, 1])) == [4]
    assert list(sum_consecutives([1, 1, 2, 2])) == [2, 4]
    assert list(sum_consecutives([1, 1, 2, 1])) == [2, 2, 1]
    assert list(sum_consecutives([3, 3, 3, 4, 4, 5, 6, 6])) == [9, 8, 5, 12]
    assert list(sum_consecutives([1])) == [1]
    assert list(sum_consecutives([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
