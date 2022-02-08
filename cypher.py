def caesar(plainText, shift):
    ciphertext = ""
    for ch in plainText.lower():
        if ch.isalpha():
            lettersonly = ord(ch) + shift
            if lettersonly > ord('z'):
                lettersonly -= 26
            nechar = chr(lettersonly)
            ciphertext += nechar
        else:
            ciphertext += ch
    print("Your  is: ", ciphertext)


def caesar_key(plainText, shift):
    ciphertext = ""
    for ch in plainText.lower():
        if ch.isalpha():
            lettersonly = ord(ch) - shift
            if lettersonly < ord('a'):
                lettersonly += 26
            nechar = chr(lettersonly)
            ciphertext += nechar
        else:
            ciphertext += ch
    print("Your decoded text is: ", ciphertext)


response = ["d", "e"]
decision = ""
key_input = ""
while decision.lower() not in response:
    decision = input("What would you like to do? Decrypt or Encrypt?: (D/E)")

if decision.lower() == "d":
    plaintext = input("What would you like to Decrypt? : ")
    while plaintext == "":
        plaintext = input("Try again.")
    while True:
        try:
            key_input = (input("Whats the key to your encryption? : "))
            key = int(key_input)
            break
        except:
            continue

    caesar_key(plaintext, key)

if decision.lower() == "e":
    plaintext = input("What would you like to change into a cipher? : ")
    while plaintext == "":
        plaintext = input("Try again.")
    while True:
        try:
            key_input = (input("What would you like the key to be? : "))
            key = int(key_input)
            break
        except:
            continue
    caesar(plaintext, key)
