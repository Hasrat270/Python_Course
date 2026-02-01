a = 150000000000000000000000000000000
b = 150000000000000000000000000000000
print(a is b)
print(f"Address of a: {id(a)}")
print(f"Address of b: {id(b)}")
print(f"Same address? {id(a) is id(b)}")