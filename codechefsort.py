def rev(l):
    return [l[-1]] + rev(l[:-1]) if l else []

n = int(input())  
a = list(map(int,input().strip().split()))[:n] 
print(rev(a))
