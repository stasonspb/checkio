import re

def find_word(message):
	p = re.compile('\w+')
	message = p.findall(message.lower())
	rez = []
	for i, word in enumerate(message):
		rez.append(map(lambda x: check_words(word,x), message))
	sums = (map(lambda x: (sum(x)-100), zip(*rez)))
	sums = sums[::-1]
	return message[::-1][sums.index(max(sums))]

def check_words(word1, word2):
	score = 0
	score += 10 if word1[0] == word2[0] else 0
	score += 10 if word1[len(word1)-1] == word2[len(word2)-1] else 0
	score += float(len(word1)) / float(len(word2)) * 30 if len(word1) <= len(word2) else float(len(word2)) / float(len(word1)) * 30
	score += float(len(set(word1) & set(word2))) / float(len((set(word1)) | (set(word2)))) * 50
	return score

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word(u"Speak friend and enter.") == "friend", "Friend"
    assert find_word(u"Beard and Bread") == "bread", "Bread is Beard"
    assert find_word(u"The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     u"I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word(u"Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     u" According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word(u"One, two, two, three, three, three.") == "three", "Repeating"
