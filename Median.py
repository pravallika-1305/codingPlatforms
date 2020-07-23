from numpy import median
n = int(input())
for _ in range(n):
    l = int(input())
    my_list = list(map(int,input().strip().split()))[:l]
    while(len(my_list) > 2):
        new = int(median(my_list[0],my_list[1],my_list[2]))
        my_list.remove(new)
    print(my_list)
             
         
         