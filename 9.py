# import time

# start = time.time()

# a + b + c = 1000 => 1
# c = a - b - 1000 //reduces iterating c from(1,1000)
# (a + b + c)^2 = 1000^2
# a^2 + b^2 + c^2 + 2ab + 2bc + 2ac = 1000^2
# 2c^2 + 2ab + 2bc + 2ab = 1000^2 : refer 1
# c(a + b + c) + ab = 500000 // divide both sides by 2
# the above statement becomes a subsitute for the traditional pythagorean triplet check: refer 2
   

for a in range(1, 1000) :
	for b in range(a, 1000 - a) :
		c = 1000 - a - b
		## 2 => if a * a + b * b == c * c :  //this particular if condition is slow 0.128
		if a * b + 1000 * c == 500000   ##this is faster: 0.098
			print a, b, c
			print a * b * c

# time_elapsed = time.time() - start
# print time_elapsed