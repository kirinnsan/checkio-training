def to_camel_case(name: str) -> str:
    # upper_list_index = [index + 1 for index,
    #                     char in enumerate(name) if char == '_']
    # upper_list_index.insert(0, 0)
    # result = ''
    # for i, char in enumerate(name):
    #     if i in upper_list_index:
    #         char = char.upper()
    #     result += char
    # result = result.replace('_', '')
    # return result

    # 別解
    return ''.join([word.capitalize() for word in name.split('_')])

if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
