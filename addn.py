for _ in range(int(input())):
    nums,add = input().split()
    sum_list = [eval(str(int(i) + int(add))) for i in nums]
    number = ""
    for i in sum_list:
        number = number + str(i)
    print(number)
