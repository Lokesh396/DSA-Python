def distinct_number(data):
	counter = []
	for i in data:
		if i not in counter:
			counter.append(i)
		else:
			return False
	else:
		return True

ls = list(map(int, input().split()))

print(distinct_number(ls))
