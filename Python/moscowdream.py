def moscowdream():
	a, b, c, n = [int(x) for x in input().split()]
	return "YES" if n >= 3 and a >= 1 and b >= 1 and c >= 1 and (a + b + c) >= n else "NO"
		
print(moscowdream())
