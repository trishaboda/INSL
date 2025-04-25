def caesar_encrypt(text, shift):
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    result = ""
    
    for char in text:
        if char in lowercase:
            index = lowercase.index(char)
            new_index = (index + shift) % 26
            result += lowercase[new_index]
        elif char in uppercase:
            index = uppercase.index(char) 
            new_index = (index + shift) % 26
            result += uppercase[new_index]
        else:
            result += char
            
    return result

def caesar_decrypt(encrypted_text, shift):
    return caesar_encrypt(encrypted_text, -shift)

message = "Aashmit"
shift_value = 2

encrypted_message = caesar_encrypt(message, shift_value)
print(f"Original: {message}")
print(f"Encrypted: {encrypted_message}")

decrypted_message = caesar_decrypt(encrypted_message, shift_value)
print(f"Decrypted: {decrypted_message}")
