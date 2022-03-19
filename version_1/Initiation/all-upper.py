import re


def is_all_upper(text: str) -> bool:
    if not text:
        return True
    result = re.search(r"[a-zA-Z]", text)
    if not result:
        return True
    return text.isupper()


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True
    assert is_all_upper('444') == True
    assert is_all_upper('55 55 5') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")