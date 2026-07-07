print("Multiplication table\n---------------------")
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
    	
    for i in range(1,10) :
    	print(f'{i} × {user_input} = {i * user_input}')