N = int(input())
string_list = []
for x in range(N):
    x = input("")    
    string_list.append(x)
string_set = set(string_list)
distinct = len(string_set)
print(distinct)
