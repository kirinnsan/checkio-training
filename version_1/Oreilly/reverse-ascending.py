def reverse_ascending(items):
    sub_list = []
    currnet = None
    l = []
    for item in items:
        if currnet is None:
            currnet = item
        if item > currnet:
            l.append(item)
        else:
            sub_list.append(l)
            l = []
            l.append(item)
        currnet = item
    if l:
        sub_list.append(l)
    reverse_ascending_list = []
    for sub in sub_list:
        reverse_ascending_list.extend(sorted(sub, reverse=True))
    return reverse_ascending_list


if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
        10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
