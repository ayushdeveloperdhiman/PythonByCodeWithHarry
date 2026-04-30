a = input("Enter your name: ")
print("My name is",a)

while(True):
    try:
        x = int(input("Enter first number: "))
        break
    except ValueError as ex:
        print("Invalid Integer Value")

while(True):
    try:
        y = int(input("Enter second number: "))
        break
    except ValueError as ex:
        print("Invalid Integer Value")

print(x + y)
