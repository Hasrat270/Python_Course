reg_fee = int(input("Enter registration fee: "))
monthly_fee = int(input("Enter monthly fee: "))
months = int(input("Enter number of months: "))

total_cost = reg_fee + (monthly_fee * months)

has_discount = input("Do you have a discount coupon? (yes/no): ").lower()

multiplier = 1.0 - (0.1 * (has_discount == "yes"))
total_cost *= multiplier

print(f"Final amount to be paid: {total_cost}")