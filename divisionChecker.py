num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

is_divisible = (num2 % num1 == 0)

print(f"Does {num1} divide {num2} evenly? {is_divisible}")