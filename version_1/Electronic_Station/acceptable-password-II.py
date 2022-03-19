def is_acceptable_password(password: str) -> bool:

    is_valid = True
    if len(password) <= 6:
        is_valid = False
        return is_valid
    is_valid = any([char.isdigit() for char in password])
    return is_valid


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
