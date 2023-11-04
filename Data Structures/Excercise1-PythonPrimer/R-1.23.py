def check_overflow():
	ls = [1,2,3,5]
	try:
		ls[4] = 4
	except IndexError:
		print("Don't try buffer overflow attacks in python !")
		
check_overflow()
