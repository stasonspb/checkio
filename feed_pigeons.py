def checkio(number):
	t = pig = 1
	new_pig = [0]
	while number - (pig + new_pig[t-1]) >= 0:
		number -= (pig + new_pig[t-1])
		pig += new_pig[t-1]
		t += 1
		new_pig.append(t)

	return max(pig, number)

#if __name__ == '__main__':
#    #These "asserts" using only for self-checking and not necessary for auto-testing
#    assert checkio(1) == 1, "1st example"
#    assert checkio(2) == 1, "2nd example"
#    assert checkio(5) == 3, "3rd example"
#    assert checkio(10) == 6, "4th example"