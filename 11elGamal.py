import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def power(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

def generate_keys():
    p = int(input("Enter a large prime number (p): "))
    g = int(input("Enter a primitive root modulo p (g): "))
    x = random.randint(2, p-2)  # Private key
    y = power(g, x, p)          # Public key
    return (p, g, y, x)

def encrypt(p, g, y, m):
    k = random.randint(2, p-2)
    a = power(g, k, p)
    b = (m * power(y, k, p)) % p
    return (a, b)

def decrypt(p, x, a, b):
    s = power(a, x, p)
    s_inv = modinv(s, p)
    m = (b * s_inv) % p
    return m

message = int(input("Enter message (as integer < p): "))
    
p, g, y, x = generate_keys()
print(f"\nPublic Key (p={p}, g={g}, y={y})")
print(f"Private Key (x={x})")
    
a, b = encrypt(p, g, y, message)
print(f"\nEncrypted Message (Pair): (a={a}, b={b})")
    
print("\nDecryption")
a = int(input("Enter a (part of ciphertext): "))
b = int(input("Enter b (part of ciphertext): "))
    
decrypted_message = decrypt(p, x, a, b)
print(f"Decrypted Message: {decrypted_message}")