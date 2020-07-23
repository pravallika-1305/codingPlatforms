import itertools as it
def convert(int_list):
    a_integer = int("".join([str(integer) for integer in int_list]))
    return a_integer
digits = [1,2,3,4,5,6,7,8,9,0]
n,m = map(int,input().split())
my_list = [convert(list(i)) for i in list(it.product(digits,repeat=n)) if sum(i) == m and i[0] != 0]
my_list.sort()
if my_list == []:
    print("-1 -1")
else:
    f = str(my_list[0])
    if(len(my_list) > 1):
        l = str(my_list[-1])
        print(f + " " + l)
    elif(len(my_list) == 1):
        print(f + " " + f)
