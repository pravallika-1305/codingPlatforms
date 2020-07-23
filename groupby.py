import itertools
def main():
     n = int(input())
     for _ in range(n):
        strr = input()
        li = [i for i in strr]
        #wc = Counter(li)
        #value_list = []
        #key_list = []
        print(li)
        my_list = []
        new_list = []
        for (key,group) in itertools.groupby(li):
            print(key,len(list(group)))
            my_list.append(key)
            new_list.append(len(list(group)))
        my = max(new_list)
        print(my)
        index = new_list.index(my)
        print(my_list[index])
main()