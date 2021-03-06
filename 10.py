import time


# copied sieve code from problem number 7
# takes about 3 seconds


# def sieve_of_eratosthenes() :
# 	D = {}
# 	q = 2
# 	while 1 :
# 		if q not in D :
# 			yield q
# 			D[q*q] = [q]
# 		else :
# 			for p in D[q] :
# 				D.setdefault(p+q,[]).append(p)
# 			del D[q]
# 		q+=1
# i = 1

# start = time.time()
# sum_of_primes = 0

# for num in sieve_of_eratosthenes() :
# 	print str(num) + '---'
# 	if num < 2000000 :
# 		sum_of_primes = sum_of_primes + num
# 	else :
# 		break



# print sum_of_primes
# time_elapsed = time.time() - start
# print time_elapsed


# optimised earlier sieve to work faster
# code now running in less than 1 second


def sumPrimes(n):
    sum, sieve = 0, [True] * n
    for p in xrange(2, n):	# using xrange() instead of range
        if sieve[p]:
            sum += p
            for i in xrange(p*p, n, p):	# used xrange here as well optimised by 20% more
                sieve[i] = False
    return sum

# start = time.time()


print sumPrimes(2000000)


# time_elapsed = time.time() - start
# print time_elapsed
