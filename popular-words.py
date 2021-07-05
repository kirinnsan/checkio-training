def popular_words(text: str, words: list) -> dict:
    # your code here
    d = {}
    text_words = [x.lower() for x in text.split()]
    for word in words:
        d[word] = text_words.count(word)
    return d


if __name__ == '__main__':
    print("Example:")
    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
      When I was One
      I had just begun
      When I was Two
      I was nearly new
    ''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
