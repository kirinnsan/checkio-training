def is_acceptable_password(text: str) -> bool:
    if len(text) < 6:
        return False
    if len(text) < 9:
        if not [i for i in text if i.isdigit()]:
            return False
        if all([i.isdigit() for i in text]):
            return False
    return True


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
