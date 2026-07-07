print('Math Game\n---------')

import random

def set_level() :
	global length , operator , score
	score = 0
	level = input('\nSelect level\n------------\nLevel 1 : numbers from 1 to 10\nLevel 2 : numbers from 1 to 100 \nLevel 3 : numbers from 1 to 1000\n--------------------------------\n\nEnter here : ')
	
	try :
		level = int(level)		
		if level > 3 or level <= 0 :
			print('\nError : Make sure you select level from 1 to 3.\n')
			set_level()
		else :
			length = 10 ** level
			
	except :
			print("\nError : Make sure you enter '1' '2' or '3'.\n")
			input('Press enter to continue : ')
			set_level()
	
	operator = input('\n+ , - , * , or / ?\n\nSelect operator : ')
	
	if operator != '+' and operator != '-' and operator != '*' and operator != '/' :
		print("Error : Make sure you entered '+' , '-' , '*' or '/'.")
		input('Press enter to continue : ')
		set_level()
		
	if operator == '/' :
		print(f'Number can be more than {length}.')

set_level()
input("\nType 'exit' to exit game and type 'restart' to restart the game at any time.\n\nPress enter to start the game : ")

while True :
	first_number = random.randint(2 , length)
	second_number = random.randint(1 , first_number - 1)
	
	if operator == '+' :
		answer = first_number + second_number
	elif operator == '-' :
		answer = first_number - second_number
	elif operator == '*' :
		answer = first_number * second_number
	else :
		length_of_second_number= len(str(second_number))
		
		if length_of_second_number == 2 or length_of_second_number == 3 :
			second_number = second_number // 10 
						
		first_number = first_number + (second_number - ( first_number % second_number ) )
		answer = first_number / second_number
		
	print(f'\n{first_number} {operator} {second_number} ?\n') 
	user_input = input('  : ')
	
	try :
		user_input = int(user_input)
		if user_input == answer :
			score += 1
                        print(f'Correct! Your score : {score}')
		else :
			print(f'\nYou loss ! \nAnswer is {answer}\nYour score : {score}\n\nEnter to restart')
			user_input = input('  : ')
			score = 0
	except :
		print("\nMake sure you entered integer , 'exit' or 'reset.'\n")
		input('Press enter to continue : ')
		
	if user_input == 'exit' :
		exit()
	elif user_input == 'reset' :
		set_level()