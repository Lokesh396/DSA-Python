import math
def euclidean(data):
	return math.sqrt(sum(i**2 for i in data))
	
data = list(map(int, input().split()))
print(euclidean(data))
