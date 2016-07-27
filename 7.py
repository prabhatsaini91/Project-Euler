def sieve_of_eratosthenes() :
	D = {}
	q = 2
	while 1 :
		if q not in D :
			yield q
			D[q*q] = [q]
		else :
			for p in D[q] :
				D.setdefault(p+q,[]).append(p)
			del D[q]
		
		q+=1

i = 1

for num in sieve_of_eratosthenes() :
		print num
		i = i + 1
		if i>10001 :
			break



