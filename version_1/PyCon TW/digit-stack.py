from enum import Enum


class Command(Enum):
    PUSH = 1
    POP = 2
    PEEK = 3


def digit_stack(commands):

    stack = []
    total = 0
    for command in commands:
        tmp_command = command.split()
        command_name = tmp_command[0]
        if command_name == Command.PUSH.name:
            stack.append(int(tmp_command[1]))
        elif command_name == Command.POP.name and stack:
            total += stack.pop()
        elif command_name == Command.PEEK.name and stack:
            total += stack[-1]

    return total


if __name__ == '__main__':
    print("Example:")
    print(digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                       "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
