def encrypt_rail_fence(text, num_rails):
    rails = [[] for _ in range(num_rails)]
    rail = 0
    direction = 1
    
    for char in text:
        rails[rail].append(char)
        rail += direction
        
        if rail == num_rails - 1 or rail == 0:
            direction *= -1
            
    ciphertext = ''.join([char for rail in rails for char in rail])
    return ciphertext

def decrypt_rail_fence(ciphertext, num_rails):
    rails = [[] for _ in range(num_rails)]
    rail = 0
    direction = 1
    for char in ciphertext:
        rails[rail].append(None)
        rail += direction
        
        if rail == num_rails - 1 or rail == 0:
            direction *= -1
            
    i = 0
    for rail in rails:
        for j in range(len(rail)):
            rail[j] = ciphertext[i]
            i += 1
            
    rail = 0
    direction = 1
    plaintext = ''
    for _ in ciphertext:
        plaintext += rails[rail].pop(0)
        rail += direction
        
        if rail == num_rails - 1 or rail == 0:
            direction *= -1
            
    return plaintext

# Test the functions
plaintext = "HELLO"
num_rails = 3
ciphertext = encrypt_rail_fence(plaintext, num_rails)
decrypted_text = decrypt_rail_fence(ciphertext, num_rails)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
