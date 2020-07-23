# your code goes here
from math import gcd as GCD

n,k,a = map(int,input().split())

def isCoprime(a, b):
    return GCD(a, b) == 1
   
def filterCoprimes(n):
	number_list = range(n)
	coprimelist = list(filter(lambda x : isCoprime(x,n),number_list))
	return coprimelist

def isKthroot(x,n,k,a):
	return x ** k == a % n

def finalOutput(n,k,a):
	coprimelist = filterCoprimes(n)
	final_list = list(filter(lambda x : isKthroot(x,n,k,a),coprimelist))
	return final_list

print(len(finalOutput(n,k,a)))
print(*finalOutput(n,k,a))
