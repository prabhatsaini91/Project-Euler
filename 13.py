# easy peasy
# python handles large numbers quite efficiently

import time
start = time.time()

sum = 0

file = open("13 numbers","r")
for line in file :
	long_num = int(line)
	sum = sum + long_num

print sum

print (time.time() - start)  # 0.000333070755005