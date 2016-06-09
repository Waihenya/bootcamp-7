def sum_of_unique_digits(A):
	'''
	 Takes in a list of numbers A, and returns the sum of all the unique digits in the numbers.
	 e.g. [10, 20, 3, 5, 6, 23] should return 1 + 0 + 2 + 3 + 5 + 6 = 17.

	'''
	my_list = []
	
	total = 0

	for x in A:

		split_numbers = [c for c in str(x)]

		my_list.extend(split_numbers)

	for y in set(my_list):
		total += int(y)
	return total


print sum_of_unique_digits([10,20,3,5,6,23])