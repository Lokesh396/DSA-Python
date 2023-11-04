def vowel_counter(s):
	vowels = ['a', 'e', 'i', 'o', 'u']
	count = 0
	for i in s:
		if i in vowels:
			count += 1
	return count

s = input('Enter the String: ')
s.lower()
print(vowel_counter(s))
