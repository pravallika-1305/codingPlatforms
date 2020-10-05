for t in range(int(input())):
    print("Case #" + str(t + 1)+":")
    n = int(input())
    for i in range(n):
            for j in range(n):
                if i + j == (n - 1) / 2 or j - i == (n - 1) / 2 or i - j ==(n - 1) / 2 or i + j == (3 * (n - 1)) / 2:
                    print('*',end='')
                else:
                    print(end=' ')
            print('\r')