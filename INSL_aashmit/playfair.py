def playfair(text, key, encrypt=True):
    # Create matrix
    key = key.upper().replace('J', 'I')
    matrix = ''
    for c in key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if c not in matrix: matrix += c
    
    # Print the matrix
    print("Key Matrix:")
    for i in range(5):
        print(matrix[i*5:i*5+5])
    print()
    
    # Prepare text
    text = ''.join([c.upper() for c in text if c.isalpha()]).replace('J', 'I')
    pairs = []
    i = 0
    while i < len(text):
        if i == len(text)-1 or text[i] == text[i+1]:
            pairs.append(text[i] + 'X')
            i += 1
        else:
            pairs.append(text[i:i+2])
            i += 2
    
    result = ''
    for p in pairs:
        # Find positions
        p1, p2 = matrix.find(p[0]), matrix.find(p[1])
        r1, c1 = p1 // 5, p1 % 5
        r2, c2 = p2 // 5, p2 % 5
        s = 1 if encrypt else -1
        
        # Simplified rules application 
        if r1 == r2:  # Same row
            c1, c2 = (c1+s)%5, (c2+s)%5
        elif c1 == c2:  # Same column
            r1, r2 = (r1+s)%5, (r2+s)%5
        else:  # Rectangle
            c1, c2 = c2, c1
            
        result += matrix[r1*5 + c1] + matrix[r2*5 + c2]
    
    return result

# Usage
key = "Aashmit"
message = "HELLO WORLD"
encrypted = playfair(message, key)
decrypted = playfair(encrypted, key, False)

print(f"Original: {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")