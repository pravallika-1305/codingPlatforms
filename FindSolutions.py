#Hackerearthproblem
import itertools as it
n = int(input())
a = list(map(int,input().strip().split()))[:n] 
new = it.combinations_with_replacement(a,6)
for i in new:
    if(i[5] != 0):
        print(i)

