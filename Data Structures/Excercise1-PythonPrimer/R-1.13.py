def reverse(data):
	return data[::-1]

ls = list(map(int, input().split()))
print("Before:",ls)
print("After:",reverse(ls))
