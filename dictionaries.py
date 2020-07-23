from collections import Counter

def main():
     n = int(input())
     for _ in range(n):
        strr = input()
        li = [i for i in strr if i.isalpha() and i.islower()]
        wc = Counter(li)
        key_value = []
        for k,v in wc.items():
            key_value.append([k,v])
        new_list = sorted(key_value,key=lambda l:l[0])
        maximum_value = max(new_list, key=lambda x: x[1])
        final_index = new_list.index(maximum_value)
        sub_list = new_list[final_index]
        print(sub_list[0])
main()