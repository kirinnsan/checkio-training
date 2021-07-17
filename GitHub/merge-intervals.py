def merge_intervals(intervals):
    """
        Merge overlapped intervals.
    """

    if not intervals:
        return intervals

    result = [intervals[0]]
    for interval in intervals:
        target_val = result[-1]
        # 対象の区間が間に収まる場合
        if interval[0] >= target_val[0] and interval[1] <= target_val[1]:
            continue
        # 対象の区間が交差しない　かつ　新しい区間に統合される場合
        elif interval[0] > target_val[1] and (interval[0] - target_val[1] == 1):
            del result[-1]
            result.append((target_val[0], interval[1]))
        # 対象の区間が交差している　かつ　新しい区間に統合される場合
        elif interval[0] <= target_val[1] and interval[1] >= target_val[1]:
            del result[-1]
            result.append((target_val[0], interval[1]))
        # 対象の区間が交差しない場合
        elif interval[0] > target_val[1]:
            result.append(interval)

    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [
        (1, 6), (8, 10), (12, 19)], "target_val"
    assert merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)], "Second"
    assert merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [
        (1, 15), (17, 20)], "Third"
    print('Done! Go ahead and Check IT')
