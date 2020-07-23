num = int(input(""))
count = 0
while(num > 0):
    digit = num % 10
    num = num // 10
    if(digit == 4 or digit == 7):
        count = count + 1
if(count == 4 or count == 7):
    print("True")
else:
    print("False")