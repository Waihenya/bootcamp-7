def binary_gap(number):
	gap = 0
	count = 0

	b = []

	while number > 0:
		 x = number % 2 

		 b.append(x)

		 number = number/2

	for i in b:
		if i == 0:
			gap += i
		elif i == 1:
			gap = 0
				
		elif gap > count :
			 count = gap
			 gap = 0

	return count

print binary_gap(46)

		  	 







