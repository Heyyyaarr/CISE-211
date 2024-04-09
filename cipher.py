import random
import json
import base64

def generate_cipher():
    # Generate a random mapping of characters for encryption
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,!?'"
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    cipher = dict(zip(alphabet, shuffled_alphabet))
    return cipher

def serialize_cipher(cipher):
    cipher_str = ''.join([f'{k}{v}' for k, v in cipher.items()])
    return base64.b64encode(cipher_str.encode()).decode()

def deserialize_cipher(cipher_str):
    cipher_str_decoded = base64.b64decode(cipher_str.encode()).decode()
    cipher = {cipher_str_decoded[i]: cipher_str_decoded[i+1] for i in range(0, len(cipher_str_decoded), 2)}
    return cipher

def encrypt(message, cipher):
    encrypted_message = ""
    for char in message:
        if char in cipher:
            encrypted_message += cipher[char]
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, cipher):
    decrypted_message = ""
    reverse_cipher = {v: k for k, v in cipher.items()}
    for char in encrypted_message:
        if char in reverse_cipher:
            decrypted_message += reverse_cipher[char]
        else:
            decrypted_message += char
    return decrypted_message

def display_cipher(cipher):
    print("Current Cipher:")
    print(serialize_cipher(cipher))

def main():
    past_cipher = None

    while True:
        choice = input("Do you want to (E)ncrypt a new message, (D)ecrypt an old message, or (Q)uit? ").lower()
        if choice == 'e':
            message = input("Enter the message to encrypt or 'q' to quit: ")
            if message.lower() == 'q':
                print("Exiting the program.")
                break
            past_cipher = generate_cipher()
            print("Encrypting message...")
            encrypted_message = encrypt(message, past_cipher)
            print("Encrypted message:", encrypted_message)
            display_cipher(past_cipher)
        elif choice == 'd':
            encrypted_message = input("Enter the encrypted message: ")
            old_cipher_str = input("Enter the old cipher: ")
            past_cipher = deserialize_cipher(old_cipher_str)
            decrypted_message = decrypt(encrypted_message, past_cipher)
            print("Decrypted message:", decrypted_message)
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 'E', 'D', or 'Q'.")

if __name__ == "__main__":
    main()
