def sum_digits(A):
	'''
	Takes a list A, and returns 
	the sum of all the digits in the
	list eg. [10,30,45] should return 
	 1+0+3+4+5
	 '''
	sum = 0
	for i in A:
	    sum += i % 10
	    sum += i / 10
        return sum

print sum_digits([1,5,4,6,10])


