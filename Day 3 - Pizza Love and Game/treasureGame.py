import os

def welcome_message():
    os.system('cls')
    print("\nWelcome to Treasure Island!\n")
    print("Your adventure begins now. You find yourself on a mysterious island.\n")

def choose_path():
    print("You stand at a crossroad.\n")
    print("To your left is a dense jungle, to your right is a rocky path.")
    choice = input("Which path will you choose? Left or Right? ").lower()
    return choice

def explore_path(choice):
    if choice == "left":
        print("\nYou venture into the dense jungle.\n")
        print("As you push through the thick foliage, you stumble upon an old temple.")
        print("Inside, you find a chest filled with ancient artifacts and treasure!")


    elif choice == "right":
        print("\nYou walk along the rocky path.\n")
        print("After a while, you come across a cave entrance.")
        print("You cautiously enter the cave and discover a hidden stash of gold!\n")

        disarmed = input("But unfortunately, inside the cave, there was a landmine.\nLuckily, you noticed it before it was activated. Do you want to jump over the bomb? ( yes / no ): ").lower()

        if disarmed == "yes":
            print("You successfully jump over the bomb and took all the gold!!")
        elif disarmed == "no":
            print("\nYou cautiously navigate around the landmine and continue exploring the cave.")
            print("You walked for a few meters and encountered a giant guardian of the sacred portal. - YOU DIED!")
        else:
            print("\n\nInvalid choice. Please enter 'yes' or 'no'.")
            explore_path(choice)
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")

def play_again():
    play = input("Do you want to play again? ( yes / no ): ").lower()
    if play == "yes":
        main()
    else:
        print("\n\n\nThanks for playing! - Treasure Game")

def main():
    welcome_message()
    path_choice = choose_path()
    explore_path(path_choice)
    play_again()

if __name__ == "__main__":
    main()