import time

# this is easy
# get the number in long, convert to string, use comprehension
# and iterate over each number to get the sum of digits

# start = time.time()

# AVOID MAGIC NUMBERS
base = 2
exponent = 1000

digit_list = list(str(base**exponent))

sum_of_digits = sum([int(d) for d in digit_list])
print sum_of_digits

# print time.time() - start // 0.000197887420654 ;)

