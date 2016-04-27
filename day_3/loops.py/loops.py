a = [10,40,-9, 45,60,89]
print a
for i in a:
#print list
	print i

#print in reverse
 
'''
	 i = len(a)

	 while i > 0:
	 	print a[i-1]
	 	i-=1

	for x in range(len(a)) -1, -1, -1)	
	    print a[x]
 
'''
b = [(2,4),(5,10),(6,20),(50,50)]

'''
     x:2 , y:4
     x:5 , y:10

'''
for m in b:
	print " x: {} , y: {} ".format(*m)
	   
f = [(10,20,40),(10,40),(4,5,50)]

'''
    a:10, b: 20, c:40
    a:10, b:40
    a:4,  b:5,   c:50
'''
'''
for x in f:
	if  x==2:
		print "a:{}, b: {}".format(*x)
		
	else:
		print " a: {}, b: {}, c: {}".format(*x)
		
'''
def super_sum(*args):
	'''
	Takes in variable number of items,
	and returns the sum.
	e.g super_sum(10,20) = 30
	    super_sum(10,20,40) = 70
	    super_sum(1,4,5,6,7) = 23

	'''
	total = 0
	for i in args:
		total += i
	return total

print super_sum(10,20)
print super_sum(1,4,5,7,3,2,7,6,8)
a = [10,40,60]
print super_sum(*a)

def hello_again(**kwargs):
	'''
	'''
	return "I am {}, {} years old and I am a {}".format(kwargs['name'],kwargs['age'],kwargs['position'])

print hello_again(name='Naomi',age=20 ,position='Banker')

print hello_again(age=29, name='Julie',position='Accountant')



Joe = {'name':'Joe','age':98,'position':'Teacher'}

print hello_again(**Joe)

print hello_again(name='Kim',age=16 ,position='Banker')

