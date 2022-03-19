from collections import Counter


def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    check_str_lis = [line[0:index+1] for index, char in enumerate(line)]
    result_length = 0
    temp_str = ''
    for char in line:
        if not char:
            temp_str = char
            continue

    return result_length


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')
