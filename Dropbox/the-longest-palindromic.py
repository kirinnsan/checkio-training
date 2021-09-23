def longest_palindromic(a):
    result = ''
    for i in range(len(a)+1):
        start_text = a[i:]
        for i in range(len(start_text)+1):
            text = start_text[0:i]
            reversed_text = text[::-1]
            if text == reversed_text and len(text) > len(result):
                result = text

    return result


if __name__ == '__main__':
    print("Example:")
    print(longest_palindromic('abc'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert longest_palindromic('abc') == 'a'
    assert longest_palindromic('abacada') == 'aba'
    assert longest_palindromic('artrartrt') == 'rtrartr'
    assert longest_palindromic('aaaaa') == 'aaaaa'
    print("Coding complete? Click 'Check' to earn cool rewards!")
