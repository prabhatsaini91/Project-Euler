import time
from math import floor

## There's a particular algorithm known as Gauss's algo to determine day of the week
## It goes like this

	#*****************************************************************
	#                                                                *
	#	w = (d + floor(2.6*m-0.2)+y+floor(y/4)+floor(c/4)-2*c) mod7  *
	#                                                                *
	#*****************************************************************

	# The terminology goes as follows :
		## Y = year - 1 for Jan and Feb, same for others
		## d = day of the month (range(1,31))
		## m = month is shifted circulary so that March = 1 and Februray = 12
		