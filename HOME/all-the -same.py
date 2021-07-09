from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # bad answer
    # if not elements or len(elements) == 1:
    #     return True
    # is_all_same = True
    # first = elements[0]
    # for element in elements:
    #     if first != element:
    #         is_all_same = False

    # return is_all_same

    # good
    # 内容表記を使ってすべての要素が条件を満たすかどうかの判定
    # allはiterableが空の場合True
    return all([element == elements[0] for element in elements])


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
