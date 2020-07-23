from itertools import permutations as npr
def isPalindrome(s):
    return s == s[::-1]


def get_input():
    n = int(input())
    s,nqueries = input().split()
    queries = [input() for i in range(nqueries)]
    queries = [(int(q[0]),int(q[1])) for q in queries]
    return n,s,queries
def gen_palindromes(s,queries):
    palindromes = []
    for L,R in queries:
        palindromes.append(s[:L -1] + make_palindrome(s[L - 1 :R]) + s[R:])
    return palindromes
def make_palindrome(s):
    palindromes = [''.join(p) for p in set(npr(s)) if isPalindrome(p)]
    if len(s) == 0:
        return s
    return sorted(pals)[0]
