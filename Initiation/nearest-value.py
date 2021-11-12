def nearest_value(values: set, one: int) -> int:
    # nearest = None
    # result = None
    # for value in sorted(list(values)):
    #     val = abs(value - one)
    #     if nearest is None:
    #         nearest = val
    #         result = value
    #         continue
    #     if val < nearest:
    #         nearest = val
    #         result = value
    # return result

    # best
    # min、max関数にはキーワード引数としてkeyを設定することができる。
    # これはソート時に利用される順序付けの関数を指定することができ、
    # 以下だと絶対値で比較して、値が同じならnの値で比較する
    result = min(values, key=lambda n: (abs(one - n), n))
    return result


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
