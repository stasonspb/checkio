def check_pangram(text):
	alphabet = set('abcdefjhigklmnopqrstuvwxyz')
    text2 = [x for x in text.lower() if x.isalpha()]
    return set(text2) == alphabet

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
