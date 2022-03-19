def is_majority(items: list) -> bool:
    # your code here
    # 1.first
    true_count = items.count(True)
    false_count = items.count(False)
    if true_count > false_count:
        return True
    else:
        return False
    # もっと短く書ける
    # return items.count(True) > items.count(False)


if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
