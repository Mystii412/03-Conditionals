age = int(input("Enter age: "))
perm = input("Parent Permission (yes/no): ")

if age >= 18 or perm == "yes":
    print("Approved: Field trip form accepted.")
else:
    print("Approved: Denied (needs permission or be 18+")