print('Password Generator\n------------------')

import random

numbers = '1234567890'
capital_letters ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small_letters ='abcdefghijklmnopqrstuvwxyz'
symbols = '@#_&-+()/*:;!?.~`''""|=°<>{}\%[]'

def ask_user() :
	character = ''
	user_input = input('Include Numericals in password ? \nEnter here : ')
	
	if user_input == 'y' :
		character += numbers

	user_input = input('Include Capital letters in password ? \nEnter here : ')

	if user_input == 'y' :
		character += capital_letters
		
	user_input = input('Include Small letters in password ? \nEnter here : ')

	if user_input == 'y' :
		character += small_letters

	user_input = input('Include Symbols in password ? \nEnter here : ')

	if user_input == 'y' :
		character += symbols
		
	return character

while True :
	length = input('\nLength : ')
	try :
		length = int(length)
	except :
		print('\nError : Make sure you entered numericals')
		continue
	
	print("\n'y' = yes\n'n' = no\n---------\n")
	characters = ask_user()
	
	if len(characters) == 0 :
		print('\nError\n')
		characters = ask_user()
	
	try :	
		print('Password : ',''.join(random.sample(characters,length)))
	except :
		print('\nError : May be the password is too long \n')
		
	user_input = input("\nEnter 'exit' to exit\nEnter to continue : ")
	if user_input == 'exit' :
		exit()