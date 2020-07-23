a = input().split(' ')
a = list(map(int, a))
c = []
d = []
e = input().split(' ')
e = list(map(int, e))
def listing_subsequences(a,e,c,d):
    for i in range(a[0]):
        c.append(e[i])
#to make a list of all contigous subsets
    for i in range(1,a[0]+1):
        for j in range(a[0]-i+1):
            d.append(c[0+j:i+j])
    return d

def checking_for_condition(a,d):
    count = len([integer for integer in d if (len(integer)== 2) and integer[0] % integer[1] != a[1]])
    single_element_list = [integer for integer in d if (len(integer) == 1)]
    count1 = len(single_element_list)
    return count + count1
first_list = listing_subsequences(a,e,c,d)
count = checking_for_condition(a,first_list)
print(count)
