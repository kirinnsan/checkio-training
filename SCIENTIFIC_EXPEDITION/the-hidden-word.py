from itertools import zip_longest


def checkio(text, word):
    text = text.lower()
    word = word.lower()
    text_list = text.replace(' ', '').split('\n')
    # 行に含まれるパターン
    for index, row in enumerate(text_list, 1):
        if word in row:
            start_index = row.index(word) + 1
            end_index = start_index + len(word) - 1
            return [index, start_index, index, end_index]
    # 列に含まれるパターン
    for index, column in enumerate(zip_longest(*text_list), 1):
        check_row = ''.join([x for x in column if x])
        if word in check_row:
            start_index = check_row.index(word) + 1
            end_index = start_index + len(word) - 1
            return [start_index, index, end_index, index]

    return []


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
checkio("xa\nxb\nx", "ab")
print("Coding complete? Click 'Check' to earn cool rewards!")
