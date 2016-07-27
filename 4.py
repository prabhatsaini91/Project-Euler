def generate_nums() :
	for i in range(1,1000) :
		for j in range(110,991,11) :
			yield i*j
			
def check_palindrome(num) :
	return str(num) == str(num)[::-1]
	
largest = 0;
for num in generate_nums() :
	if check_palindrome(num) and largest < num :
		largest = num
print largest
