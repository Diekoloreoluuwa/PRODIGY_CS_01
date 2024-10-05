
letters = "abcdefghijklmopqrstuvwxyz"
num_letters = len(letters)
# def encrypt(plaintext, key):
#     ciphertext = ''
#     for letter in plaintext:
#         letter = letter.lower()
#         if not letter == ' ':
#             index = letters.find(letter)
#             if index == -1:
#                 ciphertext += letter
#             else:
#                 new_index = index + key
#                 if new_index >= num_letters:
#                     new_index -= num_letters
#                 ciphertext += letters[new_index]
#     return ciphertext
#
# def decrypt(ciphertext, key):
#     plaintext = ''
#     for letter in ciphertext:
#         letter = letter.lower()
#         if not letter == ' ':
#             index = letters.find(letter)
#             if index == -1:
#                 plaintext += letter
#             else:
#                 new_index = index - key
#                 if new_index < 0:
#                     new_index += num_letters
#                 plaintext += letters[new_index]
#     return plaintext

def encrypt_decrypt(text, mode, shift):
    result = ''
    if mode == 'decrypt':
        shift = -shift

    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + shift
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]
    return result


print()
print("*** CAESAR CIPHER PROGRAM ***")
print()

print("Do you want to encrypt or decrypt?")
user_input = input("encrypt Or decrypt: ").lower()
# if user_input != "encrypt" or "decrypt":
#     print("invalid, Try again")
print()

if user_input == "encrypt":
    print("Encrytion Mode")
    print()
    key = int(input('Enter the shift (1 through 26): '))
    text = input("Enter text to encrypt: ")
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == "decrypt":
    print("Decrytion Mode")
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input("Enter text to encrypt: ")
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f'PLAIN TEXT: {plaintext}')
