def translate(text: str) -> str:
    vowels_letters = "aeiouy"

    def change_two_same_letter(word):
        """(a ⇒ aaa)"""
        result = word
        change_list = [('aaa', 'a'), ('eee', 'e'), ('iii', 'i'),
                       ('ooo', 'o'), ('uuu', 'u'), ('yyy', 'y')]
        for before, after in change_list:
            result = result.replace(before, after)
        return result

    change_text_list = []
    change_text = ''
    for word in text.split():
        for i, char in enumerate(word):
            # 対象の文字が子音の場合
            if char not in vowels_letters:
                change_text += char
                continue
            # 対象の文字の前の文字が子音の場合追加されない
            if i != 0 and word[i-1] not in vowels_letters:
                continue
            change_text += char
        # 連続する母音の変換
        change_text = change_two_same_letter(change_text)
        change_text_list.append(change_text)
        change_text = ''

    return ' '.join(change_text_list)


if __name__ == '__main__':
    print("Example:")
    print(translate('hieeelalaooo'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate('hieeelalaooo') == 'hello'
    assert translate('hoooowe yyyooouuu duoooiiine') == 'how you doin'
    assert translate('aaa bo cy da eee fe') == 'a b c d e f'
    assert translate('sooooso aaaaaaaaa') == 'sos aaa'
    print("Coding complete? Click 'Check' to earn cool rewards!")
