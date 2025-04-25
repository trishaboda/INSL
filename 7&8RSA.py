import random
from sympy import isprime
from math import gcd

def get_prime_input():
    while True:
        try:
            num = int(input("Enter a prime number: "))
            if isprime(num):
                return num
            else:
                print("Not a prime number. Try again.")
        except ValueError:
            print("Invalid input. Enter an integer.")

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    return None

def generate_keys():
    p = get_prime_input()
    q = get_prime_input()
    while p == q:
        print("Prime numbers must be different. Enter again.")
        q = get_prime_input()
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(plaintext, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(ciphertext, private_key):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

public_key, private_key = generate_keys()
print("\nPublic Key: ", public_key)
print("Private Key: ", private_key)

message = input("\nEnter a message to encrypt: ")
ciphertext = encrypt(message, public_key)
print("\nEncrypted: ", ciphertext)


# take input for decryption
ciphertext_input = input("Enter the ciphertext to decrypt (space-separated integers): ")
ciphertext = list(map(int, ciphertext_input.split()))

decrypted_message = decrypt(ciphertext, private_key)
print("Decrypted: ", decrypted_message)
