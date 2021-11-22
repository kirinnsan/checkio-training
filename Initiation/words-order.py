def words_order(text: str, words: list) -> bool:
    # check_index = None
    # is_result = True

    # text_list = text.split()

    # for word in words:
    #     word_index = text_list.index(word) if word in text_list else -1
    #     if word_index == -1:
    #         is_result = False
    #         break
    #     if check_index is None:
    #         check_index = word_index
    #         continue
    #     if check_index >= word_index:
    #         is_result = False
    #         break
    #     else:
    #         check_index = word_index

    # return is_result

    # good
    exist_words = [word for word in text.split() if word in words]
    return list(sorted(exist_words, key=text.index)) == words


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
