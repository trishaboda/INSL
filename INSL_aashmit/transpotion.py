def encrypt(message, key):
    return ''.join(message[i::key] for i in range(key))


def decrypt(ciphertext, key):
    num_rows = len(ciphertext) // key
    num_cols = key
    num_shaded = (num_cols * num_rows) - len(ciphertext)

    plaintext = [''] * num_rows
    col, row = 0, 0

    for symbol in ciphertext: 
        plaintext[row] += symbol
        row += 1
        if (row == num_rows) or (row == num_rows - 1 and col >= num_cols - num_shaded):
            row = 0
            col += 1

    return ''.join(plaintext)



msg = "aashmit"
key = 2

enc = encrypt(msg, key)
print("Encrypted:", enc)

dec = decrypt(enc, key)
print("Decrypted:", dec)

