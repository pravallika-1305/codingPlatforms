n = int(input())
for _ in range(n):
    number = int(input())
    temp = number
    while(temp % 10 == 0):
        temp = temp / 10

        