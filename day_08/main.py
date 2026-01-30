# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text.lower():
        if letter in alphabet:
            shifts = alphabet.index(letter) + shift_amount
            shifts %= len(alphabet)
            output_text += alphabet[shifts]
        else:
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    user_response = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if  user_response.lower() == "no":
        print("Goodbye")
        break




