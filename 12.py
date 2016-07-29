# fucking optimise this shit

from collections import Counter
import time

start = time.time()


# i have to use a sieve here instead of this function
def generate_prime_factors(num) :
	factors = []
	d = 2
	while d*d<=num :
		while(num > 1) :
			while num % d == 0 :
				factors.append(d)
				num = num / d

			d+=1

	return factors

# this is good
def number_of_factors(factors) :
	num_of_factors = 1

	# using collections in an algorithmic approach. DIE SCUM!
	counts = Counter(factors)
	for key in counts :

		# why? because the powers of the prime factors when added by 1 and then multiplied gives the number of factors
		# if only i knew how to play with numbers... could have saved loads of time!
		num_of_factors = num_of_factors * (counts[key] + 1) 

	return num_of_factors


n = 1

# infinite loop! REALLY!!
while True :
	num = (n*(n+1)) / 2
	factors = generate_prime_factors(num)
	print factors
	if number_of_factors(factors) > 500 :
		print num
		break
	n+=1

print time.time() - start


# OPTIMISE OPTIMISE OPTIMISE