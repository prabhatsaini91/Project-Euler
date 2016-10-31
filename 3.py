def prime_factors(n):
	factors = []
	d = 2
	while(d*d<=n) :
		while(n>1) :            
			while n%d==0:
				factors.append(d)
				n=n/d
			d+=1
	return factors[-1]

# print prime_factors(10)

test_cases = int(raw_input(''))
while test_cases :
	num = int(raw_input(''))
	print prime_factors(num)
	test_cases-=1	

