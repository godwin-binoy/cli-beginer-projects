import os

# 1. Complete truncated website/src/pages/index.astro
astro_path = "website/src/pages/index.astro"
if os.path.exists(astro_path):
    with open(astro_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    target = "isProgra"
    replacement = """isProgramRunning = false;
      activeVM = null;
      term.write("guest@cli-playground:~$ ");
    }

    // Controls and reset listeners
    document.getElementById("btn-run").addEventListener("click", () => {
      launchProgram(activeProjectId);
    });

    document.getElementById("btn-reset").addEventListener("click", () => {
      const p = PROJECTS.find(proj => proj.id === activeProjectId);
      if (p) {
        modifiedCodes[p.id] = p.code;
        if (editorInstance) {
          editorInstance.setValue(p.code);
        }
      }
    });

    document.getElementById("btn-clear").addEventListener("click", () => {
      term.write("\\x1b[2J\\x1b[H");
    });

    // Initialize application on load
    initTerminal().then(() => {
      renderExplorer();
      loadMonaco(() => {
        if (activeProjectId) {
          switchProject(activeProjectId);
        }
      });
    });
  </script>
</body>
</html>"""
    
    if target in content:
        content = content.replace(target, replacement)
        with open(astro_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Patched index.astro successfully.")

# 2. Fix Guess The Number Game Loop & Math Logic
guess_path = "Guss-The-Number/Guss The Number.py"
guess_code = r"""print('Guess The Number\n---------------')

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
"""
if os.path.exists(guess_path):
    with open(guess_path, "w", encoding="utf-8") as f:
        f.write(guess_code)
    print("Fixed Guess The Number game.")

# 3. Fix Math Game evaluation order & recursion overflow risks
math_path = "Math-Game/Math-Game.py"
math_code = r"""print('Math Game\n---------')

import random

length = 10
operator = '+'
score = 0

def set_level() :
    global length , operator , score
    score = 0
    while True:
        level = input('\nSelect level\n------------\nLevel 1 : numbers from 1 to 10\nLevel 2 : numbers from 1 to 100 \nLevel 3 : numbers from 1 to 1000\n--------------------------------\n\nEnter here : ')
        try :
            level = int(level)      
            if level > 3 or level <= 0 :
                print('\nError : Make sure you select level from 1 to 3.\n')
                continue
            length = 10 ** level
            break
        except :
            print("\nError : Make sure you enter '1' '2' or '3'.\n")
            input('Press enter to continue : ')

    while True:
        operator = input('\n+ , - , * , or / ?\n\nSelect operator : ')
        if operator in ['+', '-', '*', '/']:
            break
        print("Error : Make sure you entered '+' , '-' , '*' or '/'.")
        input('Press enter to continue : ')
        
    if operator == '/' :
        print(f'Number can be more than {length}.')

set_level()
input("\nType 'exit' to exit game and type 'reset' to restart the game at any time.\n\nPress enter to start the game : ")

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
        answer = int(first_number / second_number)
        
    print(f'\n{first_number} {operator} {second_number} ?\n') 
    user_input = input('  : ')
    
    if user_input == 'exit' :
        exit()
    elif user_input == 'reset' :
        set_level()
        continue
        
    try :
        user_input = int(user_input)
        if user_input == answer :
            score += 1
            print(f'Correct! Your score : {score}')
        else :
            print(f'\nYou lose ! \nAnswer is {answer}\nYour score : {score}\n\nEnter to restart')
            input('  : ')
            score = 0
    except :
        print("\nMake sure you entered integer , 'exit' or 'reset.'\n")
        input('Press enter to continue : ')
"""
if os.path.exists(math_path):
    with open(math_path, "w", encoding="utf-8") as f:
        f.write(math_code)
    print("Fixed Math Game.")

# 4. Fix Multiplication Table limits
mult_path = "Multiplication-Table/Multiplication-table.py"
mult_code = r"""print("Multiplication table\n---------------------")
while True :    
    user_input = input('\nTable of : ')
    
    try :
        user_input = int(user_input)
    except :
        print('\nError : Make sure you entered numbers\n')
        continue
        
    if user_input == 0 :
        print('\nMultiplication table of 0 cannot be calculated\n')
        continue
        
    for i in range(1,11) :
        print(f'{i} × {user_input} = {i * user_input}')
"""
if os.path.exists(mult_path):
    with open(mult_path, "w", encoding="utf-8") as f:
        f.write(mult_code)
    print("Fixed Multiplication Table (Python).")

# 5. Fix Password Generator selection and sampling
pass_path = "Password-Generator/Pasword generator.py"
pass_code = r"""print('Password Generator\n------------------')

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
"""
if os.path.exists(pass_path):
    with open(pass_path, "w", encoding="utf-8") as f:
        f.write(pass_code)
    print("Fixed Password Generator.")

# 6. Fix RAM Filler memory mechanics
ram_path = "Ram-filler/Ram filler.py"
ram_code = r"""print('Ram Filler\n----------\n\nThis program will fill RAM in chunks.\n')
input('Enter to fill ram : ')
data = []
print('Filling ram...')
try:
    while True:
        data.append('0' * (50 * 1024 * 1024)) # 50 MB chunks
except MemoryError:
    print("Out of memory!")
"""
if os.path.exists(ram_path):
    with open(ram_path, "w", encoding="utf-8") as f:
        f.write(ram_code)
    print("Fixed RAM filler.")
