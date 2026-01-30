a = input("Enter first value: ")
b = input("Enter second value: ")

print(type(a))
print(type(b))

a_float = float(a)
b_float = float(b)

print(type(a_float))
print(type(b_float))

sum = a_float + b_float
print(type(sum))
print("Sum:", sum)

new = int("4") + float("5.2")
print(new)
print(type(new))