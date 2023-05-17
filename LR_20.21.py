import numpy as np 
def hex_table():
    # Create a 16x16 array of zeros
    table = np.zeros((16, 16), dtype=int)
    
    # Fill the array with multiplication results
    for i in range(16):
        for j in range(16):
            table[i][j] = i * j
    
    # Print the multiplication table
    print("Multiplication Table:")
    print("---------------------")
    print("  |", end="")
    for i in range(16):
        print(f" {hex(i)[2:].upper()}|", end="")
    print()
    print("-" * 51)
    for i in range(16):
        print(f"{hex(i)[2:].upper()} |", end="")
        for j in range(16):
            print(f" {hex(table[i][j])[2:].upper().zfill(2)}|", end="")
        print()
    
    # Fill the array with addition results
    for i in range(16):
        for j in range(16):
            table[i][j] = i + j
    
    # Print the addition table
    print("\nAddition Table:")
    print("----------------")
    print("  |", end="")
    for i in range(16):
        print(f" {hex(i)[2:].upper()}|", end="")
    print()
    print("-" * 35)
    for i in range(16):
        print(f"{hex(i)[2:].upper()} |", end="")
        for j in range(16):
            print(f" {hex(table[i][j])[2:].upper().zfill(2)}|", end="")
        print()