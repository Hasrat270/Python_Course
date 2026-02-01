salary = float(input("Enter your current salary: "))
bonus_percentage = float(input("Enter your bonus percentage: "))

bonus_amount = salary * (bonus_percentage / 100)

salary += bonus_amount

print(f"Your updated salary is: {salary}")