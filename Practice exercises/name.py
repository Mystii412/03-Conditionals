preferred = input('Preffered name (optional) : ')
length = len(preferred)

first = input('First Name : ')

if length > 0:
    print(f'Hello, {preferred}')
else:
    print(f'Hello, {first}')