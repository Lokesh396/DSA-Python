def premoved(s):
	s1=''
	for i in s:
		if i.isalpha() or i ==' ':
			s1 += i
	return s1

s = input("Enter the String:")
print(premoved(s))
