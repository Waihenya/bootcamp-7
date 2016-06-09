def factorial(n):

	'''
	 Takes a number/ argument and returns its factorial
	 e.g factorial(4)= [4*3*2*1] = 24

	'''
	if n < 0:
		print 'Factorial does not exist for negative numbers'
	elif n == 1 or n == 0:
		return 1
	else:
		return n * factorial(n-1)

print factorial(4)
print factorial(6)
print factorial(0)
print factorial(-8)


