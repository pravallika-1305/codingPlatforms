# cook your dish here
i = int(input())
output = []
for j in range(i):
    a,b,c,d = map(int,input().split())
    output.append(a/(a + b))
    print(output[i])
    