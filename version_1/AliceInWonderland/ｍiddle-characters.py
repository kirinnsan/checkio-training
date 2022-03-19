def middle(text):
    middle_index = len(text) // 2
    if len(text) % 2 == 0:
        result = text[middle_index-1:middle_index + 1]
    else:
        result = text[middle_index]
    return result


if __name__ == '__main__':
    print("Example:")
    print(middle('example'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert middle('example') == 'm'
    assert middle('test') == 'es'
    assert middle('very-very long sentence') == 'o'
    assert middle('I') == 'I'
    assert middle('no') == 'no'
    print("Coding complete? Click 'Check' to earn cool rewards!")
