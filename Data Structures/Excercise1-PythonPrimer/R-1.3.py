def minmax(data):
	m = data[0]
	M = data[0]
	for i in data:
		if i < m:
			m = i
		if i > M:
			M = i
	return (m, M)
	
ls = list(map(int, input().split()))

print(minmax(ls))
