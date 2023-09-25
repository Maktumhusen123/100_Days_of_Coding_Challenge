alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't','u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't',
            'u','v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, caesar_direction):
    end_text = ""
    if caesar_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {caesar_direction}d result: {end_text}")
    

print("==================Caesar Cipher============================")
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    shift %= 26
    caesar(text, shift, direction)
    result = input("Type 'yes' if you want to go again, otherwise type 'no'\n")
    if result == "no":
        should_continue = False
        print("GoodBye")