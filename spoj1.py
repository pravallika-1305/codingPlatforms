from math import gcd as GCD

def GcD(a,b,c):
	first_gcd = GCD(a,b)
	final = GCD(first_gcd,c)
	return final

a,b,c = map(int,input().split())
print(GcD(a,b,c))
