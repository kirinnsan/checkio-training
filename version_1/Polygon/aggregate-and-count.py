def aggregate_and_count(items: list) -> dict:
    result_dict = {}
    for item in items:
        key, value = item
        if key not in result_dict:
            result_dict[key] = 0
        result_dict[key] += value
    return result_dict


print("Example:")
print(aggregate_and_count([["a", 1], ["b", 2], ["c", 3], ["a", 5]]))

assert aggregate_and_count([["a", 1], ["b", 2]]) == {"a": 1, "b": 2}
assert aggregate_and_count([["a", 1], ["a", 2]]) == {"a": 3}
assert aggregate_and_count([["a", 1], ["b", 2], ["c", 3], ["a", 5]]) == {
    "a": 6,
    "b": 2,
    "c": 3,
}
assert aggregate_and_count([["a", 1]]) == {"a": 1}

print("The aggregation is done! Click 'Check' to earn cool rewards!")
