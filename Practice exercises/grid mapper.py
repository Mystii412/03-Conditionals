rows = int(input('Rows'))
cols = int(input('Cols'))

for x in range(rows):
    for y in range(cols):
        print(f"({x}, {y})", end="")
    print()