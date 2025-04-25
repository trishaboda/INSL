def encrypt(message, key):
    result = ""
    key_index = 0
    
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                letter_num = ord(letter) - ord('A')
                key_letter = key[key_index % len(key)].upper()
                key_num = ord(key_letter) - ord('A')
                
                new_letter_num = (letter_num + key_num) % 26 
                new_letter = chr(new_letter_num + ord('A'))
                
            else:
                letter_num = ord(letter) - ord('a')
                key_letter = key[key_index % len(key)].upper()
                key_num = ord(key_letter) - ord('A')
                
                new_letter_num = (letter_num + key_num) % 26
                new_letter = chr(new_letter_num + ord('a'))
                
            result += new_letter
            key_index += 1
        else:
            result += letter
    
    return result

def decrypt(encrypted, key):
    result = ""
    key_index = 0
    
    for letter in encrypted:
        if letter.isalpha():
            if letter.isupper():
                letter_num = ord(letter) - ord('A')
                key_letter = key[key_index % len(key)].upper()
                key_num = ord(key_letter) - ord('A')
                
                new_letter_num = (letter_num - key_num) % 26
                new_letter = chr(new_letter_num + ord('A'))
                
            else:
                letter_num = ord(letter) - ord('a')
                key_letter = key[key_index % len(key)].upper()
                key_num = ord(key_letter) - ord('A')
                
                new_letter_num = (letter_num - key_num) % 26
                new_letter = chr(new_letter_num + ord('a'))
                
            result += new_letter
            key_index += 1
        else:
            result += letter
    
    return result

message = "Hello World"
key = "Aashmit"

encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print("Original message:", message)
print("Key:", key)
print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)