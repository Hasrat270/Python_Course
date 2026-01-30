numOne = input("Enter first number: ")
numTwo = input("Enter second number: ")

sum = float(numOne) + float(numTwo)
print("The sum is:", sum)

subtraction = float(numOne) - float(numTwo)
print("The subtraction is:", subtraction)

multiplication = float(numOne) * float(numTwo)
print("The multiplication is:", multiplication)

try:
    division = float(numOne) / float(numTwo)
    print(f"The division is: {division}")
except ZeroDivisionError:
    print("Error: You tried to divide by zero!")