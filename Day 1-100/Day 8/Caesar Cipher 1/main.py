alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for char in original_text:
        shifted_position = alphabet.index(char) + shift_amount

        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]


    print(f"Here is the encoded result: {cipher_text}")


# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?


encrypt(text, shift)

