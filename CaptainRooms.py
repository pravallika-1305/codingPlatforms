_ = input()
set1, set2 = set(), set()
for room in (input().split()):
    if room not in set1:
        set1.add(room)
    else:
        set2.add(room)
set1.difference_update(set2)
print(set1.pop())