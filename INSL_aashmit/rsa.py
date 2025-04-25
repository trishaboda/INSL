def power(base, exp, mod):
    result = 1
    for i in range(exp):
        result = (result * base) % mod
    return result

def main():
    p = 3
    q = 11
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    d = 7

    message = 17

    encrypted = power(message, e, n)
    decrypted = power(encrypted, d, n)

    print("Original:", message)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()