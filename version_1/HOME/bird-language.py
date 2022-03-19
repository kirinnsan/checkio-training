def translate(text: str) -> str:
    vowel = ["a", "i", "u", "e", "o"]
    result = ""
    is_vowel = False
    is_next_remove = False
    vowel_count = 0
    for char in text:
        if is_next_remove:
            is_next_remove = False
            continue
        if char in vowel:
            vowel_count += 1
        else:
            result += char
            is_next_remove = True


if __name__ == "__main__":
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Coding complete? Click 'Check' to earn cool rewards!")
