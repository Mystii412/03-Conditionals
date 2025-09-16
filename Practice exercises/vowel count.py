text = input('Enter text: ').strip()

vowels = 0

length = len(text)

num = length - 1

while num >= 0:
    if {text[num]} == 'a':
        vowels += 1
        num -= 1
        print(vowels)