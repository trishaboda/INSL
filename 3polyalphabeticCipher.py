def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(msg, key):
    encrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            res = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            res = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            res = char
        encrypted_text.append(res)
    return "".join(encrypted_text)

def decrypt_vigenere(msg, key):
    decrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            res = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            res = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            res = char
        decrypted_text.append(res)
    return "".join(decrypted_text)

text = input("Enter the text to encrypt: ")
key = input("Enter the key: ")

generated_key = generate_key(text, key)
print("\nGenerated Key: ", generated_key)

encrypted_text = encrypt_vigenere(text, key)
print("\nEncrypted Text: ", encrypted_text)

decrypted_text = decrypt_vigenere(encrypted_text, key)
print("Decrypted Text: ", decrypted_text)
