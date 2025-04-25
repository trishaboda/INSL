import numpy as np

def mod_inverse(matrix, mod):
    det = int(round(np.linalg.det(matrix)))  
    det_inv = pow(det, -1, mod)  
    
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % mod  
    return (det_inv * adjugate) % mod

def generate_key_matrix(key, size=3):
    key = key.replace(" ", "").upper()
    key_matrix = np.array([ord(c) - 65 for c in key[:size*size]]).reshape(size, size)
    print("Key Matrix:")
    print(key_matrix)
    return key_matrix

def generate_text_matrix(text, size=3):
    text = text.replace(" ", "").upper()
    while len(text) % size != 0:
        text += "X"  
    
    text_matrices = []
    for i in range(0, len(text), size):
        text_matrices.append(np.array([[ord(c) - 65] for c in text[i:i+size]]))
    
    print("\nText Matrix:")
    for mat in text_matrices:
        print(mat.flatten())
    
    return text_matrices, text  

def encrypt_text(text, key_matrix):
    size = key_matrix.shape[0]
    text_matrices, text = generate_text_matrix(text, size)
    
    encrypted_text = ""
    for matrix in text_matrices:
        encrypted_matrix = np.dot(key_matrix, matrix) % 26
        encrypted_text += "".join(chr(num[0] + 65) for num in encrypted_matrix)
    
    return encrypted_text

text = input("Enter the text to encrypt: ").strip()
key = input("Enter the key (length should be a perfect square, e.g., 9 characters for 3x3 matrix): ").strip()

key_matrix = generate_key_matrix(key, 3)
encrypted_text = encrypt_text(text, key_matrix)
print("\nEncrypted Text:", encrypted_text)

