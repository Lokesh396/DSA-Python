def is_even(k):
	val = 0
	for i in range(0,k//2+1):
		if val == k:
			return True
		val += 2
	else:
		return False
		
k = int(input("Please enter the 'k' value :"))

for i in range(k):
	print(is_even(i))
