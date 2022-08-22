from typing import Tuple


def follow(instructions: str) -> Tuple[int, int]:
    x = 0
    y = 0
    for data in instructions:
        if data == "f":
            y += 1
        elif data == "b":
            y += -1
        elif data == "r":
            x += 1
        elif data == "l":
            x += -1
        else:
            pass

    return (x, y)


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
