print('Guess The Number\n---------------')

import random
import math

while True :
    print('\nEnter Lower range of number\n')
    lower_range = input('  : ')
    print('\nEnter Higher range of number\n')
    higher_range = input('  : ')

    try :
        lower_range = int(lower_range)
        higher_range = int(higher_range)
        if lower_range >= higher_range:
            print('\nError : Higher range must be greater than Lower range\n')
            continue
    except :
        print('\nError : Make sure that you entered integer\n')
        continue

    player_chances_orig = round(math.log(higher_range - lower_range + 1 , 2 ))

    while True :
        player_chances = player_chances_orig
        print(f'\nYou have {player_chances} Chances')
        number = random.randint(lower_range, higher_range)
        
        while player_chances > 0 :
            user_input = input('\nGuess the number : ')

            if user_input == 'exit' :
                exit()
            
            try :
                user_input = int(user_input)
            except :
                print('\nError : Make sure that you entered integer\n')
                continue

            player_chances -= 1

            if user_input > number :
                print(f"\nIt's smaller than you guessed\nYou have {player_chances} more chances")
            elif user_input < number :
                print(f"\nIt's larger than you guessed\nYou have {player_chances} more chances")
            else :
                print("\nIt's the number\nYou done it !")
                break
        else:
            print(f"\nGame Over! The number was {number}.")

        user_input_2 = input("\nEnter 'exit' to exit\nEnter 'reset' to reset the range\nPress enter to play again : ")
        if user_input_2 == 'exit' :
            exit()
        if user_input_2 == 'reset' :
            break
