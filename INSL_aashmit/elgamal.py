import random
from sympy import mod_inverse

# Function to generate ElGamal keys
def generate_keys(p, g):
    x = random.randint(2, p - 2)
    y = pow(g, x, p)
    return (x, (p, g, y))  # Private key is 'x', public key is (p, g, y)

def encrypt(public_key, message):
    p, g, y = public_key
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    c2 = (message * pow(y, k, p)) % p
    return (c1, c2)

def decrypt(private_key, ciphertext):
    x = private_key
    c1, c2 = ciphertext
    s = pow(c1, x, p)
    s_inv = mod_inverse(s, p)
    message = (c2 * s_inv) % p
    return message

if __name__ == "__main__":
    # Define prime number 'p' and base 'g' for ElGamal
    p = 7919  # A prime number
    g = 2  # A primitive root mod p
    
    private_key, public_key = generate_keys(p, g)
    
    message = 1234  # The message must be an integer less than p

    ciphertext = encrypt(public_key, message)
    print(f"Ciphertext: {ciphertext}")

    decrypted_message = decrypt(private_key, ciphertext)
    print(f"Decrypted message: {decrypted_message}")
