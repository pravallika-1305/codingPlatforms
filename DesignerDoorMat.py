my_list = list(map(int,input().strip().split()))[:2]
n = my_list[0]
m = my_list[1]
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
