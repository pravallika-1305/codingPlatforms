def num2digits(num):
    return [int(x) for x in str(num)]

number = int(input())
n = 0
if number in range(0,10):
    print(0)

while len(str(number)) > 1:
    number = sum(num2digits(number))
    n = n + 1
print(n)
        



