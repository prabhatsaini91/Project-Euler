def calculate_hcf(a,b) :
	while(b) :
		a,b = b, a%b
	return a
	
def calculate_lcm(a,b) :
	return a*b / calculate_hcf(a,b)

##print lcm(4,18)

lcm = 1
for i in range(1,21) :
	lcm = calculate_lcm(i,lcm)

print lcm


	
