#i cannot get this to work and i do not care even close to enough to put in the work
# for quite literally 20 points

# def preprocess_input(input_str):
#     # Convert to uppercase
#     input_str = input_str.upper()
#
#     # Ensure the length is a multiple of five by padding with spaces if necessary
#     while len(input_str) % 5 != 0:
#         input_str += ' '
#
#     return input_str
#
#
# def postprocess_output(output_str):
#     # Strip trailing spaces
#     output_str = output_str.rstrip()
#
#     return output_str
#
#
# def encrypt(plaintext):
#     # Convert plaintext to uppercase and ensure length is a multiple of five
#     plaintext = preprocess_input(plaintext)
#
#     # Initialize variables
#     cipher_text = ""
#     key = 8675309  # Initial key value
#
#     # Iterate over the plaintext in groups of five characters
#     for i in range(0, len(plaintext), 5):
#         # Get the next group of five characters
#         group = plaintext[i:i + 5]
#
#         # Convert characters to numeric form (0-63)
#         numeric_group = [ord(char) - 32 for char in group]
#
#         # Combine numeric values into a 32-bit number (using only lower 30 bits)
#         combined = sum(numeric_group[i] << (i * 6) for i in range(5))
#
#         # XOR with the key (rotation left)
#         combined ^= key
#
#         # Convert the result back to human-readable text
#         cipher_group = ""
#         for _ in range(5):
#             cipher_group = chr((combined & 0x3F) + 32) + cipher_group
#             combined >>= 6
#
#         cipher_text += cipher_group
#
#         # Update key for the next group (rotate left)
#         key = ((key << 1) | (key >> 29)) & 0x3FFFFFFF
#
#     return cipher_text
#
#
# def decrypt(ciphertext):
#     # Initialize variables
#     plaintext = ""
#     key = 8675309  # Initial key value
#
#     # Iterate over the ciphertext in groups of five characters
#     for i in range(0, len(ciphertext), 5):
#         # Get the next group of five characters
#         group = ciphertext[i:i + 5]
#
#         # Convert characters to numeric form (0-63)
#         numeric_group = [ord(char) - 32 for char in group]
#
#         # Combine numeric values into a 32-bit number (using only lower 30 bits)
#         combined = sum(numeric_group[i] << (i * 6) for i in range(5))
#
#         # XOR with the key (rotation left)
#         combined ^= key
#
#         # Convert the result back to human-readable text
#         plain_group = ""
#         for _ in range(5):
#             plain_group = chr((combined & 0x3F) + 32) + plain_group
#             combined >>= 6
#
#         plaintext += plain_group
#
#         # Update key for the next group (rotate left)
#         key = ((key << 1) | (key >> 29)) & 0x3FFFFFFF
#
#     return plaintext
#
#
# # Sample session
# user_input = input("Enter plain or cipher text: ")
#
# cipher_text = encrypt(user_input)
# print("Encrypted:", cipher_text)
#
# decrypted_text = decrypt(cipher_text)
# decrypted_text = postprocess_output(decrypted_text)
# print("Decrypted:", decrypted_text)
