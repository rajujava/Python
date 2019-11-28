a = True
b = False

print( a and b)
print (a or b)
print (not b)

aa = 10
bb = 90
cc = 30
if aa<bb and aa<cc:
	print("aa less than bb",aa)
else:
	print("a is not bigger")	


if aa<bb:
	if aa<cc:
		print("aab less than bb",aa)
	else:
		print("Hello ..")	
else:
	print("a is not bigger")		


name = "Raju"

if(name == "Raju"):
	print("welcome Raju")
elif name=="raju":
 	print("welcome raju")
else:
 	print("who are you")		

greet="welcome" if name=="Raju" or name == "welcome" else "plz subscribe"
print(greet)

a=10
b=20
big=a if a>b else b  	
print("big is :",big)