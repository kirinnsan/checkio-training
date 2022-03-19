def checkio(line1: str, line2: str) -> str:
    # 共通する項目を探すのでsetを使う
    common_word = set(line1.split(',')).intersection(line2.split(','))
    return ','.join(sorted(list(common_word)))


if __name__ == '__main__':
    print("Example:")
    print(checkio('hello,world', 'hello,earth'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three',
                   'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")
