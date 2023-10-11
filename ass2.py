def encrypt():
    text = input("input value encrypt: ")
    shift = int(input("input shift space: "))
    encryption = ""

    for c in text:

        # check if character is an uppercase letter
        if c.isupper():

            # find the position in 0-25
            c_unicode = ord(c)

            c_index = ord(c) - ord("A")

            # perform the shift
            new_index = (c_index + shift) % 26

            # convert to new character
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)

            # append to encrypted string
            encryption = encryption + new_character

        else:

            # since character is not uppercase, leave it as it is
            encryption += c
            
    print("Plain text:",text)

    print("Encrypted text:",encryption)

def decrypt():
    encrypted_text = input("input value encrypt: ")
    shift = int(input("input shift space: "))
    plain_text = ""

    for c in encrypted_text:

        # check if character is an uppercase letter
        if c.isupper():

            # find the position in 0-25
            c_unicode = ord(c)

            c_index = ord(c) - ord("A")

            # perform the negative shift
            new_index = (c_index - shift) % 26

            # convert to new character
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)

            # append to plain string
            plain_text = plain_text + new_character

        else:

            # since character is not uppercase, leave it as it is
            plain_text += c

    print("Encrypted text:",encrypted_text)
    print("Decrypted text:",plain_text)
def Brute_force():
    letters = "abcdefghijklmnopqrstuvwxyz"
    enc_string = input("enter your string you want to decode: ")
    x = 0
    while x < 26:
        x = x + 1
        stringtodecrypt=enc_string
        stringtodecrypt=stringtodecrypt.lower()
        ciphershift=int(x)
        stringdecrypted=""
        for character in stringtodecrypt:
            position = letters.find(character)
            newposition = position-ciphershift
            if character in letters:
                stringdecrypted = stringdecrypted + letters[newposition]
            else:
                stringdecrypted = stringdecrypted + character
        ciphershift=str(ciphershift)
        print("You used a cipher shift of " +ciphershift)
        print("Your decrypted message reads: ")
        print(stringdecrypted)
        print("\n")
def assignment_2(choose):
    switch = {
        1: encrypt,
        2: decrypt,
        3: Brute_force,
        4: exit
    }
    func = switch.get(choose, None)
    if func:
        return func()
    else:
        print('Choose one of the following options: 1, 2, 3, 4')

choosed = " 1. encryption a text! \n 2. decryption a text \n 3. Brute-force text \n 4. exit"
print(choosed)
choose = int(input("Select your option: "))
assignment_2(choose)