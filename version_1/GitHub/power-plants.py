from typing import Set, Tuple, List, Dict


def power_plants(network: Set[Tuple[str, str]], ranges: List[int]) -> Dict[str, int]:
    nerworks = []
    for n in network:
        nerworks.extend(list(n))
    result_dict = {}
    for r in ranges:
        r

if __name__ == '__main__':
    assert power_plants({('A', 'B'), ('B', 'C')}, [1]) == {'B': 1}
    assert power_plants(
        {('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')}, [2]) == {'C': 2}
    assert power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'),
                         ('D', 'E'), ('E', 'F')}, [1, 1]) == {'B': 1, 'E': 1}
    assert power_plants({('A', 'B'), ('B', 'C'), ('A', 'D'), ('B', 'E')}, [
                        1, 0]) == {'B': 1, 'D': 0}

    print('The local tests are done. Click on "Check" for more real tests.')
