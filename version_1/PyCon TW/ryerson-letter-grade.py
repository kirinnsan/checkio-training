
TABLE = {
    "A+": (90, 150),
    "A": (85, 89),
    "A-":  (80, 84),
    "B+": (77, 79),
    "B": (73, 76),
    "B-":  (70, 72),
    "C+":  (67, 69),
    "C": (63, 66),
    "C-":  (60, 62),
    "D+":  (57, 59),
    "D": (53, 56),
    "D-":  (50, 52),
    "F": (0, 49),
}


def ryerson_letter_grade(pct: int) -> str:
    grade = ''
    for k, v in TABLE.items():
        if v[0] <= pct and v[1] >= pct:
            grade = k
            break
    return grade


if __name__ == '__main__':
    print("Example:")
    print(ryerson_letter_grade(45))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert ryerson_letter_grade(45) == "F"
    assert ryerson_letter_grade(62) == "C-"
    print("Coding complete? Click 'Check' to earn cool rewards!")
