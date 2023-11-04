def change_calculator(actual, given):
	diff = given - actual
	if diff >= 500:
		print(f"{diff//500} 500 ruppee notes")
		diff -= (diff//500)*500
	if diff >= 200:
		print(f"{diff//200} 200 ruppee notes")
		diff -= (diff//200)*200
	if diff >= 100:
		print(f"{diff//100} 100 ruppee notes")
		diff -= (diff//100)*100
	if diff >= 50:
		print(f"{diff//50} 50 ruppee notes")
		diff -= (diff//50)*50
	if diff >= 20:
		print(f"{diff//20} 20 ruppee notes")
		diff -= (diff//20)*20
	if diff >= 10:
		print(f"{diff//10} 10 ruppee notes")
		diff -= (diff//10)*10
	if diff >= 5:
		print(f"{diff%5} 5 ruppee coins")
		diff -= (diff//5)*5
	if diff >= 2:
		print(f"{diff//2} 2 ruppee coins")
		diff -= (diff//2)*2
	if diff >= 1:
		print(f"{diff//1} 1 ruppee coins")
		diff -= (diff//1)*1

actual = int(input("Enter bill amount:"))
gievn = int(input("Enter given amount:"))	
change_calculator(actual, given)
