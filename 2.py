num1 = 1
num2 = 2
sum = 0

while(num1+num2 < 4000000) :
	temp = num1+num2
	num1 = num2
	num2 = temp
	if(num2 % 2==0) :
		sum = sum + num2
print sum + 2
