time_intervals = []
minutes_list = []
minutes = []

for _ in range(int(input())):
    (l,r) = map(int, input().split())
    time_intervals.append((l,r))
    minutes_list = [[i for i in range(l,r)] for (l,r) in time_intervals]
    for i in minutes_list:
        minutes = minutes + i
    minutes =sorted(list(set(minutes)))
print(len(minutes))