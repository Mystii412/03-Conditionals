start = int(input("Start : "))
end = int(input("End : "))
end += 1
for num in range(start, end):
    if num % 2 == 1:
        print(num)