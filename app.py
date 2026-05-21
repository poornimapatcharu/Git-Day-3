# Simple Python Program

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\n--- User Details ---")
print(f"Name: {name}")
print(f"Age: {age}")

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
