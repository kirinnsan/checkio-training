def yaml(a):
    yaml_list = [text for text in a.splitlines() if text]
    result_dict = {}
    for yaml in yaml_list:
        key, value = yaml.split(': ')
        # 値が数値の場合
        if value.isdecimal():
            value = int(value)
        result_dict[key] = value
    return result_dict


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
                   'class': '12b',
                   'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
