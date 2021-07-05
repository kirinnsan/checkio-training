def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    begin_index = text.find(begin)
    end_index = text.find(end)
    if begin_index == -1 and end_index == -1:
        return text
    elif end_index != -1 and begin_index > end_index:
        return ''

    result = ''
    if begin_index == -1:
        result = text.split(end)[0]
    elif end_index == -1:
        result = text.split(begin)[-1]
    else:
        result = text.split(begin)[-1].split(end)[0]

    return result


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers(
        'No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
