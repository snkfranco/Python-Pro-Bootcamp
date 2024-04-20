import os

characters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
    '[', ']', '{', '}', ';', ':', '<', '>', ',', '.', '/', '?', '|', '♥',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '~', '`', "'", '"', " "
]

logo = '''
     _____ _   _  _   __  _   _ ___________ _____ 
    /  ___| \ | || | / / | | | |_   _|  _  \  ___|
    \ `--.|  \| || |/ /  | |_| | | | | | | | |__  
     `--. \ . ` ||    \  |  _  | | | | | | |  __| 
    /\__/ / |\  || |\  \ | | | |_| |_| |/ /| |___ 
    \____/\_| \_/\_| \_/ \_| |_/\___/|___/ \____/ 

'''

# 9~:8;3a;6850.>~;62.:9.;vl
# 154236987

def caeser(start_text, shift_amount, choice):
    end_text = ""
    if choice == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in characters:
            position = characters.index(char)
            new_position = (position + shift_amount) % len(characters)
            end_text += characters[new_position]
        else:
            end_text += char
    print(f"[>>] The {choice}d text is: {end_text}")


os.system('cls')
print(logo)

choice = input("[+] Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("[+] Type your message: ").lower()
shift = int(input("[+] Type the shift number: "))

shift %= len(characters)

caeser(start_text=text, shift_amount=shift, choice=choice)
