for _ in range(int(input())):
    students = list(input())
    count = 0
    if students == ("xy" or "yx"):
        print(1)
    else:
        for i in range(len(students) - 1):
            if ((students[i] == 'x'and students[i + 1] == 'y') or (students[i] == 'y' and students[i + 1] == 'x')):
                count += 1
                students[i] = students[i + 1] = "$"
            else:
                continue
        print(count)
        