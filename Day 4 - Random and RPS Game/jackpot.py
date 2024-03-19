import random
from time import sleep

fruits = [
    'maçã', 'uva', 'pêra', 'laranja', 'melão', 'melancia',
    'banana', 'abacaxi', 'mamão', 'morango', 'limão', 'kiwi', 'framboesa', 'cereja', 'amora', 'pêssego', 'mirtilo', '7']

fruits_with_prob = fruits[:-1] /2 + ['7']

random_fruit1 = random.choice(fruits_with_prob)
random_fruit2 = random.choice(fruits)
random_fruit3 = random.choice(fruits)

print(f' 1 - {random_fruit1}')
sleep(1)
print(f' 2 - {random_fruit2}')
sleep(3)
print(f' 3 - {random_fruit3}')
sleep(0.5)

if random_fruit1 == '7' and random_fruit2 =='7' and random_fruit3 == '7':
    print('\n JACKPOT!!! - You won: $100')

elif random_fruit1 == random_fruit2 == random_fruit3:
    print('\n HOW LUCKY YOU ARE! - You won $10')

elif random_fruit1 == random_fruit2 or random_fruit1 == random_fruit3 or random_fruit2 == random_fruit3:
    print('\n Almost there! - You won $1.5')

else:
    print('\n Nice try.. Try again!')