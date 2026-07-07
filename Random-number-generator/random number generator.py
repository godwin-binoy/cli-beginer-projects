print('Random Number Generator\n-----------------------')

import random

while True :
	lowest_number = input('\nEnter Lowest number :')
	highest_number = input('Enter Highest number : ')
	
	try :
		lowest_number = int(lowest_number)
		highest_number = int(highest_number)
	except :
		print('\nError : Make sure you entered integer\n')
		continue 
		
	while True :
		try :
			print(f'\nRandom number : {random.randint(lowest_number , highest_number)}\n')
		except :
			print('\nError : Make sure that Highest number is larger than Smallest number\n')
			continue 
			
		user_input = input("Enter 'reset' to reset highest and lowest number\nEnter 'exit' to exit\nEnter to generate another number :")

		if user_input == 'reset' :
			break
		if user_input == 'exit' :
			exit()