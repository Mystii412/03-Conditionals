user = input("Enter username: ")

length = len(user)

space = user.find(" ")

if length >= 5 and space == -1:
    print("Valid Username")
else:
    print('Invalid: too short or contains spaces.')