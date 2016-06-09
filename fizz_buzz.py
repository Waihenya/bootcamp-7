def fizz_buzz(num):
	'''
	 Takes a number:
	  if divisible by 3 return fizz,
	  if divisible by 5 return buzz,
	  if divisible by both 3 and 5 return fizz_buzz
	  if not divible by either 3,5,and 15. return number

	'''
	if num % 15 == 0:
		return "fizz_buzz"
	elif num % 5 == 0:
		return "buzz"
	elif num % 3 == 0:
		return "fizz"
	else:
		return num


print fizz_buzz(45)
print fizz_buzz(1001)
print fizz_buzz(3)
print fizz_buzz(105)
print fizz_buzz(99)