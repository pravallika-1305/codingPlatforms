import sys

def listing_the_substrings(test_str):
    res = [test_str[i: j] for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1)]
    return res

def removing_duplicates(result):
    a = set()
    a = set(listing_the_substrings(result))
    return a

test_cases=int(sys.stdin.readline())
while test_cases>0:
    string=sys.stdin.readline().strip()
    substrings_list=removing_duplicates(string)
    substrings_list=list(substrings_list)
    substrings_list.sort()    
    index=int(sys.stdin.readline().strip())
    string=''.join(substrings_list)
    print(string[index-1])
    test_cases=test_cases - 1