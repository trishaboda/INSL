import random

def power_mod(base, exp, mod):
    return pow(base, exp, mod)

def diffie_hellman():
    # Public values: a large prime p and a primitive root g
    p = 23  # Example prime number
    g = 5   # Example primitive root modulo p

    # Alice's private key
    a = random.randint(1, p-1)
    # Bob's private key
    b = random.randint(1, p-1)

    # Alice computes her public key
    A = power_mod(g, a, p)

    # Bob computes his public key
    B = power_mod(g, b, p)

    print("Public parameters: p =", p, ", g =", g)
    print("Alice's private key: ", a)
    print("Bob's private key: ", b)

    print("\nAlice's public key (A): ", A)
    print("Bob's public key (B): ", B)

    shared_secret_alice = power_mod(B, a, p)
    shared_secret_bob = power_mod(A, b, p)

    print("\nShared secret computed by Alice: ", shared_secret_alice)
    print("Shared secret computed by Bob: ", shared_secret_bob)

    # Verify if both Alice and Bob computed the same shared secret
    if shared_secret_alice == shared_secret_bob:
        print("\nKey exchange successful! Shared secret is: ", shared_secret_alice)
    else:
        print("\nKey exchange failed.")

diffie_hellman()
