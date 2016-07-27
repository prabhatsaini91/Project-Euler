def sum_to_n_terms(n) :
	return (n*(n+1))/2

def sum_to_n_squared_terms(n) :
	return (n*(n+1)*(2*n+1))/6

print pow(sum_to_n_terms(100),2) - sum_to_n_squared_terms(100)
