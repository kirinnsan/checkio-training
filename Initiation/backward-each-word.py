def backward_string_by_word(text: str) -> str:
    # word_list = []
    # now_word = ''
    # for x in text:
    #     if x == ' ':
    #         word_list.append(now_word)
    #         word_list.append(x)
    #         now_word = ''
    #         continue
    #     now_word += x

    # if now_word:
    #     word_list.append(now_word)

    # result = [x[::-1] for x in word_list]
    # result = ''.join(result)
    # return result

    # good
    return " ".join(word[::-1] for word in text.split(" "))


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
