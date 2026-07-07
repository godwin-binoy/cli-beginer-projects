print('Guss The Number\n---------------')

import random
import math

while True :
    print('\nEnter Lower range of number\n')
    lower_range = input('  : ')
    print('\nEnter Higher range of number\n')
    higher_range = input('  : ')
    count =  0

    try :
        lower_range = int(lower_range)

        higher_range = int(higher_range)
    except :
        print('\nError : Make sure that you entered integer\n')
        continue

    player_chances = round(math.log(higher_range + lower_range + 1 , 2 ))
    print('\nYou have ', player_chances, ' Chances')

    while True :
        number = random.randint(lower_range, higher_range)
        while player_chances > 0 :
            user_input = input('\nGuss the number : ')

            if user_input == 'exit' :
                exit()
            
            try :
                user_input = int(user_input)
            except :
                print('\nError : Make sure that you entered integer\n')
                continue

            player_chances -= 1

            if user_input > number :
                print(f"\nIt's smaller than you gussed\nYou have {player_chances} more chances")
            if user_input < number :
                print(f"\nIt's larger than you gussed\nYou have {player_chances} more chances")
            if user_input == int(number) :
                print("\nIt's the number\nYou done it !")
                break

        user_input_2 = input("\nEnter 'exit' to exit\nEnter 'reset' to reset the range\nPress enter to play again : ")
        if user_input_2 == 'exit' :
            exit()
        if user_input_2 == 'reset' :
            break
