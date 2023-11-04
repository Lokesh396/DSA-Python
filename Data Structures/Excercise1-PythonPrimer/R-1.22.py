def dot_product(ar1, ar2):
	res = []
	for i in range(len(ar1)):
		res.append(ar1[i] * ar2[i])
	return res

ar1 = [1, 2, 3, 4, 5]
ar2 = [5, 4, 3, 2, 1]

print(dot_product(ar1, ar2))
