def threedprinter():
	n = int(input())
	
	k = n // 2
	d = 0
	
	p = 1
	while p <= k:
		p += p
		d += 1
	

	s = 0
	while s < n:
		s += p
		d += 1
	return d
	
print(threedprinter())