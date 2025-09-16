total = 0

while True:
    item = input('Item (blank to finish) : ')
    length = len(item)
    if length > 0:
        total += 1
    else:
        print(f"You entered {total} items.")
        break