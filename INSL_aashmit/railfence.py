def rail_fence_cipher(input_array, num_rows):
    # Create the specified number of empty arrays (rows)
    rows = []
    for i in range(num_rows):
        rows.append([])
    
    current_row = 0
    direction = 1
    
    for element in input_array:
        rows[current_row].append(element)
        
        if current_row == 0:
            direction = 1
        elif current_row == num_rows - 1:
            direction = -1 
        
        current_row += direction
    
    for i, row in enumerate(rows):
        print(f"Row {i}:", row)
     
    result = []
    for row in rows:
        for element in row:
            result.append(element)
    print("Combined result:", result)

if __name__ == "__main__":
    message = "Aashmit"
    input_array = []
    for char in message:
        input_array.append(char)
    
    num_rows = 3
    
    print("Original array:", input_array)
    print("Distributing across", num_rows, "rows:")
    rail_fence_cipher(input_array, num_rows)