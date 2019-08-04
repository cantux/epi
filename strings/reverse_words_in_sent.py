def rev_words(text):
    words = text.split(' ')
    rev_words = []
    for w in words:
        rev_words.append(w[::-1])

    return ' '.join(rev_words)[::-1]

def test():
    assert 1 == 1
    assert rev_words('alice likes bob') == 'bob likes alice'

if __name__ == "__main__":
    test()
