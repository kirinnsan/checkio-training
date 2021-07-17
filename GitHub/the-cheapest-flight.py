from typing import List


def cheapest_flight(costs: List, a: str, b: str) -> int:
    # 直通パターン
    direct_cost = None
    for cost in costs:
        if a in cost and b in cost:
            if direct_cost is None or cost[2] < direct_cost:
                direct_cost = cost[2]
    # 間接パターン
    indirect_cost = None
    # 経由値をキーに、valueに合計値をlist持つ
    via_dict = {}
    for cost in costs:
        if a in cost and b in cost:
            continue
        if a in cost:
            via_index = 1 if cost.index(a) == 0 else 0
            via_value_with_a = cost[via_index]
            if via_value_with_a not in via_dict:
                via_dict[via_value_with_a] = []
            via_dict[via_value_with_a].append(cost[2])
        if b in cost:
            via_index = 1 if cost.index(b) == 0 else 0
            via_value_with_b = cost[via_index]
            if via_value_with_b not in via_dict:
                via_dict[via_value_with_b] = []
            via_dict[via_value_with_b].append(cost[2])

    if via_dict:
        for v in via_dict.values():
            if len(v) != 2:
                continue
            total = sum(v)
            if indirect_cost is None or total < indirect_cost:
                indirect_cost = total

    if direct_cost is None and indirect_cost is None:
        return 0
    elif direct_cost is not None and indirect_cost is None:
        return direct_cost
    elif direct_cost is None and indirect_cost is not None:
        return indirect_cost
    elif direct_cost < indirect_cost:
        return direct_cost
    else:
        return indirect_cost


if __name__ == '__main__':
    print("Example:")
    print(cheapest_flight([['A', 'C', 100],
                           ['A', 'B', 20],
                           ['B', 'C', 50]],
                          'A',
                          'C'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert cheapest_flight([['A', 'C', 100],
                            ['A', 'B', 20],
                            ['B', 'C', 50]],
                           'A',
                           'C') == 70
    assert cheapest_flight([['A', 'C', 100],
                            ['A', 'B', 20],
                            ['B', 'C', 50]],
                           'C',
                           'A') == 70
    assert cheapest_flight([['A', 'C', 40],
                            ['A', 'B', 20],
                            ['A', 'D', 20],
                            ['B', 'C', 50],
                            ['D', 'C', 70]],
                           'D',
                           'C') == 60
    assert cheapest_flight([['A', 'C', 100],
                            ['A', 'B', 20],
                            ['D', 'F', 900]],
                           'A',
                           'F') == 0
    assert cheapest_flight([['A', 'B', 10],
                            ['A', 'C', 15],
                            ['B', 'D', 15],
                            ['C', 'D', 10]],
                           'A',
                           'D') == 25
    print("Coding complete? Click 'Check' to earn cool rewards!")
