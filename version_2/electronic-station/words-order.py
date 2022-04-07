def words_order(text: str, words: list) -> bool:
    split_text = text.split()
    current_index = None
    for word in words:
        if word not in split_text:
            return False
        if current_index is None:
            current_index = split_text.index(word)
            continue
        if current_index >= split_text.index(word):
            return False
        current_index = split_text.index(word)

    if current_index is None:
        return False

    return True

    # better
    # 含まれた単語をフィルタリングして元の順でソートした方が簡単
    # text_words = {w for w in text.split() if w in words}
    # return list(sorted(text_words, key=text.index)) == words


if __name__ == "__main__":
    print("Example:")
    print(words_order("hi world im here", ["world", "here"]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order("hi world im here", ["world", "here"]) == True
    assert words_order("hi world im here", ["here", "world"]) == False
    assert words_order("hi world im here", ["world"]) == True
    assert words_order("hi world im here", ["world", "here", "hi"]) == False
    assert words_order("hi world im here", ["world", "im", "here"]) == True
    assert words_order("hi world im here", ["world", "hi", "here"]) == False
    assert words_order("hi world im here", ["world", "world"]) == False
    assert words_order("hi world im here", ["country", "world"]) == False
    assert words_order("hi world im here", ["wo", "rld"]) == False
    assert words_order("", ["world", "here"]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
