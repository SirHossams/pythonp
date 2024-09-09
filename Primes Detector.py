def isprime(x):
	cond=True
	if x==1:
		cond=not True
		return cond
	for i in range(2,x):
		if x%i==0:
			cond=False
			break
	return cond
	
def primes_ran(x):
	"""
	primes_ran is an abbreviation for primes range
	"""
	li=[]
	for i in range(1,x):
		if isprime(i):
			li.append(i)
	return li

x=int(input("Insert the value of x: "))
lires=primes_ran(x)
print(lires)