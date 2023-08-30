alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't','u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't',
            'u','v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def caesar(message, shift_amt, direc):
    if direc == "encode":
        cipher_text = ""
        for letter in message:
            position = alphabet.index(letter)
            new_position = position + shift_amt
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"Encoded text is {cipher_text}")
    elif direc == "decode":
        plain_text = ""
        for letter in message:
            position = alphabet.index(letter)
            new_position = position - shift_amt
            new_letter = alphabet[new_position]
            plain_text += new_letter
        print(f"Decrypted text is {plain_text}")

caesar(text, shift, direction)