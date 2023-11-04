import random
def shuffle(data):
	new_data = []
	m = min(data)
	M = max(data)
	while (len(new_data) < len(data)):
		v = random.randint(m,M)
		if v in data and v not in new_data:
			new_data.append(v)
	return new_data
	
ls = list(map(int, input().split()))
print("Before suffling:",ls)
print("After Shuffling:", shuffle(ls))


def shuffle1(data):
	n = len(data)
	for i in range(n-1, 0, -1):
		j = random.randint(0, i-1)
		data[i], data[j] = data[j], data[i]

shuffle1(ls)
print(ls)
