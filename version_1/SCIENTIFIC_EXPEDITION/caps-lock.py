def caps_lock(text: str) -> str:

    result = ''
    is_char_upper = False
    for char in text:
        if char == 'a':
            is_char_upper = not is_char_upper
            continue
        if is_char_upper:
            char = char.upper()
        result += char
    return result


if __name__ == '__main__':
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock(
        "Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock(
        "Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    print("Coding complete? Click 'Check' to earn cool rewards!")
