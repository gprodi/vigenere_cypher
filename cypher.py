# This is a simple Vigenère cipher implementation in Python
# The Vigenère cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution.
# A Vigenère cipher uses a keyword to shift letters in the plaintext by a number of positions in the alphabet.
# The keyword is repeated to match the length of the plaintext, and each letter in the plaintext is shifted by the corresponding letter in the keyword.
# For example, if the keyword is "key" and the plaintext is "hello", the first letter 'h' would be shifted by 'k', the second letter 'e' would be shifted by 'e', and so on.
# The Vigenère cipher is more secure than a simple Caesar cipher because it uses multiple shifts based on the keyword.
# This implementation uses a custom key to encrypt and decrypt the message.
# The key is a string of letters that is used to determine the shift for each letter in the plaintext.
# The key is repeated to match the length of the plaintext, and each letter in the plaintext is shifted by the corresponding letter in the key.
# The Vigenère cipher is a simple and effective way to encrypt messages, but it is not as secure as modern encryption methods.
# This implementation uses a custom key to encrypt and decrypt the message.
# The key is a string of letters that is used to determine the shift for each letter in the plaintext.
# The key is repeated to match the length of the plaintext, and each letter in the plaintext is shifted by the corresponding letter in the key.
text = 'hello world'
custom_key = 'test'
def vigenere(message, key, direction=1):
    key_index = 0
    # Define the alphabet to be used
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Initialize the final message
    # to be an empty string
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            # Check if the character is in the alphabet
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            # Append the new character to the final message
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    # Encrypt the message using the Vigenère cipher
    return vigenere(message, key)
    
def decrypt(message, key):
    # Decrypt the message using the Vigenère cipher
    # The direction is -1 for decryption
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')