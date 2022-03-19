from typing import Tuple


def follow(instructions: str) -> Tuple[int, int]:
    result = [0, 0]
    for instruction in instructions:
        if instruction == 'f':
            result[1] += 1
        elif instruction == 'b':
            result[1] += -1
        elif instruction == 'l':
            result[0] -= 1
        elif instruction == 'r':
            result[0] += 1
    return tuple(result)


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
