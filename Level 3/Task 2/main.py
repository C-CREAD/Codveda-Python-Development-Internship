"""
Created by: Shingai Dzinotyiweyi

Task 2: Basic File Encryption/Decryption
Create a Python script that encrypts and decrypts text files using a
simple encryption algorithm (e.g., Caesar cipher or Fernet encryption).

Objectives:
✅ - Allow the user to input a file for encryption or decryption.
✅ - Encrypt the file content and save it as a new file.
✅ - Provide functionality to decrypt the file back to its original form
"""

# NOTE: Using Caesar Cipher for encryption and decryption after reading a text file
#       then saving results in respective encryption and decryption folders

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encryption(text, shift):
    result = ""
    if shift <= len(alphabet) - 1:

        for character in text:
            if character.isalpha():
                index = alphabet.index(character.upper())

                if character.islower():
                    result += cipher[index].lower()
                else:
                    result += cipher[index]
            else:
                result += character

    print('Encryption:', result)

    with open("encryption/encrypted.txt", "w+") as write_file:
        write_file.writelines(result)
        print("Result written in encrypted.txt\n")


def decryption(text, shift):
    result = ""
    if shift <= len(alphabet) - 1:

        for character in text:
            if character.isalpha():
                index = cipher.index(character.upper())

                if character.islower():
                    result += alphabet[index].lower()
                else:
                    result += alphabet[index]
            else:
                result += character

    print('Decryption:', result)

    with open("decryption/decrypted.txt", "w+") as write_file:
        write_file.writelines(result)
        print("Result written in decrypted.txt\n")


# Request shift value to create cipher for encryption and decryption
shift = int(input("Pick a shift number between 1 - 26: "))
cipher = alphabet[shift:] + alphabet[0:shift]


# Performs encryption
with open('test.txt', 'r+') as read_file:
    string_text = ""

    for line in read_file:
        string_text += line

    encryption(string_text, shift)


# Performs decryption based on initial encryption
with open('encryption/encrypted.txt', 'r+') as read_file:
    string_text = ""

    for line in read_file:
        string_text += line

    decryption(string_text, shift)