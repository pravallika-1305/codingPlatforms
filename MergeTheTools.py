from collections import OrderedDict

def splitString(s, k):
     return [''.join(x) for x in zip(*[list(s[z::k]) for z in range(k)])]

def remove_duplicates(s,k):
    l = splitString(s,k)
    u_list = []
    for i in l:
        result = "".join(OrderedDict.fromkeys(i))
        u_list.append(result)
    return u_list
string = input("Enter any string:\n")
k = int(input("Enter the integral value:\n"))
req_list = remove_duplicates(string,k)
for i in req_list:
    print(i)
