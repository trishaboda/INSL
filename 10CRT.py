def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def chinese_remainder_theorem(num, rem):
    prod = 1
    for ni in num:
        prod *= ni
    
    result = 0

    for ni, ai in zip(num, rem):
        p = prod // ni
        result += ai * mod_inverse(p, ni) * p

    return result % prod

# Driver Code
if __name__ == "__main__":
    num = [3, 5, 7]  # moduli
    rem = [2, 3, 2]  # remainders
    result = chinese_remainder_theorem(num, rem)
    #print num and rem
    print("Numbers are ", num)
    print("Remainders are ", rem)
    print("Value of x is ", result)
