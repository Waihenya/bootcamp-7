
def sum_of_digits(A):
	'''
	Takes in a list of numbers A, 
	 and returns the sum of all the digits in the numbers.
	 e.g. [10, 20, 3, 5, 6, 23] should return 
	 1 + 0 + 2 + 0 + 3 + 5 + 6 + 2 + 3 = 22.

	'''
	total = 0

	for num in A:
		for num in str(num):
			total += int(num)
	return total

print sum_of_digits([10, 20, 3, 5, 6, 23])

'''
or


def sum_of_digits(A):
	
	Takes a list A, and returns 
	the sum of all the digits in the
	list eg. [10,30,45] should return 
	 1+0+3+4+5
	 
	total = 0
	for i in A:
	    total += i % 10
	    total += i / 10
        return total

print sum_of_digits([10,50,4,])

or 

def sum_of_digits(A):
    
    Using recursion
    Takes a list A, and returns
    the sum of all the digits in the
    list e.g. [10, 30, 45] should return
    1 + 0 + 3 + 0 + 4 + 5 = 13
    
    def sub(n):
        if n < 10:
            return n
        return sub(n % 10) + sub(n / 10)

    total = 0
    for i in A:
        total += sub(i)

    return total

print sum_of_digits([10, 205, 9])

'''




