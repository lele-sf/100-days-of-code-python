from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
play_again = 'yes'


def caesar(text, shift, direction):
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    crypted_text = ''
    for letter in text:
        if letter in alphabet:
            if direction == 'encode':
                index = alphabet.index(letter)
                crypted_text += shifted_alphabet[index]
            else:
                index = shifted_alphabet.index(letter)
                crypted_text += alphabet[index]
        else:
            crypted_text += letter
    print(f"The {'encoded' if direction == 'encode' else 'decoded'} text is {crypted_text}")


while play_again == 'yes':
    print(logo)
    direction = ''
    while direction not in ['encode', 'decode']:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
