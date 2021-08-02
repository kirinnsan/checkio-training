def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    # TODO itertools.groupbyが便利そう
    if not line:
        return 0

    repeat_count_dict = {}
    last_char = ''
    for char in line:
        if char not in repeat_count_dict:
            repeat_count_dict[char] = 1
        if char == last_char:
            repeat_count_dict[char] += 1
        last_char = char

    return max(repeat_count_dict.values())


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
