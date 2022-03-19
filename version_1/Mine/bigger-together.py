from typing import List


def bigger_together(ints: List[int]) -> int:
    """
        Returns difference between the largest and smallest values
        that can be obtained by concatenating the integers together.
    """
    str_list = [str(i) for i in ints]
    str_max_list = sorted(str_list, reverse=True)
    str_min_list = sorted(str_list)
    return int(''.join(str_max_list)) - int(''.join(str_min_list))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert bigger_together([1, 2, 3, 4]) == 3087, "4321 - 1234"
    assert bigger_together([1, 2, 3, 4, 11, 12]
                           ) == 32099877, "43212111 - 11112234"
    assert bigger_together([0, 1]) == 9, "10 - 01"
    assert bigger_together([100]) == 0, "100 - 100"
    print('Done! I feel like you good enough to click Check')
