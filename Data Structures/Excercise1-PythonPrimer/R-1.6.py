def squares(n):
	sum_squares = 0
	for j in range(1,n,2):
		sum_squares += j*j
	return sum_squares
	
n = int(input("Enter the 'n' value :"))

print(squares(n))
