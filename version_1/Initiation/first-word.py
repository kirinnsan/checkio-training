def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    new_text = text.split()
    for target_text in new_text:
        if not target_text:
            continue
        if any([x.isalnum() for x in target_text]):
            target_text = target_text.strip('.,')
            target_text = target_text.split('.')[0].split(',')[0]
            return target_text


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
