def yaml(a):
    yaml_list = [text for text in a.splitlines() if text]
    result_dict = {}
    for yaml in yaml_list:
        key, value = yaml.split(':')
        value = value.strip()
        # 値が未設定
        if not value:
            value = None
            result_dict[key] = value
            continue
        # 値が文字列の"null"
        elif value == '"null"':
            value = "null"
            result_dict[key] = value
            continue
        # 文字列の先頭と末尾の"を取り除く
        value = value[1:] if value[0] == '"' else value
        value = value[:-1] if value[-1] == '"' else value
        # 不要な値を取り除く
        value = value.replace('\\', '')
        # 値が数値の場合
        if value.isdecimal():
            value = int(value)
        # 真偽値の場合
        elif value == 'false':
            value = False
        elif value == 'true':
            value = True
        # 値がnullの場合
        elif value == 'null':
            value = None
        result_dict[key] = value
    return result_dict


if __name__ == '__main__':
    print("Example:")
    print(yaml('name: Alex\nage: 12'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    assert yaml('name: Alex Fox\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex Fox'}
    assert yaml('name: "Alex Fox"\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex Fox'}
    assert yaml('name: "Alex \\"Fox\\""\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex "Fox"'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'alive: false') == {'alive': False,
                                    'children': 6,
                                    'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding:') == {'children': 6,
                               'coding': None,
                               'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding: null') == {'children': 6,
                                    'coding': None,
                                    'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding: "null" ') == {'children': 6,
                                       'coding': 'null',
                                       'name': 'Bob Dylan'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
