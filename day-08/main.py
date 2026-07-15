"""
Day 8 - Caesar Cipher
Encode or decode a message by shifting each letter by a given amount.
"""

logo = """
 ,adPPYba, ,adPPYYba, ,adPPYesar,ba,  ,adPPYba,  8b,dPPYba, 
a8"     "" ""     `Y8 I8[    ""  a8"     "8a 88P'   `"8a
8b         ,adPPPPP88  `"Y8ba,  8b       d8 88       88
"8a,   ,aa 88,    ,88 aa    ]8I "8a,   ,a8" 88       88
 `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP"'  88       88
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"The {cipher_direction}d text is: {end_text}")


print(logo)
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
