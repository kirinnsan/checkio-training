import re


def checkio(text: str, words: str) -> str:
    result = ''
    for word in words.split():
        # IGNORECASEで大文字小文字を区別しない
        r = re.compile(word, re.IGNORECASE)
        target = r.match(text).group()
        # 正規表現で置換
        result = re.sub(r, f'<span>{target}</span>', text)

    return result


print("Example:")
print(checkio("This is only a text example for task example.", "example"))

assert (
    checkio("This is only a text example for task example.", "example")
    == "This is only a text <span>example</span> for task <span>example</span>."
)
assert (
    checkio("Python is a widely used high-level programming language.", "pyThoN")
    == "<span>Python</span> is a widely used high-level programming language."
)
assert (
    checkio("It is experiment for control groups with similar distributions.", "is im")
    == "It <span>is</span> exper<span>im</span>ent for control groups with s<span>im</span>ilar d<span>is</span>tributions."
)
assert (
    checkio("The National Aeronautics and Space Administration (NASA).", "nasa  THE")
    == "<span>The</span> National Aeronautics and Space Administration (<span>NASA</span>)."
)
assert checkio("Did you find anything?",
               "word space tree") == "Did you find anything?"
assert (
    checkio("Hello World! Or LOL", "hell world or lo")
    == "<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L"
)

print("The mission is done! Click 'Check' to earn cool rewards!")
