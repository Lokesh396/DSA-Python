def scale(data, factor):
	for val in data:
		val *= factor
	return data
ls = list(map(int, input().split()))
factor = int(input("Enter Factor :"))
print("Before Scaling:",ls)
print("After Scaling:",scale(ls, factor))

#here the data wont change because val is a local variable if we index it will change
