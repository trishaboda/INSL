def columnar_transposition_encrypt(plaintext, key):
    key_length = len(key)
    num_rows = -(-len(plaintext) // key_length) 
    matrix = [['' for _ in range(key_length)] for _ in range(num_rows)]

    index = 0
    for row in range(num_rows):
        for col in range(key_length):
            if index < len(plaintext):
                matrix[row][col] = plaintext[index]
                index += 1
            else:
                matrix[row][col] = ' '  

    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    ciphertext = ''

    for idx, _ in key_order:
        for row in range(num_rows):
            ciphertext += matrix[row][idx]

    return ciphertext

plaintext = input("Enter the plaintext: ").replace(" ", "")
key = input("Enter the key (alphabetic): ")

encrypted = columnar_transposition_encrypt(plaintext, key)
print("\nEncrypted Text:", encrypted)
