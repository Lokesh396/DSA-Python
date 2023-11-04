def is_multiple(n ,m):
	for i in range(1,n+1):
		if m*i == n:
			return True
	else:
		return False
		
n = int(input("Please enter 'n' value :"))
m = int(input("Please enter 'm' value :"))

print(is_multiple(n ,m))
