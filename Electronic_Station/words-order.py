def words_order(text: str, words: list) -> bool:
    check_word_list = text.split(' ')
    index_list = []
    for word in words:
        try:
            index_list.append(check_word_list.index(word))
        except Exception:
            return False
    is_ordered = all([i < j for i, j in zip(index_list, index_list[1:])])
    return is_ordered


if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here',
                       ['world', 'here', 'hi']) == False
    assert words_order('hi world im here',
                       ['world', 'im', 'here']) == True
    assert words_order('hi world im here',
                       ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here',
                       ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
