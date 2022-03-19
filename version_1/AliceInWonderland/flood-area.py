from typing import Iterable


def flood_area(diagram: str) -> Iterable[int]:
    depth = 0
    down_count = 0
    up_count = 0
    for char in diagram:
        if char == '\\':
            depth += 1
            down_count += 1
        elif char == '//':
            up_count += 1
        elif char == '_'
        


def calculate():
    pass

if __name__ == '__main__':
    print("Example:")
    print(list(flood_area(r'\\//')))
    assert list(flood_area(r'\\//')) == [4], 'valley'
    assert list(flood_area(r'/\\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/')
                ) == [4, 2, 1, 19, 9], 'mountains'
    assert list(flood_area(r'_/_\_')) == [], 'hill'

    print("Coding complete? Click 'Check' to earn cool rewards!")
