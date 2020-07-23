size = int(input())
a = list(map(int,input().strip().split()))[:size] 
length = int(input())
b = list(map(int,input().strip().split()))[:length]
first_set = set(a)
second_set = set(b)
new_set = first_set.union(second_set)
my_set = first_set.intersection(second_set)
final_set = new_set - my_set
final_list = sorted(final_set)
for i in final_list:
    print(i)