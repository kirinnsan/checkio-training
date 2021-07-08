def frequency_sort(items):
    # 1.
    # 出現回数で降順ソートして、indexの順番で昇順ソート
    # keyに複数条件を設定する
    return sorted(items, key=lambda item: (-items.count(item), items.index(item)))
    # 2.
    # result = sorted(items, key=items.index)
    # return sorted(result, key=items.count, reverse=True)


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [
        4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == [
        'bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
