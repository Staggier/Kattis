def leftbeehind():
	while True:
		n, k = [int(x) for x in input().split()]
		
		if n == 0 and k == 0:
			return
		
		if n + k == 13:
			print("Never speak again.")
		elif n == k:
			print("Undecided.")
		elif n > k:
			print("To the convention.")
		else:
			print("Left beehind.")
			
leftbeehind()
