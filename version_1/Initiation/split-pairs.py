def split_pairs(a):
    # index = 0
    # result = []
    # while True:
    #     if index >= len(a):
    #         if result and len(result[-1]) == 1:
    #             result[-1] = result[-1] + '_'
    #         break
    #     result.append(a[index:index+2])
    #     index += 2

    # return result

    # good
    a += '_' * (len(a) % 2)
    result = [a[i:i+2] for i in range(0, len(a), 2)]
    return result


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
