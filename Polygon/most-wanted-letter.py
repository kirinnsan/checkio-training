from collections import Counter


def most_wanted(text: str) -> str:

    text = [w.lower() for w in text if w.isalpha()]
    c = Counter(text)
    key_list = []
    most_counter = 0
    for key, value in c.most_common():
        if key not in key_list and value >= most_counter:
            most_counter = value
            key_list.append(key)
    return key_list


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sorted(most_wanted("Hello World!")) == ["l"], "Hello test"
    assert sorted(most_wanted("How do you do?")) == ["o"], "O is most wanted"
    assert sorted(most_wanted("One")) == [
        "e", "n", "o"], "All letter only once."
    assert sorted(most_wanted("Oops!")) == [
        "o"], "Don't forget about lower case."
    assert sorted(most_wanted("AAaooo!!!!")) == ["a", "o"], "Only letters."
    assert sorted(most_wanted("abe")) == ["a", "b", "e"], "The First."
    print("Start the long test")
    assert sorted(most_wanted("a" * 9000 + "b" * 1000)) == ["a"], "Long."
    print("The local tests are done.")
