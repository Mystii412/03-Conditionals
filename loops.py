for i in range(5):
    print(i)

print(list(range(9)))
print(list(range(5,101,5)))

penny = 1

days = 100

total = penny

for i in range(days):
    penny = penny * 2

print(f"After {days} days, you will have {(penny/100):.2f} dollars.")

#loop - execute a code block repeatedly
#For loops - good for running a controlled number of times
#Range - used to get a range that can be looped through 
# Range(end) - this is exclusive meaning it will be 0 - one less than end 
# Range(start, stop) - from start to 1 less than stop
# Range(start, stop, step) from start to stop counting by step
for num in range(50,3,-1):
    print(num)

#nested loops
rows = 5
cols = 6

for x in range(rows):
    for y in range(cols):
        print(f"({x}, {y})", end="")
    print()

    #iterables - things like strings, ranges, lists, arrays, sets, tuples
    for char in "Mr. Klins Computer Programming is crazy":
        if char.lower() == "m":
            continue # this automatically moves to the next iteration
        if char.lower() == "z":
            break # exit loop
        print(char)
    else:
        print("An else with a loop :0") # only runs if the loop isnt broken

l = -5
# while loops
while l < 50:
    l = l+5
    print(l)
#the above loop behaves the same as for start in range(0,50,5)

value = input("Enter a command or exit to stop: ").strip()
while value != "exit":
    print(f"executing {value}")
    value = input("Enter a command or exit to stop: ").strip()
print("Outside while loop")

#determine if a value is in a range
grade = 10
if 10 <= grade <= 12:
    print("You can join mr. klins' computer programming \n... if you're awesome")