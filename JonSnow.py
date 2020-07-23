n=int(input())
enemy_pos=[]
for x in range(n):
	a,b=map(int,input().split())
	enemy_pos.append([a,b])
queries = int(input())
horizontal_distance = 0
active_walkers = []
for x in range(queries):
	l,r,k=map(int,input().split())
	for y in range(l-1,r):
		horizontal_distance = enemy_pos[y][0]	
		if horizontal_distance <= k:
			active_walkers.append([enemy_pos[y][0],enemy_pos[y][1]])
	div=[]		
	for y in range(len(active_walkers)):
		num = active_walkers[y][1]
		count = 2
		if num == 2 or num == 3:
		    count = 2
		elif num == 1:
		    count = 1
		else:    
		    for z in range(2,int(num/2)+1):
			    if num % z == 0:
				    count += 1
		div.append(count)
	if len(div) == 1:
		print(1)	
	if len(div) == 2:
		print(0)
	if len(div) > 2:
		count1 = 0 
		for z in range(len(div)):
			new = div[0:z] + div[z + 1:len(div)]
			power = new[0]
			for u in range(1,len(div)-1):
				power = power ^ new[u]
			if power == 0:
				count1 += 1
		print(count1)
		active_walkers.clear()