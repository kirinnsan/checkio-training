def cut_sentence(line: str, length: int) -> str:
    '''
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    '''
    if len(line) <= length:
        return line
    for i in range(length, 0, -1):
        if line[i] == ' ':
            return line[:i] + '...'
    return '...'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
    assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
    assert cut_sentence("Hi my name is Alex",
                        18) == "Hi my name is Alex", "Third"
    assert cut_sentence("Hi my name is Alex",
                        20) == "Hi my name is Alex", "Fourth"
    print('Done! Do you like it? Go Check it!')
