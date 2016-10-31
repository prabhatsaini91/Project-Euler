import random
import time

start = time.time()

# test_cases = 50
nums = []


# i have started doing it this way
# this is the dumbest way i could think of doing it with
# about 8 minutes into this problem i have hit a realisation that taking word lengths might have been the better choice
# eh! well my code churns out the written number in english instead

ones = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 
		6:'six', 7:'seven', 8:'eight', 9:'nine'
		}

tens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',
		19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'
		}

hundreds_thousands = {0:'hundred', 1:'thousand'}



# while test_cases :
# 	nums.append(random.randrange(1,1000))
# 	test_cases -= 1


# taking certain flag vars here:
	# skip ones will be true for all number where the o's place has 0 face (YEAH! RHYME, BITCH)

def find_length(num) :
	skip_ones = False

	number = ''

	# i really want to avoid the overhead of a looping construct so just calculating faces in one go
	# i need to take care of so many branches someday (MENTAL NOTE: #9349203475)

	o = num%10
	if o == 0 :
		skip_ones = True

	t = num/10 % 10
	h = num/100 % 100

	th = num/1000 % 1000

	if th == 0 :
		# all numbers < 1000
		if h == 0 :
			# all numbers < 100
			number += ones[h]

		else :
			# all numbers that have a H's face != 0
			number += ones[h] + hundreds_thousands[th]

		if t == 1 :
			# has a ten's face
			# calculate with one's face and set skip_ones to true
			number += tens[t*10+o]
			skip_ones = True

		elif t == 0 :
			# no ten's face
			# skip one's face 
			number += ones[o]
			skip_ones = True

		else :
			# for all numbers having a ten's face > 1
			# need to calculate one's face so not skipping it
			number += tens[t*10]

		if skip_ones == False:
			number+=ones[o]

	else :
		number += 'onethousand'

	# print str(num) + " : " + number
	return len(number)

letter_counts = 0

# use xrange = scalp vital cpu time
for i in xrange(1,1001) :
	letter_counts = letter_counts + find_length(i)

# also since there are 99*9 "and"s they also need to be taken care of
print letter_counts + 99*9*3

# how is this so fast even after so many branches
print time.time() - start  #0.00130987167358