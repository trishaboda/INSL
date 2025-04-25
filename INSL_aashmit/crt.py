def mod_inverse(a, m):
    return pow(a, -1, m)

def chinese_remainder_theorem(a, m):
    M = 1
    n = len(m)
    
    # Calculate the product of all moduli
    for mi in m:
        M *= mi

    result = 0
    for i in range(n):
        Mi = M // m[i]  # M_i = M / m_i
        yi = mod_inverse(Mi, m[i])  # y_i = inverse of M_i modulo m_i
        result += a[i] * Mi * yi  # Add to result

    return result % M 

def main():  
    a = [2, 3, 2]  # Example remainders
    m = [3, 5, 11]  # Example moduli

    result = chinese_remainder_theorem(a, m)
    print(f"The solution is: {result}")

if __name__ == "__main__":
    main()
