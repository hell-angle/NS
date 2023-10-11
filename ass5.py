def vigenere_encrypt(plaintext, key):
    # Expand the key to the length of the plaintext
    key_expanded = ''
    for i in range(len(plaintext)):
        key_expanded += key[i % len(key)]
        
    # Initialize an empty string to store the ciphertext
    ciphertext = ''
    
    # Loop through each character in the plaintext
    for c, k in zip(plaintext, key_expanded):
        if c.isalpha():
            # Determine the base ASCII code ('A' or 'a') based on the case
            base = ord('A') if c.isupper() else ord('a')
            
            # Encrypt the character
            encrypted_char = chr(((ord(c) - base + ord(k.upper()) - ord('A')) % 26) + base)
        else:
            encrypted_char = c
        
        ciphertext += encrypted_char
    
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    # Expand the key to the length of the ciphertext
    key_expanded = ''
    for i in range(len(ciphertext)):
        key_expanded += key[i % len(key)]
        
    # Initialize an empty string to store the decrypted text
    plaintext = ''
    
    # Loop through each character in the ciphertext
    for c, k in zip(ciphertext, key_expanded):
        if c.isalpha():
            # Determine the base ASCII code ('A' or 'a') based on the case
            base = ord('A') if c.isupper() else ord('a')
            
            # Decrypt the character
            decrypted_char = chr(((ord(c) - base - (ord(k.upper()) - ord('A'))) % 26) + base)
        else:
            decrypted_char = c
        
        plaintext += decrypted_char
    
    return plaintext
def menu():
    print("Vigenère Cipher Program")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Please enter your choice (1/2/3): ")
    return choice

while True:
    user_choice = menu()

    if user_choice == '1':
        plaintext = input("Enter the text to encrypt: ")
        key = input("Enter the key: ")
        encrypted = vigenere_encrypt(plaintext, key)
        print(f"Encrypted text: {encrypted}")
    elif user_choice == '2':
        ciphertext = input("Enter the text to decrypt: ")
        key = input("Enter the key: ")
        decrypted = vigenere_decrypt(ciphertext, key)
        print(f"Decrypted text: {decrypted}")
    elif user_choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")


