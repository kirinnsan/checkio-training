def is_all_upper(text: str) -> bool:
    # text = text.replace(" ", "")
    # if not text or not any([i.isalpha() for i in text]):
    #     return False
    # return all([i.isupper() for i in text if i.isalpha()])

    # better
    return text.replace(" ", "").isupper()


if __name__ == "__main__":
    print("Example:")
    print(is_all_upper("ALL UPPER"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper("ALL UPPER") == True
    assert is_all_upper("all lower") == False
    assert is_all_upper("mixed UPPER and lower") == False
    assert is_all_upper("") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
