while True :
	print('Character Counter\n-----------------\n')
	string = input('Enter characters : ')
	print(f"\nLength of characters : {len(string)}\n")
	user_input = input("[Enter 'exit' to exit]\n[Enter to continue]\n")
	if user_input == 'exit' :
		exit()