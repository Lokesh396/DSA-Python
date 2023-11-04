ls = []
while True:
	try:
		i = input()
	except EOFError:
		break
	ls.append(i)

for i in range(len(ls)-1,-1,-1):
	print(ls[i])
		
