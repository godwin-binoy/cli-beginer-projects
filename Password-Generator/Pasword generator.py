print('Password Generator\n------------------')

import random

numbers = '1234567890'
capital_letters ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small_letters ='abcdefghijklmnopqrstuvwxyz'
symbols = '@#_&-+()/*:;!?.~`''""|=°<>{}\%[]'

def ask_user() :
    character = ''
    user_input = input('Include Numericals in password ? (y/n)\nEnter here : ')
    if user_input.lower() == 'y' :
        character += numbers

    user_input = input('Include Capital letters in password ? (y/n)\nEnter here : ')
    if user_input.lower() == 'y' :
        character += capital_letters
        
    user_input = input('Include Small letters in password ? (y/n)\nEnter here : ')
    if user_input.lower() == 'y' :
        character += small_letters

    user_input = input('Include Symbols in password ? (y/n)\nEnter here : ')
    if user_input.lower() == 'y' :
        character += symbols
        
    return character

while True :
    length = input('\nLength : ')
    try :
        length = int(length)
        if length <= 0:
            print('\nError : Length must be greater than 0')
            continue
    except :
        print('\nError : Make sure you entered numericals')
        continue
    
    print("\n'y' = yes\n'n' = no\n---------\n")
    
    while True:
        characters = ask_user()
        if len(characters) > 0:
            break
        print('\nError : You must select at least one character type!\n')
    
    password = ''.join(random.choice(characters) for _ in range(length))
    print('Password : ', password)
        
    user_input = input("\nEnter 'exit' to exit\nEnter to continue : ")
    if user_input == 'exit' :
        exit()
