import random
import os

Lives = 6

words = [
    "elephant", "computer", "guitar", "mountain", "ocean",
    "pizza", "universe", "butterfly", "rainbow", "volcano",
    "bicycle", "astronaut", "library", "jungle", "sunset",
    "fireworks", "sushi", "treasure", "castle", "wizard",
    "robot", "mermaid", "galaxy", "waterfall", "adventure",
    "explorer", "detective", "carnival", "penguin", "dinosaur",
    "spaceship", "superhero", "enchanted", "dragon", "rainforest",
    "wonderland", "paradise", "magic", "mystery",
    "revolution", "revolutionary", "emperor", "samurai", "gladiator",
    "vampire", "werewolf", "phoenix", "labyrinth", "journey"
]

chosen_word = random.choice(words)

print(f'Pssst, the solution is {chosen_word}\n')

pastWords = []
display = []

word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    os.system('cls')
    print('\n H A N G M A N - By: Franco\n')
    print(f'{display} Lives: {Lives}')
    guess = input("Guess a letter: ").lower()

    if guess in pastWords:
        pass
    else:
        pastWords += guess
        if not guess in chosen_word:
            Lives -= 1 

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter  == guess:
            display[position] = letter

    if not "_" in display:
        end_of_game = True
        print(f'You win! Solution: {chosen_word}')
    
    if Lives == 0:
        end_of_game = True
        print(f'Game Over! Solution: {chosen_word}')
