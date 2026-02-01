wallet = 0

add_money = float(input("How much money do you want to add? "))
wallet += add_money

food = float(input("How much money did you spend on food? "))
wallet -= food

transport = float(input("How much money did you spend on transport? "))
wallet -= transport

shopping = float(input("How much money did you spend on shopping? "))
wallet -= shopping

is_in_range = (wallet > 500) and (wallet < 5000)

print(f"Is the balance between 500 and 5000? {is_in_range}")
print(f"Final wallet balance: {wallet}")