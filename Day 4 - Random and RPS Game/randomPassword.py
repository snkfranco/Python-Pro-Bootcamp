import os
import random
import string

os.system('cls')

print('\n Welcome to the password generator!\n')

times = int(input(" How many passwords do you want to create? "))
special = input(" Want to put random special digits? (Yes / No): ").lower()
digits = int(input(" Type the password lenght (e.g: 12) "))
print(' ')

x = 1

while x <= times:
    # Define os caracteres a serem usados na senha
    specials = ['+', '*', '@', '!']
    characters = string.ascii_letters + string.digits 

    # Gera uma senha aleatória de 10 dígitos
    random_password = ''.join(random.choices(characters, k=digits))
    if special == 'yes' or special == 'y':
        passwordComplete = random_password.join(random.choices(specials, k=2))
    else:
        passwordComplete = random_password

    print(f"  └ Random password {x}:", passwordComplete)
    x += 1