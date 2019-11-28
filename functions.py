def name():
	print("My name is Raju")
name()

def name1():
	return("My name is Raju1")
v = name1()
print(v)

a = list(range(10,20,5))
print(a)	


def addParameters(a,b,c,):
	return a+b+c

print(addParameters(10,20,30))	

def addP(b,c,a=90):
	print(a+b+c)
addP(10,20)

n=100
sum = 0
for counter in range(1,n+1):
	sum = sum+counter
print("Sum of 1 until %d: %d " %(n,sum))	


def names():
	global v 
	v = 'Raju'

print(v)

def multi1(a):
	def mul2(b):
		def multi3(c):
			return a * b * c
		return multi3	
	return mul2

print(multi1(10)(30)(20))	


def factorialCalc(n):
	if n==1 or n==0:
		return 1
	else:
		return n*factorialCalc(n-1)	
print(factorialCalc(5))


f = lambda x,y:x+y
z = f(2,3)
print(z)
'''
'''
k = lambda a: lambda b,n: lambda c: a+b+c*n

print(k(2)(3,6)(5))
