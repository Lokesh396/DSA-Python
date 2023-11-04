from itertools import permutations
def strings(data):
	res = list(permutations(data))
	return set(res)

data = ['a','e','i','o','u']
print(strings(data))
