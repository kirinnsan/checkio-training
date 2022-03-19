def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    range_list = []
    start_number = None
    end_number = None
    for d in data:
        if start_number is None:
            start_number = d
            end_number = d
            continue
        if d - 1 == end_number:
            end_number = d
        elif d > end_number:
            range_list.append((start_number, end_number))
            start_number = d
            end_number = d
        else:
            pass
    if start_number is None:
        return data
    elif start_number == end_number:
        range_list.append((start_number, end_number))
    else:
        range_list.append((start_number, end_number))
    return iter(range_list)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    res = create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))
    assert hasattr(
        res, '__iter__'), "your function should return the iterator object"
    assert hasattr(
        res, '__next__'), "your function should return the iterator object"

    assert list(create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))) == [
        (1, 5), (7, 8), (12, 12)], "First"
    assert list(create_intervals(iter(sorted(list({1, 2, 3, 6, 7, 8, 4, 5}))))) == [
        (1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
