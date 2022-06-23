import random

def compare(x, y):
	x.sort()
	y.sort()
	if(x == y):
		return "A"
	else:
		return "W"

number=random.randint(1000,9999)
check=list(int(d) for d in str(number))
i=0

while i<10:
	n = int(input())
	user = list(int(e) for e in str(n))
	if check==user:
		print("R")
		break
	else:
		print(compare(check,user))
	i+=1
