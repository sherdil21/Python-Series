# a=int(input("Enter the Number= "))
# b=int(input("Enter the Number= "))

# print(f"Sum: {a+b}")
# print(f"Difference: {a-b}")
# print(f"Product: {a*b}")
# print(f"Quotient: {a/b}")

while True:
    try:
        a = int(input("Enter first number = "))
        break
    except ValueError:
        print("Invalid input! Please enter numbers only.\n")

while True:
    try:
        b = int(input("Enter second number = "))
        break
    except ValueError:
        print("Invalid input! Please enter numbers only.\n")

print(f"Sum: {a+b}")
print(f"Difference: {a-b}")
print(f"Product: {a*b}")
print(f"Quotient: {a/b}")