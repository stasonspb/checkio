def f(n):
	a = 1
	for i in range(2, n):
		a *= i - 1
		if (a+1) % i == 0:
			yield i

def golf(n):
	for i in f(100000):
		if str(i)[::-1] == str(i) and i > n:
			return i