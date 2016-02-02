#!/usr/bin/python
def count_words(text, words):
	rez = 0
	for x in words:
		if x in text.lower():
			rez += 1
	return rez

def find_message(text):
    """Find a secret message"""
    rez = ""
    for x in text:
        if x.isupper():
            rez += x
            print rez
    return rez

print find_message("How are you? Eh, ok. Low or Lower? Ohhh.")
text = "How are you? Eh, ok. Low or Lower? Ohhh."
new = ''.join(c for c in text if c.isupper())
print new