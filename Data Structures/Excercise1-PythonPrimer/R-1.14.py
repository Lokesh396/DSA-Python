def distinct_pair(data):
	for i in range(len(data)):
		for j in range(i+1, len(data)):
			if (i*j)%2 != 0:
				return (i,j)

ls = list(map(int, input().split()))

print(distinct_pair(ls))
