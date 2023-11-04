def squares(n):
	sum_squares = 0
	for i in range(n):
		sum_squares += i**2
	return(sum_squares)
	
n = int(input("Enter the 'n' value :"))

print(squares(n))
