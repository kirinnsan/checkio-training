from typing import List
# import os


def sort_by_ext(files: List[str]) -> List[str]:
    # osが使える場合
    # pair_list = [os.path.splitext(file) for file in files]
    # sorted_list = sorted(pair_list, key=lambda pair: pair[1])
    # return [root + ext for root, ext in sorted_list]

    pair_list = []
    for file in files:
        if file.startswith('.') and file.count('.') == 1:
            pair_list.append((file, ''))
            continue
        name, expand = file.rsplit('.', 1)
        pair_list.append((name, '.' + expand))
    sorted_list = sorted(pair_list, key=lambda pair: (pair[1], pair[0]))
    result_list = []
    for root, ext in sorted_list:
        if ext:
            result = root + ext
        else:
            result = root
        result_list.append(result)
    return result_list


if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == [
        '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == [
        '1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == [
        '.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == [
        '.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == [
        '1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == [
        '1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")
